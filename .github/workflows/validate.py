import sys

def main():
    print("Hello from action")
    print('Argument List:', str(sys.argv))
    if len(sys.argv) >0:
        changed_files = sys.argv[1]
        print('changed files are->',changed_files)
        for item in sys.argv[1].split(","):
            print("filename->")
            with open(item) as f:
                lines = f.readlines()
                print(lines)

    # raise Exception("Sorry, issue with the current code snip")

if __name__== '__main__':
    main()
