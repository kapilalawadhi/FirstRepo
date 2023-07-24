import sys
import re
import os

def main():
    print("Validating stated")
    path = os.getcwd()
    # prints parent directory
    all_files = []
    for root, dirs, files in os.walk(os.path.abspath(os.path.join(path, os.pardir))):
        path = root.split(os.sep)
        print((len(path) - 1) * '---', os.path.basename(root))
        for file in files:
            if file.endswith(".py"):
                print(os.path.abspath(file))
                if os.path.abspath(file).__contains__("/workflows/"):
                    print("EXCLUDED->",os.path.abspath(file))
                    continue
                else:
                    print("inCLUDED->", os.path.abspath(file))
                all_files.append(file)


    errors=''
    for file_name in all_files:
        print("Traversing filename->",file_name)
        with open(file_name) as f:
            file_data = f.read().replace("\"","\'")
            print("File_Data->\n",file_data)
            check_secret_key = re.findall("([a-zA-Z0-9+/]{40})", file_data)
            if len(check_secret_key) > 0:
                errors =  errors + " " + "secret_key found in file " + file_name
    print("Validating completed")
    if len(errors)>0:
        raise Exception("Sorry, issue with the current code snip->",errors)

if __name__== '__main__':
    main()
