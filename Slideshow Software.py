from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter import scrolledtext
import os
import platform
def find_hcf(a, b):
    if a > b:
        lesser = b
    else:
        lesser = a
    smaller = lesser+1
    for x in range(1, smaller):
        if((a % x == 0) and (b % x == 0)):
            hcf = x
        return hcf 
global change_sl
def next_func():
    welcome.destroy()
    root = Tk()
    root.title('Python Presentation Software')
    notes_frame = Tk()
    notes_frame.title('Presenter Notes')
    notes = scrolledtext.ScrolledText(notes_frame, font = ('Helevectical', 14))
    notes.pack()

    global filename
    filedir = filedialog.askdirectory(title='Where are all your images?')
    filename = os.listdir(filedir)
    filelist = ['']
    for a in range(len(filename)):
        if (filename[a].endswith('.png') == True) or (filename[a].endswith('.jpg') == True) or (filename[a].endswith('.jpeg') == True) or (filename[a].endswith('.tiff') == True) or (filename[a].endswith('.bmp') == True) or (filename[a].endswith('.gif') == True):
            if 'Windows' in platform.platform():
                a = filedir.encode('unicode_escape')+r'\\'+filename[a]
                print(a)
                filelist.append(filedir+'\\'+filename[a])
            else:
                filelist.append(filedir+'/'+filename[a])
            print("Successfully added '"+filename[a]+"' file")
        else:
            print("Removed invalid image '"+filename[a]+"'")
    def change_sl():
        panel.destroy()
        open_img()
        print(slide_wid.get())
    controls = Tk()
    controls.title('Slieshow Controls')
    change_slide = Label(controls, text = 'Slide Number:')
    change_slide.pack()
    slide_wid = Spinbox(controls, from_= 1, to = len(filelist)-1, command = change_sl)
    slide_wid.pack()
    def open_img():
        try:
            s = int(slide_wid.get())
            if (s >= 1 and s < len(filelist)):
                x = filelist[s]
            else:
                x = 1
        except:
            showinfo('Sorry', 'There is no such slide as: '+slide_no)
        print(x)
        try:
            global panel
            img = Image.open(x)
            width, height = img.size
            img = img.resize((width, height), Image.ANTIALIAS)
            root.geometry(str(width)+"x"+str(height))
            img = ImageTk.PhotoImage(img)
            panel = Label(root, image=img)
            panel.image = img
            panel.pack()
            root.resizable(0, 0)
        except Exception as error:
            showinfo("Error", error)
            root.destroy()
    open_img()
welcome = Tk()
welcome.title('Python Slideshow app')
img2 = ImageTk.PhotoImage(Image.open("Welcome_Screen.png"))
panel2 = Label(welcome, image = img2)

panel2.pack(side = "top", fill = "both", expand = "yes")
next_but = Button(welcome, text="Create your slideshow", bd=4, padx=14, pady=14, bg='orange', command=next_func, font=("Aerial Rounded MT Bold",16,'bold')).pack(side = BOTTOM)
welcome.mainloop()
