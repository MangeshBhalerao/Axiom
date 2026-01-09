"""
Orchestrator - Brings together all analysis components
"""
from analyze import count_files_by_extension
from recognize import recognize_frameworks
import json
from pathlib import Path


def analyze_repository(repo_path):
    """
    Main orchestration function that runs all analyses
    
    Args:
        repo_path: Path to the repository to analyze
        
    Returns:
        dict: Comprehensive analysis results
    """
    
    results = {
        "repo_path": str(repo_path),
        "file_analysis": {},
        "framework_detection": {},
        "tech_stack": {},
        "metadata": {}
    }
    
    # Step 1: File extension analysis
    print("\n" + "="*60)
    print("🔍 AXIOM - Repository Analysis")
    print("="*60)
    
    file_stats = count_files_by_extension(repo_path)
    results["file_analysis"] = file_stats
    
    # Step 2: Framework detection
    frameworks = recognize_frameworks(repo_path)
    results["framework_detection"] = frameworks if frameworks else {}
    
    # Step 3: Build tech stack summary
    tech_stack = build_tech_stack_summary(file_stats, frameworks)
    results["tech_stack"] = tech_stack
    
    return results


def build_tech_stack_summary(file_stats, frameworks):
    """
    Create a summary of the tech stack based on file analysis and frameworks
    """
    summary = {
        "primary_language": None,
        "frameworks": [],
        "total_files": file_stats.get("total_files", 0),
        "total_directories": file_stats.get("total_directories", 0)
    }
    
    # Determine primary language from top extensions
    sorted_extensions = file_stats.get("sorted_extensions", [])
    if sorted_extensions:
        top_ext = sorted_extensions[0][0]
        language_map = {
            ".py": "Python",
            ".js": "JavaScript",
            ".jsx": "JavaScript (React)",
            ".ts": "TypeScript",
            ".tsx": "TypeScript (React)",
            ".go": "Go",
            ".rs": "Rust",
            ".java": "Java",
            ".rb": "Ruby",
            ".php": "PHP",
            ".c": "C",
            ".cpp": "C++",
            ".cs": "C#",
            ".swift": "Swift",
            ".kt": "Kotlin"
        }
        summary["primary_language"] = language_map.get(top_ext, top_ext)
    
    # List detected frameworks
    if frameworks:
        summary["frameworks"] = list(frameworks.keys())
    
    return summary


def print_summary(results):
    """
    Print a beautiful summary of the analysis
    """
    print("\n" + "="*60)
    print("📊 ANALYSIS SUMMARY")
    print("="*60)
    
    tech_stack = results.get("tech_stack", {})
    
    print(f"\n📁 Repository: {results['repo_path']}")
    print(f"   Total Files: {tech_stack.get('total_files', 0)}")
    print(f"   Total Directories: {tech_stack.get('total_directories', 0)}")
    
    if tech_stack.get("primary_language"):
        print(f"\n💻 Primary Language: {tech_stack['primary_language']}")
    
    frameworks = tech_stack.get("frameworks", [])
    if frameworks:
        print(f"\n🚀 Detected Frameworks:")
        for fw in frameworks:
            print(f"   • {fw.upper()}")
    else:
        print(f"\n🚀 Detected Frameworks: None detected")
    
    print("\n" + "="*60)


def export_json(results, output_path):
    """
    Export results to JSON file
    """
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"✅ Results exported to: {output_path}")


if __name__ == "__main__":
    # Test the orchestrator
    test_path = '/home/mangesh/Coding/practice'
    results = analyze_repository(test_path)
    print_summary(results)
