# https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables ok I am in my own enviroment

import csv
import os.path
from random import randint

#Just for an aesthetic delay before the game loop starts
import time
   
class Scientist:
    # Class var for score, just easier this way
    Score = 0

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
        del list[0]
        self.response = list
        print("here are my responses", self.response)

    def setting_in_game_questions(self):
        self.game_questions = self.questions 

    def del_question(self, index):
        try: 
            del self.game_questions[index]
        except:
            print("Propbably no more questions")

    def load_description(self):
        pass
        # this will run at the end of the game, it will load a file with info about scientist and references
    def create_scientists(self):
        pass


#This function will handle the "front screen"       
def Game_Intro():
    print("Welcome to the ODWM gesser game! I, the computer will guess what physicist you are thinking of!")
    # print out some rules and maybe some code so I can play


def Game_Settings():
    print("here are the game settings")
    print("Do you want only ODWM?")
    odwm = input()
    print("What physics unit do you want? Type 1 for all, type 2 for F&F, type 3 for EMR, type 4 for Atomic")
    unit = input()
    print("Do you only want to play with physicists whose expariments are on the diploma?")
    diploma = input()
    
    return odwm, unit, diploma

def Name_Print(name_list):
    for people in name_list:
        print(people.name)
                
def Scientist_Sort(sci_list):

    man, unit, dip = Game_Settings()
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



 
#This function only checks if there is a game file present and imports general questions from csv
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
            print("The file is created! It is a little empty don't you think?")
    else:
        print("Game file found")


    with open(file_name, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        questions_list = list(csv_reader)
        questions_list = questions_list[1]
    del questions_list[0]
    #del questions_list[-1] this code just delets the last question-- not helpful

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
    #del response_list[-1] This would cause the last person in the list to be deleted and cause issues
    print("response list", response_list)

    # for all scientists selected, use their number name index to load reponses to the questions and make it a new attrubute to them
    for small_list in response_list:

        #then looks at all the scientists in the game
        for scientist in selected_sci_list:

            #checks to see if the name of the current scientist object is equal to the name assosaited with the response list
            #if so then that is the response list for the object and a new attrubute is made 
            if scientist.name == small_list[0]:
                scientist.response_asign(small_list)

            


# 0 will be for general questions and 1 will be for spefic questions
def General_Question_Picker(general_questions_list, blacklist):
    user_response = 0

    #General question code, it will select 
    

    #yep, this line of code returns the last index of the last question in the list
    general_questions_length = len(general_questions_list) - 1

    print("general, questions length, this should be the index of last thing in the list ", general_questions_length)
    print(general_questions_list[general_questions_length])

    print("HERE IS QUESTIONS LIST:::  ", general_questions_list)

    
    #makes the randint run until it picks a number that corisponds to an index of a question that has not been picked before 
    while True:
        count = 0 
        temp_decision = randint(0, general_questions_length)
        for number in blacklist:
            if temp_decision == number:
                count += 1 
        if count < 1:
            print("break")
            break
    
    #since a question has been picked, that question is now on black list ot prevent repition
    blacklist.append(temp_decision)
    print("blacklisted question indces::: ", blacklist)


    temp_question = general_questions_list[temp_decision]

    
    print('\n')
    print(f"{temp_question} Is this true or false?")
    
    #While loop so user has to enter 1 or 0
    while True:
        user_response = int(input())
        if user_response == 1 or user_response == 0:
            break
        else:
            print("Not true or false input")


    #Code returns the index of the question it askes 
    return user_response, temp_decision, blacklist
    
   

#This code handles if a specific question was chosen to be asked       
def Specific_Question_Picker(sci_in_game):
    print('\n', "SPECIFIC QUESTION CODE", '\n')
    user_response = 0

    scientist_list_length = len(sci_in_game) - 1

    print(scientist_list_length)
    
    #enures that a scientist with specific questions gets picked IT DOES NOT ENSURE SCI STILL HAS QUESTIONS
    error_count = 0
    while True:
        temp_sci_decision = randint(0, scientist_list_length)
        selected_sci = sci_in_game[temp_sci_decision]
        

        #Extra condition in if statement makes sure the even if the scientst had questions is still has something to choose from
        #This could cause infinate loop issues if there are no scientists with questions left but oh well
        if selected_sci.game_questions == None or len(selected_sci.game_questions) <= 0:
            error_count = error_count + 1
            #print("finding ", error_count)
        else:
            #minus one so that it shifts the amount of elements to be how the index of those elements are, question_list_length is the index of last element
            question_list_length = len(selected_sci.game_questions) - 1 
            break

        #this isnt the right error for this issue but it will let me know
        if error_count > 2000:
            raise LookupError

    #print("question_list_length", question_list_length)

    temp_question_decision = randint(0, question_list_length)

    print("selected_sci.game_questions, ", selected_sci.game_questions)

    selected_question = selected_sci.game_questions[temp_question_decision]

    #print(selected_question, "yeahhhhhh")

    print('\n')
    print(f"{selected_question} Is this true or false?")

    #While loop so user has to enter 1 or 0
    while True:
        user_response = int(input())
        if user_response == 1 or user_response == 0:
            break
        else:
            print("Not true or false input")

    selected_sci.del_question(temp_question_decision)

    return user_response, selected_sci


#Handles assigning general score values for a general question
def General_Score_Assign(sci_in_game, question_index, user_answer):
    print("Now assigning general score")
    user_answer = int(user_answer)
    print(len(sci_in_game))

    if user_answer == 1:
        print("Printing dict of all scientists:", '\n')
        for scientist in sci_in_game:
            print(scientist.__dict__)
        print('\n')
        for people in sci_in_game:
            people.Score += int(people.response[question_index])
            print(f"Here is {people.name}'s new score {people.Score}")
            #print("Here is my dict.", scientist.__dict__)
        

    elif user_answer == 0:
        print("Printing dict of all scientists:", '\n')
        for scientist in sci_in_game:
            print(scientist.__dict__)
        print('\n')
        for scientist in sci_in_game:
            scientist.Score += -1*int(scientist.response[question_index])
            print(f"Here is {scientist.name}'s new score {scientist.Score}")


def Specific_Score_Assign(user_answer, selected_scientist, sci_in_game):
    print("Now assiging a specific, heavy score")

    #If the user answers true, then it is a good chance this is the scientist they are thinkinh of and not any others
    #So this scientist gets a large score but the others get a negitive score
    #print(f"The selected scientist is {selected_scientist.name}")
    
    print("the selected sci is", selected_scientist.name)
    if user_answer == 1:
        for scientists in sci_in_game:
            scientists.Score += -20
            print(f"Here is {scientists.name}'s new score {scientists.Score}")
        selected_scientist.Score += + 40
        print(f"Here is {selected_scientist.name}'s REAL new score {selected_scientist.Score}")

    elif user_answer == 0:
        selected_scientist.Score += -20
        print(f"Here is {selected_scientist.name}'s new score {selected_scientist.Score}") 

    """ if user_answer == 1: 
        selected_scientist.Score += 20
        sci_in_game.remove(selected_scientist)
        print(f"Here is {selected_scientist.name}'s new score {selected_scientist.Score}")
        
        for others in sci_in_game:

            others.Score += -20
            print(f"Here is {others.name}'s new score {others.Score}") """
    
    #Only the score of the scientist changes, just becuase this question is false doesnt mean the other scientists are right


    


game_file_name = "Questions_and_Answers.csv"

sci_1_questions = ["Did my experimental apparatus originally use water droplets, but in 1910 I changed the substance because the droplets evaporated too fast to make measurements?", "Was a key piece of work I built off of the charge to mass ratio of an electron that was discovered by Thomson?", "In 1916, did I also devise another experiment to measure another fundamental constant? Did I also use a previous constant I measured in my calculations?"] 
sci_6_questions =["Did my discovery explain why arc lighting lamps -- the common electrical lighting technology of my time -- varied in their brightness and were inefficient?", "Using my discoveries, did my subsequent patients go on to be used from military anti-aircraft searchlights to more efficient street lamps?", "Was I the first female member of the Institution of Electrical Engineers (Now the Institution of Engineering and Technology?"]


sci_1 = Scientist("Millikan", 1, 2, None, 1, 1, sci_1_questions)
sci_2 = Scientist("Faraday",2,2,None,0,1,None)
sci_3 = Scientist("Coulomb", 3,2, None, 1, 1, None)
sci_4 = Scientist("Henry",4,2,None,0,1,None)
sci_5 = Scientist("Einstein",5,3,None,0,1,None)
sci_6 = Scientist("Ayrton",6,2,None,0,0,sci_6_questions)

#The list of all the scientist objects
scientist_list = [sci_1, sci_2, sci_3, sci_4, sci_5, sci_6]

#List of the scientist objects that made it through the filter
selected_sci_list = []
questions_dump = []
blacklist = []


#The game code:
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

print(sci_1.Score, Scientist.Score)

Game_Intro()

while len(selected_sci_list) <= 1:
    #runs the filter selection code so and lets user know about how big the game will be
    #if less than or equal to one scientist is in the game that wouldnt be that fun so the user will choose new filter parameters
    
    selected_sci_list = Scientist_Sort(scientist_list)
    print(f"The parameters you selected resulted in {len(selected_sci_list)} scientists present in the game")

    if len(selected_sci_list) <= 1:
        print("Pick new filtes because that number of scientists wouldnt be fun to play with")

#Name_Print(selected_sci_list)

questions_dump = Loading_Game_Data(game_file_name, selected_sci_list)

Loading_Question_Responses(game_file_name, selected_sci_list)


print("The game is now startingggg")
for i in range(7):
    print(".")
    time.sleep(0.5)

for people in selected_sci_list:
    people.setting_in_game_questions()

print("HERE ARE THE SELECTED SCI::: ")
for people in selected_sci_list:
    print(people.name)




while True:

    # 0 will be for general questions and 1 will be for spefic questions 
    temp_question_type = randint(0,1)
    if temp_question_type == 0:
        user_answer, chosen_question_index, blacklist = General_Question_Picker(questions_dump, blacklist)
        General_Score_Assign(selected_sci_list, chosen_question_index, user_answer)

    elif temp_question_type == 1:
        user_answer, chosen_scientist = Specific_Question_Picker(selected_sci_list)
        Specific_Score_Assign(user_answer, chosen_scientist, selected_sci_list)


    









    

### issues to fix why is henry comin up so much in the terminal? 
#### why doent Enistin have a response?
#Why does the spific question picker sometimes break?
#Remove the first index of the response list, the name of the scientist
# Issue why does Millikan disapeer after a few questions? After all the general questions have been used up Millikan's name disappers and print dict happens
# At some point in the code Millikan just is removed, also happens when Millikan has a high score