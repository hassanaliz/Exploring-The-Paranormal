#******************************************************************************************************************************************** 
#Program Author: Alyssa Lee and Zahra Hassanali
#Revision Date: June 20th 2022
#Program Name: Exploring the Paranormal
#Description: This program is designed to let the user take a lesson, quiz, and play a game about ghosts.
#********************************************************************************************************************************************

#Importing Modules
import pygame
import time
pygame.init()
from pygame import mixer

#Declaring constants/variables
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 600
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
show_instructions = bool(False)

#Declaring the size of the window and the name of the window
background = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Exploring the Paranormal')

#background sound
mixer.music.load("Music/Come-Play-with-Me.wav")
mixer.music.play(-1)

#Loading background images
backgroundImg = pygame.image.load('Images/haunted_house.png')
backgroundImg = pygame.transform.scale(backgroundImg, (1000, 600))
#Loading menu images
menuImg = pygame.image.load('Images/main_menu.png')
menuImg = pygame.transform.scale(menuImg, (1000, 600))
#Instruction images
instructionsImg = pygame.image.load('Images/Game Instructions.jpg')
instructionsImg = pygame.transform.scale(instructionsImg, (1000, 600))
#Quiz images
quizImg = pygame.image.load('Images/PQ.jpg')
quizImg = pygame.transform.scale(quizImg, (1000, 600))
q1Img = pygame.image.load('Images/PQQ1.jpg')
q1Img = pygame.transform.scale(q1Img, (1000, 600))
q2Img = pygame.image.load('Images/PQQ2.jpg')
q2Img = pygame.transform.scale(q2Img, (1000, 600))
q3Img = pygame.image.load("Images/PQQ3.jpg")
q3Img = pygame.transform.scale(q3Img, (1000, 600))
q4Img = pygame.image.load("Images/PQQ4.jpg")
q4Img = pygame.transform.scale(q4Img, (1000, 600))
q5Img = pygame.image.load("Images/PQQ5.jpg")
q5Img = pygame.transform.scale(q5Img, (1000, 600))
#Images for the instructions
ghostImg1 = pygame.image.load("Images/Ghost1.jpg")
ghostImg1 = pygame.transform.scale(ghostImg1, (1000, 600))
ghostImg2 = pygame.image.load("Images/Ghost2.jpg")
ghostImg2 = pygame.transform.scale(ghostImg2, (1000, 600))
ghostImg3 = pygame.image.load("Images/Ghost3.jpg")
ghostImg3 = pygame.transform.scale(ghostImg3, (1000, 600))
ghostImg4 = pygame.image.load("Images/Ghost4.jpg")
ghostImg4 = pygame.transform.scale(ghostImg4, (1000, 600))
ghostImg5 = pygame.image.load("Images/Ghost5.jpg")
ghostImg5 = pygame.transform.scale(ghostImg5, (1000, 600)) 
ghostImg6 = pygame.image.load("Images/Ghost6.jpg")
ghostImg6 = pygame.transform.scale(ghostImg6, (1000, 600))
ghostImg7 = pygame.image.load("Images/Ghost7.jpg")
ghostImg7 = pygame.transform.scale(ghostImg7, (1000, 600)) 
ghostImg8 = pygame.image.load("Images/Ghost8.jpg")
ghostImg8 = pygame.transform.scale(ghostImg8, (1000, 600))
bossGhostsImg = pygame.image.load("Images/Boss Ghosts.jpg")
bossGhostsImg = pygame.transform.scale(bossGhostsImg, (1000, 600)) 
#Images for the lesson
lesson1Img = pygame.image.load("Images/lesson1.jpg")
lesson1Img = pygame.transform.scale(lesson1Img, (1000, 600)) 
lesson2Img = pygame.image.load("Images/lesson2.jpg")
lesson2Img = pygame.transform.scale(lesson2Img, (1000, 600))
lesson3Img = pygame.image.load("Images/lesson3.jpg")
lesson3Img = pygame.transform.scale(lesson3Img, (1000, 600))
lesson4Img = pygame.image.load("Images/lesson4.jpg")
lesson4Img = pygame.transform.scale(lesson4Img, (1000, 600))
lesson5Img = pygame.image.load("Images/lesson5.jpg")
lesson5Img = pygame.transform.scale(lesson5Img, (1000, 600))
lesson6Img = pygame.image.load("Images/lesson6.jpg")
lesson6Img = pygame.transform.scale(lesson6Img, (1000, 600))
lesson7Img = pygame.image.load("Images/lesson7.jpg")
lesson7Img = pygame.transform.scale(lesson7Img, (1000, 600))
lesson8Img = pygame.image.load("Images/lesson8.jpg")
lesson8Img = pygame.transform.scale(lesson8Img, (1000, 600))
lesson9Img = pygame.image.load("Images/lesson9.jpg")
lesson9Img = pygame.transform.scale(lesson9Img, (1000, 600))
lesson10Img = pygame.image.load("Images/lesson10.jpg")
lesson10Img = pygame.transform.scale(lesson10Img, (1000, 600))
lesson11Img = pygame.image.load("Images/lesson11.jpg")
lesson11Img = pygame.transform.scale(lesson11Img, (1000, 600))
lesson12Img = pygame.image.load("Images/lesson12.jpg")
lesson12Img = pygame.transform.scale(lesson12Img, (1000, 600))
lesson13Img = pygame.image.load("Images/lesson13.jpg")
lesson13Img = pygame.transform.scale(lesson13Img, (1000, 600))
lesson14Img = pygame.image.load("Images/lesson14.jpg")
#Images for the game (PG stands for Paranormal Game)
pg = pygame.image.load("Images/PG.jpg")
pg = pygame.transform.scale(pg, (1000, 600))
pg1 = pygame.image.load("Images/PG1.jpg")
pg1 = pygame.transform.scale(pg1, (1000, 600))
pg2 = pygame.image.load("Images/PG2.jpg")
pg2 = pygame.transform.scale(pg2, (1000, 600))
pg3 = pygame.image.load("Images/PG3.jpg")
pg3 = pygame.transform.scale(pg3, (1000, 600))
pg4 = pygame.image.load("Images/PG4.jpg")
pg4 = pygame.transform.scale(pg4, (1000, 600))
pg5 = pygame.image.load("Images/PG5.jpg")
pg5 = pygame.transform.scale(pg5, (1000, 600))
pg6 = pygame.image.load("Images/PG6.jpg")
pg6 = pygame.transform.scale(pg6, (1000, 600))
pg7 = pygame.image.load("Images/PG7.jpg")
pg7 = pygame.transform.scale(pg7, (1000, 600))
pg8 = pygame.image.load("Images/PG8.jpg")
pg8 = pygame.transform.scale(pg8, (1000, 600))
pg9 = pygame.image.load("Images/PG9.jpg")
pg9 = pygame.transform.scale(pg9, (1000, 600))
pg10 = pygame.image.load("Images/PG10.jpg")
pg10 = pygame.transform.scale(pg10, (1000, 600))
pg11= pygame.image.load("Images/PG11.jpg")
pg11 = pygame.transform.scale(pg11, (1000, 600))
pg12 = pygame.image.load("Images/PG12.jpg")
pg12 = pygame.transform.scale(pg12, (1000, 600))
pg13 = pygame.image.load("Images/PG13.jpg")
pg13 = pygame.transform.scale(pg13, (1000, 600))
pg14 = pygame.image.load("Images/PG14.jpg")
pg14 = pygame.transform.scale(pg14, (1000, 600))
pg15 = pygame.image.load("Images/PG15.jpg")
pg15 = pygame.transform.scale(pg15, (1000, 600))
pg16 = pygame.image.load("Images/PG16.jpg")
pg16 = pygame.transform.scale(pg16, (1000, 600))
pg17 = pygame.image.load("Images/PG17.jpg")
pg17 = pygame.transform.scale(pg17, (1000, 600))
pg18 = pygame.image.load("Images/PG18.jpg")
pg18 = pygame.transform.scale(pg18, (1000, 600))
pg19 = pygame.image.load("Images/PG19.jpg")
pg19 = pygame.transform.scale(pg19, (1000, 600))
pg20 = pygame.image.load("Images/PG20.jpg")
pg20 = pygame.transform.scale(pg20, (1000, 600))
pg21 = pygame.image.load("Images/PG21.jpg")
pg21 = pygame.transform.scale(pg21, (1000, 600))
pg22 = pygame.image.load("Images/PG22.jpg")
pg22 = pygame.transform.scale(pg22, (1000, 600))
pg23 = pygame.image.load("Images/PG23.jpg")
pg23 = pygame.transform.scale(pg23, (1000, 600))
pg24 = pygame.image.load("Images/PG24.jpg")
pg24 = pygame.transform.scale(pg24, (1000, 600))
pg25 = pygame.image.load("Images/PG25.jpg")
pg25 = pygame.transform.scale(pg25, (1000, 600))
pg26 = pygame.image.load("Images/PG26.jpg")
pg26 = pygame.transform.scale(pg26, (1000, 600))
pg27 = pygame.image.load("Images/PG27.jpg")
pg27 = pygame.transform.scale(pg27, (1000, 600))
pg28 = pygame.image.load("Images/PG28.jpg")
pg28 = pygame.transform.scale(pg28, (1000, 600))
pg29 = pygame.image.load("Images/PG29.jpg")
pg29 = pygame.transform.scale(pg29, (1000, 600))
pg30 = pygame.image.load("Images/PG30.jpg")
pg30 = pygame.transform.scale(pg30, (1000, 600))
pg31 = pygame.image.load("Images/PG31.jpg")
pg31 = pygame.transform.scale(pg31, (1000, 600))
pg32 = pygame.image.load("Images/PG32.jpg")
pg32 = pygame.transform.scale(pg32, (1000, 600))
pg33 = pygame.image.load("Images/PG33.jpg")
pg33 = pygame.transform.scale(pg33, (1000, 600))
pg34 = pygame.image.load("Images/PG34.jpg")
pg34 = pygame.transform.scale(pg34, (1000, 600))
pg35 = pygame.image.load("Images/PG35.jpg")
pg35 = pygame.transform.scale(pg35, (1000, 600))
pg36 = pygame.image.load("Images/PG36.jpg")
pg36 = pygame.transform.scale(pg36, (1000, 600))
pg37 = pygame.image.load("Images/PG37.jpg")
pg37 = pygame.transform.scale(pg37, (1000, 600))
pg38 = pygame.image.load("Images/PG38.jpg")
pg38 = pygame.transform.scale(pg38, (1000, 600))
pg39 = pygame.image.load("Images/PG39.jpg")
pg39 = pygame.transform.scale(pg39, (1000, 600))
pg40 = pygame.image.load("Images/PG40.jpg")
pg40 = pygame.transform.scale(pg40, (1000, 600))
pg41 = pygame.image.load("Images/PG41.jpg")
pg41 = pygame.transform.scale(pg41, (1000, 600))
#Ending backgrounds
ending1Img = pygame.image.load("Images/Ending 1.jpg")
ending1Img = pygame.transform.scale(ending1Img, (1000, 600))
ending2Img = pygame.image.load("Images/Ending 2.jpg")
ending2Img = pygame.transform.scale(ending2Img, (1000, 600))
ending3Img = pygame.image.load("Images/Ending 3.jpg")
ending3Img = pygame.transform.scale(ending3Img, (1000, 600))
ending4Img = pygame.image.load("Images/Ending 4.jpg")
ending4Img = pygame.transform.scale(ending4Img, (1000, 600))
#Reference images
referencesImg = pygame.image.load("Images/References.jpg")
referencesImg = pygame.transform.scale(referencesImg, (1000, 600))
#Background for title screen
title_background = pygame.image.load("Images/Title-screen.jpg")
title_background = pygame.transform.scale(title_background, (1000, 600))

