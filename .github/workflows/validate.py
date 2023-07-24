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
            if changed_file.__contains__("/workflows/"):
                continue
            else:
                for file_name in changed_file.split(","):
                    print("filename->",file_name)
                    with open(file_name) as f:
                        full_line = f.readlines()
                        txt = "The rain in Spain"
                        check_secret_key = re.findall("([a-zA-Z0-9+/]{40})", full_line)
                        if len(check_secret_key) > 0:
                            print("keyfound->",check_secret_key)
                            errors =  errors + "/n" + "secret_key found in file " + file_name
                        # if full_line.__contains__("="):
                        #     while len(full_line.split("="))>0:
                        #         var_value = full_line.split("=")[1]
                        #         # Validate for secret key using regular exp
                        #         if var_value.__contains__("="):
                        #             full_line=var_value



                        print(lines)
    if len(errors)>0:
        raise Exception("Sorry, issue with the current code snip->/n",errors)

if __name__== '__main__':
    main()
