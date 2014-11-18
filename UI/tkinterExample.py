__author__ = 'fhilton & jsturtevant'
#https://docs.python.org/2/library/tkinter.html#a-simple-hello-world-program
import Tkinter as tk

class Application(tk.Frame):


    def say_hi(self):
        print "hi there, everyone!"

    def SetupQuit(self):
        self.QUIT = tk.Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.grid(row=99, column=99, sticky=tk.S + tk.E)
        self.rowconfigure(99, weight=1)
        self.columnconfigure(99, weight=1)

    def createWidgets(self):
        #configures outermost window to stretch
        top=self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=0, column=0, sticky =tk.W + tk.N)

        self.NumberOfRowsLabel = tk.Label(self)
        self.NumberOfRowsLabel["text"] = "Number of Rows"
        self.NumberOfRowsLabel.grid(row = 1, column=0, sticky = tk.W)

        self.NumberOfRowsTextBox = tk.Entry(self, textvariable= self.numberofrows)
        self.NumberOfRowsTextBox.grid(row = 1, column=1)
        self.numberofrows.set(10)

        self.FileListBox = tk.Listbox(self)
        self.FileListBox.grid(row = 2, column= 0, columnspan = 2 , sticky= tk.E + tk.W)
        self.FileListBox.insert(tk.END, "a list entry")

        self.SetupQuit()
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Log Parser")
        self.master.minsize(500,300)
        self.numberofrows = tk.StringVar()

        #makes grid expand
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

root = tk.Tk()
app = Application(master=root)
app.mainloop()