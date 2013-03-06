#!/usr/bin/python -u
#
# webloccer.py
# copyright (c) by Alexander Lehmann <afwlehmann@in.tum.de>
#
# Read Apple's .webloc files and have the URL opened in the browser.

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
