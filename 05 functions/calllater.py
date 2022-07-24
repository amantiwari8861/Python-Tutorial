def main():
    print("I'm in main")
    #calling a although it is in the bottom
    a()

def b():
   print("I'm in b")

def a():
   print("I'm in a")
   b()

main()