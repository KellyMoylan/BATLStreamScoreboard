__author__ = 'Kelly'

from tkinter import *

w = 1000
h = 600



class application(Tk):

    bgcolour = "white"
    upArrow = u"\u25B2"
    downArrow = u"\u25BC"
    throwList = ['-', 'D', '0', '1', '3', '5', '7']
    folderPath = ""
    leftAxes = [0, 0, 0, 0, 0]
    rightAxes = [0, 0, 0, 0, 0]

    leftFirst = StringVar()
    leftSecond = StringVar()
    leftThird = StringVar()
    leftFourth = StringVar()
    leftFifth = StringVar()

    rightFirst = StringVar()
    rightSecond = StringVar()
    rightThird = StringVar()
    rightFourth = StringVar()
    rightFifth = StringVar()

    def __init__(self,parent):
        Tk.__init__(self,parent)
        self.parent = parent
        # self.geometry(str(w) + "x" + str(h))
        self.resizable(width=False, height=False)
        self.configure(background=bgcolour)
        self.initialize()

    def initialize(self):
        logo = PhotoImage(file="images/batllogo.gif")
        w1 = Label(self, image=logo, bg=bgcolour)
        w1.image = logo
        w1.grid(row=1, column=1)

        pathSetEntry = Entry(self, width=60, font=('ariel', 10, 'bold'), relief=SUNKEN, borderwidth=3)
        pathSetEntry.grid(row=1, column=2, columnspan=2, sticky=W)
        pathSetButton = Button(self, text="Set")
        pathSetButton.grid(row=1, column=3, sticky=E)

        matchTitleLabelFrame = LabelFrame(self, bg=bgcolour, width=1000, text="Match", relief=GROOVE, font=("ariel", 16, "bold"))
        matchTitleLabelFrame.grid(row=2, column=1, columnspan=3, padx=50)

        matchTitleEntry =  Entry(matchTitleLabelFrame, width=40, font=('ariel', 10, 'bold'), relief=SUNKEN, borderwidth=3)
        matchTitleButton = Button(matchTitleLabelFrame, text="Set")

        matchTitleEntry.grid(row=2, column=2, sticky=E, padx=(100,0))
        matchTitleButton.grid(row=2, column=3, sticky=W, padx=(0, 100))

        self.createThrower1(logo)
        self.createThrower2(logo)

        switchButton = Button(self, text="<- SWITCH ->")
        switchButton.grid(row=3, column=2, padx=20)
        resetButton = Button(self, text="RESET")
        resetButton.grid(row=4, column=2)
        updateButton = Button(self, text="UPDATE", width=60, height=2, font=('ariel', 16, 'bold'))
        updateButton.grid(row=6,column=1,columnspan = 3, pady=5)
        nextGameButton = Button(self, text="Next Game", width=60, height=2, font=('ariel', 16, 'bold'))
        nextGameButton.grid(row=7, column=1, columnspan = 3, pady=5)

    def changeAxe(self, postion, direction):
        if(direction == 0):


    def createThrower1(self,logo):
        thrower1Frame = LabelFrame(self, bg=bgcolour, width=(w / 2) - 100, height=300, relief=GROOVE, text="Left Thrower", font=("ariel", 16, "bold"))
        thrower1Frame.grid(row=3, column=1, rowspan=3, padx=10)

        thrower1NameLabel = Label(thrower1Frame, bg=bgcolour, text="Name:")
        thrower1NameLabel.grid(row=1, column=2, padx=10)

        thrower1NameEntry = Entry(thrower1Frame, width=40)
        thrower1NameEntry.grid(row=1, column=3)

        thrower1NameButton = Button(thrower1Frame, text="SET")
        thrower1NameButton.grid(row=1, column=4, padx=10)

        thrower1GameLabel = Label(thrower1Frame, font=('ariel', 10, 'bold'), bg=bgcolour, text="Game Count")
        thrower1GameLabel.grid(row=2, column=3)

        thrower1GameCount = Entry(thrower1Frame, width=5, font=('ariel', 30, 'bold'), justify=CENTER, relief=SUNKEN,
                                  borderwidth=3)
        thrower1GameCount.grid(row=3, column=3)

        thrower1GameCountPlus = Button(thrower1Frame, text="+", width=2, height=2)
        thrower1GameCountPlus.grid(row=3, column=3, sticky=E)

        thrower1GameCountMinus = Button(thrower1Frame, text="-", width=2, height=2)
        thrower1GameCountMinus.grid(row=3, column=3, sticky=W)

        thrower1AxeFrame = LabelFrame(thrower1Frame, bg=bgcolour, width=thrower1Frame.winfo_reqwidth() - 20, height=100,
                                      relief=GROOVE, text="Axes", font=("ariel", 12, "bold"))
        thrower1AxeFrame.grid(row=4, column=2, columnspan=3, padx=5)

        thrower1Axe1UpButton = Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower1Axe1UpButton.grid(row=1, column=1, padx=20, pady=5)
        thrower1Axe2UpButton = Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower1Axe2UpButton.grid(row=1, column=2, padx=20, pady=5)
        thrower1Axe3UpButton = Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower1Axe3UpButton.grid(row=1, column=3, padx=20, pady=5)
        thrower1Axe4UpButton = Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower1Axe4UpButton.grid(row=1, column=4, padx=20, pady=5)
        thrower1Axe5UpButton = Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower1Axe5UpButton.grid(row=1, column=5, padx=20, pady=5)

        thrower1Axe1Box = Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                                borderwidth=2)
        thrower1Axe1Box.grid(row=2, column=1, pady=5)
        thrower1Axe2Box = Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                                borderwidth=2)
        thrower1Axe2Box.grid(row=2, column=2, pady=5)
        thrower1Axe3Box = Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                                borderwidth=2)
        thrower1Axe3Box.grid(row=2, column=3, pady=5)
        thrower1Axe4Box = Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                                borderwidth=2)
        thrower1Axe4Box.grid(row=2, column=4, pady=5)
        thrower1Axe5Box = Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                                borderwidth=2)
        thrower1Axe5Box.grid(row=2, column=5, pady=5)

        thrower1Axe1DownButton = Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower1Axe1DownButton.grid(row=3, column=1, pady=5)
        thrower1Axe2DownButton = Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower1Axe2DownButton.grid(row=3, column=2, pady=5)
        thrower1Axe3DownButton = Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower1Axe3DownButton.grid(row=3, column=3, pady=5)
        thrower1Axe4DownButton = Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower1Axe4DownButton.grid(row=3, column=4, pady=5)
        thrower1Axe5DownButton = Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower1Axe5DownButton.grid(row=3, column=5, pady=5)
        
    def createThrower2(self,logo):

        thrower2Frame = LabelFrame(self, bg=bgcolour, width=(w/2)-100, height=300, relief=GROOVE, text="Right Thrower", font=("ariel", 16, "bold"))
        thrower2Frame.grid(row=3, column=3, rowspan=3, padx=10)

        thrower2NameLabel = Label(thrower2Frame, bg=bgcolour, text="Name:")
        thrower2NameLabel.grid(row=1,column=2, padx=10)

        thrower2NameEntry = Entry(thrower2Frame, width=40)
        thrower2NameEntry.grid(row=1, column=3)

        thrower2NameButton = Button(thrower2Frame, text="SET")
        thrower2NameButton.grid(row=1, column=4, padx=10)

        thrower2GameLabel = Label(thrower2Frame, font=('ariel', 10, 'bold'), bg=bgcolour, text="Game Count")
        thrower2GameLabel.grid(row=2, column=3)

        thrower2GameCount = Entry(thrower2Frame, width=5, font=('ariel', 30, 'bold'), justify=CENTER, relief=SUNKEN, borderwidth=3)
        thrower2GameCount.grid(row=3, column=3)

        thrower2GameCountPlus = Button(thrower2Frame, text="+", width=2, height=2)
        thrower2GameCountPlus.grid(row=3, column=3, sticky=E)

        thrower2GameCountMinus = Button(thrower2Frame, text="-", width=2, height=2)
        thrower2GameCountMinus.grid(row=3, column=3, sticky=W)

        thrower2AxeFrame = LabelFrame(thrower2Frame, bg=bgcolour, width=thrower2Frame.winfo_reqwidth()-20, height=100, relief=GROOVE, text="Axes", font=("ariel", 12, "bold"))
        thrower2AxeFrame.grid(row=4, column=2, columnspan=3, padx=5)

        thrower2Axe1UpButton = Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower2Axe1UpButton.grid(row=1, column=1, padx=20, pady=5)
        thrower2Axe2UpButton = Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower2Axe2UpButton.grid(row=1, column=2, padx=20, pady=5)
        thrower2Axe3UpButton = Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower2Axe3UpButton.grid(row=1, column=3, padx=20, pady=5)
        thrower2Axe4UpButton = Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower2Axe4UpButton.grid(row=1, column=4, padx=20, pady=5)
        thrower2Axe5UpButton = Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"))
        thrower2Axe5UpButton.grid(row=1, column=5, padx=20, pady=5)

        thrower2Axe1Box = Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN, borderwidth=2)
        thrower2Axe1Box.grid(row=2, column=1, pady=5)
        thrower2Axe2Box = Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN, borderwidth=2)
        thrower2Axe2Box.grid(row=2, column=2, pady=5)
        thrower2Axe3Box = Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN, borderwidth=2)
        thrower2Axe3Box.grid(row=2, column=3, pady=5)
        thrower2Axe4Box = Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN, borderwidth=2)
        thrower2Axe4Box.grid(row=2, column=4, pady=5)
        thrower2Axe5Box = Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN, borderwidth=2)
        thrower2Axe5Box.grid(row=2, column=5, pady=5)

        thrower2Axe1DownButton = Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower2Axe1DownButton.grid(row=3, column=1, pady=5)
        thrower2Axe2DownButton = Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower2Axe2DownButton.grid(row=3, column=2, pady=5)
        thrower2Axe3DownButton = Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower2Axe3DownButton.grid(row=3, column=3, pady=5)
        thrower2Axe4DownButton = Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower2Axe4DownButton.grid(row=3, column=4, pady=5)
        thrower2Axe5DownButton = Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"))
        thrower2Axe5DownButton.grid(row=3, column=5, pady=5)

if __name__ == "__main__":
    app = application(None)
    app.title('BATL Stream Scoreboard')
    app.mainloop()