#Buttons
class Button:
    def __init__(self, text, width, height, pos, elevation):
        #Core attributes
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        #top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = "#989797"

        #bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(width, elevation))
        self.bottom_color = "#5E5E5E"

        #text
        self.text_surf = button_font.render(text, True, '#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

    def draw(self):
        #elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(background, self.bottom_color,self.bottom_rect, border_radius = 12)
        pygame.draw.rect(background, self.top_color,self.top_rect, border_radius = 12)
        background.blit(self.text_surf,self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = "#7E9785"  #Changing colour when curser is hovering buttons
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print("Click")
                    self.pressed = False
        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#989797'

#allows text to be displayed
def message_display(text):
    #declares the font and font size
    smallText = pygame.font.Font("freesansbold.ttf", 76) 
        
#Type of button
button_font = pygame.font.Font(None, 35)
start_button = Button('Start', 250, 80, (100, 500), 6)
lesson_button = Button('Lesson', 200, 40, (45, 80), 6)
quiz_button = Button('Quiz', 200, 40, (45, 160), 6)
results_button = Button('Results', 200, 40, (45, 240), 6)
instructions_button = Button('Instructions', 200, 40, (45, 320), 6)
play_button = Button('Play', 200, 40, (45, 400), 6)
exit_button = Button('Exit', 200, 40, (45, 480), 6)
yes_play_button =  Button("Yes", 200, 90, (235, 270), 6)
no_play_button = Button("No", 200, 90, (545, 270), 6)
next_button = Button("Next", 200, 40, (790, 550), 6)
return_button = Button("Return", 200, 40, (790, 550), 6)
back_button = Button("Back", 200, 40, (90, 550), 6)
q1_o1_button = Button("Spirits are mobile, ghosts are stuck to where they die.", 700, 60, (160, 160), 6)
q1_o2_button = Button("Ghosts are more hostile and aggressive than spirits.", 700, 60, (160, 240), 6)
q1_o3_button = Button("Spirits are, on average, much older than ghosts.", 700, 60, (160, 320), 6)
q1_o4_button = Button("Ghosts are more dangerous and chaotic than spirits.", 700, 60, (160, 400), 6)
q2_o1_button = Button("Ancient Egyptian Culture", 700, 60, (160, 160), 6)
q2_o2_button = Button("Ancient European Culture", 700, 60, (160, 240), 6)
q2_o3_button = Button("Ancient Indian Culture", 700, 60, (160, 320), 6)
q2_o4_button = Button("Ancient Russian Culture", 700, 60, (160, 400), 6)
q3_o1_button = Button("The Drury Lane Ghost", 700, 60, (160, 160), 6)
q3_o2_button = Button("The Vanishing Hitchhiker", 700, 60, (160, 240), 6)
q3_o3_button = Button("Bloody  Mary", 700, 60, (160, 320), 6)
q3_o4_button = Button("The Ghost of Christmas Past", 700, 60, (160, 400), 6)
q3_o1_button = Button("The Drury Lane Ghost", 700, 60, (160, 160), 6)
q3_o2_button = Button("The Vanishing Hitchhiker", 700, 60, (160, 240), 6)
q3_o3_button = Button("Bloody  Mary", 700, 60, (160, 320), 6)
q3_o4_button = Button("The Ghost of Christmas Past", 700, 60, (160, 400), 6)
q4_o1_button = Button("Dirty, newly created places", 700, 60, (160, 160), 6)
q4_o2_button = Button("Clean and inhabited places", 700, 60, (160, 240), 6)
q4_o3_button = Button("Remote places with occasional visitors", 700, 60, (160, 320), 6)
q4_o4_button = Button("Old and isolated places", 700, 60, (160, 400), 6)
q5_o1_button = Button("After the resident has been away for a while", 700, 60, (160, 160), 6)
q5_o2_button = Button("After a traumatic event", 700, 60, (160, 240), 6)
q5_o3_button = Button("After not cleaning for a long time", 700, 60, (160, 320), 6)
q5_o4_button = Button("After guests are invited over", 700, 60, (160, 400), 6)
phantom_button = Button("The Phantom", 225, 90, (130, 175), 6)
grimReaper_button = Button("The Grim Reaper", 225, 90, (380, 175), 6)
joltent_button = Button("Joltent", 225, 90,(630, 175), 6)
auris_button = Button("Auris", 225, 90, (255, 325), 6)
remora_button = Button("Remora", 225, 90, (505, 325), 6)
menos_button = Button("Menos", 225, 90, (130, 220), 6)
vexa_button = Button("Vexa", 225, 90, (380, 220), 6)
klaus_button = Button("Klaus", 225, 90, (630, 220), 6)

# Title screen loop
def title_screen():
    TitleScreen = True
    while TitleScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                     
        background.blit(title_background, (0,0))
        start_button.draw()

        if start_button.pressed == True:
            time.sleep(0.25)
            main_menu()
        
        # Update display
        pygame.display.update()        
        clock.tick(60)

#Main menu function which goes into the gameloop       
def main_menu():
    tutorial = True
    
    #creates loop for the game
    while tutorial:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        #draws the background images
        background.blit(menuImg, (0,0))
        
        #draws buttons
        lesson_button.draw()
        quiz_button.draw()
        results_button.draw()
        instructions_button.draw()
        play_button.draw()
        exit_button.draw()
        
        #updates the display     
        pygame.display.flip()
        clock.tick(60)
        
        #calls different functions depending on the button clicked
        if instructions_button.pressed == True:
            instructions()
            
        if quiz_button.pressed == True:
            quiz()
        
        if lesson_button.pressed == True:
            lesson()
        
        if play_button.pressed == True:
            gameIntro()
        
        if exit_button.pressed == True:
            references()
        
        if results_button.pressed == True:
            noResults()
            
#Instruction Functions    
def exit():
    quit()

#To show references before exiting the program
def references():
    sources = True
    # creates a loop for the instructions
    while sources:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        # draws the background and images
        background.blit(referencesImg, (0, 0))
        
        # updates the display
        pygame.display.flip()
        time.sleep(10)
        exit()

def instructions():
    instructions = True
    # creates a loop for the instructions
    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        # draws the background and images
        background.blit(instructionsImg, (0, 0))
        next_button.draw()
        
        if next_button.pressed == True:
            time.sleep(0.25)
            ghost1()

        # updates the display
        pygame.display.flip()
        clock.tick(60)      
        instructions_button.pressed = False
        
#2nd page of the instructions
def ghost1():
    ghostOne = True
    # creates a loop for instruction page 2
    while ghostOne:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
    
            background.blit(ghostImg1, (0,0))
            next_button.draw()         
            
            if next_button.pressed == True:
                time.sleep(0.25)
                ghost2()
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)           
            
#3rd page of the instructions
def ghost2():
    ghostTwo = True
    # creates a loop for instruction page 3
    while ghostTwo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
    
            background.blit(ghostImg2, (0,0))
            next_button.draw()
            
            if next_button.pressed == True:
                time.sleep(0.25)
                ghost3()
            
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#4th page of the instructions            
def ghost3():
    ghostThree = True
    # creates a loop for instruction page 4
    while ghostThree:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(ghostImg3, (0,0))
            next_button.draw()
            
            if next_button.pressed == True:
                time.sleep(0.25)
                ghost4()
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#5th page of the instructions                
def ghost4():
    ghostFour = True
    # creates a loop for instruction page 5
    while ghostFour:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
    
            background.blit(ghostImg4, (0,0))
            next_button.draw()
            
            if next_button.pressed == True:
                time.sleep(0.25)
                ghost5()
            
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#6th page of the instructions
def ghost5():
    ghostFive = True
    # creates a loop for instruction page 6
    while ghostFive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(ghostImg5, (0,0))
            next_button.draw()
                
            if next_button.pressed == True:
                time.sleep(0.25)
                bossGhosts()
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)      
            
