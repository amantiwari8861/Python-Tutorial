# 3.no argument(parameter) with return type

def person():
    item1,item2,item3="ghee","carrot","sugar"
    print("i am making a dish from ",item1,",",item3,"and",item2)
    # return item1+","+item2+" and "+item3+" dish"
    return "gaajar ka halwa"

def main():
    print("hello i am main person")
    dish=person() 
#if i am hiring someone then it will give service to them who called him.
    # print("i got ",dish," from person.")
    print(dish)
    print("after calling person ")

main()