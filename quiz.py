#This program is a fill in the blank quiz which requests input for each fill in the blank and will either inform you if you are correct or will prompt you to try again if you are wrong

#Below are the quiz questions

easy = "The easy quiz is about our planet: The planet we live on is called __1__. There are __2__ continents on this planet. The intelligent species on this planet are called __3__. The closest star to this planet is called the __4__."

medium = "The medium quiz is about sports. The __1__ won the 2017 NBA Finals. The __2__ won the 2018 Super Bowl. The __3__ won the 2017 Stanley Cup. The __4__ won the 2017 World Series."

hard = "The hard quiz is about US Constitutional Law. When a person is subject to a custodial interrogation, the police must first read them their __1__ rights. The Fourth Amendment only applies if a person has a reasonable expectation of __2__. The Constitution only protects individuals against bad __3__ actions, not bad private individual actions. The __4__ Amendment contains the Due Process Clause."


#Below are the quiz answers
easy_answer = ["Earth", "7", "humans", "Sun"]

medium_answer = ["Warriors", "Eagles", "Penguins", "Astros"]

hard_answer = ["Miranda", "privacy", "government", "5th"]

blank = ["__1__", "__2__", "__3__", "__4__"]
#This function takes input and confirms what level quiz you are going to do.-
def difficulty():
    level = raw_input("Please select a difficulty level... Press 1 for easy mode; Press 2 for medium mode, or press 3 for hard mode; then press Enter:  ")
    if level == "1":
      print "Ok, lets do the easy quiz."
      print easy
      return easy
    if level == "2":
      print "Ok, lets do the medium quiz."
      print medium
      return medium
    if level == "3":
      print "Ok, lets do the hard quiz."
      print hard
      return hard
    while level != "1" or level != "2" or level != "3":
        print "Sorry, that is not a valid option. Please try again."
        return difficulty()

#This function determines whether an input for the quiz is correct or not. It will ask for a new input if it is incorrect#
def correct_answer_check(guess_input, difficulty):
    level_difficulty = []
    guess_word = guess_input
    if difficulty == easy:
        level_difficulty = easy_answer
    elif difficulty == medium:
        level_difficulty = medium_answer
    else:
        level_difficulty = hard_answer
    for answer in level_difficulty:
        while guess_word != answer:
            guess_word = raw_input("Sorry, that is incorrect, please try another answer: ")
            return correct_answer_check(guess_word, difficulty)
        else:
            guess_difficulty_location = 0
            return level_difficulty.pop(guess_difficulty_location)
            guess_difficulty_location += 1




#This function is to find each blank to replace
def blank_finder(quiz_word, blank):
    for found_blank in blank:
        if found_blank in quiz_word:
            return found_blank
    return None

#This function searches each difficulty for the blank to replace it with input by the user
def quiz_input(level_input):
    correct_answer_one = []
    list_difficulty = level_input
    quiz = list_difficulty.split()
    x = 0
    for word in quiz:
        quiz_question = blank_finder(word, blank)
        if quiz_question != None:
          quiz_input = correct_answer_check(raw_input("Please submit an answer for " + quiz_question + " : "), level_input)
          word = word.replace(quiz_question, quiz_input)
          correct_answer_one.append(word)
          x += 1
          print " ".join(correct_answer_one) + " " +  " ".join(quiz[x : ])
        else:
          correct_answer_one.append(word)
          x += 1
    return "Congrats! You have finished the quiz."


print quiz_input(difficulty())
