#!/usr/bin/env python3
"""
Create time-based sprint system with dynamic issue allocation
1 Sprint = 1 Week = 20 hours of effort
Hierarchy: Org → Project → Repo → Agile → Sprint → Epic → User Story → Issue → Task
"""

import json

# Issue effort mapping (in hours)
ISSUE_EFFORT = {
    # Pre-Sprint 1: Documentation (Issues 1-100) - Quick docs
    **{i: 0.5 for i in range(1, 51)},      # Issues 1-50: 30min each (light docs)
    **{i: 1.0 for i in range(51, 101)},    # Issues 51-100: 1hr each (detailed docs)
    
    # Core Systems (Issues 101-260) - Medium complexity
    **{i: 2.0 for i in range(101, 181)},   # Issues 101-180: 2hrs each (movement)
    **{i: 2.5 for i in range(181, 261)},   # Issues 181-260: 2.5hrs each (inventory)
    
    # Combat Framework (Issues 261-420) - High complexity
    **{i: 3.0 for i in range(261, 341)},   # Issues 261-340: 3hrs each (melee)
    **{i: 3.5 for i in range(341, 421)},   # Issues 341-420: 3.5hrs each (magic)
    
    # Environment System (Issues 421-580) - Medium-high
    **{i: 2.5 for i in range(421, 501)},   # Issues 421-500: 2.5hrs each
    **{i: 2.0 for i in range(501, 581)},   # Issues 501-580: 2hrs each
    
    # Character System (Issues 581-640, 761-820) - Medium
    **{i: 1.5 for i in range(581, 641)},   # Issues 581-640: 1.5hrs each
    **{i: 2.0 for i in range(761, 821)},   # Issues 761-820: 2hrs each
    
    # UI/UX (Issues 641-760) - Light-medium
    **{i: 1.0 for i in range(641, 721)},   # Issues 641-720: 1hr each
    **{i: 1.5 for i in range(721, 761)},   # Issues 721-760: 1.5hrs each
    
    # Save System (Issues 821-900) - Complex
    **{i: 3.0 for i in range(821, 881)},   # Issues 821-880: 3hrs each
    **{i: 2.0 for i in range(881, 901)},   # Issues 881-900: 2hrs each
    
    # Audio & Polish (Issues 901-1000) - Variable
    **{i: 1.0 for i in range(901, 961)},   # Issues 901-960: 1hr each
    **{i: 0.5 for i in range(961, 1001)},  # Issues 961-1000: 30min each (polish)
}

def allocate_sprints(max_hours_per_sprint=20):
    """Allocate issues to sprints based on 20-hour weeks"""
    sprints = []
    current_sprint = {
        'number': 1,
        'issues': [],
        'total_hours': 0,
        'week': 1
    }
    
    for issue_num in range(1, 1001):
        effort = ISSUE_EFFORT.get(issue_num, 1.0)
        
        # If adding this issue would exceed sprint capacity, start new sprint
        if current_sprint['total_hours'] + effort > max_hours_per_sprint:
            sprints.append(current_sprint)
            current_sprint = {
                'number': len(sprints) + 1,
                'issues': [],
                'total_hours': 0,
                'week': len(sprints) + 1
            }
        
        current_sprint['issues'].append(issue_num)
        current_sprint['total_hours'] += effort
    
    # Add the last sprint
    if current_sprint['issues']:
        sprints.append(current_sprint)
    
    return sprints

