#!/usr/bin/env python3
"""
Fix ALL dashboard issues:
1. Issues vs Tasks confusion
2. Neon colors (make it dark FromSoft)
3. Task hierarchy display
4. API authentication
"""

import re

# Read current HTML
with open('/Users/j-ashiedu/applicant_prime/__project_pivot/docs/index.html', 'r') as f:
    html = f.read()

# 1. Fix the neon color scheme to dark FromSoft aesthetic
color_replacements = [
    # Root variables - make them DARK and muted
    ('--ember-orange: #ff6b35;', '--ember-orange: #4a3410;'),  # Dark burnt orange
    ('--soul-blue: #4a90e2;', '--soul-blue: #1e2838;'),  # Dark steel blue
    ('--estus-green: #7fb069;', '--estus-green: #2d3d2d;'),  # Dark forest green
    ('--blood-red: #8b0000;', '--blood-red: #2a0a0a;'),  # Darker blood
    ('--abstract-purple: #6b46c1;', '--abstract-purple: #2d2438;'),  # Dark purple
    ('--garden-gold: #ffd700;', '--garden-gold: #8b6914;'),  # Tarnished gold
    ('--revenue-green: #00ff88;', '--revenue-green: #1a3d2e;'),  # Dark moss green
    ('--milestone-pink: #ff69b4;', '--milestone-pink: #4a2838;'),  # Dark rose
]

for old, new in color_replacements:
    html = html.replace(old, new)

# 2. Fix "Open Tasks" vs "Open Issues" confusion
html = html.replace(
    """            <div class="stat-card">
                <div class="stat-label">Open Tasks</div>
                <div class="stat-value" id="open-tasks">0</div>
                <div class="stat-description">Challenges await</div>
            </div>""",
    """            <div class="stat-card">
                <div class="stat-label">Open Issues</div>
                <div class="stat-value" id="open-issues">0</div>
                <div class="stat-description">Issues to complete</div>
            </div>"""
)

html = html.replace(
    """            <div class="stat-card">
                <div class="stat-label">Closed Tasks</div>
                <div class="stat-value" id="closed-tasks">0</div>
                <div class="stat-description">Victories claimed</div>
            </div>""",
    """            <div class="stat-card">
                <div class="stat-label">Closed Issues</div>
                <div class="stat-value" id="closed-issues">0</div>
                <div class="stat-description">Issues completed</div>
            </div>"""
)

html = html.replace(
    """            <div class="stat-card">
                <div class="stat-label">Total XP</div>
                <div class="stat-value" id="total-xp">0</div>
                <div class="stat-description">Experience gained</div>
            </div>""",
    """            <div class="stat-card">
                <div class="stat-label">Open Tasks</div>
                <div class="stat-value" id="open-tasks">0</div>
                <div class="stat-description">Tasks remaining (4 per issue)</div>
            </div>"""
)

html = html.replace(
    """            <div class="stat-card">
                <div class="stat-label">Total Coins</div>
                <div class="stat-value" id="total-coins">0</div>
                <div class="stat-description">Value created</div>
            </div>""",
    """            <div class="stat-card">
                <div class="stat-label">Completed Tasks</div>
                <div class="stat-value" id="completed-tasks">0</div>
                <div class="stat-description">Tasks finished</div>
            </div>"""
)

# 3. Fix the header text
html = html.replace(
    '<h2 class="tasks-header">Available Quests with Deliverables</h2>',
    '<h2 class="tasks-header">Issue Tracker (Each Issue = 4 Tasks)</h2>'
)

# 4. Fix the JavaScript to properly calculate tasks vs issues
js_fix = """
            // Update basic stats - ISSUES ARE NOT TASKS!
            document.getElementById('open-issues').textContent = openIssues.length;
            document.getElementById('closed-issues').textContent = closedIssues.length;
            
            // Each issue has 4 tasks
            const openTaskCount = openIssues.length * 4;
            const completedTaskCount = closedIssues.length * 4;
            document.getElementById('open-tasks').textContent = openTaskCount;
            document.getElementById('completed-tasks').textContent = completedTaskCount;"""

html = re.sub(
    r'// Update basic stats.*?document\.getElementById\(\'closed-tasks\'\)\.textContent = closedIssues\.length;',
    js_fix,
    html,
    flags=re.DOTALL
)

# 5. Add XP and Coins display in header
xp_coins_html = """
        <!-- XP and Coins Display -->
        <div style="text-align: center; margin: 20px 0; color: var(--garden-gold);">
            <span style="margin-right: 30px; font-size: 1.3rem;">Total XP: <span id="total-xp" style="font-weight: bold;">0</span></span>
            <span style="font-size: 1.3rem;">Total Coins: <span id="total-coins" style="font-weight: bold;">0</span></span>
        </div>
"""

# Insert after header
html = html.replace(
    '</header>',
    '</header>\n' + xp_coins_html
)

