""" Write a Python function that takes a string as parameter and returns a string with
every successive repetitive character replaced by & e.g. Parameter may become Par&met&r. """

# def replaceDupli(data):
#     # print(data)
#     data2=list(data)
#     strData=""
#     for e in data2:
#         # print(e)
#         count=0
#         for i in range(len(data2)):
#             if(data2[i]==e):
#                 count+=1
#             if count>1 and data2[i]==e:
#                 data2[i]='&'
#     return strData.join(data2)

def replaceDupli(data):
    # print(data)
    data2=list(data)
    strData=""
    for i in range(len(data2)):
        if i+2<len(data2):
            if data2[i+2]==data2[i] :
                data2[i+2]='&'
        
    return strData.join(data2)


data="Parameter"
newData=replaceDupli(data)
print("the new data is:",newData)