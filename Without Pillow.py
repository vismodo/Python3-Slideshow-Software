try:
    from tkinter import *
    from tkinter.messagebox import showinfo
    import os
    import platform
    import webbrowser as wb
    from tkinter import scrolledtext, filedialog
    def next_sl():
        panel.destroy()
        slide_var.set(str(int(slide_var.get())+1))
        open_img()
        print(slide_var.get())
    def prev_sl():
        panel.destroy()
        slide_var.set(str(int(slide_var.get())-1))
        open_img()
        print(slide_var.get())
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
            if (filename[a].endswith('.png') == True) or (filename[a].endswith('.tiff') == True) or (filename[a].endswith('.bmp') == True) or (filename[a].endswith('.gif') == True):
                if 'Windows' in platform.platform():
                    b = filedir+'\\'+filename[a]
                    print(b)
                    filelist.append((filedir.replace('/', '\\')).replace(':\\', ':\\\\')+'\\'+filename[a])
                else:
                    filelist.append(filedir+'/'+filename[a])
                print("Successfully added '"+filename[a]+"' file")
            else:
                print("Removed invalid image '"+filename[a]+"'")
        def change_sl():
            panel.destroy()
            open_img()
            print(slide_var.get())
        def next_sl():
            panel.destroy()
            s = int(slide_var.get())
            slide_var.set(s+1)
            open_img()
            print(slide_var.get())
        def prev_sl():
            panel.destroy()
            s = int(slide_var.get())
            slide_var.set(str(s-1))
            open_img()
            print(slide_var.get())
        controls = Tk()
        controls.title('Slideshow Controls')
        slide_var = IntVar(controls)
        change_slide = Label(controls, text = 'Slide Number:')
        change_slide.pack()
        slide_wid = Spinbox(controls, from_= 1, to = len(filelist)-1, command = change_sl, textvariable=slide_var)
        slide_wid.pack()
        img_size = Scale(controls, from_= 1, to = 20, orient = HORIZONTAL, length = 250)
        img_size.set(10)
        img_size.pack()
        def open_img():
            try:
                s = int(slide_var.get())
                if (s >= 1 and s < len(filelist)):
                    x = filelist[s]
                else:
                    x = filelist[0]
                print(x)
            except:
                showinfo('Sorry', 'There is no such slide as: '+str(slide_var.get()))
            try:
                global panel
                img = PhotoImage(file=x)
                width, height = img.width(), img.height()
                width = int((width/10)*int(img_size.get()))
                height = int((height/10)*int(img_size.get()))
                img = img.zoom(img_size.get())
                img = img.subsample(10)
                root.geometry(str(width)+"x"+str(height))
                panel = Label(root, image=img)
                panel.image = img
                panel.pack()
                root.resizable(0, 0)
            except Exception as error:
                showinfo("Error", error)
                root.destroy()
        
        def refresh():
            panel.destroy()
            open_img()
            open_img
        refresh_but = Button(controls, text='Set Size', command = refresh)
        refresh_but.pack()
        open_img()
        def load_notes():
            notes.delete('1.0', END)
            text = open(filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes =(("Text Files","*.txt"),)).name)
            notes.insert(END, text.read())
        
        ribbon3 = Menu(notes_frame)

        notes_menu2 = Menu(ribbon3, tearoff=0)
        notes_menu2.add_command(label='Hide Presenter Notes', command= notes_frame.withdraw)
        notes_menu2.add_separator()
        notes_menu2.add_command(label='Save Presenter Notes', command= lambda: (open(filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes =(("Text Files","*.txt"),)), 'w')).write(notes.get('1.0', 'end-1c')))
        notes_menu2.add_command(label='Load Presenter Notes', command= load_notes)
        ribbon3.add_cascade(label="Presenter Notes", menu=notes_menu2)

        ribbon2 = Menu(controls)

        ctrls_menu2 = Menu(ribbon2, tearoff=0)
        ctrls_menu2.add_command(label='Hide Controls', command= controls.withdraw)
        ribbon2.add_cascade(label="Controls", menu=ctrls_menu2)
        
        ribbon = Menu(root)

        slides_menu = Menu(ribbon, tearoff=0)
        slides_menu.add_command(label='Next Slide', command=next_sl)
        slides_menu.add_command(label='Previous Slide', command=prev_sl)
        slides_menu.add_separator()
        slides_menu.add_command(label='Quit', command= lambda: exit())
        ribbon.add_cascade(label="Slideshow", menu=slides_menu)

        notes_menu = Menu(ribbon, tearoff=0)
        notes_menu.add_command(label='Hide Presenter Notes', command= notes_frame.withdraw)
        notes_menu.add_command(label='Show Presenter Notes', command= notes_frame.deiconify)
        notes_menu.add_separator()
        notes_menu.add_command(label='Save Presenter Notes', command= lambda: (open(filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes =(("Text Files","*.txt"),)), 'w')).write(notes.get('1.0', 'end-1c')))
        notes_menu.add_command(label='Load Presenter Notes', command= load_notes)
        ribbon.add_cascade(label="Presenter Notes", menu=notes_menu)

        ctrls_menu = Menu(ribbon, tearoff=0)
        ctrls_menu.add_command(label='Hide Controls', command= controls.withdraw)
        ctrls_menu.add_command(label='Show Controls', command= controls.deiconify)
        ribbon.add_cascade(label="Controls", menu=ctrls_menu)

        help_menu = Menu(ribbon, tearoff=0)
        help_menu.add_command(label='Download Latest', command=lambda: wb.open_new_tab('https://github.com/VismayaAtreya/Python3-Slideshow-Software/archive/master.zip'))
        help_menu.add_command(label='Latest Documentation', command=lambda: wb.open_new_tab('https://github.com/VismayaAtreya/Python3-Slideshow-Software/blob/master/README.md'))
        help_menu.add_command(label='Report An Issue', command=lambda: wb.open_new_tab('https://github.com/VismayaAtreya/Python3-Slideshow-Software/issues/new/choose'))
        help_menu.add_command(label='Suggest A Feature', command=lambda: wb.open_new_tab('https://github.com/VismayaAtreya/Python3-Slideshow-Software/issues/new/choose'))
        ribbon.add_cascade(label="Online Help", menu=help_menu)

        def disable_event():
            pass
        root.config(menu=ribbon)
        controls.config(menu=ribbon2)
        notes_frame.config(menu=ribbon3)
        root.protocol("WM_DELETE_WINDOW", disable_event)
        controls.protocol("WM_DELETE_WINDOW", disable_event)
        notes_frame.protocol("WM_DELETE_WINDOW", disable_event)
    welcome = Tk()
    welcome.title('Python Slideshow app')
    img2 = PhotoImage(file="Welcome_Screen.png")
    panel2 = Label(welcome, image = img2)

    panel2.pack(side = "top", fill = "both", expand = "yes")
    next_but = Button(welcome, text="Create from folder", bd=4, padx=14, pady=14, bg='orange', command=next_func, font=("Aerial Rounded MT Bold",16,'bold')).pack(side = BOTTOM)
    next_but2 = Button(welcome, text="Export PPTX as images", bd=4, padx=14, pady=14, bg='orange', command=lambda: showinfo('Export Presentation', 'In PowerPoint, click on File > Export, and save is as multiple ".png files". The resolution decides the quality of the presentation.'), font=("Aerial Rounded MT Bold",16,'bold')).pack(side = BOTTOM)
    welcome.mainloop()
except Exception as e:
    showinfo('Error', e)
