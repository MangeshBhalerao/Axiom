#!/usr/bin/env python3
"""
Axiom CLI - Repository Analysis Tool

Usage:
    axiom analyze <path>
    axiom analyze <path> --output results.json
    axiom analyze <path> --json
"""

import argparse
import sys
import os
from pathlib import Path
from orchestrator import analyze_repository, print_summary, export_json
import json


def validate_path(path_str):
    """
    Validate if the given path exists and is a directory
    """
    path = Path(path_str).resolve()
    
    if not path.exists():
        print(f"❌ Error: Path does not exist: {path_str}")
        sys.exit(1)
    
    if not path.is_dir():
        print(f"❌ Error: Path is not a directory: {path_str}")
        sys.exit(1)
    
    return str(path)


def handle_analyze(args):
    """
    Handle the 'analyze' command
    """
    # Validate path
    repo_path = validate_path(args.path)
    
    # Run analysis
    try:
        results = analyze_repository(repo_path)
        
        # Output handling
        if args.json:
            # Print JSON to stdout
            print(json.dumps(results, indent=2))
        elif args.output:
            # Export to file and print summary
            print_summary(results)
            export_json(results, args.output)
        else:
            # Just print summary
            print_summary(results)
            
    except Exception as e:
        print(f"\n❌ Error during analysis: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    """
    Main CLI entry point
    """
    parser = argparse.ArgumentParser(
        prog='axiom',
        description='🔍 Axiom - AI-Powered Repository Analysis Tool',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  axiom analyze /path/to/repo
  axiom analyze /path/to/repo --output results.json
  axiom analyze /path/to/repo --json
  
For more information, visit: https://github.com/MangeshBhalerao/Axiom
        """
    )
    
    # Create subparsers for commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # 'analyze' command
    analyze_parser = subparsers.add_parser(
        'analyze',
        help='Analyze a repository'
    )
    analyze_parser.add_argument(
        'path',
        help='Path to the repository to analyze'
    )
    analyze_parser.add_argument(
        '--output', '-o',
        help='Export results to JSON file'
    )
    analyze_parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON to stdout'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Handle commands
    if args.command == 'analyze':
        handle_analyze(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
