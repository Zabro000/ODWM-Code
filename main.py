#AS TIME GOES ON I WILL ADD MORE QUESTIONS FOR THE SCIENTISTS PRESENT


import csv
import os.path
from random import randint
import math 

#Just for an aesthetic delay before the game loop starts
import time
   
class Scientist:
    # Class var for score, just easier this way
    Score = 0
    Temp_Score = 0

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
        #print("here are my responses", self.response)

    def setting_in_game_questions(self):
        self.game_questions = self.questions 

    def del_question(self, index):
        try: 
            del self.game_questions[index]
        except:
            print("Propbably no more questions")



def Bool_Input():

    good_input = False

    while good_input == False:
        user_bool = input()
        user_bool = user_bool.lower()
    
        if user_bool == "y":
            user_bool = True
            good_input = True
        elif user_bool =="n":
            user_bool = False
            good_input = True
        elif user_bool == "yes":
            user_bool = True
            good_input = True
        elif user_bool == "no":
            user_bool = False
            good_input = True
        elif user_bool == "1":
            user_bool = True
            good_input = True
        elif user_bool == "0":
            user_bool = False
            good_input = True
        elif user_bool == "t":
            user_bool = True
            good_input = True
        elif user_bool == "f":
             user_bool = False
             good_input = True
        elif user_bool == "true":
            user_bool = True
            good_input = True
        elif user_bool == "false":
            user_bool = False
            good_input = True
        elif user_bool == "yeah":
            user_bool = True
            good_input = True
        elif user_bool == "nah":
            user_bool = False
            good_input = True
        else:
            print("This is a bad input, please try again.", '\n')
            print("Input, “y”, “yes”, “true”, “yeah”, or “1” for yes, and input, “n”, “no”, false, “nah”, or “0” for false. Capitalizing the letters in your input does not matter; for example, “YES”, or “nO” would still be a valid input.", '\n')
    

    return user_bool



def Game_Settings():

    good_input = False

    print("Do you only want old dead white men (physics 30 curriculum physicists)? Note, there are physicists outside of the curriculum too!")
    odwm = Bool_Input()

    print("What physicists from which unit do you want to load? Input, 1 for all, 2 for F&F, 3 for EMR, and 4 for Atomic.")

    #I don't use my function for inputs here because the inputs here are not bools
    while good_input == False:
        unit = input()

        try:
            unit = int(unit)
        except:
            unit = None
        
        if unit == 1:
            good_input = True
        elif unit == 2:
            good_input = True
        elif unit == 3:
            good_input = True
        elif unit == 4:
            good_input = True

        else:
            print("This is a bad input, please try again.", '\n')
            print("Remember input, 1 for all, 2 for F&F, 3 for EMR, and 4 for Atomic.", '\n')


    print("Do you only want to play with physicists whose expariments are on the diploma?")

    diploma = Bool_Input()
    
    return odwm, unit, diploma

def Name_Print(name_list):
    for people in name_list:
        print(people.name)
                
def Scientist_Sort(sci_list):

    man, unit, dip = Game_Settings()


    #Filter for old dead white men or people in the course 
    if man == True:
        sci_list2 = []
        length = len(sci_list)
        for i in range(length):
            if sci_list[i].odwm == 1:
                sci_list2.append(sci_list[i])
        sci_list = sci_list2
    
    #Filter scientists from what unit
    if unit == 1:
        pass
    else: 
        sci_list2 = []
        length = len(sci_list)
        for i in range(length):
            if unit == sci_list[i].physics_unit:
                sci_list2.append(sci_list[i])
        sci_list = sci_list2
   
    #Filter for scientists whose expariments will be questions on the diploma
    if dip == True:
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

    #This method looks to see if the game file is in the same folder as this code
    file_state = os.path.isfile(file_path)

    #Prints bool for if game file is there or not
    #print(file_state) 

    #If no game file is pressent in the file then this will create a new one but it will be empty and probably break the game
    if file_state == False:
        print("The game file is missing!!!!, attempting to create a new one")
        with open(file_name,'x'):
            print("The file is created! It is a little empty don't you think?")
    else:
        print("Game file found.")


    with open(file_name, 'r') as data_file:
        csv_reader = csv.reader(data_file)
        questions_list = list(csv_reader)
        questions_list = questions_list[1]
    del questions_list[0]
    

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


    #makes the randint run until it picks a number that corisponds to an index of a question that has not been picked before 
    while True:
        count = 0 
        temp_decision = randint(0, general_questions_length)
        for number in blacklist:
            if temp_decision == number:
                count += 1 
        #If the count has not moved (if the index selected is new) break the loop
        if count < 1:
            break
        # if the count is alot it probably means there is no questions left
        elif count > 2000:
            print("There are no more questions in the list this will cause an error")
            raise LookupError

    
    #since a question has been picked, that question is now on black list ot prevent repition
    blacklist.append(temp_decision)
    #print("blacklisted question indces::: ", blacklist)


    temp_question = general_questions_list[temp_decision]

    
    print('\n')
    print(f"{temp_question} Is this true or false?")
    
    user_response = Bool_Input()


    #Code returns the index of the question it askes 
    return user_response, temp_decision, blacklist
    
   

