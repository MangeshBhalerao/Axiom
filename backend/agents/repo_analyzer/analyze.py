import os
from pathlib import Path
from collections import defaultdict
import json

def count_files_by_extension(directory_path):
     print(f"--- Scanning Directory: {directory_path} ---\n")
     
     # Dictionary to store extension counts
     extension_count = defaultdict(int)
     total_files = 0
     total_directories = 0
     
     # Walk through directory
     for dirpath, dirnames, filenames in os.walk(directory_path):
          total_directories += len(dirnames)
          
          # Count files by extension
          for filename in filenames:
               
               total_files += 1
               # Get file extension (including the dot)
               _, ext = os.path.splitext(filename)
               
               # If no extension, mark as "no extension"
               if ext == "":
                    ext = "[no extension]"
               
               extension_count[ext] += 1


     # Print results
     print("=" * 50)
     print(f"Total Directories: {total_directories}")
     print(f"Total Files: {total_files}")
     print("=" * 50)
     print("\nFiles by Extension:")
     print("-" * 50)
     
     # Sort by count (descending)
     sorted_extensions = sorted(extension_count.items(), key=lambda x: x[1], reverse= True)
     
     for ext, count in sorted_extensions:
          percentage = (count / total_files * 100) if total_files > 0 else 0
          print(f"  {ext:<20} : {count:>5} files ({percentage:>5.1f}%)")
     
     print("=" * 50)
     
               

     return extension_count


count_files_by_extension('/home/mangesh/Coding/practice')
