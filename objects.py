
#-------------------------------------------------------------------------------
# Author: Mihail Dimitrov
# Created: 15/03/2021
#
# Course: HND Software Development - NESCOL
# Modul: OOP
# Tutor:  Chrissie Nyssen
#-------------------------------------------------------------------------------


#Parent object class created The Snitch, Seekers and Player

class Objects:

    def __init__(self, x, r, c):
        self.char = x
        self.row = r
        self.col = c


    def getRow(self):
        return self.row

    def getCol(self):
        return self.col

    def getChar(self):
        return self.char

    def setRow(self, r):
        self.row = r

    def setCol(self, c):
        self.col = c

    def moveRight(self):
        self.col += 1

    def moveLeft(self):
        self.col -= 1

    def moveUp(self):
        self.row -=1

    def moveDown(self):
        self.row +=1