def generate_sprint_report():
    """Generate comprehensive sprint allocation report"""
    sprints = allocate_sprints()
    
    report = {
        'organization': 'michael-placeholder',
        'project': 'Shadowed Realms RPG Development',
        'repository': 'shadowed-realms',
        'methodology': 'Agile Scrum',
        'sprint_duration': '1 week (20 hours)',
        'total_sprints': len(sprints),
        'total_weeks': len(sprints),
        'total_hours': sum(s['total_hours'] for s in sprints),
        'sprints': []
    }
    
    for sprint in sprints:
        # Determine which epics this sprint covers
        epics_covered = set()
        user_stories_covered = set()
        
        for issue in sprint['issues']:
            if issue <= 100:
                epics_covered.add('EPIC-001: Ideation & Documentation')
                if issue <= 50:
                    user_stories_covered.add('US-001: Documentation')
                else:
                    user_stories_covered.add('US-002: Project Structure')
            elif issue <= 260:
                epics_covered.add('EPIC-002: Core Systems')
                if issue <= 180:
                    user_stories_covered.add('US-003: Movement')
                else:
                    user_stories_covered.add('US-004: Inventory')
            elif issue <= 420:
                epics_covered.add('EPIC-003: Combat Framework')
                if issue <= 340:
                    user_stories_covered.add('US-005: Melee Combat')
                else:
                    user_stories_covered.add('US-006: Magic System')
            elif issue <= 580:
                epics_covered.add('EPIC-004: Environment System')
                if issue <= 500:
                    user_stories_covered.add('US-007: Environments')
                else:
                    user_stories_covered.add('US-008: Weather')
            elif issue <= 640 or (761 <= issue <= 820):
                epics_covered.add('EPIC-005: Character System')
                if issue <= 640:
                    user_stories_covered.add('US-009: Customization')
                else:
                    user_stories_covered.add('US-010: Progression')
            elif issue <= 760:
                epics_covered.add('EPIC-006: UI/UX Framework')
                if issue <= 720:
                    user_stories_covered.add('US-011: UI Design')
                else:
                    user_stories_covered.add('US-012: HUD')
            elif issue <= 900:
                epics_covered.add('EPIC-007: Save System')
                if issue <= 880:
                    user_stories_covered.add('US-013: Save/Load')
                else:
                    user_stories_covered.add('US-014: Cloud Saves')
            else:
                epics_covered.add('EPIC-008: Audio & Polish')
                if issue <= 960:
                    user_stories_covered.add('US-015: Audio')
                else:
                    user_stories_covered.add('US-016: Polish')
        
        sprint_data = {
            'sprint_number': sprint['number'],
            'week': sprint['week'],
            'hours': round(sprint['total_hours'], 1),
            'issue_count': len(sprint['issues']),
            'issue_range': f"{sprint['issues'][0]}-{sprint['issues'][-1]}",
            'tasks_range': f"{(sprint['issues'][0]-1)*4+1}-{sprint['issues'][-1]*4}",
            'epics': list(epics_covered),
            'user_stories': list(user_stories_covered),
            'velocity': len(sprint['issues']) / 5,  # Issues per day (5 days/week)
            'completion_percentage': round((sprint['issues'][-1] / 1000) * 100, 1)
        }
        
        report['sprints'].append(sprint_data)
    
    return report