#This code handles if a specific question was chosen to be asked       
def Specific_Question_Picker(sci_in_game):
    user_response = 0

    scientist_list_length = len(sci_in_game) - 1

    
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
            #print("QUESTION LIST LENGTH:::", question_list_length)
            break

        #this isnt the right error for this issue but it will let me know
        if error_count > 20000:
            print("There are no more questions in the list this will cause an error!")
            raise LookupError


    # Chooses an index to choose
    temp_question_decision = randint(0, question_list_length)

    #print("selected_sci.game_questions, ", selected_sci.game_questions)

    selected_question = selected_sci.game_questions[temp_question_decision]

    #print(selected_question, "yeahhhhhh")

    print('\n')
    print(f"{selected_question} Is this true or false?")

    #While loop so user has to enter 1 or 0
    user_response = Bool_Input()

    selected_sci.del_question(temp_question_decision)

    return user_response, selected_sci


#Handles assigning general score values for a general question
#If true assigns the score in the list if false the sign of the score is flipped
def General_Score_Assign(sci_in_game, question_index, user_answer):
    #print("Now assigning general score")
    
    #print(len(sci_in_game))
    #print(f"General_Score_Assign, question_index{question_index}")
    #print(f"General_Score_Assign, user answer bool{user_answer}")

    if user_answer == True:
        for people in sci_in_game:
            people.Score += int(people.response[question_index])
            
        
    elif user_answer == False:
        for scientist in sci_in_game:
            scientist.Score += -1*int(scientist.response[question_index])


 #Only the score of the spific scientist changes, just becuase the user answered false doesnt mean all other scientists are right
def Specific_Score_Assign(user_answer, selected_scientist, sci_in_game):

    #If the user answers true, then it is a good chance this is the scientist they are thinkinh of and not any others
    #So this scientist gets a large score but the others get a negitive score
    #print(f"The selected scientist is {selected_scientist.name}")

    if user_answer == True:
        for scientists in sci_in_game:
            scientists.Score += -20
            
        selected_scientist.Score += + 40
        

    elif user_answer == False:
        selected_scientist.Score += -20
    
    else:
        print("In specific score assign this was a bad input.")
    
    


#This will return 1 or 0 based on user input or computer logic
def Guesser(scientist_list):
    print('\n')

    sci_in_game = scientist_list

    #Uses cubing as a math way to measure how fast something diverages and it keeps the sign for me with no additional logic
    for scientist in sci_in_game:
        scientist.Temp_Score = scientist.Score**3

    ## Bubble sort algorithim to sort the list of scientist objects based on the temp score
    scientist_list_length = len(sci_in_game)
    for index in range(scientist_list_length):

        for person in range(0, scientist_list_length - index - 1):
            if sci_in_game[person].Temp_Score > sci_in_game[person+1].Temp_Score:
                sci_in_game[person], sci_in_game[person+1] = sci_in_game[person+1], sci_in_game[person]

    #for scientist in sci_in_game:
        #print(scientist.Temp_Score)
        
    highest_score = sci_in_game[-1].Temp_Score
    second_highest_score = sci_in_game[-2].Temp_Score

    #testing to see the difference in score between the first and the second highest score
    #if the second highest score is negitive then the first score is DEFFINITALLY the right guess but if the second highest score is positive it could be close
    if second_highest_score > 0 and (highest_score/second_highest_score < 2):
        print("I am not confedent of who you were thinking of, answer more questions")
        
        # User decision for no
        return False, sci_in_game
    
    print(f"So user, are you thinking of me, {sci_in_game[-1].name}?")

    user_decision = Bool_Input()

    # This removes the person the user said no to so the scientist can be narrowed down more
    if user_decision == False:
        print("Removed", sci_in_game[-1].name)
        sci_in_game.pop(-1)
        
    
    return user_decision, sci_in_game




 

    


