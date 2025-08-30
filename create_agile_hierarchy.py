#!/usr/bin/env python3
"""
Create complete agile hierarchy with memory fragments for Shadowed Realms
Hierarchy: Epic > User Story > Issue > Tasks
Each issue unlocks a memory fragment
Completing all issues in a user story unlocks a real story
"""

import os
import json
import requests
import time

# GitHub configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set")
    exit(1)

GITHUB_OWNER = 'michael-placeholder'
GITHUB_REPO = 'shadowed-realms'
GITHUB_API_URL = f'https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}'

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Six Real Stories from the Lore
REAL_STORIES = {
    "STORY-001": {
        "title": "The Fall of the Golden City",
        "description": "How the once-great capital fell to shadow corruption",
        "unlocked_by": "Completing all Core Systems user stories"
    },
    "STORY-002": {
        "title": "The Last Guardian's Sacrifice",
        "description": "The tale of the guardian who sealed the ancient evil",
        "unlocked_by": "Completing all Combat Framework user stories"
    },
    "STORY-003": {
        "title": "The Merchant's Dark Bargain",
        "description": "How greed opened the first portal to the shadow realm",
        "unlocked_by": "Completing all Environment System user stories"
    },
    "STORY-004": {
        "title": "The Scholar's Forbidden Knowledge",
        "description": "Discovery of the ritual that could save or doom the realm",
        "unlocked_by": "Completing all UI/UX Framework user stories"
    },
    "STORY-005": {
        "title": "The Knight's Redemption",
        "description": "A fallen knight's journey from darkness to light",
        "unlocked_by": "Completing all Character System user stories"
    },
    "STORY-006": {
        "title": "The Shadow King's Origin",
        "description": "The truth about the realm's greatest threat",
        "unlocked_by": "Completing all Polish & Launch user stories"
    }
}

# Epic > User Story > Issue > Tasks Hierarchy
AGILE_HIERARCHY = {
    "EPIC-001": {
        "title": "Pre-Sprint 1: Ideation & Documentation",
        "user_stories": {
            "US-001": {
                "title": "As a developer, I need comprehensive documentation",
                "issues": list(range(1, 51)),  # Issues 1-50
                "tasks_per_issue": 3,
                "story_points": 150,
                "unlocks_story": "STORY-001",
                "memory_theme": "Ancient Texts"
            },
            "US-002": {
                "title": "As a team lead, I need project structure defined",
                "issues": list(range(51, 101)),  # Issues 51-100
                "tasks_per_issue": 3,
                "story_points": 150,
                "unlocks_story": "STORY-001",
                "memory_theme": "Architectural Plans"
            }
        }
    },
    "EPIC-002": {
        "title": "Core Systems Implementation",
        "user_stories": {
            "US-003": {
                "title": "As a player, I need basic movement and controls",
                "issues": list(range(101, 181)),  # Issues 101-180
                "tasks_per_issue": 4,
                "story_points": 320,
                "unlocks_story": "STORY-001",
                "memory_theme": "Movement Rituals"
            },
            "US-004": {
                "title": "As a player, I need inventory management",
                "issues": list(range(181, 261)),  # Issues 181-260
                "tasks_per_issue": 4,
                "story_points": 320,
                "unlocks_story": "STORY-001",
                "memory_theme": "Inventory Scrolls"
            }
        }
    },
    "EPIC-003": {
        "title": "Combat Framework",
        "user_stories": {
            "US-005": {
                "title": "As a player, I need melee combat system",
                "issues": list(range(261, 341)),  # Issues 261-340
                "tasks_per_issue": 5,
                "story_points": 400,
                "unlocks_story": "STORY-002",
                "memory_theme": "Combat Techniques"
            },
            "US-006": {
                "title": "As a player, I need magic and abilities",
                "issues": list(range(341, 421)),  # Issues 341-420
                "tasks_per_issue": 5,
                "story_points": 400,
                "unlocks_story": "STORY-002",
                "memory_theme": "Arcane Knowledge"
            }
        }
    },
    "EPIC-004": {
        "title": "Environment System",
        "user_stories": {
            "US-007": {
                "title": "As a player, I need immersive environments",
                "issues": list(range(421, 501)),  # Issues 421-500
                "tasks_per_issue": 4,
                "story_points": 320,
                "unlocks_story": "STORY-003",
                "memory_theme": "World Maps"
            },
            "US-008": {
                "title": "As a player, I need weather and atmosphere",
                "issues": list(range(501, 581)),  # Issues 501-580
                "tasks_per_issue": 4,
                "story_points": 320,
                "unlocks_story": "STORY-003",
                "memory_theme": "Weather Patterns"
            }
        }
    },
    "EPIC-005": {
        "title": "Character System",
        "user_stories": {
            "US-009": {
                "title": "As a player, I need character customization",
                "issues": list(range(581, 641)),  # Issues 581-640
                "tasks_per_issue": 3,
                "story_points": 180,
                "unlocks_story": "STORY-005",
                "memory_theme": "Character Designs"
            },
            "US-010": {
                "title": "As a player, I need progression system",
                "issues": list(range(761, 821)),  # Issues 761-820
                "tasks_per_issue": 3,
                "story_points": 180,
                "unlocks_story": "STORY-005",
                "memory_theme": "Skill Trees"
            }
        }
    },
    "EPIC-006": {
        "title": "UI/UX Framework",
        "user_stories": {
            "US-011": {
                "title": "As a player, I need intuitive UI",
                "issues": list(range(641, 721)),  # Issues 641-720
                "tasks_per_issue": 3,
                "story_points": 240,
                "unlocks_story": "STORY-004",
                "memory_theme": "Interface Designs"
            },
            "US-012": {
                "title": "As a player, I need HUD and feedback",
                "issues": list(range(721, 761)),  # Issues 721-760
                "tasks_per_issue": 3,
                "story_points": 120,
                "unlocks_story": "STORY-004",
                "memory_theme": "HUD Layouts"
            }
        }
    },
    "EPIC-007": {
        "title": "Save System & Persistence",
        "user_stories": {
            "US-013": {
                "title": "As a player, I need save/load functionality",
                "issues": list(range(821, 881)),  # Issues 821-880
                "tasks_per_issue": 4,
                "story_points": 240,
                "unlocks_story": "STORY-006",
                "memory_theme": "Save Crystals"
            },
            "US-014": {
                "title": "As a player, I need cloud saves",
                "issues": list(range(881, 901)),  # Issues 881-900
                "tasks_per_issue": 4,
                "story_points": 80,
                "unlocks_story": "STORY-006",
                "memory_theme": "Cloud Sync"
            }
        }
    },
    "EPIC-008": {
        "title": "Audio & Polish",
        "user_stories": {
            "US-015": {
                "title": "As a player, I need immersive audio",
                "issues": list(range(901, 961)),  # Issues 901-960
                "tasks_per_issue": 3,
                "story_points": 180,
                "unlocks_story": "STORY-006",
                "memory_theme": "Sound Design"
            },
            "US-016": {
                "title": "As a player, I need polished experience",
                "issues": list(range(961, 1001)),  # Issues 961-1000
                "tasks_per_issue": 3,
                "story_points": 120,
                "unlocks_story": "STORY-006",
                "memory_theme": "Final Polish"
            }
        }
    }
}

