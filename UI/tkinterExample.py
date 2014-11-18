__author__ = 'fhilton & jsturtevant'
#https://docs.python.org/2/library/tkinter.html#a-simple-hello-world-program
import Tkinter as tk

class Application(tk.Frame):
    def ImportFileCommand(self):
        file = open('../Log.txt', 'r')
        lines = file.readlines()
        self.numberofrows.set(len(lines))


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

        #Adds a button to the screen
        self.ImportFile = tk.Button(self)
        self.ImportFile["text"] = "Load File"
        self.ImportFile["command"] = self.ImportFileCommand
        self.ImportFile.grid(row=0, column=0, sticky =tk.W + tk.N)

        #adds a label to the screen
        self.NumberOfRowsLabel = tk.Label(self)
        self.NumberOfRowsLabel["text"] = "Number of Rows"
        self.NumberOfRowsLabel.grid(row = 1, column=0, sticky = tk.W)

        #adds a text box to the screen
        self.NumberOfRowsTextBox = tk.Entry(self, textvariable= self.numberofrows)
        self.NumberOfRowsTextBox.grid(row = 1, column=1)
        self.numberofrows.set(10)

        #adds a listbox to screen
        self.FileListBox = tk.Listbox(self)
        self.FileListBox.grid(row = 2, column= 0, columnspan = 2 , sticky= tk.E + tk.W)

        #add items to the list box
        self.FileListBox.insert(tk.END, "a list entry")
        self.FileListBox.insert(tk.END, "another list entry")

        #Add current line info lines
        self.CurrentLineInfoLabel = tk.Label(self)
        self.CurrentLineInfoLabel["text"] = "Line Info:"
        self.CurrentLineInfoLabel.grid(row = 3, column=0, sticky = tk.W)

        self.CurrentLineInfo = tk.Label(self)
        self.CurrentLineInfo.grid(row = 3, column=1)
        self.CurrentLineInfo["text"] = "Select a line above"

        self.SetupQuit()

    def __init__(self, master=None):
        #basic initialization
        tk.Frame.__init__(self, master)
        self.master.title("Log Parser Answers")
        self.master.minsize(300,300)
        self.numberofrows = tk.StringVar()

        #makes grid expand
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)

        #set up the widgets on the screen
        self.createWidgets()

        #hook up 'click event' to the listbox
        self.current = None
        self.poll()

    def poll(self):
        #bit of a hack to monitor the listbox changing
        now = self.FileListBox.curselection()
        if now != self.current:
            self.list_has_changed(now)
            self.current = now
        self.after(250, self.poll)

    def list_has_changed(self, selection):
        print "selection is", selection
        if len(selection) > 0:
            self.CurrentLineInfo["text"] = self.FileListBox.get(selection[0])

#start the window
root = tk.Tk()
app = Application(master=root)
app.mainloop()