game_file_name = "Questions_and_Answers.csv"

#ODWM 1
sci_1_questions = ["Did my experimental apparatus originally use water droplets, but in 1910 I changed the substance because the droplets evaporated too fast to make measurements?", "Was a key piece of work I built off of the charge to mass ratio of an electron that was discovered by Thomson?", "In 1916, did I also devise another experiment to measure another fundamental constant? Did I also use a previous constant I measured in my calculations?"] 
sci_6_questions =["Did my discovery explain why arc lighting lamps -- the common electrical lighting technology of my time -- varied in their brightness and were inefficient?", "Using my discoveries, did my subsequent patients go on to be used from military anti-aircraft searchlights to more efficient street lamps?", "Was I the first female member of the Institution of Electrical Engineers (Now the Institution of Engineering and Technology?"]
sci_3_questions = ["Did my work build off of the research by Joseph Priestley?", "Does my equation and subsequent law regarding electricity resemble one to do with gravity?"]
sci_2_questions = ["Was I the first to discover the process to convert mechanical energy to electrical energy in 1831?"]
sci_7_questions = ["Did my discovery definitely show electricity and magnetism are linked to each other?"]
sci_8_questions = ["Did my work build off of Rutherford's model of the atom?", "Did my model use data from the light emitted from hydrogen atoms to explain how elections orbited the nucleus?"]
sci_5_questions = ["Did I point out to Planck that his idea of the quantization of energy when it is transferred between matter could describe light as well?","In 1905, did I point out that high frequency light can act very similarly to particles? Was this expanded on by de Broglie?", "Did I build off Maxwell's work that described EMR to show how energy and mass are related to each other?", "In 1905, did I describe the photoelectric effect using Planck’s quantization hypothesis? Did I win a Nobel Prize for this in 1921? Did I come up with the idea that a photon must have a minimum energy needed to free an electron from a metal atom?", "Did Millikan’s experiment that used a “stopping voltage” prove my theory about the photoelectric effect? He published his work in 1916.", "Did I expand on the phenomena that Hertz noticed in 1887 and Lenard noticed in 1902?", "Does my equation explain why light has momentum? Does it help explain the  Compton effect and how radiation pressure and solar sails work?"]
#ODWM 2
sci_9_questions = ["Did my calculations say the speed of light was about 10 times the speed of sound, or 3430m/s?", "Did I formulate my experiment to measure the speed of light in 1638?", "Would a source of error in my experiment be how I am using my pulse to measure time?", "Would a source of error be how two people are needed in my experiment to measure the speed of light?"]
sci_10_questions = ["Was I intentionally trying to measure the speed of light? Did I notice that light had a speed from a trend in my data around 1676?", "Was the data I collected about an astronomical phenomena I was observing intended to be used so measurements of that phenomena could keep track of time?", "Did the data I collected show when Earth was closest to Jupiter, the eclipse of Io would happen 11 minutes earlier than predicted?"]
sci_11_questions = ["Did my calculations of the speed of light say it traveled at 210,824.1km/s?", "Did I do my calculations of the speed of light in 1678?", "Did I use Romer's data for my calculations of the speed of light?" ]
sci_12_questions = ["In my experiment, was the manipulated variable changing the speed of a rotating mirror?", "Did I work with Edward Williams Morley to measure the speed of light?", "When did I first perform my experiment to measure the speed of light? Was it in 1881?", "Did my experiment disprove the existence of the “either”, which was the hypothesized medium that light propagated in?", "Did I try measuring the speed of light again in 1930 and was my apparatus located in Pasadena, California?"]
sci_13_questions = ["While investigating color theory and Young's three color hypothesis, did I take the first color picture in 1861 using an apparatus I built?", "Were the mathematical equations I made that described how electric and magnetic fields interact with each other my most famous contribution to physics?", "Did my equations attempt to describe Faraday's observations and his law of induction?", "Did my mathematical equations of electromagnetic waves turnout to perfectly describe the physical properties of light? Did I publish these findings in 1865?"]
sci_14_questions = ["Between 1801 to 1805, did I perform an experiment that definitively showed light has properties of transverse waves?", "Did my experiment show that light creates interference fringes interference and diffracts through slits?", "At the time, did my experiment prove Huygen's idea that light acts like a wave to be true and disprove Newton's idea that light was a particle?", "Depending on how my experiment is observed, can it show the wave-particle duality of light and electrons?"]
sci_15_questions = ["Did I initially think matter can only exchange energy in discrete amounts?", "Did Einstein help me by pointing out that my idea of energy quantization could describe light as well?", "Did my work on energy quantization and solving the ultraviolet catastrophe win a Nobel Prize in 1918?", "Did I support a return to classical physics despite what my and Einstein's work showed? Did I abandon that position after the Compton Effect was discovered?", "In 1905, did Einstein independently work on the same problems I did too?", ""]
sci_16_questions = ["Did I work with Foucault to measure the speed of light?", "Did my apparatus go through two iterations before it accurately measured the speed of light?", "Did my apparatus initially use a rotating cogwheel then was modified with a rotating mirror?", "Was I the first scientist to build an accurate apparatus to measure the speed of light that was fully on Earth?", "In 1862, after two iterations of our apparatus did we eventually get 299,796km/s for the speed of light?"]
sci_17_questions = ["Did my work describe electron orbitals, why electrons only exist in certain places and relate it to waves? Did I publish this in 1924?", "Did I say if electrons act like standing waves while orbiting around the nucleus of the atom, no energy would be lost as EMR and the electron would be stable? Did I offer this explanation to solve an issue Bohr had with his model of the atom?", "When electrons were fired at gold foil in 1927, did it confirm my theory that they have wave properties?", "Did I propose the idea of particle-wave duality and extend that to electrons and other particles?"]
sci_18_questions = ["Does my equation describe why light spreads out as the slit it travels though gets smaller? Did this publish my work in 1927?", "Does my work have large implications for experiments that measure the position and velocity of small particles?", "Did my work lay the foundation for the development of the strong force?", "Did my work lead to using probability in quantum physics because I showed that having exact knowledge of all properties of a particle was impossible?"]
sci_19_questions = ["In 1885, did I discover a formula to predict the frequency of the visible light spectral lines of hydrogen? Could nobody explain this relationship theoretically until Bohr?", "Did Rydberg generalize my formula to predict the frequency of the visible light spectral lines of the hydrogen atom? Could the generalized formula predict all the spectral lines of hydrogen?", "Was my formula combined with Bohr’s model of the atom to describe how much energy it takes to move electrons between energy levels?"]

