import time
import os 
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:\\Users\\Nisha\\Downloads"
to_dir = "C:\\Users\\Nisha\\Downloads"
dir_tree = {
     "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name,ext = os.path.splitext(event.src_path)
        for i,j in dir_tree.items():
            if ext in j : 
                file_name = os.path.basename(event.src_path)
                p1 = from_dir + "/" + file_name
                p2 = to_dir + "/" + i
                p3 = to_dir + "/" + i + "/" + file_name
                time.sleep(3)
                if os.path.exists(p2):
                    print("file move")
                    shutil.move(p1,p2)
                else:
                    os.makedirs(p2)
                    shutil.move(p1,p3)
event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive= True)
observer.start()
while True:
    time.sleep(2)
    print("Running")
        