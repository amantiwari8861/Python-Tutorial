# url="https://ninjasfiles.s3.amazonaws.com/0000000000000215.pdf?utm_source=sendgrid&utm_medium=email&utm_campaign=website"

# url="https://ninjasfiles.s3.amazonaws.com/"+0000000000000215+".pdf?utm_source=sendgrid&utm_medium=email&utm_campaign=website"


i=0
while i<5000:
    file1 = open("link.txt", "a")
    file1.write("https://ninjasfiles.s3.amazonaws.com/0000000000000"+str(i)+".pdf?utm_source=sendgrid&utm_medium=email&utm_campaign=website\n")
    file1.close()
    i+=1
