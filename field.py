

#-------------------------------------------------------------------------------
# Author: Mihail Dimitrov
# Created: 15/03/2021
#
# Course: HND Software Development - NESCOL
# Modul: OOP
#
# Tutor:  Chrissie Nyssen
#-------------------------------------------------------------------------------

#Object class created the game levels
class Field:

    def __init__(self):
        self.field = [['#','#','#','#','#','#','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#','#','#','#','#','#','#']]
        self.width = 7
        self.height = 7


    def goToLevel1(self):
        self.field = [['#','#','#','#','#','#','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#',' ',' ',' ',' ',' ','#'],
                       ['#','#','#','#','#','#','#']]
        self.width = 7
        self.height = 7

    def goToLevel2(self):
        self.field = [['#','#','#','#','#','#','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ','#','#'],
                     ['#',' ',' ',' ',' ',' ','#'],
                     ['#','#',' ',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#']]
        self.width = 7
        self.height = 7

    

    def goToLevel3(self):
        self.field = [['#','#','#','#','#','#','#','#'],
                    ['#',' ',' ',' ',' ',' ','#', '#'],
                    ['#',' ','#',' ',' ',' ',' ', '#'],
                    ['#',' ',' ',' ',' ','#',' ', '#'],
                    ['#',' ',' ',' ',' ',' ',' ', '#'],
                    ['#',' ',' ','#',' ',' ',' ', '#'],
                   ['#','#','#','#','#','#','#', '#']]
        self.width = 8
        self.height = 7

    def goToLevel4(self):
        self.field = [['#','#','#','#','#','#','#','#'],
               ['#',' ','#',' ',' ',' ','#', '#'],
               ['#',' ','#',' ',' ',' ',' ', '#'],
               ['#',' ',' ',' ',' ','#','#', '#'],
	       ['#',' ',' ',' ',' ',' ',' ', '#'],
               ['#',' ',' ',' ',' ',' ',' ', '#'],
               ['#','#',' ','#',' ',' ','#', '#'],
               ['#','#','#','#','#','#','#', '#']]
        self.width = 8
        self.height = 8

    def goToLevel5(self):
        self.field = [['#','#','#','#','#','#','#','#','#','#'],
                     ['#',' ','#',' ',' ',' ','#',' ',' ','#'],
                     ['#',' ','#',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ','#',' ',' ',' ',' ',' ',' ','#'],
	             ['#',' ','#',' ',' ','#',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ','#','#','#',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ','#',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ','#',' ',' ','#',' ','#','#'],
                     ['#','#','#','#','#','#','#','#','#','#']]
        self.width = 10
        self.height = 10


    def gameOver(self):
        self.field = [['#','#','#','#','#','#','#','#','#','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
	             ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#',' ',' ',' ',' ',' ',' ',' ',' ','#'],
                     ['#','#','#','#','#','#','#','#','#','#']]
        self.width = 10
        self.height = 10    

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def placeObj(self, rat_char, row, column):
        self.field[row][column] = rat_char

    def clearAtPos(self, row, col):
        self.field[row][col] = " "

    def getCharAtPos(self, row, col):
        return self.field[row][col]


