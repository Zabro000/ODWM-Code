# https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables ok I am in my own enviroment

import csv
import os.path


#This function will handle the "front screen"       
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
   

class Scientist:

    def __init__(self, name, num_name, physics_unit, respose_list, expariment, odwm, special_questions):
        self.name = name
        self.num = num_name
        self.physics_unit = physics_unit
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

    #Assigns and creates response attruibute for only the scientists in the game
    def response_asign(self, list):
        self.response = list
        print("here are my responses", self.response)


    def load_description(self):
        pass
        # this will run at the end of the game, it will load a file with info about scientist and references
    def create_scientists(self):
        pass


    def Game_code(scientists):
        od, unit, diploma_exp = Game_Intro()

def Scientist_Sort(sci_list):

    man, unit, dip = Game_Intro()
    man = int(man)
    dip = int(dip)
    unit = int(unit)
    print("unit", unit)

    if man == 1:
        sci_list2 = []
        length = len(sci_list)
        for i in range(length):
            if sci_list[i].odwm == True:
                sci_list2.append(sci_list[i])
        sci_list = sci_list2

    if unit == 1:
        print("all scientists are selected")
    else: 
        sci_list2 = []
        length = len(sci_list)
        for i in range(length):
            if unit == sci_list[i].physics_unit:
                sci_list2.append(sci_list[i])
        sci_list = sci_list2


    if dip == 1:
        print("Only scientists whose expariments are on the diploma selected")
        sci_list2 = []
        length = len(sci_list)
        for i in range(length):
            if sci_list[i].diploma_expariment == True:
                sci_list2.append(sci_list[i])
        sci_list = sci_list2

    return sci_list
                


#This is the function that creates, opens, and handles the main list of questions and scientist's reponsies to them and esnures all the elements in the rows are filled out
#This function will also asign or read the row numbers assosiated with each scientist
#How do I load the questions and the socres?

#The goal of this function is to build the big list of questions to randomly choose from 
game_file_name = "Questions_and_Answers.csv"
def Loading_Game_Data(file_name, selected_sci_list):
    #this will look for the main responses list file
    #This code will look to see if the game file exists 
    questions_list = []

    file_path = f'./{file_name}'
    file_state = os.path.isfile(file_path)
    print(file_state)

    if file_state == False:
        print("The game file is missing!!!!, attempting to create a new one")
        with open(file_name,'x'):
            print("The file is created!")
    else:
        print("Game file found")


    for people in selected_sci_list:
        names_list = str(people.name)
    
    #print("names of selected people:", names_list)

    with open(file_name, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        questions_list = list(csv_reader)
        questions_list = questions_list[1]
    del questions_list[0]
    del questions_list[-1]

    #Parses each question in list of questions from each scienist
    for people in selected_sci_list:
        temp_list = people.questions
        # for loop to parse every question in the list from a scientist
        # try statement to handle if in the list of question there is a None type
        try:
            for element in temp_list:
                 questions_list.append(element)
        except:
            # if there is a none then do nothing and continue through the list
            pass
    
    print("QUESTIONS LIST  ", questions_list)
    return questions_list
        

# Goal of this function is to assign each list of responses to the scientists loaded objects
def Loading_Question_Responses(file_name, selected_sci_list):

    with open(file_name, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        response_list = list(csv_reader)
    
    # deleting the first two rows -- index and questions -- so i only have the scientists present in the list thats why I am deleting 0 twice
    del response_list[0]
    del response_list[0]
    del response_list[-1]
    print("response list", response_list)

    for responder in response_list:
        temp_small_list = responder
        for scientist in selected_sci_list:
            if scientist.name == temp_small_list[0]:
                scientist.response_asign(temp_small_list)

   
        









    # for all scientists selected, use their number name index to load reponses to the questions and make it a new attrubute to them





def Name_Print(name_list):
    for people in name_list:
        print(people.name)







sci_1_questions = ["Did my experimental apparatus originally use water droplets, but in 1910 I changed the substance because the droplets evaporated too fast to make measurements?", "Was a key piece of work I built off of the charge to mass ratio of an electron that was discovered by Thomson?", "In 1916, did I also devise another experiment to measure another fundamental constant? Did I also use a previous constant I measured in my calculations?"] 

sci_1 = Scientist("Millikan", 1, 2, None, 1, 1, sci_1_questions)
sci_2 = Scientist("Faraday",2,2,None,0,1,None)
sci_25 = Scientist("Faradayyy",2,2,None,0,1,None)
sci_3 = Scientist("Coulomb", 3,2, None, 1, 1, None)
sci_4 = Scientist("Henry",4,2,None,0,1,None)
sci_5 = Scientist("Einstein",5,3,None,0,1,None)

scientist_list = [sci_1, sci_2, sci_25, sci_3, sci_4, sci_5]
selected_sci_list = []

while len(selected_sci_list) < 1:
    selected_sci_list = Scientist_Sort(scientist_list)

Name_Print(selected_sci_list)

Loading_Game_Data(game_file_name, selected_sci_list)

Loading_Question_Responses(game_file_name, selected_sci_list)

print(sci_3.response)





    