#ODWM 1
sci_1 = Scientist("Millikan", 1, 2, None, 1, 1, sci_1_questions)
sci_2 = Scientist("Faraday",2,2,None,0,1,sci_2_questions)
sci_3 = Scientist("Coulomb", 3,2, None, 1, 1, sci_3_questions)
sci_4 = Scientist("Henry",4,2,None,0,1,None)
sci_6 = Scientist("Ayrton",6,2,None,0,0,sci_6_questions)
sci_7 = Scientist("Oersted",7,2,None,0,1,sci_7_questions)
sci_8 = Scientist("Bohr", 8,1,None,0,1,sci_8_questions)

#ODWM 2
sci_5 = Scientist("Einstein",5,3,None,0,1,sci_5_questions)
sci_9 = Scientist("Galileo", 9, 3, None, 0, 1, sci_9_questions)
sci_10 = Scientist("Roemer", 10, 3, None, 1, 1, sci_10_questions)
sci_11 = Scientist("Huygens", 11, 3, None, 0, 1, sci_11_questions)
sci_12 = Scientist("Michelson", 12, 3, None, 1, 1, sci_12_questions)
sci_13 = Scientist("Maxwell", 13, 3, None, 0, 1, sci_13_questions)
sci_14 = Scientist("Young", 14, 3, None, 1, 1, sci_14_questions )
sci_15 = Scientist("Planck", 15, 3, None, 0, 1, sci_15_questions )
sci_16 = Scientist("Fizeau", 16, 3, None, 0, 1, sci_16_questions)
sci_17 =  Scientist("de Broglie", 17, 3, None, 0, 1, sci_17_questions)
sci_18 = Scientist("Heisenberg", 18, 3, None, 0, 1, sci_18_questions)
sci_19 = Scientist("Balmer", 19, 3, None, 0, 1, sci_19_questions)


