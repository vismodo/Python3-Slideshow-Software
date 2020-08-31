# Python 3 Slideshow Software - Version 2.0
The problem with any presentation software such as PowerPoint, iWork Keynote or LibreOffice Impress is that they present in full-screen, which isn't the best option when you are doing live screen sharing and using other apps at the same time. This slideshow app, written in Python 3.8 will help you out in such a case.
## Support
This project currently supports linux based platforms, including macOS. The files are have been tested on windows too, and they work.

## Features 
### In Version [1.0](https://github.com/VismayaAtreya/Python3-Slideshow-Software/tree/Version-1.0)

* Create presentations from folders with image formats like `.jpg`, `.jpeg`, `.tiff`, `.bmp`, `.png`and `.gif`.
```
if (filename[a].endswith('.png') == True) or (filename[a].endswith('.jpg') == True) or (filename[a].endswith('.jpeg') == True) or (filename[a].endswith('.tiff') == True) or (filename[a].endswith('.bmp') == True) or (filename[a].endswith('.gif') == True):
```
* Scrollable Presenter Notes

![notes](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/Version-1.0/User%20Guide%20Images/presenter_notes.png)

* Cross Platform
```
if 'Windows' in platform.platform():
    a = filedir+r'\n'+filename[a]
    print(a)
     filelist.append(filedir+'\\'+filename[a])
else:
     filelist.append(filedir+'/'+filename[a])
```
* Auto-format slides (based on name)
```
filename = os.listdir(filedir)
```
* Only retain valid files for presentations(remove invalid images from list)
```
for a in range(len(filename)):
    if (filename[a].endswith('.png') == True) or (filename[a].endswith('.jpg') == True) or (filename[a].endswith('.jpeg') == True) or (filename[a].endswith('.tiff') == True) or (filename[a].endswith('.bmp') == True) or (filename[a].endswith('.gif') == True):
        if 'Windows' in platform.platform():
            a = filedir+r'\n'+filename[a]
            print(a)
            filelist.append(filedir+'\\'+filename[a])
        else:
            filelist.append(filedir+'/'+filename[a])
            print("Successfully added '"+filename[a]+"' file"
    else:
        print("Removed invalid image '"+filename[a]+"'")
```

### In Version [2.0](https://github.com/VismayaAtreya/Python3-Slideshow-Software/)

* A new dropdown-menu to change slides, without going over to the controls window to do so, and also an option to quit.

![slideshow_dropdown.png](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/slideshow_dropdown.png)

* A new dropdown-menu to hide, show, save and load presenter notes from text files.

![notes_dropdown.png](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/notes_dropdown.png)

* Another dropdown-menu to show and hide controls.

![controls_dropdown.png](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/controls_dropdown.png)

* There is an 'Online Help' menu too, which links to files in this repository

![help_dropdown.png](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/help_dropdown.png)

* You can change the size of the slideshow too with the slider below the slide controls!

![controls.png](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/controls.png)

## Getting Started
1. Click [here](https://github.com/VismayaAtreya/Python3-Slideshow-Software/archive/master.zip) to clone the repository. Extract all the contents into one folder.
2. Open ['Slideshow Software.py'](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Slideshow%20Software.py) or [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py) in [IDLE](https://docs.python.org/3/library/idle.html)

![open_file](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/open_file.png)

3. Click on <b>Run -> Run Module</b> and wait for a tkinter window to pop up.

![run_module](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/run_module.png)

4. Click on <b>'Create your slideshow'</b> if you already have your pictures in one folder.

![welcome_tk](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/welcome_tk.png)

If you do not, click on <b>'Export PPTX as images'</b> to get the instructions as an alert, like this.

![alert](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/alert.png)

5. Select the folder which contains the images for the slideshow.

![open_dir](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/open_dir.png)

6. Your presentation has started!

![presentation](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/presentation.png)

7. You can now change the slides from the 'Controls' window.

![controls](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/controls.png)

8. In your call, click on 'Share Screen' and select your presentation! You also have a window for presenter notes!

![presenter_notes](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/presenter_notes.png)

9. If you wish to stop, from the 'Slideshow' dropdown menu in the ribbbon, select 'Quit'.

![slideshow_dropdown.png](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/slideshow_dropdown.png)

## Troubleshooting

If the image turns out to be a little blurry or degraded in [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py), Just move to a different slide and go back. This is a problem with tkinter's Photoimage attribute.

For further queries, [create an issue](https://github.com/VismayaAtreya/Python3-Slideshow-Software/issues/new/choose) and I will get back to you as fast as possible.

## Suggest a feature?
If you liked this software, star this repository or suggest a feature in the [issues](https://github.com/VismayaAtreya/Python3-Slideshow-Software/issues) tab.
