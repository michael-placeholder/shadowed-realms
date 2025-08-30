#!/usr/bin/env python3
"""
Create remaining Sprint 1 issues (601-1000) for Shadowed Realms RPG
Includes proper deliverables, monetary value explanations, and XP justifications
"""

import os
import json
import time
import requests
from typing import List, Dict

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

def check_existing_issues():
    """Check which issues already exist"""
    existing = set()
    page = 1
    while True:
        response = requests.get(
            f'{GITHUB_API_URL}/issues?state=all&per_page=100&page={page}',
            headers=headers
        )
        issues = response.json()
        if not issues:
            break
        
        for issue in issues:
            if '[ISSUE-' in issue['title']:
                num = issue['title'].split('[ISSUE-')[1].split(']')[0]
                try:
                    existing.add(int(num))
                except:
                    pass
        page += 1
    
    return existing

def generate_remaining_sprint1_issues():
    """Generate remaining Sprint 1 issues (601-1000) with deliverables"""
    
    issues = []
    
    # Environment System Continued (601-640)
    for i in range(601, 641):
        if i <= 610:
            issues.append({
                'num': i,
                'title': f'Create weather system component {i-600}',
                'deliverable': f'weather_component_{i-600}.cs script file',
                'type': 'weather-system',
                'xp': 200,
                'coins': 100,
                'value': 'Weather effects increase immersion, worth $2,000 in environmental assets'
            })
        elif i <= 620:
            issues.append({
                'num': i,
                'title': f'Design dynamic lighting setup {i-610}',
                'deliverable': f'lighting_setup_{i-610}.unity scene with configured lights',
                'type': 'lighting',
                'xp': 250,
                'coins': 125,
                'value': 'Professional lighting adds $3,000 value to environment pack'
            })
        elif i <= 630:
            issues.append({
                'num': i,
                'title': f'Create fog and atmosphere effect {i-620}',
                'deliverable': f'atmosphere_{i-620}.mat material with shader',
                'type': 'atmosphere',
                'xp': 175,
                'coins': 85,
                'value': 'Atmospheric effects crucial for Dark Souls aesthetic'
            })
        else:
            issues.append({
                'num': i,
                'title': f'Optimize environment LODs {i-630}',
                'deliverable': f'LOD_settings_{i-630}.asset configuration file',
                'type': 'optimization',
                'xp': 150,
                'coins': 75,
                'value': 'LOD optimization ensures 60FPS, critical for positive reviews'
            })
    
    # UI/UX Systems (641-780)
    for i in range(641, 781):
        if i <= 680:
            issues.append({
                'num': i,
                'title': f'Design UI element {i-640}',
                'deliverable': f'ui_element_{i-640}.png with transparency',
                'type': 'ui-design',
                'xp': 100,
                'coins': 50,
                'value': f'UI assets sell for $45-95 per pack, element {i-640} contributes'
            })
        elif i <= 720:
            issues.append({
                'num': i,
                'title': f'Create menu screen {i-680}',
                'deliverable': f'menu_screen_{i-680}.prefab Unity prefab',
                'type': 'ui-screens',
                'xp': 150,
                'coins': 75,
                'value': 'Complete menu systems worth $125 on asset store'
            })
        elif i <= 760:
            issues.append({
                'num': i,
                'title': f'Implement UI animation {i-720}',
                'deliverable': f'ui_animation_{i-720}.anim animation file',
                'type': 'ui-animation',
                'xp': 125,
                'coins': 60,
                'value': 'Animated UI increases perceived quality, supports premium pricing'
            })
        else:
            issues.append({
                'num': i,
                'title': f'Create HUD component {i-760}',
                'deliverable': f'hud_component_{i-760}.cs with visual prefab',
                'type': 'hud',
                'xp': 175,
                'coins': 85,
                'value': 'HUD systems essential for gameplay, drives game sales ($197/copy)'
            })
    
    # Save System (781-900)
    for i in range(781, 901):
        if i <= 820:
            issues.append({
                'num': i,
                'title': f'Implement save data structure {i-780}',
                'deliverable': f'save_data_{i-780}.cs serializable class',
                'type': 'save-data',
                'xp': 200,
                'coins': 100,
                'value': 'Save system worth $150 as standalone asset'
            })
        elif i <= 860:
            issues.append({
                'num': i,
                'title': f'Create save file encryption {i-820}',
                'deliverable': f'encryption_{i-820}.cs security implementation',
                'type': 'save-security',
                'xp': 250,
                'coins': 125,
                'value': 'Secure saves prevent cheating, maintains game integrity'
            })
        else:
            issues.append({
                'num': i,
                'title': f'Build cloud save integration {i-860}',
                'deliverable': f'cloud_save_{i-860}.cs with API integration',
                'type': 'cloud-save',
                'xp': 300,
                'coins': 150,
                'value': 'Cloud saves enable cross-platform play, increases market reach'
            })
    
    # Audio System & Polish (901-1000)
    for i in range(901, 1001):
        if i <= 940:
            issues.append({
                'num': i,
                'title': f'Create sound effect {i-900}',
                'deliverable': f'sfx_{i-900}.wav audio file (44.1kHz)',
                'type': 'audio-sfx',
                'xp': 150,
                'coins': 75,
                'value': 'SFX pack sells for $35-75, each sound adds value'
            })
        elif i <= 970:
            issues.append({
                'num': i,
                'title': f'Compose music track segment {i-940}',
                'deliverable': f'music_segment_{i-940}.ogg loopable track',
                'type': 'audio-music',
                'xp': 250,
                'coins': 125,
                'value': 'Original soundtrack worth $15-25 separately'
            })
        elif i <= 990:
            issues.append({
                'num': i,
                'title': f'Implement audio mixer settings {i-970}',
                'deliverable': f'audio_mixer_{i-970}.mixer Unity audio mixer',
                'type': 'audio-system',
                'xp': 175,
                'coins': 85,
                'value': 'Professional audio mixing essential for quality'
            })
        else:
            issues.append({
                'num': i,
                'title': f'Final polish task {i-990}',
                'deliverable': f'polish_report_{i-990}.md with before/after screenshots',
                'type': 'polish',
                'xp': 200,
                'coins': 100,
                'value': 'Polish determines review scores, directly impacts sales'
            })
    
    return issues

