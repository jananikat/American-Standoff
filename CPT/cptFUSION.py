#American politics trivia game with action involved
#@course ICS 3U
#@date 2019/06/14
#@author Kathirkamar, Janani - Soosaipillai, Andrea

import pygame
import os
 
# Initialize the game engine
pygame.init()
print(os.getcwd())

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (77, 0, 0)
LIGHTBLUE = (0, 128, 255)

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("American Standoff")

clock = pygame.time.Clock()
#--------------------------------------------------------------------------------------------
#START SCREEN: Defining
#--------------------------------------------------------------------------------------------
play = False
def startScreen():
    global font, play
    while play == False:
        backgroundstart = pygame.image.load("backgroundshooting.jpg")
        screen.blit(backgroundstart,[0,0])
        title = pygame.image.load("americanstandofftitle.png")
        title = pygame.transform.scale(title,[300,300])
        screen.blit(title,[250,100])
        
        font = pygame.font.Font(None,60)
        text = font.render("Play if you dare",True,WHITE)
        
        font1 = pygame.font.Font(None,30)
        screen.blit(text,[250,500])
        text1 = font1.render("When the time comes, Player 1 is arrow keys, Player 2 is WASD.",True,WHITE)
        screen.blit(text1,[10,10])
        text2 = font1.render("Use space bar to shoot.",True,WHITE)
        screen.blit(text2,[10,40])
        text3 = font1.render("Click on the letter you believe is correct.",True,WHITE)
        screen.blit(text3,[200,450])

        pygame.draw.rect(screen, BLACK,[200,480,400,100], 10)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                if 200 < x < 600 and 480 < y < 580:
                    play = True
                               
        pygame.display.update()
    return


#--------------------------------------------------------------------------------------------
#PART1 - TRIVIA: Defining
#--------------------------------------------------------------------------------------------
#Creating Question class
class Question():
    def __init__(self,prompt, answer):
        self.prompt = prompt
        self.answer = answer
        
#Question prompts          
question_prompts = [

    "1. How many presidents have there been?\n(a) 45\n(b) 78\n(c) 3\n(d) 100",
    "2. Who is the first American President?\n(a) John A.MacDoncald\n(b) George Washington\n(c) Franklin Roosevelt\n(d) Herbert Hoover\n\n",
    "3. The president who brought the emancipation of slaves?\n(a) Abraham Lincoln\n(b) Thomas Jefferson\n(c) Alexander Hamilton\n(d) Andrew Johnson\n\n" ,
    "4. Where did the U.S. Senate first meet?\n(a) Ottawa\n(b) Boston\n(c) Dallas\n(d) New York\n\n", 
    "5. Which is the July 4th known as\n(a) Civil Rights Day\n(b) Independace day\n(c) Canada Day\n(d) American Day\n\n",
    "6. How many people serve in the U.S. congress?\n(a)100 \n(b) 250\n(c) 535\n(d) 400\n\n", 
    "7. How many U.S. presidents have been assassinated?\n(a) 3\n(b) 2\n(c)4\n(d) 1\n\n",
    "8. As of 2019, who is the current president?\n(a) Donald Tramp\n(b) Barack Obama\n(c) Justin Trudeau\n(d) None of the above\n\n",
    "9.  How many terms is a president allowed to have?\n(a) 4 terms\n(b) 8 terms\n(c) 2 terms\n(d) 1 term\n\n",
    "10. Who is the first woman president in the U.S?\n(a) Kim Campbell\n(b) Hilary Clinton\n(c) Michelle Obama\n(d) Its a trick\n\n",
]

#List that stores question instances and their answers 
questions = [Question(question_prompts[0],"a"),
            Question(question_prompts[1],"b"), #b
            Question(question_prompts[2],"a"),
            Question(question_prompts[3],"d"), #d
            Question(question_prompts[4],"b"), #b
            Question(question_prompts[5],"c"), #c
            Question(question_prompts[6],"c"), #c
            Question(question_prompts[7],"d"), #d
            Question(question_prompts[8],"c"), #c
            Question(question_prompts[9],"d"), #d
            ]
          
