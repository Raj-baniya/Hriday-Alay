#!/usr/bin/env python
"""
Project Transfer Helper Script

This script helps prepare your Django project for transfer to a new laptop.
It creates a zip file of the project, excluding unnecessary files.
"""

import os
import shutil
import zipfile
import datetime
import sys
import subprocess

def create_backup_zip():
    """Create a zip file of the project, excluding unnecessary files."""
    # Get the current directory (project root)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a timestamp for the zip file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"heart_disease_prediction_{timestamp}.zip"
    
    # Files and directories to exclude
    exclude_patterns = [
        '__pycache__',
        '.git',
        '.gitignore',
        '.idea',
        '.vscode',
        'venv',
        'env',
        '*.pyc',
        '*.pyo',
        '*.pyd',
        '*.so',
        '*.egg',
        '*.egg-info',
        'dist',
        'build',
        'eggs',
        'parts',
        'bin',
        'var',
        'sdist',
        'develop-eggs',
        'installs',
        'downloads',
        'logs',
        'tmp',
        'temp',
        '.DS_Store',
        'Thumbs.db',
        '*.log',
        '*.sqlite3-journal',
        '*.bak',
        '*.swp',
        '*.swo',
        '*.swn',
        '*.bak',
        '*.tmp',
        '*.temp',
        '*.db',
        '*.sqlite3',
    ]
    
    # Create a temporary directory for the files to zip
    temp_dir = os.path.join(project_dir, f"temp_transfer_{timestamp}")
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        # Copy project files to the temporary directory
        for root, dirs, files in os.walk(project_dir):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if not any(pattern in d for pattern in exclude_patterns)]
            
            # Calculate the relative path
            rel_path = os.path.relpath(root, project_dir)
            
            # Skip the temporary directory itself
            if rel_path.startswith(f"temp_transfer_{timestamp}"):
                continue
            
            # Create the same directory structure in the temp directory
            temp_path = os.path.join(temp_dir, rel_path)
            os.makedirs(temp_path, exist_ok=True)
            
            # Copy files
            for file in files:
                # Skip excluded files
                if any(pattern in file for pattern in exclude_patterns):
                    continue
                
                src_file = os.path.join(root, file)
                dst_file = os.path.join(temp_path, file)
                shutil.copy2(src_file, dst_file)
        
        # Create the zip file
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, temp_dir)
                    zipf.write(file_path, arcname)
        
        print(f"Successfully created {zip_filename}")
        print(f"Size: {os.path.getsize(zip_filename) / (1024*1024):.2f} MB")
        
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir, ignore_errors=True)

def check_dependencies():
    """Check if all required dependencies are installed."""
    try:
        import django
        import numpy
        import pandas
        import sklearn
        import matplotlib
        import seaborn
        import joblib
        import PIL
        import crispy_forms
        import crispy_bootstrap5
        
        print("All required dependencies are installed.")
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def check_model_files():
    """Check if the machine learning model files exist."""
    model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml_model', 'models')
    model_file = os.path.join(model_dir, 'heart_disease_model.pkl')
    
    if os.path.exists(model_file):
        print(f"Model file found: {model_file}")
        print(f"Size: {os.path.getsize(model_file) / 1024:.2f} KB")
        return True
    else:
        print(f"Model file not found: {model_file}")
        print("Please run: python ml_model/train.py")
        return False

def main():
    """Main function to run the transfer preparation."""
    print("=== Heart Disease Prediction System - Transfer Helper ===")
    print("This script will help you prepare your project for transfer to a new laptop.")
    print()
    
    # Check dependencies
    print("Checking dependencies...")
    deps_ok = check_dependencies()
    
    # Check model files
    print("\nChecking model files...")
    model_ok = check_model_files()
    
    if not deps_ok or not model_ok:
        print("\nSome checks failed. Please fix the issues before transferring.")
        return
    
    # Create backup zip
    print("\nCreating backup zip file...")
    create_backup_zip()
    
    print("\n=== Transfer Preparation Complete ===")
    print("1. Copy the zip file to your new laptop")
    print("2. Extract the zip file")
    print("3. Follow the instructions in transfer_guide.txt")
    print("\nGood luck with your transfer!")

if __name__ == "__main__":
    main() 