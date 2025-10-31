#!/usr/bin/env python
"""
GitHub Upload Helper Script

This script helps initialize Git and upload the project to GitHub.
"""

import os
import subprocess
import sys

def run_command(command):
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e.stderr}")
        return None

def init_git():
    """Initialize Git repository if not already initialized."""
    if not os.path.exists('.git'):
        print("Initializing Git repository...")
        if run_command('git init') is None:
            return False
    return True

def configure_remote(repo_url):
    """Configure the remote repository."""
    print(f"Setting remote repository to: {repo_url}")
    
    # Remove existing remote if it exists
    run_command('git remote remove origin')
    
    # Add new remote
    if run_command(f'git remote add origin {repo_url}') is None:
        return False
    return True

def create_gitignore():
    """Create .gitignore file with common Python patterns."""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/
env/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Django
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal
media/

# Project specific
ml_model/models/*.pkl
.env
"""
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    print("Created .gitignore file")

def stage_and_commit():
    """Stage all files and create initial commit."""
    print("Staging files...")
    if run_command('git add .') is None:
        return False
    
    print("Creating initial commit...")
    if run_command('git commit -m "Initial commit: Heart Disease Prediction System"') is None:
        return False
    return True

def push_to_remote():
    """Push code to remote repository."""
    print("Pushing to remote repository...")
    if run_command('git push -u origin master') is None:
        return False
    return True

def main():
    """Main function to handle GitHub upload process."""
    print("=== GitHub Upload Helper ===")
    
    # Repository URL
    repo_url = "https://github.com/dinesh90040/HRIDAY-LAYA-Project.git"
    
    # Initialize Git
    if not init_git():
        print("Failed to initialize Git repository")
        return
    
    # Create .gitignore
    create_gitignore()
    
    # Configure remote
    if not configure_remote(repo_url):
        print("Failed to configure remote repository")
        return
    
    # Stage and commit
    if not stage_and_commit():
        print("Failed to create initial commit")
        return
    
    # Push to remote
    if not push_to_remote():
        print("Failed to push to remote repository")
        print("If you're using HTTPS, make sure you have entered your GitHub credentials")
        print("If you're using SSH, ensure your SSH key is properly configured")
        return
    
    print("\n=== Upload Complete ===")
    print(f"Your code has been uploaded to: {repo_url}")
    print("\nNext steps:")
    print("1. Visit your repository on GitHub to verify the upload")
    print("2. Update repository settings if needed")
    print("3. Add collaborators if required")

if __name__ == "__main__":
    main() 