import os
import shutil
import time
import json
import logging
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# Setup logging
LOG_FILE = "logs/file_monitor.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # Log everything (INFO, WARNING, ERROR)
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

#load the file_path and folders from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

FILE_PATH = rf"{config["download_directory"]}"

organized_folders = config["organized_folders"]

video_extensions = (
    ".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".webm",
    ".mpeg", ".mpg", ".3gp", ".m4v", ".ts", ".ogv", ".rm",
    ".rmvb", ".vob", ".asf", ".dv", ".m2ts"
)
image_extensions = (".jpeg", ".jpg", ".png", ".gif", ".bmp", ".svg", ".tiff", ".webp", ".ico")
document_extensions = (".txt", ".doc", ".docx", ".pdf", ".odt", ".rtf", ".tex", ".epub")
spreadsheet_extensions = (".csv", ".xlsx", ".xls", ".ods", ".json", ".xml", ".tsv")
audio_extensions = (".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".opus", ".mid")
archive_extensions = (".zip", ".rar", ".tar", ".gz", ".7z", ".bz2", ".xz", ".iso")
code_extensions = (".py", ".js", ".html", ".css", ".json", ".yaml", ".yml", ".c", ".cpp", ".java", ".go", ".sh", ".sql")
excluded_extensions = (".tmp", ".crdownload", ".part", ".download")


class MyHandler(FileSystemEventHandler):
    def process_file(self, file_path, folder_name):
        #Moves a file to the specified folder after ensuring it is completely downloaded.
        new_folder_path = os.path.join(FILE_PATH, folder_name)

        # Create folder if it doesn't exist
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)

        # Get file name
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(new_folder_path, file_name)

        # Wait for file to be fully downloaded
        time.sleep(2)

        # Retry mechanism to ensure file is fully available
        for _ in range(5):  # Try for 10 seconds (5 * 2s)
            if os.path.exists(file_path):
                try:
                    shutil.move(file_path, destination_path)
                    logging.info(f"✅ Moved {file_name} to {new_folder_path}")
                    return
                except PermissionError:
                    logging.warning(f"⏳ File {file_name} is still in use. Retrying...")
                    time.sleep(2)
            else:
                logging.error(f"⚠️ File {file_path} not found. Skipping move.")
                return

    def on_created(self, event):
        #Detects new file creation and organizes it into the correct folder
        if not event.is_directory and not event.src_path.lower().endswith(excluded_extensions):
            logging.info(f"📂 New file detected: {event.src_path}")


    def on_modified(self, event):
        #Detects file modification (important for downloads)
        file_ext = event.src_path.lower()
        if not event.is_directory and file_ext.endswith(image_extensions):
            logging.info(f"📝 Video file modified: {event.src_path}")
            self.process_file(event.src_path, organized_folders["images"])
        elif not event.is_directory and file_ext.endswith(video_extensions):
            logging.info(f"📝 Video file modified: {event.src_path}")
            self.process_file(event.src_path, organized_folders["videos"])
        elif not event.is_directory and file_ext.endswith(document_extensions):
            logging.info(f"📝 Video file modified: {event.src_path}")
            self.process_file(event.src_path, organized_folders["documents"])
        elif not event.is_directory and file_ext.endswith(spreadsheet_extensions):
            logging.info(f"📝 Video file modified: {event.src_path}")
            self.process_file(event.src_path, organized_folders["spreadsheets"])
        elif not event.is_directory and file_ext.endswith(audio_extensions):
            logging.info(f"📝 Video file modified: {event.src_path}")
            self.process_file(event.src_path, organized_folders["audio"])
        elif not event.is_directory and file_ext.endswith(archive_extensions):
            logging.info(f"📝 Video file modified: {event.src_path}")
            self.process_file(event.src_path, organized_folders["archives"])
        elif not event.is_directory and file_ext.endswith(code_extensions):
            logging.info(f"📝 Video file modified: {event.src_path}")
            self.process_file(event.src_path, organized_folders["code"])



if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, FILE_PATH, recursive=False)

    observer.start()
    logging.info("👀 Watching for downloads...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("🛑 Stopping observer...")
        observer.stop()

    observer.join()
    logging.info("✅ Observer stopped.")
