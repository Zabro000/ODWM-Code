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
        print("Game file found")


    
    #printing quesiton lists


# given the game intro prarameters if zero scientists fit raise error 

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

def Game_code():
    odwm, unit, diploma_exp = Game_Intro()
    



class Scientist:

    def __init__(self, name, num_name, physics_unit, respose_list, expariment, odwm, special_questions):
        self.name = name
        self.num = num_name
        self.unit = physics_unit
        self.respose_list = respose_list
        self.diploma_expariment = bool(expariment)
        self.odwm = bool(odwm)
        self.questions = special_questions
        pass

    def load_scientists(self, list): 
        pass
        #parse through the each row and load the scientists with spificied quailities and also load their unique questions
        #Unique questions will only affect the score of the scientst they are for
        # All Spceical questions are +20 or a high score
    
    
    def print_summary(self):
        Units = ["forces and fields", "EMR", "atomic"]
        print(f"This Scientists name is {self.name} and they are found in {Units[self.unit -1]}")


    def load_description(self):
        pass
        # this will run at the end of the game, it will load a file with info about scientist and references
    def create_scientists(self):
        pass

sci_1 = Scientist("Millikan", 1, 1, None, 1, 1, ["Did I first decide to use water droplets for my 1909 expariment", "I used the charge to mass ratio, figured out by JJ Thopmson for my expariement"])
sci_2 = Scientist("Faraday", 2, 1, None, 0, 1, None)
sci_3 = Scientist("Coulomb", 3, 1, None, 1, 1, None)
sci_4 = Scientist("Henry", 4, 1, None, 0, 1, None)

Game_list(Gamefile_Name)
print(sci_1.name)
print(sci_1.odwm)
print(sci_1.questions)

#Csv(Gamefile_Name)


#### To do  different sets of questions for each unit some how split it up