#displays the intro to the boss ghosts
def bossGhosts():
    boss = True
    # creates a loop for instruction page 6
    while boss:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(bossGhostsImg, (0,0))
            next_button.draw()
                
            if next_button.pressed == True:
                time.sleep(0.25)
                ghost6()
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)   
            
#displays the first boss ghost               
def ghost6():
    ghostSix = True
    # creates a loop for instruction page 6
    while ghostSix:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(ghostImg6, (0,0))
            next_button.draw()
                
            if next_button.pressed == True:
                time.sleep(0.25)
                ghost7()
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)     

            
#displays the second boss ghost
def ghost7():
    ghostSeven = True
    # creates a loop for instruction page 6
    while ghostSeven:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(ghostImg7, (0,0))
            next_button.draw()
                
            if next_button.pressed == True:
                time.sleep(0.25)
                ghost8()
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)       

#displays the third boss ghost                
def ghost8():
    ghostEight = True
    # creates a loop for instruction page 7
    while ghostEight:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
    
            background.blit(ghostImg8, (0,0))
            return_button.draw()
            
            if return_button.pressed == True:
                instructions_button.pressed = False
                main_menu()
            
            # updates the display
            pygame.display.flip()
            clock.tick(60)

correct = int(0)
#Quiz
def quiz():
    quizStart = True
    # creates a loop for the quiz
    while quizStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        # draws the background and images
        background.blit(quizImg, (0, 0))
        yes_play_button.draw()
        no_play_button.draw()

        if yes_play_button.pressed == True:
            time.sleep(0.25)
            quizQuestionOne()

        if no_play_button.pressed == True:
            time.sleep(0.25)
            main_menu()

        # updates the display
        pygame.display.flip()
        clock.tick(60)        