def create_sprint_dashboard_html():
    """Create HTML dashboard showing time-based sprints"""
    report = generate_sprint_report()
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shadowed Realms - Time-Based Sprint System</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            background: linear-gradient(135deg, #1a1a2e, #0f0f1e);
            color: #e0e0e0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            padding: 30px;
            background: rgba(107, 70, 193, 0.1);
            border-radius: 12px;
            margin-bottom: 30px;
            border: 2px solid #6b46c1;
        }}
        
        h1 {{
            font-size: 2.5rem;
            color: #ffd700;
            margin-bottom: 10px;
        }}
        
        .hierarchy {{
            font-size: 1.1rem;
            color: #87ceeb;
            margin: 15px 0;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: rgba(42, 42, 42, 0.9);
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #ffd700;
            text-align: center;
        }}
        
        .stat-value {{
            font-size: 2rem;
            color: #ffd700;
            font-weight: bold;
        }}
        
        .stat-label {{
            color: #a0a0a0;
            margin-top: 5px;
        }}
        
        .sprints-container {{
            background: rgba(20, 20, 20, 0.8);
            border-radius: 12px;
            padding: 20px;
            max-height: 600px;
            overflow-y: auto;
        }}
        
        .sprint-card {{
            background: rgba(42, 42, 42, 0.9);
            border: 1px solid #6b46c1;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }}
        
        .sprint-card:hover {{
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(107, 70, 193, 0.3);
        }}
        
        .sprint-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        
        .sprint-number {{
            font-size: 1.3rem;
            color: #ffd700;
            font-weight: bold;
        }}
        
        .sprint-week {{
            background: #6b46c1;
            padding: 5px 15px;
            border-radius: 20px;
            color: white;
        }}
        
        .sprint-details {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin-bottom: 10px;
        }}
        
        .detail-item {{
            background: rgba(0, 0, 0, 0.3);
            padding: 8px;
            border-radius: 4px;
        }}
        
        .detail-label {{
            color: #87ceeb;
            font-size: 0.85rem;
        }}
        
        .detail-value {{
            color: #ffffff;
            font-weight: bold;
        }}
        
        .epics-list {{
            margin-top: 10px;
            padding-top: 10px;
            border-top: 1px solid #444;
        }}
        
        .epic-tag {{
            display: inline-block;
            background: rgba(107, 70, 193, 0.3);
            padding: 3px 10px;
            border-radius: 12px;
            margin: 3px;
            font-size: 0.85rem;
            color: #e0e0e0;
        }}
        
        .progress-bar {{
            background: rgba(0, 0, 0, 0.3);
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }}
        
        .progress-fill {{
            background: linear-gradient(90deg, #6b46c1, #ffd700);
            height: 100%;
            transition: width 0.3s ease;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>⚔️ Shadowed Realms - Time-Based Sprint System ⚔️</h1>
            <div class="hierarchy">
                Organization → Project → Repository → Agile → Sprint → Epic → User Story → Issue → Task
            </div>
            <div class="hierarchy">
                <strong>{report['organization']}</strong> → 
                <strong>{report['project']}</strong> → 
                <strong>{report['repository']}</strong>
            </div>
            <div style="color: #4caf50; margin-top: 10px;">
                ⏱️ 1 Sprint = 1 Week = 20 Hours of Effort
            </div>
        </div>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{report['total_sprints']}</div>
                <div class="stat-label">Total Sprints</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{report['total_weeks']}</div>
                <div class="stat-label">Weeks to Complete</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{report['total_hours']:.0f}</div>
                <div class="stat-label">Total Hours</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">1000</div>
                <div class="stat-label">Total Issues</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">4000</div>
                <div class="stat-label">Total Tasks</div>
            </div>
        </div>
        
        <h2 style="color: #ffd700; margin-bottom: 20px;">📅 Sprint Schedule (Ascending Order)</h2>
        
        <div class="sprints-container">
"""
    
    for sprint in report['sprints'][:20]:  # Show first 20 sprints
        progress = sprint['completion_percentage']
        html += f"""
            <div class="sprint-card">
                <div class="sprint-header">
                    <div class="sprint-number">Sprint {sprint['sprint_number']}</div>
                    <div class="sprint-week">Week {sprint['week']}</div>
                </div>
                
                <div class="sprint-details">
                    <div class="detail-item">
                        <div class="detail-label">Issues</div>
                        <div class="detail-value">{sprint['issue_range']}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Tasks</div>
                        <div class="detail-value">{sprint['tasks_range']}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Hours</div>
                        <div class="detail-value">{sprint['hours']}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Issue Count</div>
                        <div class="detail-value">{sprint['issue_count']}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Daily Velocity</div>
                        <div class="detail-value">{sprint['velocity']:.1f}</div>
                    </div>
                    <div class="detail-item">
                        <div class="detail-label">Progress</div>
                        <div class="detail-value">{progress}%</div>
                    </div>
                </div>
                
                <div class="epics-list">
                    <strong style="color: #87ceeb;">Epics:</strong>
                    {''.join([f'<span class="epic-tag">{epic.split(":")[0]}</span>' for epic in sprint['epics']])}
                </div>
                
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {progress}%"></div>
                </div>
            </div>
"""
    
    html += """
        </div>
    </div>
</body>
</html>"""
    
    return html

def main():
    """Generate time-based sprint system"""
    print("=" * 60)
    print("SHADOWED REALMS - Time-Based Sprint System")
    print("=" * 60)
    
    report = generate_sprint_report()
    
    print(f"\nOrganization: {report['organization']}")
    print(f"Project: {report['project']}")
    print(f"Repository: {report['repository']}")
    print(f"Methodology: {report['methodology']}")
    print(f"\nSprint Duration: {report['sprint_duration']}")
    print(f"Total Sprints: {report['total_sprints']}")
    print(f"Total Weeks: {report['total_weeks']}")
    print(f"Total Hours: {report['total_hours']:.0f}")
    
    print("\n" + "=" * 60)
    print("FIRST 10 SPRINTS (ASCENDING ORDER)")
    print("=" * 60)
    
    for sprint in report['sprints'][:10]:
        print(f"\nSprint {sprint['sprint_number']} (Week {sprint['week']}):")
        print(f"  Issues: {sprint['issue_range']} ({sprint['issue_count']} issues)")
        print(f"  Tasks: {sprint['tasks_range']}")
        print(f"  Hours: {sprint['hours']}")
        print(f"  Epics: {', '.join([e.split(':')[0] for e in sprint['epics']])}")
        print(f"  Progress: {sprint['completion_percentage']}%")
    
    # Save report as JSON
    with open('sprint_allocation.json', 'w') as f:
        json.dump(report, f, indent=2)
    
    # Save HTML dashboard
    html = create_sprint_dashboard_html()
    with open('docs/sprint_schedule.html', 'w') as f:
        f.write(html)
    
    print("\n" + "=" * 60)
    print("✅ Sprint allocation complete!")
    print("✅ Dynamic time-based system (20 hours per week)")
    print("✅ All hierarchies in ascending order")
    print(f"✅ Report saved to: sprint_allocation.json")
    print(f"✅ Dashboard saved to: docs/sprint_schedule.html")
    print("=" * 60)

if __name__ == "__main__":
    main()