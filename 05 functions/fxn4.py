# 4.with argument(parameter) and return type

def person(item1,item2,item3="milk"):
    print("i am making a dish from ",item1,",",item2,"and",item3)
    return item1+","+item2+" and "+item3+" dish"

def main():
    print("hello i am main person")
    item1,item2="ghee","carrot"
    dish=person(item1,item2) 
    print("i got ",dish," from person.")
    print("after calling person ")

main()
#h.w make a mini calculator using function which add,sub,mul,div 2 numbers.