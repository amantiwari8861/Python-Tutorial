# Collection:-
# List Tuple Set Dictionary

# s=["apple","banana"]
# print(s)
# print(type(s))






# s=["apple","banana","cherry"]
# print(s,type(s))
# s=("apple","banana","cherry")
# print(s,type(s))
# s={"apple","banana","cherry"}
# print(s,type(s))
# s={"a":"apple","b":"banana","c":"cherry"}
# print(s,type(s))









# s=["apple","banana","cherry","apple"]
# print(s,type(s))
# s=("apple","banana","cherry","apple")
# print(s,type(s))
# s={"apple","banana","cherry","apple"}
# print(s,type(s))
# s={"a":"apple","b":"banana","c":"cherry","a":"apple"}
# print(s,type(s))












# s=["apple","banana","cherry","apple"]
# s[3]="mango"
# print(s,type(s))
# s=("apple","banana","cherry","apple")
# sl=list(s)
# print(sl,type(sl),"sl srring list")
# sl[3]="mango list"
# s=tuple(sl)
# print(s,type(s))
# s={"apple","banana","cherry","apple"}
# sl=list(s)
# print(sl,type(sl),"sl srring list")
# sl[0]="mango"
# s=set(sl)
# print(s,type(s))
# s={"a":"apple","b":"banana","c":"cherry","a":"apple"}
# s["a"]="mango"
# print(s,type(s))












# s=["apple","banana","cherry","apple"]
# s[3]="mango"
# print(s,type(s))
# s.append("date")
# print(s,type(s))

# s=("apple","banana","cherry","apple")
# sl=list(s)
# print(sl,type(sl),"sl srring list")
# sl[3]="mango list"
# sl.append("date")
# s=tuple(sl)
# print(s,type(s))

# s={"apple","banana","cherry","apple"}
# sl=list(s)
# print(sl,type(sl),"sl srring list")
# sl[0]="mango"
# sl.append("date")
# s=set(sl)
# print(s,type(s))

# s={"a":"apple","b":"banana","c":"cherry","a":"apple"}
# s["a"]="mango"
# s["d"]="date"
# print(s,type(s))















s=["apple","banana","cherry","apple"]
s[3]="mango"
print(s,type(s))
s.append("date")
s.remove("apple")
print(s,type(s))

s=("apple","banana","cherry","apple")
sl=list(s)
print(sl,type(sl),"sl srring list")
sl[3]="mango list"
sl.append("date")
sl.remove("apple")
s=tuple(sl)
print(s,type(s))

s={"apple","banana","cherry","apple"}
sl=list(s)
print(sl,type(sl),"sl srring list")
sl[0]="mango"
sl.append("date")
sl.remove("cherry")
s=set(sl)
print(s,type(s))

s={"a":"apple","b":"banana","c":"cherry","a":"apple"}
s["a"]="mango"
s["d"]="date"
s.pop("a")
print(s,type(s))
