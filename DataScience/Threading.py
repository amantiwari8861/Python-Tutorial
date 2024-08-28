import subprocess
import threading
import time 

# Example: Open Notepad
# subprocess.run(["notepad.exe"])
subprocess.run(["explorer.exe"])

# Example: Open a specific file with its default application
# subprocess.run(["C:\\Program Files\\Google\\Chrome Dev\\Application\\chrome.exe"])
# subprocess.run(["C:\\Windows\\System32\\calc.exe"])



def eat():
    # time.sleep(2)
    print("eating break fast by ",threading.enumerate())
    # subprocess.Popen(("open","C:\\Windows\\System32\\calc.exe"))

def watchMovie():
    # time.sleep(2)
    print("watching Movieby ",threading.enumerate())

def talking():
    # time.sleep(2)
    print("talking with familyby ",threading.enumerate())

# sequential execution 
# eat()
# watchMovie()
# talking()

# print(threading.active_count())
# print(threading.enumerate())

t1=threading.Thread(target=eat)
t1.start()
t2=threading.Thread(target=watchMovie)
t2.start()
t3=threading.Thread(target=talking)
t3.start()

t1.join()
t2.join()
t3.join()

print(threading.active_count(),threading.enumerate())
print(time.perf_counter())