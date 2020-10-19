from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfile
import os
def newfile():
    global file
    root.title("Untitled - Notepad")
    file=None
    textarea.delete(1.0,END)
def openFile():
   global file
   file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
   if file=="":
       file=None
   else:
       root.title(os.path.basename(file)+"- Notepad")
       textarea.delete(1.0,END)
       f=open(file,"r")
       textarea.insert(1.0,f.read())
       f.close()
def savefile():
    global file
    if file==None:
        file=asksaveasfile(initialfile='Untitled.txt',
                           defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("file saved")
    else:
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        print("file saved")

def Quitapp():
    root.destroy()
def cut():
    Cut=lambda:textarea.event_generate("<<Control x>>")

def copy():
    Copy=lambda:textarea.event_generate("<<Control c>>")
def paste():
    Paste = lambda: textarea.event_generate("<<Control v>>")
def about():
    showinfo("Notepad","Notepad by code with depanshu")
if __name__ == '__main__':
    #basic tkinter setup
    root=Tk()
    root.title("Untitled- Notepad")
    root.wm_iconbitmap("1.ico")
    root.geometry("644x788")


    #add textarea
    textarea=Text(root,font="lucida 13").pack(expand=True,fill=BOTH)
    file=None

    #creating menubar
    menubar=Menu(root)
    #file menu starts
    filemenu=Menu(menubar,tearoff=0)
    #open new file
    filemenu.add_command(label="New",command=newfile)
    #to open already existing file
    filemenu.add_command(label="open",command=openFile)
    #to save the current file
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=Quitapp)
    menubar.add_cascade(label="File",menu=filemenu)
    #file menu ends

    #Edit menu starts
    Editmenu=Menu(menubar,tearoff=0)
    #to give a feature of cut
    Editmenu.add_command(label="cut",command=cut)
    Editmenu.add_command(label="copy",command=copy)
    Editmenu.add_command(label="Paste",command=paste)
    menubar.add_cascade(label="Edit",menu=Editmenu)
    #Edit menu ends

    #help menu starts
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)
    #help menu ends
    root.config(menu=menubar)
    #adding scrollbar
   # scroll=Scrollbar(textarea)
   # scroll.pack(side=RIGHT,fill=Y)
    #scroll.config(command=textarea.yview)
    #textarea.config(yscrollcommand=scroll.set)
    root.mainloop()