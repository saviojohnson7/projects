
letter=['a','v','i','s','o','j','n','o','h','n','s'],['e','m','i','o','c','x','r']
words = ["savio","avi","johnson"],["emi","micro","mixer"]

lives = 3
# level= 0
score = 0

name=input("enter your name: ")
print("welcome to the game",name)
print()
print("lets begin the wordscape game!!")

level=0
lvl = level + 1
print("level: ", lvl)
print("create three words")
print(letter[level])

enter_words=3
for i in range(enter_words): # 0,1,2
    s=input("words: ")
    if s in words[level]:
        print("correct")
        lives=3
        score += 10
        print("Your score is: ",score)
        print("===============================")


    elif lives == 0:
        print("Better luck next time :) Thank you playing.")


    else:
        print("incorrect")
        lives -= 1
        print(f"lives left {lives}")
        print("===============================")
        if lives == 2:
            s = input("words: ")
            if s in words[level]:
                print("correct")
                score += 10
                print("Your score is: ", score)
                print("===============================")
            else:
                print("incorrect")
                lives -= 1
                print(f"lives left {lives}")
                print("===============================")

        if lives == 1:
            s = input("words: ")
            if s in words[level]:
                print("correct")
                score += 10
                print("Your score is: ", score)
                print("===============================")

                s = input("words: ")
                if s in words[level]:
                    print("correct")
                    score += 10
                    print("Your score is: ", score)
                    print("===============================")

            else:
                print("incorrect")
                lives -= 1
                print(f"lives left {lives}")
                print("===============================")

            break


        if lives == 0:
            print("Better luck next time :) Thank you for playing.")
            break

    if score==30:
            print("Do you want to play the next level? (yes or no)")
            response = input("Enter: ")
            if response == "yes" or response == "Yes":
                level += 2
                print("level: ", level)
                print("create three words")
                print(letter[1])
                enter_words = 3
                for i in range(enter_words):  # 0,1,2
                    s = input("words: ")
                    if s in words[1]:
                        # words[level]
                        print("correct")
                        score += 10
                        print("Your score is: ", score)
                    else:
                        print("incorrect")
                        break
                print()
                print("Thank you for playing!!!")