taken_quiz = bool(False)

#displays the first question
def quizQuestionOne():
    global correct
    global taken_quiz
    quizOne = True
    taken_quiz = True
    # creates a loop for quiz question 1
    while quizOne:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        # draws the background and images
        background.blit(q1Img, (0, 0))
        q1_o1_button.draw()
        q1_o2_button.draw()
        q1_o3_button.draw()
        q1_o4_button.draw()

        if q1_o1_button.pressed == True:
            time.sleep(0.25)
            correct += 1
            quizQuestionTwo()

        elif q1_o2_button.pressed == True or q1_o3_button.pressed == True or q1_o4_button.pressed == True:
            time.sleep(0.25)
            quizQuestionTwo()

        # updates the display
        pygame.display.flip()
        clock.tick(60)           

#displays the second question
def quizQuestionTwo():
    global correct
    quizTwo = True
    # creates a loop for quiz question 2
    while quizTwo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        # draws the background and images
        background.blit(q2Img, (0, 0))
        q2_o1_button.draw()
        q2_o2_button.draw()
        q2_o3_button.draw()
        q2_o4_button.draw()

        if q2_o1_button.pressed == True:
            correct += 1 
            time.sleep(0.25)
            quizQuestionThree()

        elif q2_o2_button.pressed == True or q2_o3_button.pressed == True or q2_o4_button.pressed == True:
            time.sleep(0.25)
            quizQuestionThree()

        # updates the display
        pygame.display.flip()
        clock.tick(60)                           

