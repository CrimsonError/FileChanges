import os
import time
import shutil

option = input("What do you want to do?\nRead a file?\nWrite a file?\nDelete a file?\nCopy a file?\nMove a file? ")

print("Please make sure that the directory that you put is correct.")
print("Make sure the file directory has double back slashes instead of single back slashes.")

if option == "Read a file".lower():
    dir = input("Please enter the file directory: ")

    try:
        with open(dir) as file:
            print(file.read())
            time.sleep(3)
            quit()
    except FileNotFoundError:
        print("Try inputting the file directory again!")
        time.sleep(3)
        quit()

if option == "Write a file".lower():
    text = input("Please enter the text: ")
    dir = input("Please enter the directory: ")

    try:
        with open(dir, 'w') as file:
            file.write(text)
            print(text)
            time.sleep(3)
            quit()
    except FileNotFoundError:
        print("Try putting the file directory in correctly!")
        time.sleep(3)
        quit()

if option == "Delete a file".lower():
    dir = input("Please enter the directory: ")

    try:
        os.remove(dir)
        print("File successfully deleted!")
        time.sleep(3)
        quit()
    except FileNotFoundError:
        print("Please input the file in correctly.")
        time.sleep(3)
        quit()

if option == "Copy a file".lower():
    dir = input("Please enter the directory: ")

    try:
        shutil.copyfile(dir, 'copy.txt')
        print("File copied!")
        time.sleep(3)
        quit()
    except FileNotFoundError:
        print("File was not found.")
        time.sleep(3)
        quit(3)

if option == "Move a file".lower():
    dir = input("Please enter the directory: ")
    dest = input("Please enter the destination: ")

    try:
        if os.path.exists(dest):
            print("The file is already there!")
        else:
            os.replace(dir, dest)
            print(dir + " was moved")
    except FileNotFoundError:
        print(dir + " was not found")