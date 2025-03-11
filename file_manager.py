import os
import shutil  # For file copying and moving
import time    # For file info (creation date, etc.)

class FileManager:
    def create_file(self, path, content=""):
        try:
            with open(path, 'w') as file:
                file.write(content)
            print(f"File '{path}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def delete_file(self, path):
        try:
            if os.path.exists(path):
                os.remove(path)
                print(f"File '{path}' deleted.")
            else:
                print("File not found.")
        except Exception as e:
            print(f"Error deleting file: {e}")

    def view_file(self, path):
        try:
            with open(path, 'r') as file:
                print(f"--- {path} ---")
                print(file.read())
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def rename_file(self, old_path, new_path):
        try:
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
                print(f"File renamed to '{new_path}' successfully.")
            else:
                print(f"File '{old_path}' not found.")
        except Exception as e:
            print(f"Error renaming file: {e}")

    def copy_file(self, source_path, destination_path):
        try:
            if os.path.exists(source_path):
                shutil.copy(source_path, destination_path)
                print(f"File copied to '{destination_path}' successfully.")
            else:
                print(f"Source file '{source_path}' not found.")
        except Exception as e:
            print(f"Error copying file: {e}")
            
    def move_file(self, source_path, destination_path):
        try:
            if os.path.exists(source_path):
                shutil.move(source_path, destination_path)
                print(f"File moved to '{destination_path}' successfully.")
            else:
                print(f"Source file '{source_path}' not found.")
        except Exception as e:
            print(f"Error moving file: {e}")
    
    def file_info(self, path):
        try:
            if os.path.exists(path):
                size = os.path.getsize(path)
                created_time = time.ctime(os.path.getctime(path))
                modified_time = time.ctime(os.path.getmtime(path))
                
                print(f"--- File Info for '{path}' ---")
                print(f"Size: {size} bytes")
                print(f"Created On: {created_time}")
                print(f"Last Modified: {modified_time}")
            else:
                print(f"File '{path}' not found.")
        except Exception as e:
            print(f"Error fetching file info: {e}")