#displays the 3rd question
def quizQuestionThree():
    global correct
    quizThree = True
    # creates a loop for quiz question 3
    while quizThree:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        # draws the background and images
        background.blit(q3Img, (0, 0))
        q3_o1_button.draw()
        q3_o2_button.draw()
        q3_o3_button.draw()
        q3_o4_button.draw()

        if q3_o3_button.pressed == True:
            correct += 1
            time.sleep(0.25)
            quizQuestionFour()

        elif q3_o1_button.pressed == True or q3_o2_button.pressed == True or q3_o4_button.pressed == True:
            time.sleep(0.25)
            quizQuestionFour()        

        # updates the display
        pygame.display.flip()
        clock.tick(60)

#displays the fourth question
def quizQuestionFour():
    global correct
    quizFour = True
    # creates a loop for quiz question 4
    while quizFour:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
        # draws the background and images
        background.blit(q4Img, (0, 0))
        q4_o1_button.draw()
        q4_o2_button.draw()
        q4_o3_button.draw()
        q4_o4_button.draw()

        if q4_o4_button.pressed == True:
            correct += 1
            time.sleep(0.25)
            quizQuestionFive()

        elif q4_o1_button.pressed == True or q4_o2_button.pressed == True or q4_o3_button.pressed == True:
            time.sleep(0.25)
            quizQuestionFive()

        # updates the display
        pygame.display.flip()
        clock.tick(60)        

#displays question five
def quizQuestionFive():
    global correct
    quizFive = True
    # creates a loop for quiz question 5
    while quizFive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

        # draws the background and images
        background.blit(q5Img, (0, 0))
        q5_o1_button.draw()
        q5_o2_button.draw()
        q5_o3_button.draw()
        q5_o4_button.draw()

        if q5_o2_button.pressed == True:
            time.sleep(0.25)
            correct += 1
            results()
        elif q5_o1_button.pressed == True or q5_o3_button.pressed == True or q5_o4_button.pressed == True:
            time.sleep(0.25)
            results()
        # updates the display
        pygame.display.flip()
        clock.tick(60)   

