__author__ = 'Kelly'

from tkinter import filedialog
from tkinter import *
import os
import sys

# sys.setdefaultencoding('utf-8')
w = 1000
h = 600

bgcolour = "white"

upArrow = u"\u25B2"
downArrow = u"\u25BC"

throwList = ['-', '5', '3', 'D', '1', '0', '7']
bigAxeThrowList = ['-', u"\u2717", u"\u2713", ]

directory = "score_files"

leftAxes = [0, 0, 0, 0, 0]
rightAxes = [0, 0, 0, 0, 0]
leftBigAxes = [0, 0, 0, 0]
rightBigAxes = [0, 0, 0, 0]

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

gameCount = [0, 0]

gameScore = []

score = [0, 0]

gameBox = []

matchTitleEntry = ""

pathSetEntry = ""


class application(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.resizable(width=False, height=False)
        self.configure(background=bgcolour)
        self.initialize_ui()
        self.set_boxes()
        self.update_text()
        self.update_files()

    def initialize_ui(self):
        global directory

        directory = filedialog.askdirectory()

        if not os.path.exists(directory):
            os.makedirs(directory)

        matchTitleLabelFrame = LabelFrame(self, bg=bgcolour, width=1000, text="Match", relief=GROOVE,
                                          font=("ariel", 16, "bold"))
        matchTitleLabelFrame.grid(row=2, column=1, columnspan=3, padx=50)

        global matchTitleEntry

        matchTitleEntry = Entry(matchTitleLabelFrame, width=40, font=('ariel', 10, 'bold'), relief=SUNKEN,
                                borderwidth=3)
        matchTitleButton = Button(
            matchTitleLabelFrame, text="Set", command=lambda: self.update_text())

        matchTitleEntry.grid(row=2, column=2, sticky=E, padx=(100, 0))
        matchTitleButton.grid(row=2, column=3, sticky=W, padx=(0, 100))

        self.create_thrower1()
        self.create_thrower2()

        switchButton = Button(self, text="<- SWITCH ->",
                              command=lambda: self.switch_sides())
        switchButton.grid(row=3, column=2, padx=20)
        resetButton = Button(self, text="RESET",
                             command=lambda: self.reset_info())
        resetButton.grid(row=4, column=2)

        nextGameButton = Button(self, text="Next Game", width=60, height=2, font=('ariel', 16, 'bold'),
                                command=lambda: self.next_game())
        nextGameButton.grid(row=7, column=1, columnspan=3, pady=5)

    def set_boxes(self):

        for i in range(0, 2):
            gameBox[i].delete(0, 'end')
            gameBox[i].insert(0, gameCount[i])
        for i in range(0, 2):
            gameScore[i].delete(0, 'end')
            gameScore[i].insert(0, score[i])
        for i in range(0, 5):
            thrower1AxeBoxes[i].delete(0, 'end')
            thrower1AxeBoxes[i].insert(0, throwList[leftAxes[i]])
            thrower2AxeBoxes[i].delete(0, 'end')
            thrower2AxeBoxes[i].insert(0, throwList[rightAxes[i]])
        for i in range(0, 3):
            thrower1BigAxeBoxes[i].delete(0, 'end')
            thrower1BigAxeBoxes[i].insert(0, bigAxeThrowList[leftBigAxes[i]])
            thrower2BigAxeBoxes[i].delete(0, 'end')
            thrower2BigAxeBoxes[i].insert(0, bigAxeThrowList[rightBigAxes[i]])
        thrower1BigAxeBoxes[3].delete(0, 'end')
        thrower1BigAxeBoxes[3].insert(0, throwList[leftBigAxes[3]])
        thrower2BigAxeBoxes[3].delete(0, 'end')
        thrower2BigAxeBoxes[3].insert(0, throwList[rightBigAxes[3]])

    def update_game_score(self, side):
        if side == 0:
            score[0] = sum([int(x) for x in [throwList[y]
                                         for y in leftAxes] if str(x).isdigit()])
            gameScore[0].delete(0, 'end')
            gameScore[0].insert(0, score[0])
            file = open(directory + "/thrower_1_game_score.txt", "w")
            file.write(str(score[0]))
            file.close()
        else:
            score[1] = sum([int(x) for x in [throwList[y]
                                         for y in rightAxes] if str(x).isdigit()])
            gameScore[1].delete(0, 'end')
            gameScore[1].insert(0, score[1])
            file = open(directory + "/thrower_2_game_score.txt", "w")
            file.write(str(score[1]))
            file.close()

    def change_axe(self, position, direction, side):
        global directory

        if position != 4:
            if side == 0:
                if ((direction == 1 and leftAxes[position] < len(throwList) - 2) or (
                        direction == -1 and leftAxes[position] > 0)):
                    leftAxes[position] += direction
                    thrower1AxeBoxes[position].delete(0, 'end')
                    thrower1AxeBoxes[position].insert(0, throwList[leftAxes[position]])
                    file = open(f"{directory}/thrower_1_axe_{position + 1}.txt", "w")
                    file.write(str(throwList[leftAxes[position]]))
                    file.close()
                    self.update_game_score(side)
            else:
                if ((direction == 1 and rightAxes[position] < len(throwList) - 2) or (
                        direction == -1 and rightAxes[position] > 0)):
                    rightAxes[position] += direction
                    thrower2AxeBoxes[position].delete(0, 'end')
                    thrower2AxeBoxes[position].insert(0, throwList[rightAxes[position]])
                    file = open(f"{directory}/thrower_2_axe_{position + 1}.txt", "w")
                    file.write(str(throwList[rightAxes[position]]))
                    file.close()
                    self.update_game_score(side)
        else:
            if side == 0:
                if ((direction == 1 and leftAxes[position] < len(throwList) - 1) or (
                        direction == -1 and leftAxes[position] > 0)):
                    leftAxes[position] += direction
                    thrower1AxeBoxes[position].delete(0, 'end')
                    thrower1AxeBoxes[position].insert(0, throwList[leftAxes[position]])
                    file = open(f"{directory}/thrower_1_axe_{position + 1}.txt", "w")
                    file.write(str(throwList[leftAxes[position]]))
                    file.close()
                    self.update_game_score(side)
            else:
                if ((direction == 1 and rightAxes[position] < len(throwList) - 1) or (
                        direction == -1 and rightAxes[position] > 0)):
                    rightAxes[position] += direction
                    thrower2AxeBoxes[position].delete(0, 'end')
                    thrower2AxeBoxes[position].insert(0, throwList[rightAxes[position]])
                    file = open(f"{directory}/thrower_2_axe_{position + 1}.txt", "w")
                    file.write(str(throwList[rightAxes[position]]))
                    file.close()
                    self.update_game_score(side)

    def change_big_axe(self, position, direction, side):
        global directory

        if position != 3:
            if side == 0:
                if ((direction == 1 and leftBigAxes[position] < len(bigAxeThrowList) - 1) or (
                        direction == -1 and leftBigAxes[position] > 0)):
                    leftBigAxes[position] += direction
                    thrower1BigAxeBoxes[position].delete(0, 'end')
                    thrower1BigAxeBoxes[position].insert(0, bigAxeThrowList[leftBigAxes[position]])
                    file = open(f"{directory}/thrower_1_big_axe_{position + 1}.txt", "wb")
                    file.write(bigAxeThrowList[leftBigAxes[position]].encode('utf8'))
                    file.close()
            else:
                if ((direction == 1 and rightBigAxes[position] < len(bigAxeThrowList) - 1) or (
                        direction == -1 and rightBigAxes[position] > 0)):
                    rightBigAxes[position] += direction
                    thrower2BigAxeBoxes[position].delete(0, 'end')
                    thrower2BigAxeBoxes[position].insert(0, bigAxeThrowList[rightBigAxes[position]])
                    file = open(f"{directory}/thrower_2_big_axe_{position + 1}.txt", "wb")
                    file.write(bigAxeThrowList[rightBigAxes[position]].encode('utf8'))
                    file.close()
        else:
            if side == 0:
                if ((direction == 1 and leftBigAxes[position] < len(throwList) - 1) or (
                        direction == -1 and leftBigAxes[position] > 0)):
                    leftBigAxes[position] += direction
                    thrower1BigAxeBoxes[position].delete(0, 'end')
                    thrower1BigAxeBoxes[position].insert(0, throwList[leftBigAxes[position]])
                    file = open(f"{directory}/thrower_1_big_axe_point.txt", "w")
                    file.write(str(throwList[leftBigAxes[position]]))
                    file.close()
            else:
                if ((direction == 1 and rightBigAxes[position] < len(throwList) - 1) or (
                        direction == -1 and rightBigAxes[position] > 0)):
                    rightBigAxes[position] += direction
                    thrower2BigAxeBoxes[position].delete(0, 'end')
                    thrower2BigAxeBoxes[position].insert(0, throwList[rightBigAxes[position]])
                    file = open(f"{directory}/thrower_2_big_axe_point.txt", "w")
                    file.write(str(throwList[rightBigAxes[position]]))
                    file.close()

    def change_game_count(self, side, direction):
        if gameCount[side] != 0 or direction == 1:
            gameCount[side] += direction
            gameBox[side].delete(0, 'end')
            gameBox[side].insert(0, gameCount[side])

    def set_folder(self):
        global folderPath
        folderPath = filedialog.askdirectory()
        pathSetEntry.delete(0, 'end')
        pathSetEntry.insert(0, folderPath)

    def switch_sides(self):
        self.switch_info()

    def next_game(self):
        winner_determined = self.determine_winner()
        if winner_determined:
            self.reset_axes()
            self.switch_info()

    def update_game_count(self):
        gameBox[0].delete(0, 'end')
        gameBox[0].insert(0, gameCount[0])
        gameBox[1].delete(0, 'end')
        gameBox[1].insert(0, gameCount[1])

    def determine_winner(self):
        leftSum = sum([int(x) for x in [throwList[y]
                                        for y in leftAxes] if str(x).isdigit()]) + sum(leftBigAxes)
        rightSum = sum([int(x) for x in [throwList[y]
                                         for y in rightAxes] if str(x).isdigit()]) + sum(rightBigAxes)
        if leftSum > rightSum:
            self.change_game_count(0, 1)
            return True
        elif rightSum > leftSum:
            self.change_game_count(1, 1)
            return True
        return False

    def switch_info(self):
        gameCount[0], gameCount[1] = gameCount[1], gameCount[0]
        score[0], score[1] = score[1], score[0]
        temp = throwerNames[0].get()
        throwerNames[0].delete(0, 'end')
        throwerNames[0].insert(0, throwerNames[1].get())
        throwerNames[1].delete(0, 'end')
        throwerNames[1].insert(0, temp)
        global leftAxes
        global rightAxes
        leftAxes, rightAxes = rightAxes, leftAxes
        self.set_boxes()
        self.update_text()
        self.update_files()

    def reset_info(self):
        self.reset_axes()
        gameCount[0] = 0
        gameCount[1] = 0
        score[0] = 0
        score[1] = 0
        throwerNames[0].delete(0, 'end')
        throwerNames[1].delete(0, 'end')
        global matchTitleEntry
        matchTitleEntry.delete(0, 'end')
        self.set_boxes()
        self.update_text()
        self.update_files()

    def reset_axes(self):
        global leftAxes
        global rightAxes
        global leftBigAxes
        global rightBigAxes
        score[0] = 0
        score[1] = 0
        leftAxes = [0, 0, 0, 0, 0]
        rightAxes = [0, 0, 0, 0, 0]
        leftBigAxes = [0, 0, 0, 0]
        rightBigAxes = [0, 0, 0, 0]

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
        file = open(directory + "/thrower_1_axe_1.txt", "w")
        file.write(str(throwList[leftAxes[0]]))
        file.close()
        file = open(directory + "/thrower_1_axe_2.txt", "w")
        file.write(str(throwList[leftAxes[1]]))
        file.close()
        file = open(directory + "/thrower_1_axe_3.txt", "w")
        file.write(str(throwList[leftAxes[2]]))
        file.close()
        file = open(directory + "/thrower_1_axe_4.txt", "w")
        file.write(str(throwList[leftAxes[3]]))
        file.close()
        file = open(directory + "/thrower_1_axe_5.txt", "w")
        file.write(str(throwList[leftAxes[4]]))
        file.close()

        # Thrower 2 axes
        file = open(directory + "/thrower_2_axe_1.txt", "w")
        file.write(str(throwList[rightAxes[0]]))
        file.close()
        file = open(directory + "/thrower_2_axe_2.txt", "w")
        file.write(str(throwList[rightAxes[1]]))
        file.close()
        file = open(directory + "/thrower_2_axe_3.txt", "w")
        file.write(str(throwList[rightAxes[2]]))
        file.close()
        file = open(directory + "/thrower_2_axe_4.txt", "w")
        file.write(str(throwList[rightAxes[3]]))
        file.close()
        file = open(directory + "/thrower_2_axe_5.txt", "w")
        file.write(str(throwList[rightAxes[4]]))
        file.close()

        # Thrower 1 big axes
        file = open(directory + "/thrower_1_big_axe_1.txt", "wb")
        file.write(bigAxeThrowList[leftBigAxes[0]].encode('utf8'))
        file.close()
        file = open(directory + "/thrower_1_big_axe_2.txt", "wb")
        file.write(bigAxeThrowList[leftBigAxes[1]].encode('utf8'))
        file.close()
        file = open(directory + "/thrower_1_big_axe_3.txt", "wb")
        file.write(bigAxeThrowList[leftBigAxes[2]].encode('utf8'))
        file.close()
        file = open(directory + "/thrower_1_big_axe_point.txt", "w")
        file.write(str(throwList[leftBigAxes[3]]))
        file.close()

        # Thrower 2 big axes
        file = open(directory + "/thrower_2_big_axe_1.txt", "wb")
        file.write(bigAxeThrowList[rightBigAxes[0]].encode('utf8'))
        file.close()
        file = open(directory + "/thrower_2_big_axe_2.txt", "wb")
        file.write(bigAxeThrowList[rightBigAxes[1]].encode('utf8'))
        file.close()
        file = open(directory + "/thrower_2_big_axe_3.txt", "wb")
        file.write(bigAxeThrowList[rightBigAxes[2]].encode('utf8'))
        file.close()
        file = open(directory + "/thrower_2_big_axe_point.txt", "w")
        file.write(str(throwList[rightBigAxes[3]]))
        file.close()

    def create_thrower1(self):
        thrower1Frame = LabelFrame(self, bg=bgcolour, width=(w / 2) - 100, height=300, relief=GROOVE,
                                   text="Left Thrower", font=("ariel", 16, "bold"))
        thrower1Frame.grid(row=3, column=1, rowspan=3, padx=10)

        thrower1NameLabel = Label(thrower1Frame, bg=bgcolour, text="Name:")
        thrower1NameLabel.grid(row=1, column=2, padx=10)

        throwerNames.append(Entry(thrower1Frame, width=40))
        throwerNames[0].grid(row=1, column=3)

        thrower1NameButton = Button(
            thrower1Frame, text="SET", command=lambda: self.update_text())
        thrower1NameButton.grid(row=1, column=4, padx=10)

        thrower1GameLabel = Label(thrower1Frame, font=(
            'ariel', 10, 'bold'), bg=bgcolour, text="Game Count")
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

        for i in range(0, 5):
            thrower1UpButtons.append(Button(thrower1AxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                            command=lambda i=i: self.change_axe(i, 1, 0)))
            thrower1UpButtons[i].grid(row=1, column=i + 1, padx=20, pady=5)

        for i in range(0, 5):
            thrower1AxeBoxes.append(
                Entry(thrower1AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower1AxeBoxes[i].grid(row=2, column=i + 1, pady=5)

        for i in range(0, 5):
            thrower1DownButtons.append(Button(thrower1AxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                              command=lambda i=i: self.change_axe(i, -1, 0)))
            thrower1DownButtons[i].grid(row=3, column=i + 1, pady=5)

        thrower1BigAxeFrame = LabelFrame(thrower1Frame, bg=bgcolour, width=thrower1Frame.winfo_reqwidth() - 20,
                                         height=100,
                                         relief=GROOVE, text="Big Axe", font=("ariel", 12, "bold"))
        thrower1BigAxeFrame.grid(row=7, column=2, columnspan=3, padx=5)

        thrower1BigAxePaintFrame = LabelFrame(thrower1BigAxeFrame, bg=bgcolour,
                                              width=thrower1Frame.winfo_reqwidth() - 20, height=100,
                                              relief=GROOVE, text="Paint", font=("ariel", 12, "bold"))
        thrower1BigAxePaintFrame.grid(row=1, column=1, columnspan=1, padx=5)

        for i in range(0, 3):
            thrower1BigUpButtons.append(Button(thrower1BigAxePaintFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i: self.change_big_axe(i, 1, 0)))
            thrower1BigUpButtons[i].grid(row=1, column=i + 1, padx=20, pady=5)

        for i in range(0, 3):
            thrower1BigAxeBoxes.append(
                Entry(thrower1BigAxePaintFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower1BigAxeBoxes[i].grid(row=2, column=i + 1, pady=5)

        for i in range(0, 3):
            thrower1BigDownButtons.append(Button(thrower1BigAxePaintFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i: self.change_big_axe(i, -1, 0)))
            thrower1BigDownButtons[i].grid(row=3, column=i + 1, pady=5)

        thrower1BigAxePointFrame = LabelFrame(thrower1BigAxeFrame, bg=bgcolour,
                                              width=thrower1Frame.winfo_reqwidth() - 20, height=100,
                                              relief=GROOVE, text="Points", font=("ariel", 12, "bold"))
        thrower1BigAxePointFrame.grid(row=1, column=2, columnspan=1, padx=5)

        for i in range(0, 1):
            thrower1BigUpButtons.append(Button(thrower1BigAxePointFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i: self.change_big_axe(3, 1, 0)))
            thrower1BigUpButtons[3].grid(row=1, column=i + 1, padx=20, pady=5)

        for i in range(0, 1):
            thrower1BigAxeBoxes.append(
                Entry(thrower1BigAxePointFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower1BigAxeBoxes[3].grid(row=2, column=i + 1, pady=5)

        for i in range(0, 1):
            thrower1BigDownButtons.append(Button(thrower1BigAxePointFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i: self.change_big_axe(3, -1, 0)))
            thrower1BigDownButtons[3].grid(row=3, column=i + 1, pady=5)

    def create_thrower2(self):

        thrower2Frame = LabelFrame(self, bg=bgcolour, width=(w / 2) - 100, height=300, relief=GROOVE,
                                   text="Right Thrower", font=("ariel", 16, "bold"))
        thrower2Frame.grid(row=3, column=3, rowspan=3, padx=10)

        thrower2NameLabel = Label(thrower2Frame, bg=bgcolour, text="Name:")
        thrower2NameLabel.grid(row=1, column=2, padx=10)

        throwerNames.append(Entry(thrower2Frame, width=40))
        throwerNames[1].grid(row=1, column=3)

        thrower2NameButton = Button(
            thrower2Frame, text="SET", command=lambda: self.update_text())
        thrower2NameButton.grid(row=1, column=4, padx=10)

        thrower2GameLabel = Label(thrower2Frame, font=(
            'ariel', 10, 'bold'), bg=bgcolour, text="Game Count")
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

        for i in range(0, 5):
            thrower2UpButtons.append(Button(thrower2AxeFrame, text=upArrow, font=("ariel", 7, "bold"),
                                            command=lambda i=i: self.change_axe(i, 1, 1)))
            thrower2UpButtons[i].grid(row=1, column=i + 1, padx=20, pady=5)

        for i in range(0, 5):
            thrower2AxeBoxes.append(
                Entry(thrower2AxeFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower2AxeBoxes[i].grid(row=2, column=i + 1, pady=5)

        for i in range(0, 5):
            thrower2DownButtons.append(Button(thrower2AxeFrame, text=downArrow, font=("ariel", 7, "bold"),
                                              command=lambda i=i: self.change_axe(i, -1, 1)))
            thrower2DownButtons[i].grid(row=3, column=i + 1, pady=5)

        thrower2BigAxeFrame = LabelFrame(thrower2Frame, bg=bgcolour, width=thrower2Frame.winfo_reqwidth() - 20,
                                         height=100,
                                         relief=GROOVE, text="Big Axe", font=("ariel", 12, "bold"))
        thrower2BigAxeFrame.grid(row=7, column=2, columnspan=3, padx=5)

        thrower2BigAxePaintFrame = LabelFrame(thrower2BigAxeFrame, bg=bgcolour,
                                              width=thrower2Frame.winfo_reqwidth() - 20, height=100,
                                              relief=GROOVE, text="Paint", font=("ariel", 12, "bold"))
        thrower2BigAxePaintFrame.grid(row=1, column=1, columnspan=1, padx=5)

        for i in range(0, 3):
            thrower2BigUpButtons.append(Button(thrower2BigAxePaintFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i: self.change_big_axe(i, 1, 1)))
            thrower2BigUpButtons[i].grid(row=1, column=i + 1, padx=20, pady=5)

        for i in range(0, 3):
            thrower2BigAxeBoxes.append(
                Entry(thrower2BigAxePaintFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower2BigAxeBoxes[i].grid(row=2, column=i + 1, pady=5)

        for i in range(0, 3):
            thrower2BigDownButtons.append(Button(thrower2BigAxePaintFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i: self.change_big_axe(i, -1, 1)))
            thrower2BigDownButtons[i].grid(row=3, column=i + 1, pady=5)

        thrower2BigAxePointFrame = LabelFrame(thrower2BigAxeFrame, bg=bgcolour,
                                              width=thrower2Frame.winfo_reqwidth() - 20, height=100,
                                              relief=GROOVE, text="Points", font=("ariel", 12, "bold"))
        thrower2BigAxePointFrame.grid(row=1, column=2, columnspan=1, padx=5)

        for i in range(0, 1):
            thrower2BigUpButtons.append(Button(thrower2BigAxePointFrame, text=upArrow, font=("ariel", 7, "bold"),
                                               command=lambda i=i: self.change_big_axe(3, 1, 1)))
            thrower2BigUpButtons[3].grid(row=1, column=i + 1, padx=20, pady=5)

        for i in range(0, 1):
            thrower2BigAxeBoxes.append(
                Entry(thrower2BigAxePointFrame, width=2, font=('ariel', 12, 'bold'), justify=CENTER, relief=SUNKEN,
                      borderwidth=2))
            thrower2BigAxeBoxes[3].grid(row=2, column=i + 1, pady=5)

        for i in range(0, 1):
            thrower2BigDownButtons.append(Button(thrower2BigAxePointFrame, text=downArrow, font=("ariel", 7, "bold"),
                                                 command=lambda i=i: self.change_big_axe(3, -1, 1)))
            thrower2BigDownButtons[3].grid(row=3, column=i + 1, pady=5)


if __name__ == "__main__":
    app = application(None)
    app.title('Axe Throwing Stream Scoreboard')
    app.mainloop()
