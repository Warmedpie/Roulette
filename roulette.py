#Pygame is used to power the graphics
import pygame
#Enum used for bet types
from enum import Enum
# import random  
import random 

#Create a class holding all the bet types
class betTypes(Enum):
    GREEN = 0
    RED = 1
    BLACK = 2
    FIRST12 = 3
    SECOND12 = 4    
    THIRD12 = 5
    FIRST18 = 6
    SECOND18 = 7
    EVEN = 8
    ODD = 9
    FIRSTROW = 10
    SECONDROW = 11
    THIRDROW = 12
    NUMBER = 13

#This is the struture of a bet, holding a bet type, an amount, and an additional parameter
class bet:
    def __init__(self, betType, amount, additional = None):
        self.betType = betType
        self.amount = amount
        self.additional = additional

#Create a class to hold the information for all the bets and multipliers
class table:
    #Set up multipliers
    def __init__(self):
        
        #Multiplier for each bet type
        self.multipliers = [14, 2, 2, 3, 3, 3, 2, 2, 2, 2, 3, 3, 3, 35]
        
        #List of numbers for each bet type
        #00 is represented by 37
        self.greens    = [0, 37]
        self.reds      = [1, 3, 5, 7, 9,  12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]  
        self.blacks    = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35] 
        first12        = [i for i in range(1,13)]
        second12       = [i for i in range(13,25)]
        third12        = [i for i in range(25,37)]
        first18        = [i for i in range(1,19)]
        second18       = [i for i in range(19,37)]
        even           = [i for i in range(1,37) if i % 2 == 0]
        odd            = [i for i in range(1,37) if i % 2 == 1]
        self.firstrow  = [i for i in range(1,37) if i % 3 == 0]
        self.secondrow = [i for i in range(1,37) if i % 3 == 2]
        self.thirdrow  = [i for i in range(1,37) if i % 3 == 1]
        
        self.winningNumbers = [self.greens, self.reds, self.blacks, first12, second12, third12, first18, second18, even, odd, self.firstrow, self.secondrow, self.thirdrow]
        
        #Stores all the bets on the table
        self._bets = []
        
        #The order of the table
        self.tableConfig = [37, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2, 0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13, 1]
        
        #Long list is used to make it easier to get the elements for a looping wheel
        self.tableConfigLong = [i for q in range(0,3) for i in self.tableConfig ]
        
    #Given a bet, return a multiplier
    def multiplier(self, betType):
        return self.multipliers[betType.value]
    
    #Create a new bet
    def createBet(self, bet):
        self._bets.append(bet)
    
    #payout for the bets of the table
    def payout(self, number):
        pay = 0
        for bet in self._bets:
            if self.checkBet(bet, number): pay += bet.amount * self.multiplier(bet.betType)
        
        self._bets = []
        
        return pay
                
    #Given a bet and a number from the table, see if player wins
    def checkBet(self, bet, number):
        #Check for single number win
        if (bet.betType.value == 13): return number is bet.additional
            
        #otherwise use the winning numbers array to deturnmine win
        return number in self.winningNumbers[bet.betType.value] 
    
    #Given a "curentNumber", spit out a list of the elments around it to draw
    def getDraw(self, index):
        return [self.tableConfigLong[q] for q in range(index + len(self.tableConfig) - 4, index + len(self.tableConfig) + 5)]
    
    #Given a number, what color should it be
    def getColor(self, number):
        if number in self.reds:
            return (255,0,0)
        elif number in self.blacks:
            return (0,0,0)
        else:
            return (0,128,0)
    
    #Draw all bets on the board
    def drawBets(self, screen, chip):
        locations = []
        for b in self._bets:
            if b.betType == betTypes.NUMBER:
                #00
                if b.additional == 37:
                    screen.blit(chip, (374, 533))
                #0
                if b.additional == 0:
                    screen.blit(chip, (374, 610))
                #First row
                if b.additional in self.firstrow:
                    x = self.firstrow.index(b.additional)
                    screen.blit(chip, (411 + (x * 39), 519))
                #Second row
                if b.additional in self.secondrow:
                    x = self.secondrow.index(b.additional)
                    screen.blit(chip, (411 + (x * 39), 567))
                #third row
                if b.additional in self.thirdrow:
                    x = self.thirdrow.index(b.additional)
                    screen.blit(chip, (411 + (x * 39), 615))
            if  b.betType == betTypes.FIRST12:
                screen.blit(chip, (471, 656))
            if  b.betType == betTypes.SECOND12:
                screen.blit(chip, (629, 656))
            if  b.betType == betTypes.THIRD12:
                screen.blit(chip, (785, 656))
            if  b.betType == betTypes.FIRSTROW:
                screen.blit(chip, (882, 522))
            if  b.betType == betTypes.SECONDROW:
                screen.blit(chip, (882, 571))
            if  b.betType == betTypes.THIRDROW:
                screen.blit(chip, (882, 619))  
            if  b.betType == betTypes.FIRST18:
                screen.blit(chip, (430, 685))  
            if  b.betType == betTypes.EVEN:
                screen.blit(chip, (510, 685))  
            if  b.betType == betTypes.RED:
                screen.blit(chip, (589, 685))  
            if  b.betType == betTypes.BLACK:
                screen.blit(chip, (668, 685))  
            if  b.betType == betTypes.ODD:
                screen.blit(chip, (744, 685))  
            if  b.betType == betTypes.SECOND18:
                screen.blit(chip, (821, 685))    
