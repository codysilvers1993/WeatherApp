import requests

def main():
    # Code for main functionality of the program goes here
    print("Hello, word!")
    loc = str(input("Enter Location:"))
    print(loc)
    x = requests.get('http://www.yahoo.com')
    print(x.text)

if __name__ == '__main__':
    main()
