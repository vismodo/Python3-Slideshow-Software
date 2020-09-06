# Python 3 Slideshow Software - Version 2.0 
The problem with any presentation software such as PowerPoint, iWork Keynote or LibreOffice Impress is that they present in full-screen, which isn't the best option when you are doing live screen sharing and using other apps at the same time. This slideshow app, written in Python 3.8 will help you out in such a case.
The best part is that it is open-source, and even Not-Experienced Python developers can understand, easily!


![Basic Demo.gif](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Demonstrations/Basic%20Demo.gif)

### More Demonstrations: [Wiki Page](https://github.com/VismayaAtreya/Python3-Slideshow-Software/wiki/Demonstrations)

### See [progress in version 3](https://github.com/VismayaAtreya/Python3-Slideshow-Software/projects/1?add_cards_query=is%3Aopen)

## Usage

1. Click [here](https://github.com/VismayaAtreya/Python3-Slideshow-Software/archive/master.zip) to clone the repository. Extract all the contents into one folder.

<b>If you choose to use ['Slideshow Software.py'](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Slideshow%20Software.py) or [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py) in [IDLE](https://docs.python.org/3/library/idle.html), open Command Prompt or Terminal on your computer and install [Pillow](https://python-pillow.org/) with [pip](https://pypi.org/project/pip/), like this:</b>

```
pip install Pillow
```
Or, if your default Python version is Python 2.7 (find out with `python --version`),

```
pip3 install Pillow
```

2. Open ['Slideshow Software.py'](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Slideshow%20Software.py) and not [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py) in [IDLE](https://docs.python.org/3/library/idle.html)

3. Click on <b>Run -> Run Module</b> and wait for a tkinter window to pop up.

<b>Alternatively, you can also try executing `python3` or `python` followed by your file's location like this, in Terminal or Command Prompt</b>

```
python3 /Users/Me/Documents/Python3-Slideshow-Software-master/Slideshow Software.py
```

4. Click on <b>'Create your slideshow'</b> if you already have your pictures in one folder.

<img src="https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/welcome_tk.png" alt="drawing" width="600"/>

If you do not, click on <b>'Export PPTX as images'</b> to get the instructions as an alert, like this.

![alert](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/alert.png)

5. Select the folder which contains the images for the slideshow.

![open_dir](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/open_dir.png)

6. Your presentation has started!

<img src="https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/presentation.png" alt="drawing" width="600"/>

7. You can now change the slides from the 'Controls' window.

![controls](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/controls.png)

8. In your call, click on 'Share Screen' and select your presentation! You also have a window for presenter notes!

<img src="https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/presenter_notes.png" alt="drawing" width="600"/>

9. If you wish to stop, from the 'Slideshow' dropdown menu in the ribbbon, select 'Quit'.

![slideshow_dropdown.png](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/User%20Guide%20Images/slideshow_dropdown.png)

## Customising the Code

* Change the name of the presentation (Window Title) from line 23 of [Slideshow Software.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Slideshow%20Software.py) or line 22 of [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py)

```
root.title('Python Presentation Software')
```
* Change [Welcome_Screen.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Welcome_Screen.png) to a picture that you prefer, or change the directory on line 162 of [Slideshow Software.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Slideshow%20Software.py) or line 161 of [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py)

## Troubleshooting

### Degraded Image quality after resizing in [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py)

* If the image turns out to be a little blurry or degraded in [Without Pillow.py](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Without%20Pillow.py), Just move to a different slide and go back. This is a problem with [tkinter's Photoimage class](https://effbot.org/tkinterbook/photoimage.htm).

* Click on the <b>Set Size</b> to resize the image, which also refreshes the slide during runtime

* Execute `open_img` one more time, though the <b>Set Size</b> button already does that

For further queries, [create an issue](https://github.com/VismayaAtreya/Python3-Slideshow-Software/issues/new/choose) and I will get back to you as fast as possible.

### The slideshow quits unexpectedly after an alert

* This happens if you try and go to the next slide after reaching the last one. I have fixed the code once it first happened.

* You need to check your code and see if any extra item gets added to `filelist`. If that is happening, just remove it with `filelist.pop()` and the index as argument

### Tkinter Error if I select cancel in `filedialog`

* This is an error that occurs only because the filedialog returns an empty string, and `os.listdir` can't make out what is in the directory, so that too returns an empty list. 

```
filedir = filedialog.askdirectory(title='Where are all your images?')
filename = os.listdir(filedir)
```

* Now, tkinter wants to open the image from the directory, and nothing is there for it to open, so you will get a huge error linking to line `1883` of tkinter's `__init__.py` file.

```
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Some Directory/tkinter/__init__.py", line 1883, in __call__
    return self.func(*args)
  File "/Some Directory/Slideshow App V2.py", line 33, in next_func
    filename = os.listdir(filedir)
FileNotFoundError: [Errno 2] No such file or directory: ''
```

* To fix this, you need to show an alert with `showinfo` and quit the program if `filename` is empty


### An issue is not listed here?

* I have worked on this project and debugged it for over a week. If you have any other problem or feature you would like to suggest, [submit an issue](https://github.com/VismayaAtreya/Python3-Slideshow-Software/issues). I will give update the code in a couple days and put the soulution in this list and I will also respond to your issue in the issues tab

## Releases

Release Information in [Wiki](https://github.com/VismayaAtreya/Python3-Slideshow-Software/wiki/Releases)

* Version 1.0 (Deprecated): Presenter notes, slidehshow controls in new window

* Version 2.0: Save an load presenter notes, hide and show presenter notes and controls, resize slides with slider, ribbon menus for slideshow, controls, presenter notes and help

### See [progress in version 3](https://github.com/VismayaAtreya/Python3-Slideshow-Software/projects/1?add_cards_query=is%3Aopen)

## Areas for improvement

I am unable to fix these issues, so you can solve these and tell me how you solved by [submitting an issue](https://github.com/VismayaAtreya/Python3-Slideshow-Software/issues)

* Split `.pptx` presentations to images without the `python-pptx` module.
* Split `.pdf` documents into images without the `pdf2jpg` module.
* Download images from the web and create presentations from those.
