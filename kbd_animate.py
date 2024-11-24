"""Keyboard Heatmap With New Layout:
Name: Deepak Charan S

Roll No: EE23B022

Date: 28.09.24

Description: To analyze keyboard usage patterns for a given keyboard layout and text input by generating a heatmap visualization of key usage. To also calculate the total distance traveled by fingers while typing. (This script implements animations on the keyboard)
"""

from collections import defaultdict  # Importing libraries
import math
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Rectangle

import pylab

cm = pylab.get_cmap("jet")  # this is the colourmap I am using

QWERTY_LAYOUT = {  # Sample layout provided in handout
    "row1": {
        "keys": "`1234567890-=",
        "positions": [
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 0),
            (4, 0),
            (5, 0),
            (6, 0),
            (7, 0),
            (8, 0),
            (9, 0),
            (10, 0),
            (11, 0),
            (12, 0),
        ],
    },
    "row2": {
        "keys": "qwertyuiop[]\\",
        "positions": [
            (0.5, 1),
            (1.5, 1),
            (2.5, 1),
            (3.5, 1),
            (4.5, 1),
            (5.5, 1),
            (6.5, 1),
            (7.5, 1),
            (8.5, 1),
            (9.5, 1),
            (10.5, 1),
            (11.5, 1),
            (12.5, 1),
        ],
    },
    "row3": {
        "keys": "asdfghjkl;'",
        "positions": [
            (0.75, 2),
            (1.75, 2),
            (2.75, 2),
            (3.75, 2),
            (4.75, 2),
            (5.75, 2),
            (6.75, 2),
            (7.75, 2),
            (8.75, 2),
            (9.75, 2),
            (10.75, 2),
        ],
    },
    "row4": {
        "keys": "zxcvbnm,./",
        "positions": [
            (1.25, 3),
            (2.25, 3),
            (3.25, 3),
            (4.25, 3),
            (5.25, 3),
            (6.25, 3),
            (7.25, 3),
            (8.25, 3),
            (9.25, 3),
            (10.25, 3),
        ],
    },
    "special_keys": {
        "Shift_L": (0, 3),
        "Shift_R": (11.25, 3),
        "Space": (3.5, 4),
        "Backspace": (13, 0),
        "Tab": (0, 1),
        "CapsLock": (0, 2),
        "Enter": (12, 2),
    },
}


