import sys

def main():
    print("Hello from action")
    print('Argument List:', str(sys.argv))
    if len(sys.argv) >0:
        changed_files = sys.argv[1]
        print('changed files are->',changed_files)
        for changed_file in sys.argv:
            if changed_file.__contains__("/workflows/"):
                continue
            else:
                for file_name in changed_file.split(","):
                    print("filename->",file_name)
                    with open(file_name) as f:
                        lines = f.readlines()
                        print(lines)

    # raise Exception("Sorry, issue with the current code snip")

if __name__== '__main__':
    main()
