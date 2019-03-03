__author__ = 'Kelly'

from tkinter import filedialog
from tkinter import *
import tkinter.ttk
import os
import sys
# sys.setdefaultencoding('utf-8')
w = 1000
h = 600
bgcolour = "white"
upArrow = u"\u25B2"
downArrow = u"\u25BC"
checkmark = u"\u2713"
throwList = ['-', '5', '3', 'D', '1', '0', '7']
bigAxeThrowList = ['-', u"\u2717", u"\u2713",]
directory = "score_files"
leftAxes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
rightAxes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
leftBigAxes = [0, 0, 0, 0, 0, 0]
rightBigAxes = [0, 0, 0, 0, 0, 0]

throwerNames = []

thrower1UpButtons = []
thrower1AxeBoxes = []
thrower1DownButtons = []

thrower2UpButtons = []
thrower2AxeBoxes = []
thrower2DownButtons = []

thrower1BigUpButtons = []
thrower1BigAxeBoxes = []
thrower1BigDownButtons = []

thrower2BigUpButtons = []
thrower2BigAxeBoxes = []
thrower2BigDownButtons = []

gameCount = [-1, -1]

gameScore = []

score = [0,0]

gameBox = []

matchTitleEntry = ""

pathSetEntry = ""


class application(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        # self.geometry(str(w) + "x" + str(h))
        self.resizable(width=False, height=False)
        self.configure(background=bgcolour)
        self.initialize()
        self.update_axes()
        self.update_big_axes()
        self.change_game_count(0, 1)
        self.change_game_count(1, 1)

    def initialize(self):
        if not os.path.exists(directory):
            os.makedirs(directory)

        matchTitleLabelFrame = LabelFrame(self, bg=bgcolour, width=1000, text="Match", relief=GROOVE,
                                          font=("ariel", 16, "bold"))
        matchTitleLabelFrame.grid(row=2, column=1, columnspan=3, padx=50)

        global matchTitleEntry

        matchTitleEntry = Entry(matchTitleLabelFrame, width=40, font=('ariel', 10, 'bold'), relief=SUNKEN,
                                borderwidth=3)
        matchTitleButton = Button(matchTitleLabelFrame, text="Set", command=lambda: self.update_text())

        matchTitleEntry.grid(row=2, column=2, sticky=E, padx=(100, 0))
        matchTitleButton.grid(row=2, column=3, sticky=W, padx=(0, 100))

        self.create_thrower1()
        self.create_thrower2()

        switchButton = Button(self, text="<- SWITCH ->", command=lambda: self.switch_sides())
        switchButton.grid(row=3, column=2, padx=20)
        resetButton = Button(self, text="RESET", command=lambda: self.reset_info())
        resetButton.grid(row=4, column=2)
        updateButton = Button(self, text="UPDATE", width=60, height=2, font=('ariel', 16, 'bold'),
                              command=lambda: self.update_files())
        updateButton.grid(row=6, column=1, columnspan=3, pady=5)
        nextGameButton = Button(self, text="Next Game", width=60, height=2, font=('ariel', 16, 'bold'),
                                command=lambda: self.next_game())
        nextGameButton.grid(row=7, column=1, columnspan=3, pady=5)

    def update_axes(self):
        for i in range(0, thrower1AxeBoxes.__len__()):
            thrower1AxeBoxes[i].delete(0, 'end')
            if (i < 10):
                thrower1AxeBoxes[i].insert(0, throwList[leftAxes[i]])
            else:
                thrower1AxeBoxes[i].insert(0, bigAxeThrowList[leftAxes[i]])
        for i in range(0, thrower2AxeBoxes.__len__()):
            thrower2AxeBoxes[i].delete(0, 'end')
            if (i < 10):
                thrower2AxeBoxes[i].insert(0, throwList[rightAxes[i]])
            else:
                thrower2AxeBoxes[i].insert(0, bigAxeThrowList[rightAxes[i]])
        self.update_game_score()
        self.update_files()

    def update_game_score(self):
        score[0] = sum([int(x) for x in [throwList[y] for y in leftAxes[:-2]] if str(x).isdigit()])
        score[1] = sum([int(x) for x in [throwList[y] for y in rightAxes[:-2]] if str(x).isdigit()])
        gameScore[0].delete(0, 'end')
        gameScore[0].insert(0, score[0])
        gameScore[1].delete(0, 'end')
        gameScore[1].insert(0, score[1])

    def update_big_axes(self):
        for i in range(0, thrower1BigAxeBoxes.__len__()):
            thrower1BigAxeBoxes[i].delete(0, 'end')
            thrower1BigAxeBoxes[i].insert(0, throwList[leftBigAxes[i]])
        for i in range(0, thrower2BigAxeBoxes.__len__()):
            thrower2BigAxeBoxes[i].delete(0, 'end')
            thrower2BigAxeBoxes[i].insert(0, throwList[rightBigAxes[i]])
        self.update_files()

    def change_axe(self, position, direction, side):
        if (position <= 7):
            if (side == 0):
                if ((direction == 1 and leftAxes[position] < len(throwList) - 2) or (
                        direction == -1 and leftAxes[position] > 0)):
                    leftAxes[position] += direction
                    self.update_axes()
            else:
                if ((direction == 1 and rightAxes[position] < len(throwList) - 2) or (
                        direction == -1 and rightAxes[position] > 0)):
                    rightAxes[position] += direction
                    self.update_axes()
        elif (position <=9):
            if (side == 0):
                if ((direction == 1 and leftAxes[position] < len(throwList) - 1) or (
                        direction == -1 and leftAxes[position] > 0)):
                    leftAxes[position] += direction
                    self.update_axes()
            else:
                if ((direction == 1 and rightAxes[position] < len(throwList) - 1) or (
                        direction == -1 and rightAxes[position] > 0)):
                    rightAxes[position] += direction
                    self.update_axes()
        else:
            if (side == 0):
                if ((direction == 1 and leftAxes[position] < len(bigAxeThrowList) - 1) or (
                        direction == -1 and leftAxes[position] > 0)):
                    leftAxes[position] += direction
                    self.update_axes()
            else:
                if ((direction == 1 and rightAxes[position] < len(bigAxeThrowList) - 1) or (
                        direction == -1 and rightAxes[position] > 0)):
                    rightAxes[position] += direction
                    self.update_axes()

    def change_big_axe(self, position, direction, side):
        if (side == 0):
            if ((direction == 1 and leftBigAxes[position] < len(throwList) - 1) or (
                    direction == -1 and leftBigAxes[position] > 0)):
                leftBigAxes[position] += direction
                self.update_big_axes()
        else:
            if ((direction == 1 and rightBigAxes[position] < len(throwList) - 1) or (
                    direction == -1 and rightBigAxes[position] > 0)):
                rightBigAxes[position] += direction
                self.update_big_axes()

    def change_game_count(self, side, direction):
        if (gameCount[side] != 0 or direction == 1):
            gameCount[side] += direction
            gameBox[side].delete(0, 'end')
            gameBox[side].insert(0, gameCount[side])
            self.update_files()
        elif (direction == 0):
            gameBox[0].delete(0, 'end')
            gameBox[0].insert(0, gameCount[0])
            gameBox[1].delete(0, 'end')
            gameBox[1].insert(0, gameCount[1])
            self.update_files()

    def set_folder(self):
        global folderPath
        folderPath = filedialog.askdirectory()
        pathSetEntry.delete(0, 'end')
        pathSetEntry.insert(0, folderPath)
        self.update_files()

    def switch_sides(self):
        self.switch_info()
        self.update_files()

    def next_game(self):
        self.determine_winner()
        self.switch_info()
        self.reset_axes()
        self.update_files()

    def update_game_count(self):
        gameBox[0].delete(0, 'end')
        gameBox[0].insert(0, gameCount[0])
        gameBox[1].delete(0, 'end')
        gameBox[1].insert(0, gameCount[1])
        self.update_files()

    def determine_winner(self):
        leftSum = sum([int(x) for x in [throwList[y] for y in leftAxes[:-2]] if str(x).isdigit()]) + leftAxes[10] + leftAxes[11] + sum(leftBigAxes)
        leftBigAxeSum = sum([int(x) for x in [throwList[y] for y in leftBigAxes] if str(x).isdigit()])
        rightSum = sum([int(x) for x in [throwList[y] for y in rightAxes[:-2]] if str(x).isdigit()]) + rightAxes[10] + rightAxes[11] + sum(rightBigAxes)
        rightBigAxeSum = sum([int(x) for x in [throwList[y] for y in rightBigAxes] if str(x).isdigit()])
        leftSum += leftBigAxeSum
        rightSum += rightBigAxeSum
        if leftSum > rightSum:
            self.change_game_count(0, 1)
        else:
            self.change_game_count(1, 1)

    def switch_info(self):
        gameCount[0], gameCount[1] = gameCount[1], gameCount[0]
        self.update_game_count()
        temp = throwerNames[0].get()
        throwerNames[0].delete(0, 'end')
        throwerNames[0].insert(0, throwerNames[1].get())
        throwerNames[1].delete(0, 'end')
        throwerNames[1].insert(0, temp)
        global leftAxes
        global rightAxes
        leftAxes, rightAxes = rightAxes, leftAxes
        self.update_axes()
        self.update_text()

    def reset_info(self):
        self.reset_axes()
        gameCount[0] = 0
        gameCount[1] = 0
        self.change_game_count(0, 0)
        self.change_game_count(1, 0)
        throwerNames[0].delete(0, 'end')
        throwerNames[1].delete(0, 'end')
        global matchTitleEntry
        matchTitleEntry.delete(0, 'end')
        self.update_files()

    def reset_axes(self):
        global leftAxes
        global rightAxes
        global leftBigAxes
        global rightBigAxes
        leftAxes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        rightAxes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        leftBigAxes = [0, 0, 0, 0, 0, 0]
        rightBigAxes = [0, 0, 0, 0, 0, 0]
        self.update_axes()
        self.update_big_axes()

    def update_text(self):
        # Match Name
        global directory
        file = open(directory + "/match_title.txt", "w")
        file.write(matchTitleEntry.get())
        file.close()

        # Player Names
        file = open(directory + "/thrower_1_name.txt", "w")
        file.write(throwerNames[0].get())
        file.close()
        file = open(directory + "/thrower_2_name.txt", "w")
        file.write(throwerNames[1].get())
        file.close()

    def update_files(self):
        # Match Name
        global directory

        # Game counts
        file = open(directory + "/thrower_1_game_count.txt", "w")
        file.write(str(gameCount[0]))
        file.close()
        file = open(directory + "/thrower_2_game_count.txt", "w")
        file.write(str(gameCount[1]))
        file.close()

        # Game scores
        file = open(directory + "/thrower_1_game_score.txt", "w")
        file.write(str(score[0]))
        file.close()
        file = open(directory + "/thrower_2_game_score.txt", "w")
        file.write(str(score[1]))
        file.close()

        # Thrower 1 axes
        for axe in range(0, 10):
            file = open(directory + f"/thrower_1_axe_{axe+1}.txt", "w")
            file.write(str(throwList[leftAxes[axe]]))
            file.close()
        for axe in range(10, 12):
            file = open(directory + f"/thrower_1_axe_{axe+1}.txt", "wb")
            file.write(str(bigAxeThrowList[leftAxes[axe]]).encode('utf8'))
            file.close()

        # Thrower 2 axes
        for axe in range(0, 10):
            file = open(directory + f"/thrower_2_axe_{axe+1}.txt", "w")
            file.write(str(throwList[rightAxes[axe]]))
            file.close()
        for axe in range(10, 12):
            file = open(directory + f"/thrower_2_axe_{axe+1}.txt", "wb")
            file.write(str(bigAxeThrowList[rightAxes[axe]]).encode('utf8'))
            file.close()

        # Thrower 1 big axes
        for axe in range(0, 6):
            file = open(directory + f"/thrower_1_big_axe_{axe+1}.txt", "w")
            file.write(str(throwList[leftBigAxes[axe]]))
            file.close()

        # Thrower 2 big axes
        for axe in range(0, 6):
            file = open(directory + f"/thrower_2_big_axe_{axe+1}.txt", "w")
            file.write(str(throwList[rightBigAxes[axe]]))
            file.close()

    def create_thrower1(self):
        thrower1Frame = LabelFrame(self, bg=bgcolour, width=(w / 2) - 100, height=300, relief=GROOVE,
                                   text="Left Thrower", font=("ariel", 16, "bold"))
        thrower1Frame.grid(row=3, column=1, rowspan=3, padx=10)

        thrower1NameLabel = Label(thrower1Frame, bg=bgcolour, text="Name:")
        thrower1NameLabel.grid(row=1, column=2, padx=10)

        throwerNames.append(Entry(thrower1Frame, width=40))
        throwerNames[0].grid(row=1, column=3)

        thrower1NameButton = Button(thrower1Frame, text="SET", command=lambda: self.update_text())
        thrower1NameButton.grid(row=1, column=4, padx=10)

        thrower1GameLabel = Label(thrower1Frame, font=('ariel', 10, 'bold'), bg=bgcolour, text="Game Count")
        thrower1GameLabel.grid(row=2, column=3)

        gameBox.append(Entry(thrower1Frame, width=5, font=('ariel', 30, 'bold'), justify=CENTER, relief=SUNKEN,
                             borderwidth=3))
        gameBox[0].grid(row=3, column=3)

        thrower1GameCountPlus = Button(thrower1Frame, text="+", width=2, height=2,
                                       command=lambda: self.change_game_count(0, 1))
        thrower1GameCountPlus.grid(row=3, column=3, sticky=E)

        thrower1GameCountMinus = Button(thrower1Frame, text="-", width=2, height=2,
                                        command=lambda: self.change_game_count(0, -1))
        thrower1GameCountMinus.grid(row=3, column=3, sticky=W)

        gameScore.append(Entry(thrower1Frame, width=5, font=('ariel', 30, 'bold'), justify=CENTER, relief=SUNKEN,
                             borderwidth=3))
        gameScore[0].grid(row=4, column=3)

        thrower1AxeFrame = LabelFrame(thrower1Frame, bg=bgcolour, width=thrower1Frame.winfo_reqwidth() - 20, height=100,
                                      relief=GROOVE, text="Axes", font=("ariel", 12, "bold"))
        thrower1AxeFrame.grid(row=5, column=2, columnspan=3, padx=5)

        for i in range(0, 11, 2):
            thrower1UpButtons.append(Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                            command=lambda i=i: self.change_axe(i, 1, 0)))
            thrower1UpButtons[i].grid(row=1, column=i +1, padx=2, pady=5)
            thrower1UpButtons.append(Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                            command=lambda i=i+1: self.change_axe(i, 1, 0)))
            thrower1UpButtons[i+1].grid(row=1, column=i + 2, padx=(2,10), pady=5)

        for i in range(0, 11, 2):
            thrower1AxeBoxes.append(
                Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower1AxeBoxes[i].grid(row=2, column=i + 1,padx=2, pady=5)
            thrower1AxeBoxes.append(
                Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower1AxeBoxes[i+1].grid(row=2, column=i + 2,padx=(2,10), pady=5)

        for i in range(0, 11, 2):
            thrower1DownButtons.append(Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                              command=lambda i=i: self.change_axe(i, -1, 0)))
            thrower1DownButtons[i].grid(row=3, column=i + 1, padx=2, pady=5)
            thrower1DownButtons.append(Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                              command=lambda i=i+1: self.change_axe(i, -1, 0)))
            thrower1DownButtons[i+1].grid(row=3, column=i + 2, padx=(2,10), pady=5)

        thrower1BigAxeFrame = LabelFrame(thrower1Frame, bg=bgcolour, width=thrower1Frame.winfo_reqwidth() - 20,
                                         height=100,
                                         relief=GROOVE, text="Big Axe", font=("ariel", 12, "bold"))
        thrower1BigAxeFrame.grid(row=7, column=2, columnspan=3, padx=5)

        for i in range(0, 6, 2):
            thrower1BigUpButtons.append(Button(thrower1BigAxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i: self.change_big_axe(i, 1, 0)))
            thrower1BigUpButtons[i].grid(row=1, column=i + 1, padx=2, pady=5)
            thrower1BigUpButtons.append(Button(thrower1BigAxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i+1: self.change_big_axe(i, 1, 0)))
            thrower1BigUpButtons[i+1].grid(row=1, column=i + 2, padx=(2,10), pady=5)

        for i in range(0, 6, 2):
            thrower1BigAxeBoxes.append(
                Entry(thrower1BigAxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower1BigAxeBoxes[i].grid(row=2, column=i + 1, padx=2, pady=5)
            thrower1BigAxeBoxes.append(
                Entry(thrower1BigAxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower1BigAxeBoxes[i+1].grid(row=2, column=i + 2, padx=(2,10), pady=5)

        for i in range(0, 6, 2):
            thrower1BigDownButtons.append(Button(thrower1BigAxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i: self.change_big_axe(i, -1, 0)))
            thrower1BigDownButtons[i].grid(row=3, column=i + 1,padx=2, pady=5)
            thrower1BigDownButtons.append(Button(thrower1BigAxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i+1: self.change_big_axe(i, -1, 0)))
            thrower1BigDownButtons[i+1].grid(row=3, column=i + 2, padx=(2,10), pady=5)

    def create_thrower2(self):

        thrower2Frame = LabelFrame(self, bg=bgcolour, width=(w / 2) - 100, height=300, relief=GROOVE,
                                   text="Right Thrower", font=("ariel", 16, "bold"))
        thrower2Frame.grid(row=3, column=3, rowspan=3, padx=10)

        thrower2NameLabel = Label(thrower2Frame, bg=bgcolour, text="Name:")
        thrower2NameLabel.grid(row=1, column=2, padx=10)

        throwerNames.append(Entry(thrower2Frame, width=40))
        throwerNames[1].grid(row=1, column=3)

        thrower2NameButton = Button(thrower2Frame, text="SET", command=lambda: self.update_text())
        thrower2NameButton.grid(row=1, column=4, padx=10)

        thrower2GameLabel = Label(thrower2Frame, font=('ariel', 10, 'bold'), bg=bgcolour, text="Game Count")
        thrower2GameLabel.grid(row=2, column=3)

        gameBox.append(
            Entry(thrower2Frame, width=5, font=('ariel', 30, 'bold'), justify=CENTER, relief=SUNKEN, borderwidth=3))
        gameBox[1].grid(row=3, column=3)

        thrower2GameCountPlus = Button(thrower2Frame, text="+", width=2, height=2,
                                       command=lambda: self.change_game_count(1, 1))
        thrower2GameCountPlus.grid(row=3, column=3, sticky=E)

        thrower2GameCountMinus = Button(thrower2Frame, text="-", width=2, height=2,
                                        command=lambda: self.change_game_count(1, -1))
        thrower2GameCountMinus.grid(row=3, column=3, sticky=W)

        gameScore.append(Entry(thrower2Frame, width=5, font=('ariel', 30, 'bold'), justify=CENTER, relief=SUNKEN,
                               borderwidth=3))
        gameScore[1].grid(row=4, column=3)

        thrower2AxeFrame = LabelFrame(thrower2Frame, bg=bgcolour, width=thrower2Frame.winfo_reqwidth() - 20, height=100,
                                      relief=GROOVE, text="Axes", font=("ariel", 12, "bold"))
        thrower2AxeFrame.grid(row=5, column=2, columnspan=3, padx=5)

        for i in range(0, 11, 2):
            thrower2UpButtons.append(Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                            command=lambda i=i: self.change_axe(i, 1, 1)))
            thrower2UpButtons[i].grid(row=1, column=i +1, padx=2, pady=5)
            thrower2UpButtons.append(Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                            command=lambda i=i+1: self.change_axe(i, 1, 1)))
            thrower2UpButtons[i+1].grid(row=1, column=i + 2, padx=(2,10), pady=5)

        for i in range(0, 11, 2):
            thrower2AxeBoxes.append(
                Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower2AxeBoxes[i].grid(row=2, column=i + 1,padx=2, pady=5)
            thrower2AxeBoxes.append(
                Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower2AxeBoxes[i+1].grid(row=2, column=i + 2,padx=(2,10), pady=5)

        for i in range(0, 11, 2):
            thrower2DownButtons.append(Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                              command=lambda i=i: self.change_axe(i, -1, 1)))
            thrower2DownButtons[i].grid(row=3, column=i + 1, padx=2, pady=5)
            thrower2DownButtons.append(Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                              command=lambda i=i+1: self.change_axe(i, -1, 1)))
            thrower2DownButtons[i+1].grid(row=3, column=i + 2, padx=(2,10), pady=5)

        thrower2BigAxeFrame = LabelFrame(thrower2Frame, bg=bgcolour, width=thrower2Frame.winfo_reqwidth() - 20,
                                         height=100,
                                         relief=GROOVE, text="Big Axe", font=("ariel", 12, "bold"))
        thrower2BigAxeFrame.grid(row=7, column=2, columnspan=3, padx=5)

        for i in range(0, 6, 2):
            thrower2BigUpButtons.append(Button(thrower2BigAxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i: self.change_big_axe(i, 1, 1)))
            thrower2BigUpButtons[i].grid(row=1, column=i + 1, padx=2, pady=5)
            thrower2BigUpButtons.append(Button(thrower2BigAxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i+1: self.change_big_axe(i, 1, 1)))
            thrower2BigUpButtons[i+1].grid(row=1, column=i + 2, padx=(2,10), pady=5)

        for i in range(0, 6, 2):
            thrower2BigAxeBoxes.append(
                Entry(thrower2BigAxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower2BigAxeBoxes[i].grid(row=2, column=i + 1, padx=2, pady=5)
            thrower2BigAxeBoxes.append(
                Entry(thrower2BigAxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower2BigAxeBoxes[i+1].grid(row=2, column=i + 2, padx=(2,10), pady=5)

        for i in range(0, 6, 2):
            thrower2BigDownButtons.append(Button(thrower2BigAxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i: self.change_big_axe(i, -1, 1)))
            thrower2BigDownButtons[i].grid(row=3, column=i + 1, padx=2, pady=5)
            thrower2BigDownButtons.append(Button(thrower2BigAxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i+1: self.change_big_axe(i, -1, 1)))
            thrower2BigDownButtons[i+1].grid(row=3, column=i + 2, padx=(2,10), pady=5)


if __name__ == "__main__":
    app = application(None)
    app.title('Axe Throwing Stream Scoreboard')
    app.mainloop()