class kdb_analysis:  # Using a class which performs all the necessary operations
    def __init__(self, layout):
        self.layout = layout  # Uses the layout provided by user
        self.travel = (
            self.key_dist()
        )  # Dictionary which stores the distance travelled by fingers to type each key
        self.freq = defaultdict(
            int
        )  # Dictionary which stores the stores the frequencies of each key pressed
        self.let_rank = (
            []
        )  # List which ranks the usage of each letter and is used while assinging colour
        self.fig = None  # for plotting
        self.ax = None

    def load_kyb(self):  # Loading the keyboard initially
        self.fig, self.ax = plt.subplots(figsize=(13, 4))
        # self.ax.pcolormesh(self.maze, cmap=cmap)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_xlim(-1, 15)
        self.ax.set_ylim(-1, 5)
        plt.tight_layout()
        plt.gca().invert_yaxis()
        plt.show(block=False)

    def visualise_kyb(self, s, shift_detect, end):  # Method to visualise the keyboard
        self.ax.clear()
        self.ax.set_xlim(
            -1, 15
        )  # Removing axis points (1,2,3.. on x axis wont show up)
        self.ax.set_ylim(-1, 5)

        self.ax.set_xticks([])
        self.ax.set_yticks([])
        plt.gca().invert_yaxis()

        for rows in layout:
            if (
                rows == "special_keys"
            ):  # all the special characters on the side of the keyboard
                for key in layout[rows]:
                    key_loc = self.get_key_position(key)

                    if self.freq[key] == 0:  # Key was never pressed
                        color = cm(1.0 * 0)
                    elif (
                        key == s and not end
                    ):  # Adjust its colour according to its usage
                        color = (0.5, 0.5, 0.5)
                    else:
                        color = cm(
                            1.0
                            * (
                                (self.let_rank.index(self.freq[key]) + 1)
                                / len(self.let_rank)
                            )
                        )

                    # Since the coordinates provided were quite bad and resulted in a cluttered keyboard, I decided to offset the coordinates (pushed the special keys a bit to the left/right)
                    if key == "Shift_L":

                        if shift_detect == True and self.get_key_position(
                            s
                        ) > self.get_key_position(self.layout["row3"]["keys"][4]):
                            color = (0.5, 0.5, 0.5)

                        rect = Rectangle(
                            (key_loc[0], key_loc[1]),
                            1,
                            0.75,
                            facecolor=color,
                            alpha=0.9,
                            edgecolor="black",
                        )
                        self.ax.text(
                            key_loc[0] + 0.5,
                            key_loc[1] + 0.375,
                            key,
                            horizontalalignment="center",
                            verticalalignment="center",
                        )
                        self.ax.add_patch(rect)

                    elif key == "CapsLock":
                        rect = Rectangle(
                            (key_loc[0], key_loc[1]),
                            0.6,
                            0.75,
                            facecolor=color,
                            alpha=0.9,
                            edgecolor="black",
                        )
                        self.ax.text(
                            key_loc[0] + 0.25,
                            key_loc[1] + 0.375,
                            "Caps",
                            horizontalalignment="center",
                            verticalalignment="center",
                        )
                        self.ax.add_patch(rect)

                    elif key == "Tab":
                        rect = Rectangle(
                            (key_loc[0], key_loc[1]),
                            0.35,
                            0.75,
                            facecolor=color,
                            alpha=0.9,
                            edgecolor="black",
                        )
                        self.ax.text(
                            key_loc[0] + 0.2,
                            key_loc[1] + 0.375,
                            key,
                            horizontalalignment="center",
                            verticalalignment="center",
                        )
                        self.ax.add_patch(rect)

                    elif key == "Shift_R":

                        if shift_detect == True and self.get_key_position(
                            s
                        ) < self.get_key_position(self.layout["row3"]["keys"][5]):
                            color = (0.5, 0.5, 0.5)

                        rect = Rectangle(
                            (key_loc[0], key_loc[1]),
                            1,
                            0.75,
                            facecolor=color,
                            alpha=0.9,
                            edgecolor="black",
                        )
                        self.ax.text(
                            key_loc[0] + 0.5,
                            key_loc[1] + 0.375,
                            key,
                            horizontalalignment="center",
                            verticalalignment="center",
                        )
                        self.ax.add_patch(rect)

                    elif key == "Enter":
                        rect = Rectangle(
                            (key_loc[0] - 0.3, key_loc[1]),
                            1,
                            0.75,
                            facecolor=color,
                            alpha=0.9,
                            edgecolor="black",
                        )
                        self.ax.text(
                            key_loc[0] + 0.25,
                            key_loc[1] + 0.375,
                            key,
                            horizontalalignment="center",
                            verticalalignment="center",
                        )
                        self.ax.add_patch(rect)

                    elif key == "Backspace":
                        rect = Rectangle(
                            (key_loc[0], key_loc[1]),
                            1,
                            0.75,
                            facecolor=color,
                            alpha=0.9,
                            edgecolor="black",
                        )
                        self.ax.text(
                            key_loc[0] + 0.5,
                            key_loc[1] + 0.375,
                            "Bckspc",
                            horizontalalignment="center",
                            verticalalignment="center",
                        )
                        self.ax.add_patch(rect)

                    else:
                        rect = Rectangle(
                            (3.5, key_loc[1]),
                            6,
                            0.75,
                            facecolor=(0,0,0),
                            alpha=0.9,
                            edgecolor="black",
                        )
                        self.ax.text(
                            6.25,
                            key_loc[1] + 0.375,
                            "Space",
                            horizontalalignment="center",
                            verticalalignment="center",
                        )
                        self.ax.add_patch(rect)

            else:
                for key in layout[rows]["keys"]:
                    if self.freq[key] == 0:  # Key was never pressed
                        color = cm(1.0 * 0)
                    elif (
                        key == s and not end
                    ):  # Current key pressed is given a grey colour
                        color = (0.5, 0.5, 0.5)
                    else:  # Give it colour accoring to its usage
                        color = cm(
                            1.0
                            * (
                                (self.freq[key])/self.let_rank[-1]
                            )
                        )
                    key_loc = self.get_key_position(
                        key
                    )  # Getting the key coordinates and drawing a rectangle around it
                    rect = Rectangle(
                        key_loc,
                        0.75,
                        0.75,
                        facecolor=color,
                        alpha=0.9,
                        edgecolor="black",
                    )
                    self.ax.text(
                        key_loc[0] + 0.375,
                        key_loc[1] + 0.375,
                        key,
                        horizontalalignment="center",
                        verticalalignment="center",
                    )
                    self.ax.add_patch(rect)
                    
                    
        plt.pause(0.1)  # To slow the animation
        plt.draw()  # Drawing keyboard

    def euc_dist(
        self, key1, key2
    ):  # Method to get the distance between two keys (needed for computing travel distance)
        return math.sqrt((key2[1] - key1[1]) ** 2 + (key2[0] - key1[0]) ** 2)

    def get_key_position(
        self, key
    ):  # Method to get the key position from the input layout
        for row in self.layout.values():
            if "keys" in row and key in row["keys"]:
                index = row["keys"].index(key)
                return row["positions"][index]
        return self.layout["special_keys"].get(key)

    def key_dist(self):  # To map each key to a distance
        di = {}

        for i in range(4):
            di[self.layout["row3"]["keys"][i]] = (
                0  # Left hand rest on these keys (home row)
            )
            # keys on rows other than home rows are pressed accroding to touch typing convention
            di[self.layout["row1"]["keys"][i]] = self.euc_dist(
                self.get_key_position(self.layout["row1"]["keys"][i]),
                self.get_key_position(self.layout["row3"]["keys"][i]),
            )
            di[self.layout["row2"]["keys"][i]] = self.euc_dist(
                self.get_key_position(self.layout["row2"]["keys"][i]),
                self.get_key_position(self.layout["row3"]["keys"][i]),
            )
            di[self.layout["row4"]["keys"][i]] = self.euc_dist(
                self.get_key_position(self.layout["row4"]["keys"][i]),
                self.get_key_position(self.layout["row3"]["keys"][i]),
            )

        di[self.layout["row3"]["keys"][4]] = 1
        di[self.layout["row1"]["keys"][4]] = self.euc_dist(
            self.get_key_position(self.layout["row1"]["keys"][4]),
            self.get_key_position(self.layout["row3"]["keys"][3]),
        )
        di[self.layout["row2"]["keys"][4]] = self.euc_dist(
            self.get_key_position(self.layout["row2"]["keys"][4]),
            self.get_key_position(self.layout["row3"]["keys"][3]),
        )
        di[self.layout["row4"]["keys"][4]] = self.euc_dist(
            self.get_key_position(self.layout["row4"]["keys"][4]),
            self.get_key_position(self.layout["row3"]["keys"][3]),
        )
        di[self.layout["row1"]["keys"][5]] = di[self.layout["row1"]["keys"][4]]
        di[self.layout["row2"]["keys"][5]] = di[self.layout["row2"]["keys"][4]]
        di[self.layout["row4"]["keys"][5]] = di[self.layout["row4"]["keys"][4]]
        di[self.layout["row3"]["keys"][5]] = 1

        for i in range(6, 10):
            di[self.layout["row3"]["keys"][i]] = (
                0  # Right hand rest on these keys (home row)
            )
            di[self.layout["row1"]["keys"][i]] = self.euc_dist(
                self.get_key_position(self.layout["row1"]["keys"][i]),
                self.get_key_position(self.layout["row3"]["keys"][i]),
            )
            di[self.layout["row2"]["keys"][i]] = self.euc_dist(
                self.get_key_position(self.layout["row2"]["keys"][i]),
                self.get_key_position(self.layout["row3"]["keys"][i]),
            )
            di[self.layout["row4"]["keys"][i]] = self.euc_dist(
                self.get_key_position(self.layout["row4"]["keys"][i]),
                self.get_key_position(self.layout["row3"]["keys"][i]),
            )

        # All the remaining keys on the right side of the keyboard are assumed to be pressed by right little finger
        for j in range(10, len(self.layout["row1"]["keys"])):
            di[self.layout["row1"]["keys"][j]] = self.euc_dist(
                self.get_key_position(self.layout["row1"]["keys"][j]),
                self.get_key_position(self.layout["row3"]["keys"][9]),
            )

        for j in range(10, len(self.layout["row2"]["keys"])):
            di[self.layout["row2"]["keys"][j]] = self.euc_dist(
                self.get_key_position(self.layout["row2"]["keys"][j]),
                self.get_key_position(self.layout["row3"]["keys"][9]),
            )

        for j in range(10, len(self.layout["row3"]["keys"])):
            di[self.layout["row3"]["keys"][j]] = self.euc_dist(
                self.get_key_position(self.layout["row3"]["keys"][j]),
                self.get_key_position(self.layout["row3"]["keys"][9]),
            )

        for j in range(10, len(self.layout["row4"]["keys"])):
            di[self.layout["row4"]["keys"][j]] = self.euc_dist(
                self.get_key_position(self.layout["row4"]["keys"][j]),
                self.get_key_position(self.layout["row3"]["keys"][9]),
            )

        for j in self.layout["special_keys"]:
            if j == "Space":
                di["Space"] = (
                    0  # I have assumed thumbs rest on space so distance travelled=0
                )
                continue

            # To check which finger I need to press to type the special character
            di[j] = min(
                self.euc_dist(
                    self.get_key_position(j),
                    self.get_key_position(self.layout["row3"]["keys"][9]),
                ),
                self.euc_dist(
                    self.get_key_position(j),
                    self.get_key_position(self.layout["row3"]["keys"][0]),
                ),
            )
        return di

    def travel_dist(self, seq):
        self.load_kyb()
        self.freq = defaultdict(int)
        trav = 0  # Stores distance travelled
        shift_detect = False
        special = 0

        for s in seq:
            if s == " ":
                # trav+=2*self.travel['Space']  #Needn't bother since travel distance of space is 0
                # self.freq["Space"] += 1
                self.visualise_kyb("Space", shift_detect, False)
                self.let_rank = list(set(self.freq.values()))
                self.let_rank.sort()
                continue
            elif s == "\n":  # Enter was pressed
                trav +=   self.travel["Enter"]
                self.freq["Enter"] += 1
                self.let_rank = list(set(self.freq.values()))
                self.let_rank.sort()
                self.visualise_kyb("Enter", shift_detect, False)
                continue

            elif not s.isalnum():  # A symbol was pressed
                # characters which appear only while pressing shift (like !,#,@,(,_) dont come in the layout so I had to brute force to check for their prescence
                shift_detect = (
                    True  # Boolean variable to detect if shift key wa pressed or not
                )
                if s == "!":
                    trav +=   (self.travel["Shift_R"] + self.travel["1"])
                    self.freq["Shift_R"] += 1
                    self.freq["1"] += 1
                    s = "1"

                elif s == "@":
                    trav +=   (self.travel["Shift_R"] + self.travel["2"])
                    self.freq["Shift_R"] += 1
                    self.freq["2"] += 1
                    s = "2"

                elif s == "#":
                    trav +=   (self.travel["Shift_R"] + self.travel["3"])
                    self.freq["Shift_R"] += 1
                    self.freq["3"] += 1
                    s = "3"

                elif s == "$":
                    trav +=   (self.travel["Shift_R"] + self.travel["4"])
                    self.freq["Shift_R"] += 1
                    self.freq["4"] += 1
                    s = "4"

                elif s == "%":
                    trav +=   (self.travel["Shift_R"] + self.travel["5"])
                    self.freq["Shift_R"] += 1
                    self.freq["5"] += 1
                    s = "5"

                elif s == "^":
                    trav +=   (self.travel["Shift_L"] + self.travel["6"])
                    self.freq["Shift_L"] += 1
                    self.freq["6"] += 1
                    s = "6"

                elif s == "&":
                    trav +=   (self.travel["Shift_L"] + self.travel["7"])
                    self.freq["Shift_l"] += 1
                    self.freq["7"] += 1
                    s = "7"

                elif s == "*":
                    trav +=   (self.travel["Shift_L"] + self.travel["8"])
                    self.freq["Shift_L"] += 1
                    self.freq["8"] += 1
                    s = "8"

                elif s == "(":
                    trav +=   (self.travel["Shift_L"] + self.travel["9"])
                    self.freq["Shift_L"] += 1
                    self.freq["9"] += 1
                    s = "9"

                elif s == ")":
                    trav +=   (self.travel["Shift_L"] + self.travel["0"])
                    self.freq["Shift_L"] += 1
                    self.freq["0"] += 1
                    s = "0"

                elif s == "_":
                    trav +=   (self.travel["Shift_L"] + self.travel["-"])
                    self.freq["Shift_L"] += 1
                    self.freq["-"] += 1
                    s = "-"

                elif s == "+":
                    trav +=   (self.travel["Shift_L"] + self.travel["="])
                    self.freq["Shift_L"] += 1
                    self.freq["="] += 1
                    s = "="

                elif s == "|":
                    trav +=   (self.travel["Shift_L"] + self.travel["\\"])
                    self.freq["Shift_L"] += 1
                    self.freq["\\"] += 1
                    s = "\\"

                elif s == "}":
                    trav +=   (self.travel["Shift_L"] + self.travel["]"])
                    self.freq["Shift_L"] += 1
                    self.freq["]"] += 1
                    s = "]"

                elif s == "{":
                    trav +=   (self.travel["Shift_L"] + self.travel["["])
                    self.freq["Shift_L"] += 1
                    self.freq["["] += 1
                    s = "["

                elif s == ":":
                    trav +=   (self.travel["Shift_L"] + self.travel[";"])
                    self.freq["Shift_L"] += 1
                    self.freq[";"] += 1
                    s = ";"

                elif s == '"':
                    trav +=   (self.travel["Shift_L"] + self.travel["'"])
                    self.freq["Shift_L"] += 1
                    self.freq["'"] += 1
                    s = "'"

                elif s == "?":
                    trav +=   (self.travel["Shift_L"] + self.travel["/"])
                    self.freq["Shift_L"] += 1
                    self.freq["/"] += 1
                    s = "/"

                elif s == ">":
                    trav +=   (self.travel["Shift_L"] + self.travel["."])
                    self.freq["Shift_L"] += 1
                    self.freq["."] += 1
                    s = "."

                elif s == "<":
                    trav +=   (self.travel["Shift_L"] + self.travel[","])
                    self.freq["Shift_L"] += 1
                    self.freq[","] += 1
                    s = ","

                elif s == "~":
                    trav +=   (self.travel["Shift_R"] + self.travel["`"])
                    self.freq["Shift_R"] += 1
                    self.freq["`"] += 1
                    s = "`"

                else:
                    trav +=   self.travel[s]
                    self.freq[s] += 1
                    shift_detect = (
                        False  # We didnt need to press shift (key present in layout)
                    )

                self.let_rank = list(set(self.freq.values()))
                self.let_rank.sort()
                self.visualise_kyb(s, shift_detect, False)
                continue

            elif (
                s.isupper()
            ):  # Capital letter was pressed (but we need to check which shift we needed to press)
                shift_detect = True
                s = s.lower()
                if self.euc_dist(
                    self.get_key_position(s.lower()),
                    self.get_key_position(self.layout["row3"]["keys"][3]),
                ) < self.euc_dist(
                    self.get_key_position(s.lower()),
                    self.get_key_position(self.layout["row3"]["keys"][9]),
                ):
                    trav +=   self.travel["Shift_R"]
                    self.freq["Shift_R"] += 1
                else:
                    trav +=   self.travel["Shift_L"]
                    self.freq["Shift_L"] += 1

            trav +=   self.travel[s.lower()]
            self.freq[s.lower()] += 1

            self.let_rank = list(
                set(self.freq.values())
            )  # ranking each character's frequency
            self.let_rank.sort()
            self.visualise_kyb(s, shift_detect, False)  # Calling the animation

        self.visualise_kyb("e", False, True)
        print(f"The travel distance is {trav}")
        plt.show()  # To keep plot open


if __name__ == "__main__":
    layout = QWERTY_LAYOUT

    sample_string_1 = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
    sample_string_2 = """COULDN'T PRONOUNCE THE NAME EITHER? Don't sweat it-what mattersG time with us! """

    seq = "`1234567890-=1234567890-=234567890-=34567890-=4567890-=567890-=67890-=67890-=7890-=890-=90-=0-=-=="
    get = kdb_analysis(layout)
    # strin=input()
    get.travel_dist(sample_string_2)
