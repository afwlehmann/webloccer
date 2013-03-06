# webloccer

Have KDE open your favorite URLs that were long forgotten and locked away in `*.webloc` files.

![Screenshot](http://213.239.219.185/webloccer/screenshot.png)

## Oh wow, so why's that supposed to be useful?

For example, if you're like me and have finally abandoned your closed-platform caM in favor of the better goods, you might want to re-use all those web-location files you've created over the years.

### Created? How?

Those URLs that you once dragged-and-dropped from your browser onto your desktop and which were then stored as `*.webloc` files.

### Now what?

Guess it's just that simple. Have KDE open those URLs from either the terminal or your favorite file manager.

## Installation

### Requirements
- [PyKDE4](http://techbase.kde.org/Development/Languages/Python)

Easily installed, for example, via Ubuntu's package management system like so:

```bash
sudo apt-get install python3-pykde4
```

### Once you have what you need

- Install `webloccer.py` to a reasonable location, such as eg.
  ```bash
  install -m 755 webloccer.py /usr/local/bin/webloccer.py
  ```

If you want support from your file manager, then also do the following:

- Open KDE *System Settings* and select *File Assocations*.

  ![FirstStepPic](http://213.239.219.185/webloccer/step_1.png)
  
- Press the *Add* button, set *Group* to `text` and enter `webloc` as *type name*.

  ![SecondStepPic](http://213.239.219.185/webloccer/step_2.png)
  
- Add `*.webloc` to filename patterns, then add the `webloccer.py` executable to the group that says *Application Preference Order*. Make sure it's all the way up.

  ![ThirdStepPic](http://213.239.219.185/webloccer/step_3.png)
