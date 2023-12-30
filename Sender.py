import socket
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def connection():
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('192.168.75.135', 25000)  
    sock2.connect(server_address)
    return sock2

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        change_message = f"File {event.src_path} {event.event_type}"
        sock2.send(change_message.encode('utf-8'))


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path='.', recursive=True)
observer.start()


sock2 = connection()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()
sock2.close()
