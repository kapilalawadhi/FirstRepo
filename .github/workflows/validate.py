import sys
import re

def main():
    print("Hello from action")
    print('Argument List:', str(sys.argv))
    if len(sys.argv) >0:
        changed_files = sys.argv[1]
        print('changed files are->',changed_files)
        errors=''
        for changed_file in sys.argv:
            print('Traverse changed files are->', changed_files)
            if changed_file.__contains__("/workflows/"):
                continue
            else:
                print('effective changed_file name->', changed_file)
                for file_name in changed_file.split(","):
                    print("filename->",file_name)
                    with open(file_name) as f:
                        # print("full_line_before",full_line)
                        full_line = f.read().replace("\"","\'")
                        # full_line = f.readlines().replace("\"","\'")
                        print("full_line_after",full_line)
                        check_secret_key = re.findall("([a-zA-Z0-9+/]{40})", full_line)
                        if len(check_secret_key) > 0:
                            errors =  errors + "/n" + "secret_key found in file " + file_name
                        # if full_line.__contains__("="):
                        #     while len(full_line.split("="))>0:
                        #         var_value = full_line.split("=")[1]
                        #         # Validate for secret key using regular exp
                        #         if var_value.__contains__("="):
                        #             full_line=var_value



    if len(errors)>0:
        raise Exception("Sorry, issue with the current code snip->/n",errors)

if __name__== '__main__':
    main()
