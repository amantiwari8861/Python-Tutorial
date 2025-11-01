# process vs thread
# GTA6 download -> setup.exe 

# process : when a program is in execution it is called process 
# threads : smallest unit of task is called thread

# sequential

# from time import sleep
# def eat():
#     print("eating started...")
#     sleep(5)
#     print("eating ended...")
    
# def talk():
#     print("talking...")

# def watchTv():
#     print("watching...")
    
# talk()
# eat()
# watchTv()


# thread ?

from time import sleep
import threading

def eat():
    print("eating started...")
    sleep(5)
    print("eating ended...")
    
def talk():
    print("talking...")

def watchTv():
    print("watching...")

# Create threads for each task
t1 = threading.Thread(target=eat)
t2 = threading.Thread(target=talk)
t3 = threading.Thread(target=watchTv)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all to complete
t1.join()
t2.join()
t3.join()

print("All tasks finished ✅")