#Recived from website 'Stack overflow' 
def blit_text(surface, text, pos, font, color=pygame.Color('WHITE')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on neTw row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row

#Displaying the questions
def draw_ques(screen,question):
    global font
    background1 = pygame.image.load("Backgroundmult3.jpg")
    screen.blit(background1,[0,0])
    pygame.draw.rect(screen, LIGHTBLUE, [25,150,600,300], 10)
    pygame.draw.rect(screen, LIGHTBLUE, [25,150,600,60], 7)
    pygame.draw.rect(screen, LIGHTBLUE, [25,150,600,110], 7)
    pygame.draw.rect(screen, LIGHTBLUE, [25,150,600,160], 7)
    pygame.draw.rect(screen, LIGHTBLUE, [25,150,600,210], 7)

    #global text, font
    font = pygame.font.Font(None, 75)
    blit_text(screen,question_prompts[question],[50,50],font)

    tinyfont = pygame.font.Font(None, 50)
    text1 = tinyfont.render("Player 1, your turn.",True,WHITE)
    text2 = tinyfont.render("Player 2, your turn.",True,WHITE)

    if (i+1) % 2 == 0:
        screen.blit(text2,[450,550])
    else:
        screen.blit(text1,[450,550])

#Determining which letter the mouse click was on 
def checkanswer(x,y): #x and y are mouse coordinates
    answers = ""
    if((56< x < 101) and (157 < y <202)):
        answers = "a"
    elif((56<x<101) and (213<y<256)):
        answers = "b"
    elif((56<x<101) and (263<y<308)):
        answers = "c"
    elif((56<x<101) and (314<y<358)):
        answers = "d"        
    return answers 

#Displaying both player scores
def displayScore(score,player):
    BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
    scoreSurf = BASICFONT.render(player+' Score: ' + str(score), 1, WHITE)
    scoreRect = scoreSurf.get_rect()
    if player == "Player 2":
        scoreRect.topleft = (650, 10)
    if player == "Player 1":
        scoreRect.topleft = (10, 10)
    screen.blit(scoreSurf, scoreRect)

#--------------------------------------------------------------------------------------------------------------
#PART 2: MEXICAN STANDOFF: Defining
#--------------------------------------------------------------------------------------------------------------

trumppewpew = True #Used for the direction of the bullet 
backgroundshooting = pygame.image.load("backgroundshooting.jpg")

class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
class Player(pygame.sprite.Sprite):
    def __init__(self,picture,x,y):
        super().__init__()
 
        self.image = picture
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.xspeed = 0
        self.yspeed = 0
        self.walls = None
        
    def update(self):
        self.rect.x += self.xspeed
        
        #Wall Collisions
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If moving right, set right side to the left side of
            # the item player hit
            if self.xspeed > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if moving left, do the opposite.
                self.rect.left = block.rect.right
                
        self.rect.y += self.yspeed
        # If we are moving up, set our up side to the bottom side of
        # the item we hit
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset position based on the top/bottom of the object.
            if self.yspeed > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
#Bullets     
class Bullet(pygame.sprite.Sprite):
    #This class represents the bullet
    def __init__(self):
        super().__init__()
 
        self.image = pygame.image.load('kanye.jpg')
        self.image = pygame.transform.scale(self.image,(10,10))
 
        self.rect = self.image.get_rect()
 
    def update(self):
        if trumppewpew == True: #if trump is shooting
            self.rect.x += 3 #bullet moves right
        if trumppewpew == False: #if clinton is shooting
            self.rect.x -= 3 #bullet moves left

#List that holds all the sprites
all_sprite_list = pygame.sprite.Group()

#List of each bullet
bullet_list = pygame.sprite.Group()

#Wall Coordinates and instances 
wall_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(0, 0, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(0,590,800,10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(790,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(395,0,10,600)
wall_list.add(wall)
all_sprite_list.add(wall)

#Players
picture1 = pygame.image.load("Picture1.jpg")
picture1 = pygame.transform.scale(picture1,(75,75))

picture2 = pygame.image.load("Picture2.jpg")
picture2 = pygame.transform.scale(picture2,(75,75))
picture2 = pygame.transform.flip(picture2,True,False)

#Creating the Player class instances
player1 = Player(picture1,250,200)
player2 = Player(picture2,450,200)

all_sprite_list.add(player1)
all_sprite_list.add(player2)

player_list = pygame.sprite.Group()

#Adds the wall to its collision list
player1.walls = wall_list
player2.walls = wall_list

#--------------------------------------------------------------------------------------------
#MEXICAN STANDOFF GAME FUNCTION
#--------------------------------------------------------------------------------------------
doneshooting = False
def mexicanstandoff(shooter,defender,num): #num is which player it is; for text purposes
    global doneshooting
    player_list.add(defender)
    while not doneshooting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneshooting = True
                
            elif event.type == pygame.KEYDOWN:         
            #Player 1 Controls: Trump
                if event.key == pygame.K_UP:
                    player1.yspeed = -5       
                elif event.key == pygame.K_DOWN:
                    player1.yspeed = 5
                elif event.key == pygame.K_RIGHT:
                    player1.xspeed = 5       
                elif event.key == pygame.K_LEFT:
                    player1.xspeed = -5
                #Player 2 COntrols: Clinton
                elif event.key == pygame.K_w:
                    player2.yspeed = -5
                elif event.key == pygame.K_s:
                    player2.yspeed = 5
                elif event.key == pygame.K_a:
                    player2.xspeed = -5
                elif event.key == pygame.K_d:
                    player2.xspeed = 5

            #Shooting Controls
                if event.key == pygame.K_SPACE:
                    bullet = Bullet()
                    bullet.rect.x = shooter.rect.x + 50
                    bullet.rect.y = shooter.rect.y + 50
                    
                    all_sprite_list.add(bullet)
                    bullet_list.add(bullet)

                    #Remove the bullet when it goes offscreen
                    if bullet.rect.y < -10:
                        bullet_list.remove(bullet)
                        all_sprite_list.remove(bullet)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player1.xspeed = 0   
                elif event.key == pygame.K_a or event.key == pygame.K_d:
                    player2.xspeed = 0   
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player1.yspeed = 0 
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    player2.yspeed = 0
                   
        screen.fill(WHITE)
        screen.blit(backgroundshooting,[0,0])

        #Tells the user which player is taking the steal
        BASICFONT1 = pygame.font.Font('freesansbold.ttf', 30)
        scoreSurf1 = BASICFONT1.render("Player "+str(num)+" TAKE THE STEAL", 1, WHITE)
        scoreRect1 = scoreSurf1.get_rect()
        scoreRect1.topleft = (200, 10)
        
        screen.blit(scoreSurf1, scoreRect1)
        
        all_sprite_list.update()
        all_sprite_list.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

        for bullet in bullet_list:
            block_hit_list = pygame.sprite.spritecollide(bullet, player_list, True)

        #if the defending player (without the gun) is eliminated
        if defender not in player_list:
            doneshooting = True #the function is over
            return


#--------------------------------------------------------------------------------------------
#TRIVIA GAME FUNCTION
#--------------------------------------------------------------------------------------------
    
# Loop until the user clicks the close button.
done = False

score1 = 0
score2 = 0
i = 0 #counting variable
#Main
startScreen()
while not done:
    if i == 10: #once the questions are done
        pygame.quit() #end the program
    listOfAnswers = ["a","b","c","d"] #resets the list of all possible answers
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True

        draw_ques(screen,i) #Draw the question screen
        displayScore(score1,"Player 1")
        displayScore(score2,"Player 2")
        if event.type == pygame.MOUSEBUTTONDOWN: #if user clicks
            pos = pygame.mouse.get_pos() #get the position
            x = pos[0]
            y = pos[1]
            checkanswer(x,y) #and check if it's on one of the possible answers

            if checkanswer(x,y) != questions[i].answer: #if the answer is wrong 
                #listOfAnswers.remove(questions[i].answer) #remove the correct answer from the list of answers
                                
                if checkanswer(x,y) in listOfAnswers: #if the mouse click is one of the other possible answers
                    if (i+1)%2 == 1: #determines whether player 1 or player 2 got it wrong 
                        trumppewpew = False
                        mexicanstandoff(player2,player1,2) #activate the shooting game
                        score2 += 1
                        i += 1
                    elif (i+1)%2 == 0: 
                        trumppewpew = True
                        mexicanstandoff(player1,player2,1)
                        score1 += 1
                        i += 1
                    
            elif checkanswer(x,y) == questions[i].answer: #if it's correct
                if (i+1)%2 == 0: #and if the user is player 2 (even number questions are player 2's)
                    score2 += 1
                    i += 1 #move on the next question 
                else: #if it's player 1
                    score1 += 1 
                    i += 1 #move on the next question

             
    pygame.display.flip()
    clock.tick(120)
 
pygame.quit()
