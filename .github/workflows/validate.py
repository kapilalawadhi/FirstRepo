import sys

def main():
    print("Hello from action")
    print('Argument List:', str(sys.argv))
    files = sys.argv[0]
    for item in files.split('$'):
        print("filename->"& item)
        with open(item) as f:
            lines = f.readlines()
            print(lines)

    # raise Exception("Sorry, issue with the current code snip")

if __name__== '__main__':
    main()
