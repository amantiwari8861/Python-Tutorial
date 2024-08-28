# import threading

# def print_numbers():
#     for i in range(5):
#         print(i)

# # Create a thread
# thread = threading.Thread(target=print_numbers)

# # Start the thread
# thread.start()

# # Wait for the thread to complete
# thread.join()
# print("Thread finished.")


# import threading

# def print_numbers(prefix):
#     for i in range(5):
#         print(f"{prefix} {i}")

# # Create a thread with arguments
# thread = threading.Thread(target=print_numbers, args=("Thread 1",))

# # Start the thread
# thread.start()

# # Wait for the thread to complete
# thread.join()


# import threading

# lock = threading.Lock()

# def thread_safe_function():
#     with lock:
#         # Critical section of code
#         print("This section is thread-safe.")

# thread = threading.Thread(target=thread_safe_function)
# thread.start()
# thread.join()



import threading
import requests

def download_url(url):
    response = requests.get(url)
    print(f"Downloaded {url} with status code {response.status_code}")

urls = [
    "https://www.example.com",
    "https://www.python.org",
    "https://www.github.com"
]

threads = []

for url in urls:
    thread = threading.Thread(target=download_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All downloads finished.")
