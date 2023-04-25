# 2.with argument(parameter) no return type

def person(item1,item3,item4="sugar"):
    # print("i will make dish from ",item1," and ",item3)
    print("i will make a dish with ",item1,item4,"and",item3," then i will eat that")


def main():
    print("hello i am main person")
    item1,item2="ghee","carrot"
    person(item1,item2)
    print("after calling person ")

main()