#displays the results        
def results():
    percentage = correct * 20
    W = 400
    Z = 250
    R = 500
    S = 350
    T = 800
    U = 900
    show_results = True
    font = pygame.font.Font('Fonts/Fonts/Rye-Regular.ttf', 64)
    font1 = pygame.font.Font('Fonts/Fonts/Rye-Regular.ttf', 32)
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(str(percentage) + "% (" + str(correct) + "/5)", True, WHITE)
    text1 = font.render("Thanks for taking the quiz!", True, WHITE)
    text2 = font.render("Your results are below:", True, WHITE)
    text3 = font1.render("Uh oh! You didn't do too well!", True, WHITE)
    text4 = font1.render("Good job! You did very well!", True, WHITE)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    textRect1 = text.get_rect()
    textRect2 = text.get_rect()
    textRect3 = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)
    textRect1.center = (W // 2, Z // 2) 
    textRect2.center = (R // 2, S // 2)
    textRect3.center = (T // 2, U //2)
    # creates a loop for instruction page 5
    while show_results:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(backgroundImg, (0,0))
            background.blit(text, textRect)
            background.blit(text1, textRect1)
            background.blit(text2, textRect2)
            if percentage <= 60:
                background.blit(text3, textRect3)
            else:
                background.blit(text4, textRect3)
            return_button.draw()
            if return_button.pressed == True:
                show_quiz = False
                gameLoop()
            # updates the display
            pygame.display.flip()
            clock.tick(60)    

#displays the first lesson slide           
def lesson():
    slide1 = True
    # creates a loop for instruction page 5
    while slide1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(lesson1Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_2()

            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#displays the 2nd slide
def lesson_2():
    slide2 = True
    # creates a loop for instruction page 5
    while slide2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson2Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_3()

            # updates the display
            pygame.display.flip()
            clock.tick(60)    

#displays the 3rd slide
def lesson_3():
    slide3 = True
    # creates a loop for instruction page 5
    while slide3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson3Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_4()

            # updates the display
            pygame.display.flip()
            clock.tick(60)    

#displays the 4th slide
def lesson_4():
    slide4 = True
    # creates a loop for instruction page 5
    while slide4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(lesson4Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_5()

            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#displays the 5th slide
def lesson_5():
    slide5 = True
    # creates a loop for instruction page 5
    while slide5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson5Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_6()

            # updates the display
            pygame.display.flip()
            clock.tick(60)   

#displays the 6th slide            
def lesson_6():
    slide6 = True
    while slide6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson6Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_7()

            # updates the display
            pygame.display.flip()
            clock.tick(60)  

#displays the 7th slide            
def lesson_7():
    slide7 = True
    while slide7:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson7Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_8()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

#displays the 8th slide
def lesson_8():
    slide8 = True
    while slide8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson8Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_9()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

#displays the 9th slide
def lesson_9():
    slide9 = True
    while slide9:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(lesson9Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_10()

            # updates the display
            pygame.display.flip()
            clock.tick(60) 

#displays the 10th slide
def lesson_10():
    slide10 = True
    while slide10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson10Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_11()

            # updates the display
            pygame.display.flip()
            clock.tick(60) 

#displays the 11th slide
def lesson_11():
    slide11 = True
    while slide11:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(lesson11Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_12()

            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#displays the 12th slide
def lesson_12():
    slide12 = True
    while slide12:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson12Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_13()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

#displays the 13th slide
def lesson_13():
    slide13 = True
    while slide13:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson13Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson_14()

            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#displays the 14th slide
def lesson_14():
    slide14 = True
    while slide14:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(lesson14Img, (0,0))
            return_button.draw()

            if return_button.pressed == True:
                main_menu()

            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#This function tells the user to take the quiz if they try to access results before taking it
def noResults():
    global taken_quiz
    if taken_quiz == False:
        noQuizAnswers = True
        font = pygame.font.Font('Fonts/Rye-Regular.ttf', 30)

        # on which text is drawn on it.
        text = font.render("You have not completed the quiz. Return back to", True, WHITE)
        text1 = font.render("the main menu if you want to take it.", True, WHITE)

        # create a rectangular object for the text surface object
        textRect = text.get_rect()
        textRect1 = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (DISPLAY_WIDTH // 2, 500// 2)
        textRect1.center = (1200// 2, 600// 2)

        # creates a loop for instruction page 5
        while noQuizAnswers:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    references()
                    
            background.blit(backgroundImg, (0,0))
            background.blit(text, textRect)
            background.blit(text1, textRect1)
            return_button.draw()

            if return_button.pressed == True:
                results_button.pressed = False
                main_menu()        

            # updates the display
            pygame.display.flip()
            clock.tick(60)
    else:
        results1()
        
#gives the user results and answer key if they've taken the quiz
def results1():
    percentage = correct * 20
    W = 400
    Z = 250
    R = 500
    S = 350
    T = 800
    U = 900
    M = 700
    N = 800
    show_results = True
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 64)
    font1 = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    # create a text surface object,
    # on which text is drawn on it.
    text = font.render(str(percentage) + "% (" + str(correct) + "/5)", True, WHITE)
    text1 = font.render("Thanks for taking the quiz!", True, WHITE)
    text2 = font.render("Your results are below:", True, WHITE)
    text3 = font1.render("Uh oh! You didn't do too well!", True, WHITE)
    text4 = font1.render("Good job! You did very well!", True, WHITE)
    text5 = font1.render("Press the button to see the right answers!", True, WHITE)
    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()
    textRect1 = text.get_rect()
    textRect2 = text.get_rect()
    textRect3 = text.get_rect()
    textRect4 = text.get_rect()
    # set the center of the rectangular object.
    textRect.center = (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)
    textRect1.center = (W // 2, Z // 2) 
    textRect2.center = (R // 2, S // 2)
    textRect3.center = (T // 2, U //2)
    textRect4.center = (M // 2, N // 2)
    # creates a loop for instruction page 5
    while show_results:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(backgroundImg, (0,0))
            background.blit(text, textRect)
            background.blit(text1, textRect1)
            background.blit(text2, textRect2)
            background.blit(text5, textRect4)
            if percentage <= 60:
                background.blit(text3, textRect3)
            else:
                background.blit(text4, textRect3)
                next_button.draw()
            if next_button.pressed == True:
                show_quiz = False
                results2()
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
#right answer for Q1
def results2():
    results2 = True
    while results2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(rightQ1Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                results3()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

#right answer for Q2
def results3():
    results3 = True
    while slide3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(rightQ2Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                results4()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

#right answer for Q3
def results4():            
    results4 = True
    while results4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(rightQ3Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                results5()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

#right answer for Q4
def results5():
    results5 = True
    while results5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(rightQ4Img, (0,0))
            next_button.draw()

            if next_button.pressed == True:
                lesson6()

            # updates the display
            pygame.display.flip()
            clock.tick(60) 

#right answer for Q5
def results6():
    results6 = True
    while results6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(rightQ5Img, (0,0))
            return_button.draw()

            if return_button.pressed == True:
                main_menu()

            # updates the display
            pygame.display.flip()
            clock.tick(60)    

#This function creates a fading effect to transition from one screen to another                     
def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        background.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

#The following functions are a series of screens which display conssectutivly and run our game.  Each scene loads a new background and generates a different occurences and some screens are informational slides 
def gameIntro1():
    gameIntro1 = True
    while gameIntro1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(pg1, (0,0))
            yes_play_button.draw()
            no_play_button.draw()
            if yes_play_button.pressed == True:
                time.sleep(0.25)
                fade(1000,600)
                scene1()
            
            if no_play_button.pressed == True:
                time.sleep(0.25)
                main_menu()

            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
def scene1():
    scene1 = True
    while scene1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(pg2, (0,0))
            next_button.draw()
            if next_button.pressed == True:
                fade(1000, 600)
                time.sleep(0.25)
                scene2()

            # updates the display
            pygame.display.flip()
            clock.tick(60) 

def scene2():
    sceneTwo = True
    while sceneTwo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(pg3, (0,0))
            next_button.draw()
            
            if next_button.pressed == True:
                time.sleep(0.25)
                scene3()

            # updates the display
            pygame.display.flip()
            clock.tick(60)  

def scene3():
    sceneThree = True
    while sceneThree:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()

            background.blit(pg4, (0,0))
            next_button.draw()
            
            if next_button.pressed == True:
                time.sleep(0.25)
                scene4()

            # updates the display
            pygame.display.flip()
            clock.tick(60) 

def scene4():
    sceneFour = True
    while sceneFour:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
            background.blit(pg5, (0,0))
            next_button.draw()
            


            # updates the display
            pygame.display.flip()
            clock.tick(60) 
            
#Gameloop which runs the main menu       
def gameLoop():
    correct = int(0)
    x = (DISPLAY_WIDTH * 0.45)
    y = (DISPLAY_HEIGHT * 0.8)
    gameExit = False

    while gameExit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                references()
                
        main_menu()
        reload() 
        
def gameIntro():
    gameIntro = True
    while gameIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg, (0,0))
            yes_play_button.draw()
            no_play_button.draw()
            if no_play_button.pressed == True:
                gameIntro1()
            if yes_play_button.pressed == True:
                main_menu()
            # updates the display
            pygame.display.flip()
            clock.tick(60) 

def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        background.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
        
def gameIntro1():
    gameIntro1 = True
    while gameIntro1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg1, (0,0))
            yes_play_button.draw()
            no_play_button.draw()
            if yes_play_button.pressed == True:
                fade(1000, 600)
                scene1()
            elif no_play_button.pressed == True:
                instructions()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

def scene1():
    scene1 = True
    while scene1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg2, (0,0))
            next_button.draw()
            if next_button.pressed == True:
                fade(1000, 600)
                scene2()

            # updates the display
            pygame.display.flip()
            clock.tick(60) 
            
def scene2():
    show_scene2 = True
    while show_scene2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg3, (0,0))
            next_button.draw()
            if next_button.pressed == True:
                scene3()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

def scene3():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)            
    show_scene3 = True
    while show_scene3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg4, (0,0))
            background.blit(text, textRect)
            pygame.display.flip()            
            time.sleep(2)
            scene4()
 
def scene4():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)            
    show_scene4 = True
    while show_scene4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg5, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(2)
            scene5()            

def scene5():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)            
    show_scene5 = True
    while show_scene5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg6, (0,0))
            scream_sound = mixer.Sound("Music/lightFlicker.wav")
            scream_sound.play()            
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(2)
            scene6()

def scene6():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)            
    show_scene6 = True
    while show_scene6:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg7, (0,0))
            scream_sound = mixer.Sound("Music/SprayPainting.wav")
            scream_sound.play()              
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip() 
            time.sleep(2)
            scene7()
         
number_of_lives = 2           
def scene7():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene7 = True
    while show_scene7:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg8, (0,0))
            background.blit(text, textRect)
            phantom_button.draw()
            grimReaper_button.draw()
            joltent_button.draw()
            auris_button.draw()
            remora_button.draw()
        
            
            if phantom_button.pressed == True:
                scene8()
            elif grimReaper_button.pressed == True or joltent_button.pressed == True or auris_button.pressed == True or remora_button.pressed == True:
                number_of_lives -= 1
                scene8()
            pygame.display.flip()
            clock.tick(60)
            
                    
def scene8():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)            
    phantom_button.pressed = False
    grimReaper_button.pressed = False
    joltent_button.pressed = False
    auris_button.pressed = False
    remora_button.pressed = False    
    show_scene8 = True

    while show_scene8:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg9, (0,0))  
            background.blit(text, textRect)
        
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene9()
            
def scene9():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)    
    show_scene9 = True
    while show_scene9:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
            
            background.blit(pg10, (0,0))
            scream_sound = mixer.Sound("Music/lightFlicker.wav")
            scream_sound.play()             
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)            
            scene10()            

