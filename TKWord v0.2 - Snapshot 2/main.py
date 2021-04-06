from tkinter import *
from tkinter import messagebox
from tkinter import Frame
from tkinter import Tk
from tkinter import BOTH
from tkinter import Text
from tkinter import Menu
from tkinter import ttk
from tkinter.font import Font
from tkinter import END
from tkinter import filedialog
import os
import webbrowser
############################################
#                                          #
#                                          #
#                  TKWORD                  #
#          OPEN-SOURCE APPLICATION         #
#              BY JACOB ROGERS             #
#                                          #
#                                          #
############################################

##### ROOT FUNCTION #####
root = Tk()
##### MAIN APPLICATION WINDOW #####
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu=menu)
        termsAgreement = messagebox.askquestion("Agree to our terms and conditions?", "Do you agree to our terms and conditions? Please read the Terms and Conditions along with the Privacy Policy text files provided before clicking yes or no.")
        if termsAgreement == 'no':
            exit()
        elif termsAgreement == 'yes':
            messagebox.showinfo("Thanks for agreeing! Enjoy TKWord!", "Thanks for agreeing to our terms and conditions!")
        else:
            exit()

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
        editMenu.add_command(label="Undo", command=txt.edit_undo)
        editMenu.add_command(label="Redo", command=txt.edit_redo)
        editMenu.add_command(label="Cut", command=self.cutCommand)
        editMenu.add_command(label="Copy", command=self.copyCommand)
        editMenu.add_command(label="Paste", command=self.pasteCommand)
        editMenu.add_separator()
        editMenu.add_command(label="Select All", command=self.selectAllCommand)
        menu.add_cascade(label="Edit", menu=editMenu)

        fontMenu = Menu(menu)
        fontMenu.add_command(label="Font Family", command=self.fontFamily)
        fontMenu.add_command(label="Font Type", command=self.fontType)
        fontMenu.add_command(label="Size", command=self.fontSize)
        fontMenu.add_command(label="Color", command=self.fontColor)
        menu.add_cascade(label="Font", menu=fontMenu)

        helpMenu = Menu(menu)
        helpMenu.add_command(label="FAQ", command=self.FAQ)
        helpMenu.add_command(label="How To Use", command=self.HTU)
        helpMenu.add_command(label="Shortcuts", command=self.shortCuts)
        menu.add_cascade(label="Help", menu=helpMenu)

        aboutMenu = Menu(menu)
        aboutMenu.add_command(label="Check for Updates", command=self.updateCheck)
        aboutMenu.add_command(label="Terms And Conditions", command=self.termsCondition)
        aboutMenu.add_command(label="Privacy Policy", command=self.privacyPolicy)
        aboutMenu.add_command(label="Patch Notes", command=self.patchNotes)
        aboutMenu.add_command(label="About TKWord", command=self.aboutTK)
        aboutMenu.add_command(label="About The Dev", command=self.aboutDev)
        menu.add_cascade(label="About", menu=aboutMenu)