if __name__ == '__main__':

    #Table variables
    t = table()
    money = 2000
    
    #The index being displayed
    curentNumber = 0
    #The index the table will spin until it reached
    spinUntil = random.randint(0, 360)
    #spin velocity (spins/s)
    spinVel = 7
    #is the board spinning
    spinning = False
    
    
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    clock = pygame.time.Clock()
    running = True
    dt = 0
    rt = 0
    
    #bets image
    betImage = pygame.image.load("roulette-bets.jpg")
    chipImage = pygame.image.load("chip.png")
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        x = 0
        y = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            #set click position for future use  
            if event.type == pygame.MOUSEBUTTONUP:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((1,102,0))
        
        
        #draw bets
        screen.blit(betImage, (357, 500))
        t.drawBets(screen,chipImage)
        
        #Check for clicking bets
        if money >= 25:
            #00
            if x > 357 + 5 and x < 357 + 5 + 41 and y > 500 + 6 and y < 500 + 6 + 73:
                b = bet(betTypes.NUMBER,25,37)
                money -= 25
                t.createBet(b)
            #0
            if x > 357 + 5 and x < 357 + 5 + 41 and y > 500 + 79 and y < 500 + 79 + 73:
                b = bet(betTypes.NUMBER,25,0)
                money -= 25
                t.createBet(b)
            #First 12
            if x > 357 + 46 and x < 357 + 46 + 156 and y > 500 + 152 and y < 500 + 152 + 29:
                b = bet(betTypes.FIRST12,25)
                money -= 25
                t.createBet(b)
            #second 12
            if x > 357 + 202 and x < 357 + 202 + 156 and y > 500 + 152 and y < 500 + 152 + 29:
                b = bet(betTypes.SECOND12,25)
                money -= 25
                t.createBet(b)
            #third 12
            if x > 357 + 359 and x < 357 + 359 + 156 and y > 500 + 152 and y < 500 + 152 + 29:
                b = bet(betTypes.THIRD12,25)
                money -= 25
                t.createBet(b)
            #First 18
            if x > 357 + 46 and x < 357 + 46 + 78 and y > 500 + 182 and y < 500 + 182 + 29:
                b = bet(betTypes.FIRST18,25)
                money -= 25
                t.createBet(b)  
            #Even
            if x > 357 + 124 and x < 357 + 124 + 78 and y > 500 + 182 and y < 500 + 182 + 29:
                b = bet(betTypes.EVEN,25)
                money -= 25
                t.createBet(b)  
            #Red
            if x > 357 + 202 and x < 357 + 202 + 78 and y > 500 + 182 and y < 500 + 182 + 29:
                b = bet(betTypes.RED,25)
                money -= 25
                t.createBet(b)  
            #Black
            if x > 357 + 281 and x < 357 + 281 + 78 and y > 500 + 182 and y < 500 + 182 + 29:
                b = bet(betTypes.BLACK,25)
                money -= 25
                t.createBet(b)  
            #Odd
            if x > 357 + 359 and x < 357 + 359 + 78 and y > 500 + 182 and y < 500 + 182 + 29:
                b = bet(betTypes.ODD,25)
                money -= 25
                t.createBet(b)  
            #Second 18
            if x > 357 + 437 and x < 357 + 437 + 78 and y > 500 + 182 and y < 500 + 182 + 29:
                b = bet(betTypes.SECOND18,25)
                money -= 25
                t.createBet(b)  
            #First row
            if x > 357 + 516 and x < 357 + 516 + 39 and y > 500 + 7 and y < 500 + 7 + 48:
                b = bet(betTypes.FIRSTROW,25)
                money -= 25
                t.createBet(b)  
            #Second row
            if x > 357 + 516 and x < 357 + 516 + 39 and y > 500 + 55 and y < 500 + 55 + 48:
                b = bet(betTypes.SECONDROW,25)
                money -= 25
                t.createBet(b)  
            #third row
            if x > 357 + 516 and x < 357 + 516 + 39 and y > 500 + 104 and y < 500 + 104 + 48:
                b = bet(betTypes.THIRDROW,25)
                money -= 25
                t.createBet(b)  
            #numbers on rows
            for i in range(0,12):
                if x > 357 + 54 + (i*39) and x < 357 + 54 + 39 + (i*39):
                    if y > 507 and y < 507 + 48:
                        b = bet(betTypes.NUMBER,25,t.firstrow[i])
                        money -= 25
                        t.createBet(b)  
                    if y > 555 and y < 555 + 48:
                        b = bet(betTypes.NUMBER,25,t.secondrow[i])
                        money -= 25
                        t.createBet(b)  
                    if y > 604 and y < 604 + 48:
                        b = bet(betTypes.NUMBER,25,t.thirdrow[i])
                        money -= 25
                        t.createBet(b) 
            if x > 357 + 606 and x < 357 + 606 + 110 and y > 593 and y < 593 + 60 and not spinning:
                spinning = True
                spinUntil = curentNumber + random.randint(0, 72)
        
        x = 0
        #Loop throuhg a list of all the numbers next the center number
        for i in t.getDraw(curentNumber % 37):
            #Get the color
            color = t.getColor(i)
            
            #Draw a rectangle of the color
            pygame.draw.rect(screen, color, pygame.Rect(x * 160 - 80, 30, 160, 350))
            
            #get number to draw
            string = i
            
            #37 is 00
            if string == 37: 
                string = "00"
            else:
                string = str(string)
            #draw, only if not off the screen
            numberDraw = my_font.render(string, False, (255, 255, 255))
            screen.blit(numberDraw, (x * 160 - 20, 100))
            
            x += 1
            
            pygame.draw.circle(screen, (200, 200, 200), [4 * 160, 190], 25, 0)

        #Draw the amount of money the player has
        moneyDraw = my_font.render(str(money) + "$", False, (0, 0, 0))
        screen.blit(moneyDraw, (0, 374))
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        #rt is the running total of time since last switch
        dt = clock.tick(60) / 1000
        rt += dt
        
        #see if we need to switch the middle index
        if rt > 1 / spinVel:
            rt = 0
            if spinning: 
                curentNumber += 1
                #Stop spinning when we hit our target
                if curentNumber == spinUntil: 
                    spinning = False
                    money += t.payout(curentNumber % 37)
        
    pygame.quit()