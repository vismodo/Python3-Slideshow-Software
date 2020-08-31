# Python 3 Slideshow Software - Version 2.0
The problem with any presentation software such as PowerPoint, iWork Keynote or LibreOffice Impress is that they present in full-screen, which isn't the best option when you are doing live screen sharing and using other apps at the same time. This slideshow app, written in Python 3.8 will help you out in such a case.

![Basic Demo.gif](https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/Demonstrations/Basic%20Demo.gif)

### More Demonstrations: [Wiki Page](https://github.com/VismayaAtreya/Python3-Slideshow-Software/wiki/Demonstrations)

## 

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
