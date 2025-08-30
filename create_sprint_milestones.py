#!/usr/bin/env python3
"""
Create 10 Sprint milestones (simplified from 103 to avoid rate limits)
Each sprint represents a major phase of development
"""

import os
import requests
import time
from datetime import datetime, timedelta

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    print("Set GITHUB_TOKEN environment variable")
    exit(1)

GITHUB_OWNER = 'michael-placeholder'
GITHUB_REPO = 'shadowed-realms'
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Define 10 major sprint milestones
SPRINTS = [
    {
        'title': 'Sprint 1: Foundation (Week 1-10)',
        'description': 'Issues 1-100: Documentation, project setup, initial planning',
        'due_date': '2025-11-09T00:00:00Z'
    },
    {
        'title': 'Sprint 2: Core Systems (Week 11-20)',
        'description': 'Issues 101-260: Movement, inventory, basic mechanics',
        'due_date': '2025-01-18T00:00:00Z'
    },
    {
        'title': 'Sprint 3: Combat Framework (Week 21-30)',
        'description': 'Issues 261-420: Melee combat, magic system, abilities',
        'due_date': '2025-03-29T00:00:00Z'
    },
    {
        'title': 'Sprint 4: Environment (Week 31-40)',
        'description': 'Issues 421-580: World building, weather, atmosphere',
        'due_date': '2025-06-07T00:00:00Z'
    },
    {
        'title': 'Sprint 5: Characters (Week 41-50)',
        'description': 'Issues 581-640: Character customization, models',
        'due_date': '2025-08-16T00:00:00Z'
    },
    {
        'title': 'Sprint 6: UI/UX (Week 51-60)',
        'description': 'Issues 641-760: Interface design, HUD, menus',
        'due_date': '2025-10-25T00:00:00Z'
    },
    {
        'title': 'Sprint 7: Progression (Week 61-70)',
        'description': 'Issues 761-820: Character progression, skill trees',
        'due_date': '2026-01-03T00:00:00Z'
    },
    {
        'title': 'Sprint 8: Save System (Week 71-80)',
        'description': 'Issues 821-900: Save/load, cloud saves, persistence',
        'due_date': '2026-03-14T00:00:00Z'
    },
    {
        'title': 'Sprint 9: Audio (Week 81-90)',
        'description': 'Issues 901-960: Sound effects, music, audio mixing',
        'due_date': '2026-05-23T00:00:00Z'
    },
    {
        'title': 'Sprint 10: Polish & Launch (Week 91-103)',
        'description': 'Issues 961-1000: Final polish, optimization, launch prep',
        'due_date': '2026-08-29T00:00:00Z'
    }
]

def create_milestone(sprint):
    """Create a single milestone"""
    url = f'{GITHUB_API_URL}/milestones'
    data = {
        'title': sprint['title'],
        'description': sprint['description'],
        'due_on': sprint['due_date'],
        'state': 'open'
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            return response.json()
        elif response.status_code == 422:
            print(f"  Milestone '{sprint['title']}' may already exist")
            return None
        else:
            print(f"  Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"  Exception: {e}")
        return None

def main():
    print("=" * 60)
    print("Creating Sprint Milestones")
    print("=" * 60)
    
    created = 0
    skipped = 0
    
    for i, sprint in enumerate(SPRINTS, 1):
        print(f"\n[{i}/10] Creating: {sprint['title']}")
        result = create_milestone(sprint)
        
        if result:
            created += 1
            print(f"  ✓ Created milestone #{result['number']}")
        else:
            skipped += 1
            print(f"  ⊘ Skipped (may already exist)")
        
        # Rate limiting
        if i % 3 == 0:
            time.sleep(1)
    
    print("\n" + "=" * 60)
    print(f"Sprint Milestones Summary:")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Total: {created + skipped}/10")
    print("\nView at: https://github.com/{}/{}/milestones".format(GITHUB_OWNER, GITHUB_REPO))
    print("=" * 60)

if __name__ == "__main__":
    main()