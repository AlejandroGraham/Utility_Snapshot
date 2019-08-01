from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror

def load_file(self):
        fname = askopenfilename(filetypes=(("PDF files", "*.pdf"),
                                           ("PNG files", "*.png"),
                                           ("JPEG files", "*.jpeg")
                                           ("All files", "*.*") ))
        if fname:
            try:
                print("""here it comes: self.settings["file"].set(fname)""")
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return