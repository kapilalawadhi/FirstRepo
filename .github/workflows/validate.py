import sys

def main():
    print("Hello from action")
    print('Argument List:', str(sys.argv))
    for item in sys.argv:
        print("filename->")
        with open(item) as f:
            lines = f.readlines()
            print(lines)

    # raise Exception("Sorry, issue with the current code snip")

if __name__== '__main__':
    main()
