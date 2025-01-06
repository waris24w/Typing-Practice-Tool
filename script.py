import random

words = ['random', 'counter','Fellan',' Heroism','Washington]

Corrected = 0
Wrong = 0
running = False
while not running:
    random_words = random.choice(words)
    print('**********************')
    print(random_words)
    print('***********************')
    user_input = input("Enter you word: (q to quit) ")
    
    if user_input == random_words:
        print('\tCorrect')
        Corrected += 1
    else:
        print('\tWrong')
        Wrong += 1
        
    if user_input == "q":
        running = True
        print('----------RESULT------------')
        print(f'\nCorrected Words: {Corrected} Wrong Words: {Wrong}')
        print('\n----------RESULT------------')
    else:
        continue
