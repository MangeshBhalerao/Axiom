import os
from pathlib import Path

extensions = {".py",".js"}

def scan_directory_os_walk(directory_path):
     
     print(f"--- Scanning Directory: {directory_path} ---")

     for dirpath, dirnames, filenames in os.walk(directory_path):
          print(f"\nCurrently in directory: {dirpath}")
          
          if not dirnames and not filenames:
               print("  (Empty directory)")
          
          for dirname in dirnames:
               print(f"  [Directory]: {os.path.join(dirpath, dirname)}")

          counting_files = len(filenames)
          print(f"  Total files in this directory: {counting_files}")
          
          extensions_files = [f for f in filenames if any(f.endswith(ext) for ext in extensions)]
          print(f"  Files with specified extensions: {len(extensions_files)}")
          
          for filename in filenames:
               print(f"  [File]: {os.path.join(dirpath, filename)}")

# Example usage: Replace '.' with your target directory path
scan_directory_os_walk('/home/mangesh/Coding/practice/Backend/1.Routing')
