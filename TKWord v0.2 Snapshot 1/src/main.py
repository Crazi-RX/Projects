from tkinter import *
from tkinter import messagebox
from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog
import os
##### MAIN APPLICATION WINDOW #####
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)

##### BUTTONS #####
        fileMenu = Menu(menu)
        fileMenu.add_command(label="New", command=self.newFile)
        fileMenu.add_command(label="Open", command=self.openFile)
        fileMenu.add_command(label="Save", command=self.saveFile)
        fileMenu.add_command(label="Save As", command=self.saveAs)
        fileMenu.add_command(label="Options", command=self.optionMenu)
        fileMenu.add_command(label="Quit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        editMenu.add_command(label="Cut")
        editMenu.add_command(label="Copy")
        editMenu.add_command(label="Paste")
        editMenu.add_command(label="Select All")
        menu.add_cascade(label="Edit", menu=editMenu)

        fontMenu = Menu(menu)
        fontMenu.add_command(label="Font Family")
        fontMenu.add_command(label="Size")
        fontMenu.add_command(label="Color")
        menu.add_cascade(label="Font", menu=fontMenu)

        helpMenu = Menu(menu)
        helpMenu.add_command(label="FAQ")
        helpMenu.add_command(label="How To Use")
        helpMenu.add_command(label="Shortcuts")
        menu.add_cascade(label="Help", menu=helpMenu)

        aboutMenu = Menu(menu)
        aboutMenu.add_command(label="Check for Updates", command=self.updateCheck)
        aboutMenu.add_command(label="Patch Notes", command=self.patchNotes)
        aboutMenu.add_command(label="About TKWord")
        aboutMenu.add_command(label="About The Dev")
        menu.add_cascade(label="About", menu=aboutMenu)

##### BUTTON AND MENU FUNCTIONS #####
    def updateCheck(self):
        messagebox.showerror("Check For Updates", "Check For Updates is not available for this update...")

    def patchNotes(self):
        messagebox.showinfo("Patch Notes", "In TKWord v0.2 includes: Improved Bug Fixes, Font Functionality, More Edit Functions")

    def newFile(self):
        global txt
        root.title("Untitled - TKWord v0.2 | ALPHA")
        file = None
        txt.delete(1.0, END)

    def openFile(self):
        global txt
        file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        file = file.name

        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - TKWord v0.2 | ALPHA")
            txt.delete(1.0, END)
            file = open(file, "rb")
            txt.insert(1.0, file.read())
            file.close()

    def saveFile(self):
        global txt
        global file
        if file == None:
            file = filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if file == None:
                file = None
            else:
                file = open(file, "w")
                file.write(txt.get(1.0, END))
                file.close()
                file = file.name
                root.title(os.path.basename(file) + " - TKWord v0.2 | ALPHA")
        else:
            file = open(file, "w")
            file.write(txt.get(1.0, END))
            file.close()

    def saveAs(self):
        files = [('All Files', '*.*'),('Text Documents', '*.txt')]
        file = filedialog.asksaveasfile(filetypes = files, defaultextension = files)
        
    def optionMenu(self):
        messagebox.showerror("Options Menu | TKWord v0.2 | ALPHA", "Options Menu Is Currently Disabled In This Version...")

    def exitProgram(self):
        exit()

    def quitOptions(self):
        pass

##### INITIALIZE TKINTER #####
root = Tk()
root.geometry("800x600")
root.wm_title("Untitled - TKWord v0.2 | ALPHA")
file = None
global txt
txt = Text(root, width=800, height=600)
txt.pack(side=LEFT, expand=YES, fill=BOTH)
txt.grid(sticky = N+E+S+W)  
window = Window(root)
##### SHOW WINDOW #####
root.mainloop()