##### BUTTON AND MENU FUNCTIONS #####
    def updateCheck(self):
        messagebox.showerror("Check For Updates", "Check For Updates is not available for this update...")

    def termsCondition(self):
        webbrowser.open("https://www.termsandconditionsgenerator.com/live.php?token=SBsCoz73ag9X5yU66qzKhsj6UT6cSTxX")

    def privacyPolicy(self):
        webbrowser.open("https://www.privacypolicygenerator.info/live.php?token=FuMiSsRPvZVFc2L372RiOPuOALL3wfsb")

    def patchNotes(self):
        patchNotesWindow = Toplevel(root)
        patchNotesWindow.title("Patch Notes | TKWord v0.2 | ALPHA")
        patchNotesWindow.geometry("650x300")
        patchNotesTitleCard = Label(patchNotesWindow, font=LARGE_FONT, 
        text = "Patch Notes")
        versionDescription2 = Label(patchNotesWindow, font=LARGE_FONT,
        text = "VERSION 0.2")
        patchNotesParagraph2 = Label(patchNotesWindow, font=PARA_FONT, 
        text = """Version 0.2 includes: New functionality like font selection,
        scrollbar, font color, and font size. New Edit Functions (Select All, Cut).
        Bug Fixes (Words goes off the screen, New file sometimes doesn't delete
        the text from previous documents.""")
        versionDescription = Label(patchNotesWindow, font=LARGE_FONT, 
        text = "VERSION 0.1")
        patchNotesParagraph = Label(patchNotesWindow, font=PARA_FONT, 
        text = """Version 0.1 includes: Creating new files and saving files, Copy and Paste 
        edit functions, Added About Menu""")
        patchNotesTitleCard.pack(padx=5, pady=5)
        versionDescription2.pack(padx=5, pady=5)
        patchNotesParagraph2.pack(padx=5, pady=5)
        versionDescription.pack(padx=5, pady=5)
        patchNotesParagraph.pack(padx=5, pady=5)

    def aboutTK(self):
        TKDescription = Toplevel(root)
        TKDescription.title("About TKWord")
        TKDescription.geometry("800x300")
        tkTitleCard = Label(TKDescription, font=LARGE_FONT,
        text = "About TKWord")
        tkParagraph = Label(TKDescription, font=PARA_FONT, 
            text = """TKWord is developed by a beginner programmer named Jacob Rogers. 
            TKWord is a open-source application made for normal use or beginner programmmers 
            to tinker around with the features in the code. v0.2 was made from 
            scratch compared to v0.1 (Not available to download anymore due too many bugs). 
            v0.2 started developement on 3/24/2021.""")
        tkTitleCard.pack(padx=5, pady=5)
        tkParagraph.pack(padx=5, pady=5)

    def aboutDev(self):
        DEVDescription = Toplevel(root)
        DEVDescription.title("About The Dev")
        DEVDescription.geometry("800x300")
        devTitleCard = Label(DEVDescription, font=LARGE_FONT, 
        text = """About The Dev""")
        devTitleCard.pack(padx=5, pady=5)
        devParagraph = Label(DEVDescription, font=PARA_FONT, 
        text = """Jacob Rogers is an beginner python programmer and this is one of his
        official projects for the public. The first version he made
        (v0.1) was a failure due to many bugs and functions that barely worked,
        so he decided to make version 0.2 from scratch and make it bigger,
        better, and more functional than before.""")
        devParagraph.pack(padx=5, pady=5)

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

    def quitOptions(self):
        pass

    def popup(self, event):
        self.rightClick.post(event.x_root, event.y_root)

    def cutCommand(self):
        sel = self.txt.selection.get()
        self.clipboard = sel
        self.txt.delete(SEL_FIRST, SEL_LAST)

    def copyCommand(self):
        sel = self.txt.selection.get()
        self.clipboard = sel

    def pasteCommand(self):
        self.txt.insert(INSERT, self.clipboard)

    def selectAllCommand(self):
        self.txt.tag_add(SEL, "1.0", END)
        self.txt.mark_set(0.0, END)
        self.txt.see(INSERT)

    def fontFamily(self):
        pass

    def fontType(self):
        pass

    def fontSize(self):
        pass

    def fontColor(self):
        pass

    def FAQ(self):
        pass

    def HTU(self):
        pass

    def shortCuts(self):
        pass

    def exitProgram(self):
        exit()

##### CANVAS AND SCROLLBAR #####
scroll_frame = Frame(root)
scroll_frame.pack(fill=BOTH, side=LEFT, expand=1)
scroll_canvas = Canvas(scroll_frame)
scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)
txt_scrollbar = ttk.Scrollbar(scroll_frame, orient=VERTICAL, 
command=scroll_canvas.yview)
txt_scrollbar.pack(side=RIGHT, fill=Y)
scroll_canvas.configure(yscrollcommand=txt_scrollbar.set)
scroll_canvas.bind('<Configure>', lambda e: 
scroll_canvas.configure(scrollregion = scroll_canvas.bbox("all")))
scroll_frame2 = Frame(scroll_canvas)
scroll_canvas.create_window((0,0), window=scroll_frame2, anchor="nw")

##### INITIALIZE TKINTER #####
root.geometry("800x600")
root.wm_title("Untitled - TKWord v0.2 | ALPHA")
root.resizable(False, False)
file = None
global txt
txt = Text(scroll_frame2, width=87, height=87, undo=True, font="Arial")
txt.grid(sticky = N+E+S+W)  
window = Window(root)
LARGE_FONT = Font(
    family="Segoe UI", 
    size=16, 
    weight="bold", 
    slant="roman", 
    underline=0, 
    overstrike=0)
PARA_FONT = Font(
    family="Segoe UI", 
    size=12,
    weight="normal", 
    slant="roman", 
    underline=0, 
    overstrike=0)
##### SHOW WINDOW #####
root.mainloop()