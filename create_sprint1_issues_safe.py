#!/usr/bin/env python3
"""
Create Sprint 1 issues for Shadowed Realms RPG
Based on SPRINT_1_COMPLETE_TASKS.md
"""

import os
import json
import time
import requests
from typing import List, Dict

# GitHub configuration - Token should be set as environment variable
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set")
    print("Please set: export GITHUB_TOKEN='your_token_here'")
    exit(1)

GITHUB_OWNER = 'michael-placeholder'
GITHUB_REPO = 'shadowed-realms'
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}'

# Headers for GitHub API
headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def create_issue(title: str, body: str, labels: List[str]) -> Dict:
    """Create a single GitHub issue"""
    url = f'{GITHUB_API_URL}/issues'
    data = {
        'title': title,
        'body': body,
        'labels': labels
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating issue '{title}': {e}")
        return None

def generate_sprint1_issues():
    """Generate the first 200 issues for Sprint 1"""
    issues = []
    
    # EPIC-001: Project Setup & Infrastructure (Issues 0001-0160)
    epic1_issues = [
        # Install Core Development Tools (0001-0010)
        {'num': '0001', 'title': 'Download Unity Hub from unity.com', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        {'num': '0002', 'title': 'Install Unity 2024.3 LTS', 'xp': 50, 'coins': 20, 'labels': ['setup', 'easy']},
        {'num': '0003', 'title': 'Download Visual Studio 2022', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        {'num': '0004', 'title': 'Install Visual Studio Unity Tools', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        {'num': '0005', 'title': 'Download Git for Windows/Mac', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        {'num': '0006', 'title': 'Install Git LFS for large files', 'xp': 50, 'coins': 20, 'labels': ['setup', 'medium']},
        {'num': '0007', 'title': 'Download GitHub Desktop', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        {'num': '0008', 'title': 'Install Node.js v20 LTS', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        {'num': '0009', 'title': 'Install Python 3.11', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        {'num': '0010', 'title': 'Run npm install -g yarn', 'xp': 25, 'coins': 10, 'labels': ['setup', 'easy']},
        
        # Initialize Git Repository (0011-0020)
        {'num': '0011', 'title': 'Run git init in project folder', 'xp': 25, 'coins': 10, 'labels': ['git', 'easy']},
        {'num': '0012', 'title': 'Create .gitignore file', 'xp': 50, 'coins': 20, 'labels': ['git', 'easy']},
        {'num': '0013', 'title': 'Add Unity-specific gitignore rules', 'xp': 50, 'coins': 20, 'labels': ['git', 'medium']},
        {'num': '0014', 'title': 'Run git lfs track "*.fbx"', 'xp': 25, 'coins': 10, 'labels': ['git', 'easy']},
        {'num': '0015', 'title': 'Run git lfs track "*.png"', 'xp': 25, 'coins': 10, 'labels': ['git', 'easy']},
        {'num': '0016', 'title': 'Run git lfs track "*.psd"', 'xp': 25, 'coins': 10, 'labels': ['git', 'easy']},
        {'num': '0017', 'title': 'Create README.md', 'xp': 100, 'coins': 40, 'labels': ['documentation', 'medium']},
        {'num': '0018', 'title': 'Run git add .', 'xp': 25, 'coins': 10, 'labels': ['git', 'easy']},
        {'num': '0019', 'title': 'Run git commit -m "Initial commit"', 'xp': 25, 'coins': 10, 'labels': ['git', 'easy']},
        {'num': '0020', 'title': 'Create GitHub repository online', 'xp': 50, 'coins': 20, 'labels': ['git', 'easy']},
        
        # Configure Unity Project (0021-0040)
        {'num': '0021', 'title': 'Open Unity Hub', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0022', 'title': 'Click "New Project"', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0023', 'title': 'Select 3D (URP) template', 'xp': 50, 'coins': 20, 'labels': ['unity', 'easy']},
        {'num': '0024', 'title': 'Name project "ShadowedRealms"', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0025', 'title': 'Choose project location', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0026', 'title': 'Click "Create project"', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0027', 'title': 'Wait for project creation', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0028', 'title': 'Open Project Settings', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0029', 'title': 'Set Company Name', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0030', 'title': 'Set Product Name', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        
        # More Unity Configuration (0031-0050)
        {'num': '0031', 'title': 'Configure Player Settings', 'xp': 50, 'coins': 20, 'labels': ['unity', 'medium']},
        {'num': '0032', 'title': 'Set Default Screen Width: 1920', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0033', 'title': 'Set Default Screen Height: 1080', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0034', 'title': 'Enable Fullscreen Mode', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0035', 'title': 'Set Graphics API to DX11', 'xp': 50, 'coins': 20, 'labels': ['unity', 'medium']},
        {'num': '0036', 'title': 'Configure Quality Settings', 'xp': 50, 'coins': 20, 'labels': ['unity', 'medium']},
        {'num': '0037', 'title': 'Add Ultra quality level', 'xp': 50, 'coins': 20, 'labels': ['unity', 'medium']},
        {'num': '0038', 'title': 'Set Anti-aliasing to 4x', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0039', 'title': 'Enable Soft Shadows', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
        {'num': '0040', 'title': 'Save project', 'xp': 25, 'coins': 10, 'labels': ['unity', 'easy']},
    ]
    
    # Add more issues for folders, packages, etc.
    folder_issues = [
        {'num': '0041', 'title': 'Create Assets/_Project folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0042', 'title': 'Create Scripts folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0043', 'title': 'Create Prefabs folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0044', 'title': 'Create Materials folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0045', 'title': 'Create Textures folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0046', 'title': 'Create Models folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0047', 'title': 'Create Animations folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0048', 'title': 'Create Audio folder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0049', 'title': 'Create Audio/Music subfolder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
        {'num': '0050', 'title': 'Create Audio/SFX subfolder', 'xp': 25, 'coins': 10, 'labels': ['organization', 'easy']},
    ]
    
    # Package installation issues (0061-0080)
    package_issues = [
        {'num': '0061', 'title': 'Open Package Manager', 'xp': 25, 'coins': 10, 'labels': ['packages', 'easy']},
        {'num': '0062', 'title': 'Switch to Unity Registry', 'xp': 25, 'coins': 10, 'labels': ['packages', 'easy']},
        {'num': '0063', 'title': 'Search "Cinemachine"', 'xp': 25, 'coins': 10, 'labels': ['packages', 'easy']},
        {'num': '0064', 'title': 'Install Cinemachine', 'xp': 50, 'coins': 20, 'labels': ['packages', 'medium']},
        {'num': '0065', 'title': 'Search "Input System"', 'xp': 25, 'coins': 10, 'labels': ['packages', 'easy']},
        {'num': '0066', 'title': 'Install Input System', 'xp': 50, 'coins': 20, 'labels': ['packages', 'medium']},
        {'num': '0067', 'title': 'Search "TextMeshPro"', 'xp': 25, 'coins': 10, 'labels': ['packages', 'easy']},
        {'num': '0068', 'title': 'Import TMP Essentials', 'xp': 50, 'coins': 20, 'labels': ['packages', 'medium']},
        {'num': '0069', 'title': 'Search "ProBuilder"', 'xp': 25, 'coins': 10, 'labels': ['packages', 'easy']},
        {'num': '0070', 'title': 'Install ProBuilder', 'xp': 50, 'coins': 20, 'labels': ['packages', 'medium']},
    ]
    
    # Character System Foundation issues (0161-0200)
    character_issues = [
        {'num': '0161', 'title': 'Launch Maya 2024', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0162', 'title': 'Set project location', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0163', 'title': 'Configure Maya preferences', 'xp': 50, 'coins': 20, 'labels': ['3d-modeling', 'medium']},
        {'num': '0164', 'title': 'Set working units to meters', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0165', 'title': 'Set up rate to 30fps', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0166', 'title': 'Enable autosave', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0167', 'title': 'Create new scene', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0168', 'title': 'Save as character_base.ma', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0169', 'title': 'Create polygon cube', 'xp': 25, 'coins': 10, 'labels': ['3d-modeling', 'easy']},
        {'num': '0170', 'title': 'Scale to human proportions', 'xp': 50, 'coins': 20, 'labels': ['3d-modeling', 'medium']},
    ]
    
    # Combine all issues
    all_issues = epic1_issues + folder_issues + package_issues + character_issues
    
    return all_issues

def main():
    """Main function to create issues"""
    print("=" * 60)
    print("SHADOWED REALMS - Sprint 1 Issue Creator")
    print("=" * 60)
    
    issues_to_create = generate_sprint1_issues()
    total_issues = len(issues_to_create)
    
    print(f"\nPrepared {total_issues} issues for creation")
    print("This will create issues with:")
    print("- Granular micro-tasks from Sprint 1")
    print("- XP and coin rewards")
    print("- Appropriate labels")
    
    # Create issues with rate limiting
    created_count = 0
    failed_count = 0
    
    for i, issue_data in enumerate(issues_to_create, 1):
        title = f"[ISSUE-{issue_data['num']}] {issue_data['title']}"
        
        body = f"""## Task Details
**Issue Number**: {issue_data['num']}
**XP Reward**: {issue_data['xp']}
**Coin Reward**: {issue_data['coins']}

### Description
{issue_data['title']}

### Acceptance Criteria
- [ ] Task completed as described
- [ ] Verified working correctly
- [ ] Documented if necessary

### Sprint
Sprint 1 - Foundation & Core Systems

---
*Part of the Shadowed Realms RPG development journey*
"""
        
        labels = [
            'issue',
            'micro-task',
            f"xp-{issue_data['xp']}",
            f"coins-{issue_data['coins']}",
            'sprint-1'
        ] + issue_data['labels']
        
        print(f"\n[{i}/{total_issues}] Creating: {title}")
        
        result = create_issue(title, body, labels)
        
        if result:
            created_count += 1
            print(f"  ✓ Created successfully (#{result['number']})")
        else:
            failed_count += 1
            print(f"  ✗ Failed to create")
        
        # Rate limiting - GitHub allows 5000 requests per hour for authenticated requests
        # But let's be conservative to avoid any issues
        if i % 10 == 0:
            print(f"\n  Pausing for rate limiting...")
            time.sleep(2)
    
    print("\n" + "=" * 60)
    print("CREATION COMPLETE")
    print(f"Successfully created: {created_count} issues")
    print(f"Failed: {failed_count} issues")
    print("=" * 60)
    
    print(f"\nView issues at: https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/issues")
    print(f"Dashboard: https://{GITHUB_OWNER}.github.io/{GITHUB_REPO}/")

if __name__ == "__main__":
    main()