def scene10():
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)      
    show_scene10 = True
    while show_scene10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg11, (0,0))
            background.blit(text, textRect)            
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)            
            scene11()
                
def scene11():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)    
    show_scene11 = True
    while show_scene11:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg12, (0,0))
            background.blit(text, textRect)                        
            phantom_button.draw()
            grimReaper_button.draw()
            joltent_button.draw()
            auris_button.draw()
            remora_button.draw()
          
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
            if joltent_button.pressed == True: 
                scene12()     
            elif grimReaper_button.pressed == True or auris_button.pressed == True or remora_button.pressed == True or phantom_button.pressed == True:
                number_of_lives -= 1
                if number_of_lives == 0:
                    ending1()
                else:
                    scene12()
                    
#Ending #1 for the game                    
def ending1():
    ending1 = True
    while ending1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(ending1Img, (0,0))
            return_button.draw()
            
            if return_button.pressed == True:
                main_menu()
            # updates the display
            pygame.display.flip()
            clock.tick(60)
def scene12():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    phantom_button.pressed = False
    grimReaper_button.pressed = False
    joltent_button.pressed = False
    auris_button.pressed = False
    remora_button.pressed = False      
    show_scene12 = True
    while show_scene12:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
                
            background.blit(pg13, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3) 
            scene13()

def scene13():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene13 = True
    while show_scene13:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg14, (0,0))
            scream_sound = mixer.Sound("Music/lightFlicker.wav")
            scream_sound.play()            
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.5)
            scene14()
            
def scene14():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene14 = True
    while show_scene14:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg15, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.5)
            scene15()

def scene15():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene15 = True
    while show_scene15:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg14, (0,0))
            scream_sound = mixer.Sound("Music/lightFlicker.wav")
            scream_sound.play()
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.5)
            scene16()
            
def scene16():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene16 = True
    while show_scene16:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg15, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.5)
            scene17()
            
def scene17():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene13 = True
    while show_scene13:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg14, (0,0))
            scream_sound = mixer.Sound("Music/lightFlicker.wav")
            scream_sound.play()                  
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.5)
            scene18()

def scene18():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene14 = True
    while show_scene14:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg15, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene19()

def scene19():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene19 = True
    while show_scene19:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg16, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene20()

def scene19():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene19 = True
    while show_scene19:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg16, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene20()
            
def scene20():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)        
    show_scene20 = True
    while show_scene20:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
                
            background.blit(pg17, (0,0))
            background.blit(text, textRect)
            phantom_button.draw()
            grimReaper_button.draw()
            joltent_button.draw()
            auris_button.draw()
            remora_button.draw()
          
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
            if grimReaper_button.pressed == True: 
                scene21()   
            elif joltent_button.pressed == True or auris_button.pressed == True or remora_button.pressed == True or phantom_button.pressed == True:
                number_of_lives -= 1
                if number_of_lives == 0:
                    ending2()

#Ending #2 for the game
def ending2():
    ending2 = True
    while ending2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(ending2Img, (0,0))
            return_button.draw()
            
            if return_button.pressed == True:
                main_menu()
            # updates the display
            pygame.display.flip()
            clock.tick(60)
def scene21():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    phantom_button.pressed = False
    grimReaper_button.pressed = False
    joltent_button.pressed = False
    auris_button.pressed = False
    remora_button.pressed = False        
    show_scene21 = True
    while show_scene21:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg18, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene22()

def scene22():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene22 = True
    while show_scene22:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg19, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene23()

def scene23():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene23 = True
    while show_scene23:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg20, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.2)
            scene24()

def scene24():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene24 = True
    while show_scene24:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg21, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.2)
            scene25()

def scene25():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene25 = True
    while show_scene25:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg22, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.2)
            scene26()

def scene26():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene26 = True
    while show_scene26:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg23, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.2)
            scene27()

def scene27():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene27 = True
    while show_scene27:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg24, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.2)
            scene28()

