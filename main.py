# https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables ok I am in my own enviroment

import csv
import os.path

#This is the function that creates, opens, and handles the main list of questions and scientist's reponsies to them and esnures all the elements in the rows are filled out
#This function will also asign or read the row numbers assosiated with each scientist

Gamefile_Name = "Questions_and_Answers.csv"
def Game_list(File_Name):
    #this will look for the main responses list file
    #This code will look to see if the game file exists 

    FIle_Path = f'./{File_Name}'
    File_State = os.path.isfile(FIle_Path)
    print(File_State)

    if File_State == False:
        print("The game file is missing!!!!, attempting to create a new one")
        with open(File_Name,'x'):
            print("The file is created!")
    else:
        print("found")


#def Csv(File_Name):
   # with open(File_Name, 'w') as File:
        #Writer = csv.writer(File)
        #Headers = [["index"], ["llll"]]
       # Length = len(Headers)

       # for i in range(Length):
         #   Writer.writerow(Headers[i])

    
       
        
def Game_Intro():
    print("Welcome to the ODWM gesser game! I the computer will guess what physicist you are thinking of!")
    print("To start this game you need to set some settings")
    print("Do you want only ODWM?")
    odwm = input()
    print("What physics unit do you want? Type 1 for all, type 2 for F&F, type 3 for EMR, type 4 for Atomic")
    unit = input()
    print("Do you only want to play with physicists whose expariments are on the diploma?")
    diploma = input()
    
    return odwm, unit, diploma
   
    #This function will handle the "front screen"

class Scientist:

    def __init__(self, name, num_name, physics_unit, respose_list, expariment, odwm):
        self.name = name
        self.num = num_name
        self.unit = physics_unit
        self.respose_list = respose_list
        self.diploma_expariment = expariment
        self.odwm = odwm
        pass

    def load_scientists(self): 
        pass
        #parse through the each row and load the scientists with spificied quailities 
    def load_description(self):
        pass
        # this will run at the end of the game, it will load a file with info about scientist and references
    def create_scientists(self):
        pass

sci_1 = Scientist("Millikan", 1, 1, None, 1, 1)

Game_list(Gamefile_Name)
Game_Intro()
print(sci_1.name)

#Csv(Gamefile_Name)


