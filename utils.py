import os

class Utils:
    def search_file(self, directory, filename):
        for root, _, files in os.walk(directory):
            if filename in files:
                print(f"File found: {os.path.join(root, filename)}")
                return
        print(f"File '{filename}' not found in '{directory}'.")
