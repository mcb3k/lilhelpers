#!/usr/bin/python3

import sys, getopt, os, subprocess

def main(argv):
    helpMsg = "mkDjangoProj.py takes a project name and makes a venv. installs django, and makes a project for you.  \n mkDjangoProj.py -p <project name> \n mkDjangoProj.py --project <project name> "

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
        subprocess.run(["python3", "-m", "venv", project + "-venv"])

#   eep!  source isn't a "command", it's built into bash! D'oh!
#    subprocess.run(["source", "venv/bin/activate"])
#    subprocess.run(["pip", "install", "django"])
#   welp! if we don't use os.system to run the django-admin, it fails!
#   This is because the venv we activated earlier gets yeeted into the void
#    subprocess.run(["django-admin", "startproject", project])
        os.system ("source " + project + "-venv/bin/activate; pip install django; django-admin startproject "+ project)

        print("All Done!  Work on your project by: \n 1) cd " + project + "-project \n 2) source " + project + "-venv/bin/activate")
    
if __name__ == "__main__":
    main(sys.argv[1:])
