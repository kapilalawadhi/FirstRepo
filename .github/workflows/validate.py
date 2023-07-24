import sys
import re

def main():
    print("Validating stated")
    print('Argument List:', str(sys.argv))
    if len(sys.argv) >0:
        changed_files = sys.argv[1]
        errors=''
        for changed_file in sys.argv:
            if changed_file.__contains__("/workflows/"):
                continue
            else:
                print('Effective Changed Files->', changed_file)
                for file_name in changed_file.split(","):
                    print("Traversing filename->",file_name)
                    with open(file_name) as f:
                        file_data = f.read().replace("\"","\'")
                        print("File_Data->\n",file_data)
                        check_secret_key = re.findall("([a-zA-Z0-9+/]{40})", file_data)
                        if len(check_secret_key) > 0:
                            errors =  errors + "\n" + "secret_key found in file " + file_name
    print("Validating completed")
    if len(errors)>0:
        raise Exception("Sorry, issue with the current code snip->\n",errors)

if __name__== '__main__':
    main()
