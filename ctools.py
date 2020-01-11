#ctools.py
#ctools stand for compile tools

import subprocess
import filecmp

#compiles all of the file names given. executable is named after first file.
def compile(filename):
    #gcc command default
    compilable = True
    tokens = tokenize(filename)
    tokcount = len(tokens)
    argv = ["gcc","-o"]

    #makes sure that only .c and .o files are given to compile.
    for tok in tokens:
        toklen = len(tok)
        if(toklen>2):
            if(not(tok[toklen-2:toklen] == ".c" or tok[toklen-2:toklen] == ".o")):
                compilable = False
                break
        else:
            compilable = False
            break

    #only execute if file name is valid and last file ends in .c
    if(tokcount>0):
        if(compilable):
            print("Compiling",filename,"...")
            exename = tokens[0][0:len(tokens[0])-2]
            argv.append(exename)
            argv = argv + tokens
            exitresult = subprocess.run(argv, capture_output=True, text=True)
            #display the result, or error if execution failed
            if(exitresult.returncode == 0):
                print("Compilation successful.")
                print("Executable name:",exename)
            else:
                print("Compilation failed. Please check the compiling format.")
                print("--------------------------------------------------")
                print(exitresult.stderr, end='')
                print("--------------------------------------------------")
        else:
            print("Compilation failed. Incorrect compiling format.")
    else:
        print("Compilation failed. No files are given.")

#takes a string and return a list of each token separated by spaces
def tokenize(cmdstring):
    command = list()
    left = 0
    right = 0
    for char in cmdstring:
        right+=1
        if(char == ' '):
            command.append(cmdstring[left:right-1])
            left = right
    command.append(cmdstring[left:right])
    return command

#This function is not complete
def test(exe, filein="", fileout=""):
    UNIX = False
    #yes, I should create a function to check inputs.

    #I should not compare filein with fileout
    #cuz filein is the input file.
    
    if(" " in exe or ("." in exe and ".exe" not in exe)):
        print("Invalid executable name provided.")
    elif(" " in filein and ".txt" not in filein):
        print("Invalid input file name.")
    elif(" " in fileout and ".txt" not in fileout):
        print("Invalid output file name.")
    else:
        if(UNIX):
            exe = "./"+exe
        if(len(filein)>0):
            exe = exe + " < " + filein
        exitresult = subprocess.run(exe, capture_output=True, text=True, shell=True)
        if(exitresult.returncode==0):
            print("--------------------------------------------------")
            print(exitresult.stdout)
            print("--------------------------------------------------")
            if(len(fileout)>0):
                correct = filecmp.cmp(filein, fileout)
                if(not correct):
                    print("Results are not correct.")
        else:
            print("Failed to run program. See below for error message:")
            print("--------------------------------------------------")
            print(exitresult.stderr, end='')
            print("--------------------------------------------------")

        
        
    

def make():
    #preset are the c or o files that you want to compile
    preset_files = "hello.c"
    compile(preset_files)

def main():
    #main program will call make on execute... can comment out
    make();

main()
