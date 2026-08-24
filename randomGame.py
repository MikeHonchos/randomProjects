#I created this program to randomly select games because sometimes I don't know what to play.
#This can also be used to randomly select any file type, not just games. Just change the folder path to whatever you want.

#For this to work you need to put all games inside of a folder
#Currently this program only works on windows

import os
import random

#Insert your folder path that contains the games
#Turn every forward slash(\) into a backslash (/)
folder = ""

#Finding all files in the folder
files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]



def main():
    #Main code
    print("Selecting game...")
    random_file = random.choice(files)

    #Creating path
    file_path = os.path.join(folder, random_file)
    print(f"Game chosen: {random_file}")
    yesNo = input("Do you want to play this game? (y/n): ")
    if yesNo.lower() == "y":
        os.startfile(file_path)
    else:
        #Rerun the program if the user doesn't want to play the game
        main()



if __name__ == "__main__":
    main()