def main():
    """Main function to create remaining Sprint 1 issues"""
    print("=" * 60)
    print("SHADOWED REALMS - Remaining Sprint 1 Issues")
    print("Creating issues 601-1000 with proper deliverables")
    print("=" * 60)
    
    # Check existing issues
    existing_issues = check_existing_issues()
    print(f"Found {len(existing_issues)} existing issues")
    
    # Generate issues
    all_issues = generate_remaining_sprint1_issues()
    
    # Filter out existing
    new_issues = [issue for issue in all_issues if issue['num'] not in existing_issues]
    total_issues = len(new_issues)
    
    print(f"\nNeed to create {total_issues} new issues")
    
    if total_issues == 0:
        print("All remaining Sprint 1 issues already exist!")
        return
    
    created_count = 0
    failed_count = 0
    
    for i, issue_data in enumerate(new_issues, 1):
        issue_num = issue_data['num']
        title = f"[ISSUE-{issue_num:04d}] {issue_data['title']}"
        
        # Determine memory fragment range
        if issue_num <= 640:
            fragment_range = "Fragments 22-28: Environment System Done"
            epic = "EPIC-004: Environment System"
        elif issue_num <= 780:
            fragment_range = "Fragments 29-35: UI/UX Complete"
            epic = "EPIC-008: UI/UX Framework"
        elif issue_num <= 900:
            fragment_range = "Fragments 36-42: Save System Implemented"
            epic = "EPIC-007: Save System & Persistence"
        else:
            fragment_range = "Fragments 43-49: Audio System & Polish"
            epic = "EPIC-009: Audio & Polish"
        
        body = f"""## 🎯 Task Details
**Epic**: {epic}
**Sprint**: Sprint 1 - Foundation & Core Systems
**Issue Number**: {issue_num:04d}

## 📦 Deliverable Requirements
**What you must upload:**
- {issue_data['deliverable']}

**Verification Criteria:**
- [ ] File created and functional
- [ ] Follows project standards
- [ ] Tested and verified working
- [ ] Properly documented
- [ ] Integrated with existing systems

## 💰 Monetary Value Explanation
**Coin Value**: {issue_data['coins']} coins = ${issue_data['coins'] * 10} project value

**Why this value:**
{issue_data['value']}

**Market Context:**
- Similar assets sell for ${issue_data['coins'] * 2} to ${issue_data['coins'] * 4}
- Contributes to revenue stream target of $50,000
- Part of {epic} valued at $10,000+

## 🎮 XP Justification
**XP Value**: {issue_data['xp']} XP

**Why this XP:**
- Task difficulty: {'Advanced' if issue_data['xp'] >= 250 else 'Intermediate' if issue_data['xp'] >= 150 else 'Basic'}
- Skill development in: {issue_data['type']}
- Prerequisites: Previous tasks in this epic
- Unlocks: Next level of complexity

**Skill Mastery Progress:**
- {issue_data['type']} path: +{issue_data['xp'] // 10}% progress
- Contributes to specialist certification

## 🔮 Memory Fragment Progress
**{fragment_range}**

Completing this issue brings you closer to unlocking:
- Lore about the game world
- Technical documentation access
- Market strategy insights

## ✅ Acceptance Criteria
- [ ] Deliverable uploaded to repository
- [ ] Meets quality standards
- [ ] Performance optimized
- [ ] No critical bugs
- [ ] Documentation updated

## 🔗 Dependencies
- Requires: Issues {issue_num - 10} to {issue_num - 1} completed
- Blocks: Issues {issue_num + 1} to {issue_num + 10}
- Related Epic: {epic}

## 📊 Business Impact
- Direct Revenue Impact: ${issue_data['coins'] * 10}
- Asset Store Potential: ${issue_data['coins'] * 20}
- Course Material Value: ${issue_data['coins'] * 5}
- Long-term Value: Reusable in future projects

## 🛠️ Technical Requirements
- Software: Unity 2024.3 LTS / Unreal 5
- Tools: Visual Studio, Git
- Skills: {issue_data['type']}
- Time Estimate: {30 if issue_data['xp'] < 150 else 60 if issue_data['xp'] < 250 else 90} minutes

## 📈 Progress Tracking
- Sprint Progress: {((issue_num - 600) / 400 * 100):.1f}% of remaining Sprint 1
- Overall Progress: {(issue_num / 1000 * 100):.1f}% of Sprint 1 complete
- XP toward next level: {issue_data['xp']} / 1000

---
*Part of Shadowed Realms RPG - Sprint 1*
*Building toward $50,000+ revenue target*
"""
        
        labels = [
            'issue',
            'sprint-1',
            f"xp-{issue_data['xp']}",
            f"coins-{issue_data['coins']}",
            issue_data['type'],
            'deliverable-required'
        ]
        
        print(f"\n[{i}/{total_issues}] Creating: {title}")
        print(f"  Epic: {epic}")
        print(f"  XP: {issue_data['xp']}, Coins: {issue_data['coins']}")
        print(f"  Deliverable: {issue_data['deliverable']}")
        
        result = create_issue(title, body, labels)
        
        if result:
            created_count += 1
            print(f"  ✓ Created successfully (#{result['number']})")
        else:
            failed_count += 1
            print(f"  ✗ Failed to create (likely rate limited)")
        
        # Rate limiting - pause every 3 issues
        if i % 3 == 0:
            print(f"  Pausing for rate limiting...")
            time.sleep(2)
    
    print("\n" + "=" * 60)
    print("SPRINT 1 COMPLETION STATUS")
    print(f"Successfully created: {created_count} issues")
    print(f"Failed (rate limited): {failed_count} issues")
    print("=" * 60)
    
    # Calculate totals for all 1000 issues
    total_xp = 0
    total_coins = 0
    
    # Rough calculation based on ranges
    # Issues 1-160: avg 50 XP, 25 coins
    total_xp += 160 * 50
    total_coins += 160 * 25
    
    # Issues 161-300: avg 150 XP, 75 coins
    total_xp += 140 * 150
    total_coins += 140 * 75
    
    # Issues 301-480: avg 250 XP, 125 coins
    total_xp += 180 * 250
    total_coins += 180 * 125
    
    # Issues 481-640: avg 200 XP, 100 coins
    total_xp += 160 * 200
    total_coins += 160 * 100
    
    # Issues 641-780: avg 150 XP, 75 coins
    total_xp += 140 * 150
    total_coins += 140 * 75
    
    # Issues 781-900: avg 250 XP, 125 coins
    total_xp += 120 * 250
    total_coins += 120 * 125
    
    # Issues 901-1000: avg 200 XP, 100 coins
    total_xp += 100 * 200
    total_coins += 100 * 100
    
    total_value = total_coins * 10
    
    print(f"\nComplete Sprint 1 Totals (All 1000 issues):")
    print(f"Total XP Pool: {total_xp:,}")
    print(f"Total Coins: {total_coins:,}")
    print(f"Total Financial Value: ${total_value:,}")
    print(f"\nMemory Fragments: 1-49 (7 per milestone)")
    print(f"Asset Production Target: 1,666 assets")
    print(f"Revenue Target Progress: ${total_value:,} / $50,000 ({total_value/50000*100:.1f}%)")
    
    if failed_count > 0:
        print(f"\n⚠️ Note: {failed_count} issues failed due to rate limiting.")
        print("Wait 1 hour and run the script again to create remaining issues.")
    
    print(f"\nView issues at: https://github.com/{GITHUB_OWNER}/{GITHUB_REPO}/issues")
    print(f"Dashboard: https://{GITHUB_OWNER}.github.io/{GITHUB_REPO}/")

if __name__ == "__main__":
    main()