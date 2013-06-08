from Tkinter import *
import tkFileDialog
import image_resizer

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        master.wm_title("Image Resizer")
        self.dir_button = Button(frame, text="Select Folder",command=self.select_folder)
        self.dir_button.pack()
        self.dirname = StringVar()
        Label(master, textvariable=self.dirname).pack()
        self.width = StringVar()
        self.enterWidth = Entry(master, textvariable=self.width)
        self.enterWidth.pack()
        self.resize_button = Button(frame, text="Resize Images", command=self.resize)
        self.resize_button.pack()
        self.status = StringVar()
        self.status_label = Label(master, textvariable=self.status)
        self.status_label.pack()

    def select_folder(self):
        self.dirname.set(tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory'))
        self.status.set("")

    def resize(self):
        if self.width.get() != '' and self.dirname != '':
            countImages = image_resizer.resizeImages(self.dirname.get(), int(self.width.get()))
            self.status.set(str(countImages) + ' images resized')
        if self.width.get() == '':
            self.status.set("Please input an image resize width.")
        if self.dirname.get() == '':
            self.status.set(self.status.get() + " Please select a folder.")
root = Tk()
app = App(root)
root.mainloop()
