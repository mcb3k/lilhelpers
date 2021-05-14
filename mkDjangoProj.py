#!/usr/bin/python3

import sys, getopt, os, subprocess

def mkDjangoProject(argv):
    #known issue - This script does *not* care about the number of arguments.  I should fix that.
    helpMsg = "mkDjangoProj.py takes a project name and makes a project directory, a venv, installs django, and makes a django project for you.  \n USAGE: \n mkDjangoProj.py -p <project name> \n mkDjangoProj.py --project <project name> "

    project = ''

    try:
        opts, args = getopt.getopt(argv, "hp:",["help","project"])
    except getopt.GetoptError:
        print(helpMsg)
    for opt, arg in opts:
        if opt in ("-h","--help"):
            print(helpMsg)
        elif opt in ("-p","--project"):
            project = arg
        else:
            print("Oops! Doublecheck your options!")
            print(helpMsg)
            sys.exit(2)

    if project != '' and ' ' not in project:
        myPath = os.path.join(os.getcwd(),project + "-project")
        print("Creating " + myPath)
        try:
            os.mkdir(myPath, mode=0o755)
        except OSError as error:
            print(error)
            print("exiting...")
            exit(3)
        print("Successfully made " +myPath)
    else:
        print(helpMsg)
        print("exiting...")
        sys.exit(4)
    try:
        os.chdir(myPath)
    except OSError as error:
        print(error)
        print("exiting...")
        exit(5)

    if project != '' and ' ' not in project:
        print("Setting up virtual environment " + project + "-venv")
        subprocess.run(["python3", "-m", "venv", project + "-venv"])
        print("Successfully set up virtual environment")
        #using os.system because source doesn't work with subprocess
        print("Setting up Django in the virtual environment")
        os.system ("source " + project + "-venv/bin/activate; pip install django; django-admin startproject "+ project)

        print("\nAll Done!  Work on your project by: \n 1) cd " + project + "-project \n 2) source " + project + "-venv/bin/activate")
    

if __name__ == "__main__":
    mkDjangoProject(sys.argv[1:])
