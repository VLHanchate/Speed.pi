import time

import random

print("Waking up now! Booting. Progress: 0%")
time.sleep(1)
print(random.randint(1, 10))
time.sleep(1)
print(random.randint(11, 20))
time.sleep(1)
print(random.randint(21, 30))
time.sleep(1)
print(random.randint(31, 40))
time.sleep(1)
print(random.randint(41, 50))
time.sleep(1)
print(random.randint(51, 60))
time.sleep(1)
print(random.randint(61, 70))
time.sleep(1)
print(random.randint(71, 80))
time.sleep(1)
print(random.randint(81, 90))
time.sleep(1)
print(random.randint(91, 99))
time.sleep(1)
print("Progress: 100 %. Finished Booting Up!")
time.sleep(1)
print("Okay, now that was just for fun. LOL! Sorry to waste you around 10 seconds.")
time.sleep(1)
print("Hello everyone!")
time.sleep(1)
print("Bot name: Speed.pi")
time.sleep(1)
print("What does this bot do? This bot lets you count regularly, and you can guess a number.")
time.sleep(1)
print("Made by VLHanchate. Contact = VLHanchate#9585 through discord OR laksh.hanchate22@gmail.com through gmail.")
time.sleep(1)
print("Venkatasai Laksh Hanchate = VLHanchate")
time.sleep(1)
print("Discord: https://discord.gg/uP87tKwQXW")
time.sleep(1)
print("Channel: https://www.youtube.com/channel/UCyL1tSCypJ6rqAe_HLS8kTQ")
time.sleep(1)
print("Subscription: https://www.youtube.com/channel/UCyL1tSCypJ6rqAe_HLS8kTQ?sub_confirmation=1")
time.sleep(1)
print("Alternative Nitrotype Account: https://www.nitrotype.com/racer/vlhanchate_pi_3_1415")
time.sleep(1)
print("Github: https://github.com/VLHanchate")
time.sleep(1)
print("Main Nitrotype Account: https://www.nitrotype.com/racer/vlhanchate_3_141592")
time.sleep(1)
print("Spotify: https://open.spotify.com/user/3emjf48fnm7hjjjbmhrwt38fx")
time.sleep(1)
print("Nitrotype Team: https://www.nitrotype.com/team/VLHYT")
time.sleep(1)
print("Version: 1.0.0")
time.sleep(1)
print("Bot Release Date: 03/11/2021. ")
time.sleep(1)
print("You might think that this bot is slow but I made it like that so that it can be easier for you to see the messages.")
time.sleep(1)
print("If you find any errors, or suggestions, please contact me: VLHanchate#9585 through discord OR laksh.hanchate22@gmail.com through gmail")
time.sleep(1)
print("Copyright © - 2021. All Rights Reserved. No copying anything in this program. No copying name, etc.")
time.sleep(1)
help=str(input("How does this bot work? Type ';help' The prefix is ';' Please type ';help' right now as the program is waiting for your response."))
time.sleep(1)
while True:
    if help == ";help":
        print("The prefix is ';'. All functions are ';help', ';gtn', ';count', ';end'.")
        time.sleep(1)
        print("';gtn' is for guessing a number. Speed.pi chooses a number and you have to guess it. You can input the amount of guesses you want. Number is between -100 and 100. It gives you hints along the way.")
        time.sleep(1)
        print("';count' is for counting starting from 1. You just go on and if you get a number incorrect, you have to restart.")
        time.sleep(1)
        print("';end' closes the whole program and you have to rerun it.")
        time.sleep(1)
        print("PLEASE NOTE this DOWN: Speed.pi will not allow you to do any function in the middle of any mini game. If you want to do something else, you have to re reun the program. Sorry about that.")
        time.sleep(1)
        choose=str(input("What do you want to do? Guess a number or Count? The prefix is ';'. All functions are ';help', ';gtn', ';count', ';end'."))
        if choose == ';help':
            time.sleep(1)
            print("Please read above messages.")
            time.sleep(1)
        elif choose == ';gtn':
            time.sleep(1)
            print("Welcome to guessing a number. Basic rules are guess a number in your chosen amount of tries between -100 and 100.")
            time.sleep(1)
            guessesTakenInt = 0
            time.sleep(1)
            myNameStr = input("Hello! What is your name?")
            time.sleep(1)
            maxGuessesStr = input("How many guesses will you get?")

            numberToGuessInt = random.randint(-100, 100)
            maxGuessesInt = int(maxGuessesStr)
            time.sleep(1)
            print("Well, " + myNameStr + ", I am thinking of a number between -100 and 100. You have " + maxGuessesStr + " guesses to get it right!")

            while guessesTakenInt < maxGuessesInt:
                time.sleep(1)
                print("Take a guess.")
                guessStr = input()
                guessInt = int(guessStr)

                guessesTakenInt = guessesTakenInt + 1

                if guessInt < numberToGuessInt:
                    time.sleep(1)
                    print("Your guess is to low. Guess a higher number")
                elif guessInt > numberToGuessInt:
                    time.sleep(1)
                    print("Your guess is to high. Guess a lower number")
                elif guessInt == numberToGuessInt:
                    time.sleep(1)
                    guessesTaken = str(guessesTakenInt)
                    print('Great job, ' + myNameStr + '! You guessed my random  number from 1 to 100 in ' + guessesTaken + ' guesses!')
                    break
                else:
                    time.sleep(1)
                    print("Something is wrong! Please try again!")
                    break

            if guessInt != numberToGuessInt:
                numberToGuessStr = str(numberToGuessInt)
                time.sleep(1)
                print('Nope. The number I was thinking of was ' + numberToGuessStr)
        elif choose == ';count':
            time.sleep(1)
            print("Welcome to counting. Basic rules are you have to count to as far as you can go, no time limit, and if you mess up, you have to restart. You start from the number 1.")
            count = 0
            while int(count) >= 0:
                count = count + 1
                time.sleep(1)
                counting = str(input("Please start counting: Type 'break' if you want to quit."))
                if counting == 'break':
                    time.sleep(1)
                    print("Thanks for playing! :) Hope you liked this bot.")
                    break
                if count != counting:
                    time.sleep(1)
                    print("You messed up. Please redo it again.")
                    count = 0
                    counting = 0


        elif choose == ';end':
            time.sleep(1)
            print("Thanks for playing! :) Hope you liked this bot.")
            break
        else:
            time.sleep(1)
            print("We do not understand what you put. Please restart the whole process")
            break

    else:
        time.sleep(1)
        print("Please re run the program and type ';help' next time to check out the commands. The prefix is ';'.")
        break