def scene28():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene28 = True
    while show_scene28:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg25, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.2)
            scene29()  

def scene29():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene29 = True
    while show_scene29:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg26, (0,0))
            shattering_sound = mixer.Sound("Music/breakingPot.wav")
            shattering_sound.play()              
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            time.sleep(0.2)
            scene30()
            
def scene30():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene30 = True
    while show_scene30:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
                
            background.blit(pg27, (0,0))
            background.blit(text, textRect)
            phantom_button.draw()
            grimReaper_button.draw()
            joltent_button.draw()
            auris_button.draw()
            remora_button.draw()
          
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            
            if auris_button.pressed == True:
                scene31()
            elif phantom_button.pressed == True or grimReaper_button.pressed == True or joltent_button.pressed == True or remora_button.pressed == True:
                number_of_lives -= 1
                if number_of_lives == 0:
                    ending3()
                else:
                    scene31()
                    
#Ending #3 for the game                    
def ending3():
    ending3 = True
    while ending3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(ending3Img, (0,0))
            return_button.draw()
            
            if return_button.pressed == True:
                main_menu()
            # updates the display
            pygame.display.flip()
            clock.tick(60)

def scene31():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)      
    phantom_button.pressed = False
    grimReaper_button.pressed = False
    joltent_button.pressed = False
    auris_button.pressed = False
    remora_button.pressed = False        
    show_scene31 = True
    while show_scene31:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg28, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene32() 

def scene32():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)      
    show_scene32 = True
    while show_scene32:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg29, (0,0))
            scream_sound = mixer.Sound("Music/lightFlicker.wav")
            scream_sound.play()                        
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene33()

def scene33():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)      
    show_scene33 = True
    while show_scene33:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg30, (0,0))
            scream_sound = mixer.Sound("Music/scream.wav")
            scream_sound.play()            
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene34()

def scene34():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    show_scene34 = True
    while show_scene34:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            background.blit(pg31, (0,0))
            background.blit(text, textRect)
            phantom_button.draw()
            grimReaper_button.draw()
            joltent_button.draw()
            auris_button.draw()
            remora_button.draw()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

            if remora_button.pressed == True:
                scene35()
            elif phantom_button.pressed == True or grimReaper_button.pressed == True or joltent_button.pressed == True or auris_button.pressed == True:
                number_of_lives -= 1
                if number_of_lives == 0:
                    ending2()
                else:
                    scene35()
    
def scene35():
    phantom_button.pressed = False
    grimReaper_button.pressed = False
    joltent_button.pressed = False
    auris_button.pressed = False
    remora_button.pressed = False        
    show_scene35 = True
    while show_scene35:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg32, (0,0))
            next_button.draw()
            
            # updates the display
            pygame.display.flip()
            clock.tick(60)                
            
            if next_button.pressed == True:
                time.sleep(0.25)
                scene36() 
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)               

def scene36():
    show_scene36 = True
    while show_scene36:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg33, (0,0))
            next_button.draw()
            
            
            if next_button.pressed == True:
                time.sleep(1)
                scene37()
            
            # updates the display
            pygame.display.flip()
            clock.tick(60)               
    
def scene37():
    show_scene37 = True
    while show_scene37:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg34, (0,0))
            next_button.draw()
            
            # updates the display
            pygame.display.flip()
            clock.tick(60)    
            
            if next_button.pressed == True:
                time.sleep(3)
                scene38()
            # updates the display
            pygame.display.flip()
            clock.tick(60)      
            
def scene38():
    show_scene38 = True
    while show_scene38:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg35, (0,0))
            next_button.draw()
           
            # updates the display
            pygame.display.flip()
            clock.tick(60)     
            
            if next_button.pressed == True:
                time.sleep(3)
                scene39()
                
            # updates the display
            pygame.display.flip()
            clock.tick(60)               
            
def scene39():
    show_scene39 = True
    while show_scene39:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg36, (0,0))
            next_button.draw()    

            # updates the display
            pygame.display.flip()
            clock.tick(60)   
            
            if next_button.pressed == True:
                time.sleep(3)
                scene40()             
            # updates the display
            pygame.display.flip()
            clock.tick(60)       
            
def scene40():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene40 = True
    while show_scene40:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg37, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(2)
            scene41()            
        
def scene41():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene41 = True
    while show_scene41:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg38, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene42()

def scene42():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene42 = True
    while show_scene42:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg39, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene43()

def scene43():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)         
    show_scene43 = True
    while show_scene43:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()   
            background.blit(pg40, (0,0))
            background.blit(text, textRect)
            # updates the display
            pygame.display.flip()
            clock.tick(60)
            time.sleep(3)
            scene44()

def scene44():
    global number_of_lives
    X = 400
    Y = 75
    font = pygame.font.Font('Fonts/Rye-Regular.ttf', 32)
    text = font.render("Number of lives: " + str(number_of_lives), True, WHITE)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    show_scene44 = True
    while show_scene44:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            background.blit(pg41, (0,0))
            background.blit(text, textRect)
            menos_button.draw()
            vexa_button.draw()
            klaus_button.draw()

            # updates the display
            pygame.display.flip()
            clock.tick(60)

            if klaus_button.pressed == True:
                ending4()

            elif menos_button.pressed == True or vexa_button.pressed == True:
                number_lives -= 1
                if number_of_lives == 0:
                    ending3()
                else:
                    ending4()
#Ending #4 for the game
def ending4():
    ending4 = True
    while ending4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            background.blit(ending4Img, (0,0))
            scream_sound = mixer.Sound("Music/lightFlicker.wav")
            scream_sound.play()            
            return_button.draw()

            if return_button.pressed == True:
                main_menu()
            # updates the display
            pygame.display.flip()
            clock.tick(60)

#Calling the functions        
title_screen()
main_menu()        
gameLoop()