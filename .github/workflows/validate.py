import sys

def main():
    print("Hello from action")
    print('Argument List:', str(sys.argv))
    print('Argument List[1]:', str(sys.argv[1]))
    with open(str(sys.argv[1])) as f:
        lines = f.readlines()
        print(lines)

    # raise Exception("Sorry, issue with the current code snip")

if __name__== '__main__':
    main()