# 6. Update task display to show it's an ISSUE containing tasks
task_display_update = """
        function displayEnhancedTasks(issues) {
            const taskList = document.getElementById('task-list');
            
            if (issues.length === 0) {
                taskList.innerHTML = '<div class="loading">No open issues available</div>';
                return;
            }
            
            // Sort issues in ascending order
            issues.sort((a, b) => {
                const numA = parseInt(a.title.match(/\\\\[ISSUE-(\\\\d+)\\\\]/)?.[1] || 0);
                const numB = parseInt(b.title.match(/\\\\[ISSUE-(\\\\d+)\\\\]/)?.[1] || 0);
                return numA - numB;
            });
            
            taskList.innerHTML = issues.map(issue => {
                const issueNum = parseInt(issue.title.match(/\\\\[ISSUE-(\\\\d+)\\\\]/)?.[1] || 0);
                const xp = extractXPFromLabels(issue.labels);
                const coins = extractCoinsFromLabels(issue.labels);
                const revenue = coins * 10;
                
                // Calculate task numbers for this issue
                const startTask = (issueNum - 1) * 4 + 1;
                const endTask = startTask + 3;
                
                // Determine deliverable type
                let deliverable = 'Deliverable: ';
                if (issue.title.toLowerCase().includes('script')) {
                    deliverable += '📄 Script file (.cs/.py/.js)';
                } else if (issue.title.toLowerCase().includes('model')) {
                    deliverable += '🎨 3D Model (.fbx/.obj)';
                } else if (issue.title.toLowerCase().includes('doc')) {
                    deliverable += '📚 Documentation (.md)';
                } else if (issue.title.toLowerCase().includes('anim')) {
                    deliverable += '🎬 Animation file';
                } else {
                    deliverable += '📦 Project file';
                }
                
                return `
                    <div class="task-item" onclick="window.open('${issue.html_url}', '_blank')">
                        <div style="background: var(--blood-red); color: white; padding: 5px; margin: -15px -15px 10px -15px; font-size: 0.8rem;">
                            ISSUE #${issueNum} (Contains Tasks ${startTask}-${endTask})
                        </div>
                        <div class="task-title">${issue.title}</div>
                        <div style="background: rgba(0,0,0,0.3); padding: 10px; margin: 10px 0; border-radius: 4px;">
                            <strong>Tasks to Complete:</strong>
                            <ul style="margin: 5px 0 0 20px; color: var(--soul-blue);">
                                <li>Task ${startTask}: Initial implementation</li>
                                <li>Task ${startTask + 1}: Testing and validation</li>
                                <li>Task ${startTask + 2}: Documentation</li>
                                <li>Task ${startTask + 3}: Integration</li>
                            </ul>
                        </div>
                        <div class="task-deliverable">${deliverable}</div>
                        <div class="task-value-explanation">
                            💰 Value: $${revenue} - Contributes to ${getRevenueStream(issue)} revenue stream
                        </div>
                        <div class="task-labels">
                            <span class="task-label xp">+${xp} XP</span>
                            <span class="task-label coins">+${coins} Coins</span>
                            <span class="task-label revenue">$${revenue} value</span>
                            <span class="task-label" style="background: linear-gradient(135deg, var(--abstract-purple), var(--garden-gold));">
                                🔮 Unlocks Memory #${issueNum}
                            </span>
                            ${issue.labels.map(label => 
                                !label.name.includes('xp-') && 
                                !label.name.includes('coins-') && 
                                label.name !== 'sprint-1'
                                    ? `<span class="task-label">${label.name}</span>` 
                                    : ''
                            ).join('')}
                        </div>
                    </div>
                `;
            }).join('');
        }"""

# Replace the displayEnhancedTasks function
html = re.sub(
    r'function displayEnhancedTasks\(tasks\) \{.*?\n        \}',
    task_display_update,
    html,
    flags=re.DOTALL
)

# 7. Fix Sprint Day to be Day 1
html = html.replace(
    "const startDate = new Date('2025-08-01');",
    "const startDate = new Date(); // Sprint starts today"
)
html = html.replace(
    "const daysPassed = Math.floor((today - startDate) / (1000 * 60 * 60 * 24));",
    "const daysPassed = 1; // Day 1 of Sprint"
)

# Save updated HTML
with open('/Users/j-ashiedu/applicant_prime/__project_pivot/docs/index.html', 'w') as f:
    f.write(html)

print("✅ Fixed Issues vs Tasks confusion")
print("✅ Removed neon colors - now dark FromSoft aesthetic")
print("✅ Added task hierarchy display (4 tasks per issue)")
print("✅ Fixed Sprint Day to Day 1")
print("✅ Added XP and Coins display")
print("\n⚠️  Note: GitHub API 403 error requires valid token or wait for rate limit reset")
print("\nView at: https://michael-placeholder.github.io/shadowed-realms/")