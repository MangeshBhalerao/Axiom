
# This is the code which will tell us which framework it will be
from analyze import count_files_by_extension
from signature import load_signature
import os


def recognize_frameworks(directory_path):
     """
     Steps:
     1. Get sorted extensions from analyze.py
     2. Start with highest percentage extension
     3. Load signature.json
     4. Scan files with that extension
     5. Check for framework/dependency keywords
     """
     
     # Step 1: Get results from analyze.py (already sorted highest to lowest)
     results = count_files_by_extension(directory_path)
     sorted_extensions = results["sorted_extensions"]  # [(ext, count), (ext, count), ...]
     total_files = results["total_files"]
     
     # Step 2: Get the highest percentage extension
     if sorted_extensions:
          top_extension, top_count = sorted_extensions[0]  # First item = highest count
          percentage = (top_count / total_files * 100) if total_files > 0 else 0
          print(f"\n🔍 Top extension: {top_extension} ({percentage:.1f}%)")
     else:
          print("No files found!")
          return
     
     # Step 3: Load signature.json
     signature_path = os.path.join(os.path.dirname(__file__), "signature.json")
     signatures = load_signature(signature_path)
     
     # Step 4: Find all files with the top extension
     files_to_scan = []
     for dirpath, dirnames, filenames in os.walk(directory_path):
          for filename in filenames:
               if filename.endswith(top_extension):
                    files_to_scan.append(os.path.join(dirpath, filename))
     
     print(f"📁 Found {len(files_to_scan)} files with {top_extension} extension to scan")
     
     # Step 5: Read each file and check for framework signatures
     # First, find which language this extension belongs to
     detected_frameworks = {}  # {framework_name: count}
     
     # Find the language for this extension
     target_language = None
     for lang_name, lang_data in signatures["languages"].items():
          if top_extension in lang_data.get("file_extensions", []):
               target_language = lang_name
               break
     
     if not target_language:
          print(f"⚠️ No language found for extension {top_extension}")
          return
     
     print(f"Detected language: {target_language}")
     
     # Get frameworks for this language
     frameworks = signatures["languages"][target_language].get("frameworks", {})
     
     # Scan each file for framework import patterns
     for file_path in files_to_scan:
          try:
               with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    
                    # Check each framework's import patterns
                    for framework_name, framework_data in frameworks.items():
                         import_patterns = framework_data.get("import_patterns", [])
                         
                         for pattern in import_patterns:
                              if pattern in content:
                                   # Found a match!
                                   if framework_name not in detected_frameworks:
                                        detected_frameworks[framework_name] = 0
                                   detected_frameworks[framework_name] += 1
                                   break  # No need to check more patterns for this framework in this file
                                   
          except Exception as e:
               print(f"  ⚠️ Could not read {file_path}: {e}")
     
     # Print results
     print("\n" + "=" * 50)
     print(" DETECTED FRAMEWORKS:")
     print("=" * 50)
     
     if detected_frameworks:
          # Sort by count (highest first)
          sorted_frameworks = sorted(detected_frameworks.items(), key=lambda x: x[1], reverse=True)
          for framework, count in sorted_frameworks:
               print(f"  ✅ {framework.upper()} - found in {count} file(s)")
     else:
          print("  No frameworks detected.")
     
     return detected_frameworks


# Test it
if __name__ == "__main__":
     recognize_frameworks('/home/mangesh/Coding/practice')