from file_manager import FileManager
from directory_manager import DirectoryManager
from utils import Utils  # Import the search utility

# Initialize classes
fm = FileManager()
dm = DirectoryManager()
utils = Utils()

# Sample operations
dm.create_directory("data/projects")      # Create a directory
fm.create_file("data/projects/notes.txt", "Python OOP Concepts")  # Create a sample file
dm.list_directory("data")                 # List directory contents
fm.view_file("data/projects/notes.txt")   # View file content

# Search Example
utils.search_file("data", "notes.txt")

# Rename Example
fm.rename_file("data/projects/notes.txt", "data/projects/python_notes.txt")

# Copy Example
fm.copy_file("data/projects/python_notes.txt", "data/projects/copy_notes.txt")

# Move Example
fm.move_file("data/projects/python_notes.txt", "data/moved_notes.txt")

# File Info Example
fm.file_info("data/moved_notes.txt")