#The list of all the scientist objects
scientist_list = [sci_1, sci_2, sci_3, sci_4, sci_5, sci_6, sci_7, sci_8, sci_9, sci_10, sci_11, sci_12, sci_13, sci_14, sci_15, sci_16, sci_17, sci_18, sci_19]

#List of the scientist objects that made it through the filter
selected_sci_list = []
questions_dump = []
blacklist = []
message = "THE OLD DEAD WHITE MEN GUESSER GAME"


#The game code:
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


""" for i in range(6):
    print(".")
    time.sleep(0.5) """


print("Welcome to the ODWM game! I, the computer will guess what physicist you are thinking of!")
print("This is the Old Dead White Men Guessing Game! I, the computer will take on the persona of the physicist you are thinking of!")
print("Input, “y”, “yes”, “true”, “yeah”, or “1” for yes, and input, “n”, “no”, false, “nah”, or “0” for false. Capitalizing the letters in your input does not matter; for example, “YES”, or “nO” would still be a valid input.", '\n')
print("Now you need to choose some settings!", '\n')

while len(selected_sci_list) <= 1:
    #runs the filter selection code so and lets user know about how big the game will be
    #if less than or equal to one scientist is in the game that wouldnt be that fun so the user will choose new filter parameters
    
    selected_sci_list = Scientist_Sort(scientist_list)

    print(f"The parameters you selected resulted in {len(selected_sci_list)} scientists present in the game.")
    
    #If there is only one scientist then that might cause issues and it wont be fun
    if len(selected_sci_list) <= 1:
        print(f"{len(selected_sci_list)} scientist(s) are in the game, pick new filters because that number of scientists isn't fun to play with!")


#Runs code so all the scientists in the game have a temp list of their special questions
#This is useful so the information isnt lost and the game can be reset within the code
for people in selected_sci_list:
    people.setting_in_game_questions()

print('\n')

#Name_Print(selected_sci_list)

questions_dump = Loading_Game_Data(game_file_name, selected_sci_list)

Loading_Question_Responses(game_file_name, selected_sci_list)

print('\n')
print("I AM LOADING THE GAME NOW.")
for i in range(7):
    print(".")
    time.sleep(0.5)

print('\n')


#print("HERE ARE THE SELECTED SCI::: ")
#for people in selected_sci_list:
    #print(people.name)


#This varible counting how many times the loop itterates will be used by the computer to determine when it should make a guess
game_loop_itterations = 0 
user_guess_decision = 0


#This is the loop of questions and answering it runs untill the computer guess right
while user_guess_decision == False:

    # 0 will be for general questions and 1 will be for spefic questions 
    temp_question_type = randint(0,1)
    if temp_question_type == 0:
        user_answer, chosen_question_index, blacklist = General_Question_Picker(questions_dump, blacklist)
        General_Score_Assign(selected_sci_list, chosen_question_index, user_answer)

    elif temp_question_type == 1:
        user_answer, chosen_scientist = Specific_Question_Picker(selected_sci_list)
        Specific_Score_Assign(user_answer, chosen_scientist, selected_sci_list)


    game_loop_itterations += 1

    if game_loop_itterations > 7:

        user_guess_decision, selected_sci_list = Guesser(selected_sci_list)
        game_loop_itterations = 0 

print('\n')
print("Yay I was right!!! The game is now over you should restart it!")
print("The ability to restart the game along with other features and more physicists will be coming soon!")
print('\n')
        
    


    










# Fix code so the response attrubute is innitallized in the start and not created during the code for organization 
# Maybe make the guesser code not a function
# Make the loop better at reseting the questions and score 
# If the user or the guesser returns a zero, then reset the score of the scientists to remove bias