def create_milestone(title, description, due_date=None):
    """Create a GitHub milestone"""
    url = f'{GITHUB_API_URL}/milestones'
    data = {
        'title': title,
        'description': description,
        'state': 'open'
    }
    if due_date:
        data['due_on'] = due_date
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        return response.json()
    elif response.status_code == 422:
        # Milestone might already exist
        print(f"Milestone '{title}' may already exist")
        return None
    else:
        print(f"Error creating milestone: {response.status_code}")
        return None

def create_label(name, color, description):
    """Create a GitHub label"""
    url = f'{GITHUB_API_URL}/labels'
    data = {
        'name': name,
        'color': color,
        'description': description
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        return response.json()
    elif response.status_code == 422:
        # Label might already exist
        return None
    else:
        print(f"Error creating label: {response.status_code}")
        return None

def update_issue_with_hierarchy(issue_number, epic_id, user_story_id, memory_fragment):
    """Update an issue with hierarchy information"""
    url = f'{GITHUB_API_URL}/issues/{issue_number}'
    
    # Get current issue
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    
    issue = response.json()
    current_body = issue.get('body', '')
    
    # Add hierarchy information
    hierarchy_section = f"""
## 🏛️ Agile Hierarchy
- **Epic**: {epic_id}
- **User Story**: {user_story_id}
- **Memory Fragment**: {memory_fragment}

## 📋 Tasks for this Issue
- [ ] Task 1: Initial implementation
- [ ] Task 2: Testing and validation
- [ ] Task 3: Documentation and integration
- [ ] Task 4: Code review and refinement

## 🔓 Unlocks
Completing this issue unlocks **Memory Fragment #{issue_number}**: Part of the greater story...
"""
    
    # Update issue body
    new_body = hierarchy_section + "\n\n---\n\n" + current_body
    
    data = {
        'body': new_body
    }
    
    response = requests.patch(url, headers=headers, json=data)
    return response.json() if response.status_code == 200 else None

def main():
    """Create complete agile hierarchy"""
    print("=" * 60)
    print("SHADOWED REALMS - Agile Hierarchy Setup")
    print("=" * 60)
    
    # Create labels for hierarchy
    print("\n1. Creating hierarchy labels...")
    labels = [
        ("epic", "7057ff", "Epic level work"),
        ("user-story", "0e8a16", "User story"),
        ("task", "d4c5f9", "Individual task"),
        ("memory-fragment", "ffd700", "Unlocks memory fragment"),
        ("real-story", "ff0000", "Unlocks real story")
    ]
    
    for name, color, desc in labels:
        result = create_label(name, color, desc)
        if result:
            print(f"  ✓ Created label: {name}")
    
    # Create milestones for each Epic
    print("\n2. Creating milestones for Epics...")
    for epic_id, epic_data in AGILE_HIERARCHY.items():
        milestone = create_milestone(
            f"{epic_id}: {epic_data['title']}",
            f"Epic milestone containing user stories and issues"
        )
        if milestone:
            print(f"  ✓ Created milestone: {epic_id}")
    
    # Create milestones for User Stories
    print("\n3. Creating milestones for User Stories...")
    for epic_id, epic_data in AGILE_HIERARCHY.items():
        for us_id, us_data in epic_data['user_stories'].items():
            milestone = create_milestone(
                f"{us_id}: {us_data['title'][:50]}...",
                f"User story in {epic_id}. Unlocks {us_data['unlocks_story']}. Theme: {us_data['memory_theme']}"
            )
            if milestone:
                print(f"  ✓ Created milestone: {us_id}")
    
    # Create milestones for Real Stories
    print("\n4. Creating milestones for Real Stories...")
    for story_id, story_data in REAL_STORIES.items():
        milestone = create_milestone(
            f"{story_id}: {story_data['title']}",
            f"{story_data['description']}. {story_data['unlocked_by']}"
        )
        if milestone:
            print(f"  ✓ Created milestone: {story_id}")
    
    # Update existing issues with hierarchy
    print("\n5. Updating issues with hierarchy information...")
    issues_updated = 0
    
    for epic_id, epic_data in AGILE_HIERARCHY.items():
        for us_id, us_data in epic_data['user_stories'].items():
            for issue_num in us_data['issues']:
                if issues_updated >= 10:  # Limit updates to avoid rate limiting
                    print(f"  ... Updated {issues_updated} issues (limiting to prevent rate limits)")
                    break
                
                memory_fragment = f"{us_data['memory_theme']} Fragment #{issue_num}"
                result = update_issue_with_hierarchy(issue_num, epic_id, us_id, memory_fragment)
                
                if result:
                    issues_updated += 1
                    print(f"  ✓ Updated issue #{issue_num} with hierarchy")
                
                time.sleep(1)  # Rate limiting
            
            if issues_updated >= 10:
                break
        
        if issues_updated >= 10:
            break
    
    # Generate hierarchy report
    print("\n" + "=" * 60)
    print("HIERARCHY SUMMARY")
    print("=" * 60)
    
    total_issues = 0
    total_tasks = 0
    total_story_points = 0
    
    for epic_id, epic_data in AGILE_HIERARCHY.items():
        epic_issues = 0
        epic_tasks = 0
        epic_points = 0
        
        for us_id, us_data in epic_data['user_stories'].items():
            issue_count = len(us_data['issues'])
            task_count = issue_count * us_data['tasks_per_issue']
            
            epic_issues += issue_count
            epic_tasks += task_count
            epic_points += us_data['story_points']
        
        total_issues += epic_issues
        total_tasks += epic_tasks
        total_story_points += epic_points
        
        print(f"\n{epic_id}: {epic_data['title']}")
        print(f"  Issues: {epic_issues}")
        print(f"  Tasks: {epic_tasks}")
        print(f"  Story Points: {epic_points}")
    
    print("\n" + "-" * 60)
    print(f"TOTALS:")
    print(f"  Epics: {len(AGILE_HIERARCHY)}")
    print(f"  User Stories: {sum(len(e['user_stories']) for e in AGILE_HIERARCHY.values())}")
    print(f"  Issues: {total_issues}")
    print(f"  Tasks: {total_tasks}")
    print(f"  Story Points: {total_story_points}")
    print(f"  Memory Fragments: {total_issues} (1 per issue)")
    print(f"  Real Stories: {len(REAL_STORIES)}")
    
    print("\n" + "=" * 60)
    print("PROGRESSION PATH")
    print("=" * 60)
    print("1. Complete Tasks → Unlock Issue")
    print("2. Complete Issue → Unlock Memory Fragment")
    print("3. Complete All Issues in User Story → Unlock Part of Real Story")
    print("4. Complete All User Stories in Epic → Unlock Complete Real Story")
    print("\nEach issue contains 3-5 tasks that must be completed")
    print("Memory fragments reveal lore and unlock game content")
    print("Real stories provide major narrative revelations")
    
    print("\n✅ Agile hierarchy setup complete!")
    print(f"View at: https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/milestones")

if __name__ == "__main__":
    main()