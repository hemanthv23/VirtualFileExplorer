import os

class DirectoryManager:
    def list_directory(self, path, level=0):
        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                print("    " * level + "|__ " + item)
                if os.path.isdir(item_path):
                    self.list_directory(item_path, level + 1)
        except FileNotFoundError:
            print("Directory not found.")

    def create_directory(self, path):
        os.makedirs(path, exist_ok=True)
        print(f"Directory '{path}' created successfully.")
