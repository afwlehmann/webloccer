#!/usr/bin/python -u
#
# webloccer.py 
# copyright (c) 2013 by Alexander Lehmann <afwlehmann@googlemail.com>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# 
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
# webloccer.py
# copyright (c) by Alexander Lehmann <afwlehmann@in.tum.de>

import xml.parsers.expat, sys, os
from PyQt4.QtCore import QCoreApplication
from PyKDE4.kdecore import KToolInvocation

class WebLocParser(QCoreApplication):

    def __init__(self):
        super(QCoreApplication, self).__init__(sys.argv)

        self.reset()
         
    def parseAndOpen(self, fileName):
        try:
            with open(fileName, 'r') as fIn:
                self._p.ParseFile(fIn)
                if self._url:
                    KToolInvocation.invokeBrowser(self._url)
                else:
                    raise "Hell"
        except:
            sys.stderr.write("Invalid webloc file: %s\n" % fileName)

    def _startElement(self, name, attrs):
        self._insideURL = name.lower() == "string"

    def _endElement(self, name):
        self._insideURL = name.lower() == "string" and False

    def _charData(self, data):
        if self._insideURL:
            self._url = data

    def reset(self):
        self._insideURL = False
        self._url = None
        self._p = xml.parsers.expat.ParserCreate()
        self._p.StartElementHandler = self._startElement
        self._p.EndElementHandler = self._endElement
        self._p.CharacterDataHandler = self._charData

if __name__ == "__main__":
    if len(sys.argv) < 2:
        bn = os.path.basename(sys.argv[0])
        sys.stderr.write("Syntax: %s file1 [file2 [file3 ...]]" % bn)
        sys.exit(1)

    wlp = WebLocParser()
    for fileName in filter(os.path.isfile, sys.argv[1:]):
        wlp.parseAndOpen(fileName)
        wlp.reset()
    wlp.exit(0)
