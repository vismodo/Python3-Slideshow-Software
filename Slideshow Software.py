try: #Try execution of lines below with indentation
    from tkinter import * # Import everything from the pre-installed tkinter TK GUI toolkit
    from PIL import ImageTk, Image # Import ImageTk and Image classes from the pillow library
    from tkinter.messagebox import showinfo # Import the showinfo class from the pre-installed tkinter.messagebox module(showinfo lets you display alerts in the centre of the screen
    import os # Import the the pre-installed os module
    import platform # Import the the pre-installed platform module (platform allows you to find system data through python)
    import webbrowser as wb # Import the the pre-installed webbrowser module as wb (webbrowser allows you to do open urls in your browser, among many other things)
    def next_sl(): # Define the function next_sl() as the code that follows below it with indentation
        panel.destroy() # Destroy the tkinter label 'panel' from the parent window
        slide_var.set(str(int(slide_var.get())+1)) # Set the tkinter integer variable 'slide_var' to the sum of the integer form of the data in the tkinter integer variable 'slide_var' and 1
        open_img() # Carry out the 'open_img()' function
        print(slide_var.get()) # Print the data in the tkinter integer variable 'slide_var'
    def prev_sl(): # Define the function prev_sl() as the code that follows below it with indentation
        panel.destroy()# Destroy the tkinter label 'panel' from the parent window
        slide_var.set(str(int(slide_var.get())-1))# Set the tkinter integer variable 'slide_var' to the difference of the integer form of the data in the tkinter integer variable 'slide_var' and 1
        open_img() # Carry out the 'open_img()' function
        print(slide_var.get()) # Print the data in the tkinter integer variable 'slide_var'

    global change_sl # Make the variable 'change_sl' visible to all functions
    def next_func(): # Define the function next_func() as the code that follows below it with indentation
        welcome.destroy() # Destroy the tkinter window 'welcome' from the parent window
        root = Tk() # Create a new tkinter window called 'root' with which is tkinter's 'Tk' object
        root.title('Python Presentation Software') # Set the title of the tkinter window 'root' to 'Python Presentation Software'
        notes_frame = Tk() # Create a new tkinter window called 'notes_frame' with which is tkinter's 'Tk' object
        notes_frame.title('Presenter Notes') # Set the title of the tkinter window 'notes_frane' to 'Presenter Notes'
        notes = scrolledtext.ScrolledText(notes_frame, font = ('Helevectical', 14)) # Create a new tkinter scrolledtext scrollable text box called 'notes' with which is scrolledtext's 'ScrolledText' object. It is created in the 'notes_frame' window, with the font 'Helevectical' and size 14
        notes.pack() # Shows the tkinter widget 'notes' in the parent window on the top hand side

        global filename # Make the variable 'filename' visible to all functions
        filedir = filedialog.askdirectory(title='Where are all your images?') # Use the 'askdirectory' object ok tkinter's filedialog class with the title 'Where are all your images?', so that the directory can be taken and saved as a string in 'filedir'
        filename = os.listdir(filedir) # Use the os module's 'listdir' object to list down all the files and subfolders in the directory 'filedir' and save it in a variable called filelist
        filelist = [''] # Create a list called filelist with one empty string
        for a in range(len(filename)): # While the integer 'a' is in the range of the length of the list 'filename', execute the indented code that follows.
            if (filename[a].endswith('.png') == True) or (filename[a].endswith('.jpg') == True) or (filename[a].endswith('.jpeg') == True) or (filename[a].endswith('.tiff') == True) or (filename[a].endswith('.bmp') == True) or (filename[a].endswith('.gif') == True):
                if 'Windows' in platform.platform():
                    a = filedir+r'\n'+filename[a]
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
                img = Image.open(x)
                width, height = img.size
                width = int((width/10)*int(img_size.get()))
                height = int((height/10)*int(img_size.get()))
                img = img.resize((width, height), Image.ANTIALIAS)
                #root.geometry(str(width)+"x"+str(height))
                img = ImageTk.PhotoImage(img)
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
    img2 = ImageTk.PhotoImage(Image.open("Welcome_Screen.png"))
    panel2 = Label(welcome, image = img2)

    panel2.pack(side = "top", fill = "both", expand = "yes")
    next_but = Button(welcome, text="Create from folder", bd=4, padx=14, pady=14, bg='orange', command=next_func, font=("Aerial Rounded MT Bold",16,'bold')).pack(side = BOTTOM)
    next_but2 = Button(welcome, text="Export PPTX as images", bd=4, padx=14, pady=14, bg='orange', command=lambda: showinfo('Export Presentation', 'In PowerPoint, click on File > Export, and save is as multiple ".jpeg files". The resolution decides the quality of the presentation.'), font=("Aerial Rounded MT Bold",16,'bold')).pack(side = BOTTOM)
    welcome.mainloop()
except Exception as e:
    showinfo('Error', e)
