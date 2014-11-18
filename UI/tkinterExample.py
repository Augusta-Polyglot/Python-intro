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
        self.FileListBox.insert(tk.END, "another list entry")

        self.CurrentLineInfoLabel = tk.Label(self)
        self.CurrentLineInfoLabel["text"] = "Line Info:"
        self.CurrentLineInfoLabel.grid(row = 3, column=0, sticky = tk.W)

        self.CurrentLineInfo = tk.Label(self)
        self.CurrentLineInfo.grid(row = 3, column=1)
        self.CurrentLineInfo["text"] = "Select a line above"

        self.SetupQuit()
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Log Parser")
        self.master.minsize(500,300)
        self.numberofrows = tk.StringVar()

        #makes grid expand
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

        self.current = None
        self.poll()

    def poll(self):
        now = self.FileListBox.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.after(250, self.poll)

    def list_has_changed(self, selection):
        print "selection is", selection
        if len(selection) > 0:
            self.CurrentLineInfo["text"] = self.FileListBox.get(selection[0])

root = tk.Tk()
app = Application(master=root)
app.mainloop()