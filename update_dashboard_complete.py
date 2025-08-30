#!/usr/bin/env python3
"""
Update dashboard with:
1. Issues in ascending order (1, 2, 3...)
2. Task hierarchy (Issues contain Tasks)
3. Epic completion rewards
4. Sprint Day 1 start
5. Memory fragments per issue
"""

import re

# Read current HTML
with open('/Users/j-ashiedu/applicant_prime/__project_pivot/docs/index.html', 'r') as f:
    html = f.read()

# 1. Add Epic Rewards CSS
epic_rewards_css = """
        /* Epic Rewards */
        .epic-rewards {
            background: linear-gradient(135deg, rgba(107, 70, 193, 0.1), rgba(255, 215, 0, 0.1));
            border: 2px solid var(--garden-gold);
            border-radius: 12px;
            padding: 25px;
            margin: 30px 0;
            box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
        }
        
        .epic-rewards-header {
            font-family: 'Cinzel', serif;
            font-size: 1.8rem;
            color: var(--garden-gold);
            text-align: center;
            margin-bottom: 25px;
            text-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
        }
        
        .epic-reward-list {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }
        
        .epic-reward {
            background: rgba(10, 10, 10, 0.9);
            border: 1px solid var(--abstract-purple);
            border-radius: 8px;
            padding: 15px;
            transition: all 0.3s ease;
        }
        
        .epic-reward:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(107, 70, 193, 0.3);
        }
        
        .epic-name {
            color: var(--ember-orange);
            font-weight: bold;
            margin-bottom: 8px;
        }
        
        .reward-value {
            color: var(--garden-gold);
            font-size: 1.1rem;
            margin-bottom: 8px;
        }
        
        .reward-status {
            padding: 5px 10px;
            border-radius: 15px;
            display: inline-block;
            font-size: 0.9rem;
        }
        
        .reward-status.locked {
            background: rgba(139, 0, 0, 0.3);
            color: #ff6b6b;
            border: 1px solid #ff6b6b;
        }
        
        .reward-status.unlocked {
            background: rgba(76, 175, 80, 0.3);
            color: var(--estus-green);
            border: 1px solid var(--estus-green);
            animation: pulse 2s infinite;
        }
        
        .total-epic-value {
            text-align: center;
            font-size: 1.3rem;
            color: var(--soul-blue);
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid var(--abstract-purple);
        }
        
        .reward-total {
            color: var(--garden-gold);
            font-weight: bold;
            font-size: 1.5rem;
        }
        
        .task-hierarchy {
            background: rgba(107, 70, 193, 0.1);
            padding: 10px;
            border-radius: 4px;
            margin: 10px 0;
            border-left: 3px solid var(--abstract-purple);
        }
        
        .task-checklist {
            list-style: none;
            padding: 0;
            margin: 5px 0 0 15px;
        }
        
        .task-checklist li {
            padding: 3px 0;
            color: var(--soul-blue);
            font-size: 0.9rem;
        }
        
        .task-label.memory {
            background: linear-gradient(135deg, #6b46c1, #ffd700);
            color: white;
            font-weight: bold;
        }
        
        .task-explanation {
            color: var(--soul-blue);
            font-size: 0.95rem;
            margin-bottom: 20px;
            padding: 10px;
            background: rgba(0, 0, 0, 0.3);
            border-radius: 4px;
            border-left: 3px solid var(--soul-blue);
        }
"""

# Insert Epic Rewards CSS before Connection Status
html = html.replace("        /* Connection Status */", epic_rewards_css + "\n        /* Connection Status */")

# 2. Add Epic Rewards HTML section
epic_rewards_html = """
        <!-- Epic Rewards Section -->
        <div class="epic-rewards">
            <h3 class="epic-rewards-header">🏆 Epic Completion Rewards</h3>
            <div class="epic-reward-list">
                <div class="epic-reward" id="epic-1-reward">
                    <div class="epic-name">EPIC-001: Ideation & Documentation</div>
                    <div class="reward-value">🎫 Tokyo Game Show Trip ($3,500)</div>
                    <div class="reward-status locked">🔒 Locked (0/100 issues)</div>
                </div>
                <div class="epic-reward" id="epic-2-reward">
                    <div class="epic-name">EPIC-002: Core Systems</div>
                    <div class="reward-value">💻 Mac Studio M2 Ultra ($6,999)</div>
                    <div class="reward-status locked">🔒 Locked (0/160 issues)</div>
                </div>
                <div class="epic-reward" id="epic-3-reward">
                    <div class="epic-name">EPIC-003: Combat Framework</div>
                    <div class="reward-value">🎮 Full Gaming Setup ($5,000)</div>
                    <div class="reward-status locked">🔒 Locked (0/160 issues)</div>
                </div>
                <div class="epic-reward" id="epic-4-reward">
                    <div class="epic-name">EPIC-004: Environment System</div>
                    <div class="reward-value">🎨 Wacom Cintiq Pro 32 ($3,500)</div>
                    <div class="reward-status locked">🔒 Locked (0/160 issues)</div>
                </div>
                <div class="epic-reward" id="epic-5-reward">
                    <div class="epic-name">EPIC-005: Character System</div>
                    <div class="reward-value">📚 MasterClass All-Access + Books ($2,000)</div>
                    <div class="reward-status locked">🔒 Locked (0/120 issues)</div>
                </div>
                <div class="epic-reward" id="epic-6-reward">
                    <div class="epic-name">EPIC-006: UI/UX Framework</div>
                    <div class="reward-value">🖥️ Triple Monitor Setup ($2,500)</div>
                    <div class="reward-status locked">🔒 Locked (0/120 issues)</div>
                </div>
                <div class="epic-reward" id="epic-7-reward">
                    <div class="epic-name">EPIC-007: Save System</div>
                    <div class="reward-value">☁️ 5-Year Cloud Services ($2,000)</div>
                    <div class="reward-status locked">🔒 Locked (0/80 issues)</div>
                </div>
                <div class="epic-reward" id="epic-8-reward">
                    <div class="epic-name">EPIC-008: Audio & Polish</div>
                    <div class="reward-value">🎵 Professional Audio Studio ($4,000)</div>
                    <div class="reward-status locked">🔒 Locked (0/100 issues)</div>
                </div>
            </div>
            <div class="total-epic-value">
                Total Epic Rewards Value: <span class="reward-total">$31,499</span>
            </div>
        </div>
        
"""

# Insert Epic Rewards HTML before Tasks Container
tasks_container_pattern = r'(        <!-- Enhanced Tasks Container -->)'
html = re.sub(tasks_container_pattern, epic_rewards_html + r'\1', html)

# 3. Update Tasks Container title to Task Picker
html = html.replace(
    '<h2 class="tasks-header">Available Quests with Deliverables</h2>',
    '<h2 class="tasks-header">Task Picker - Complete Tasks to Unlock Issues</h2>\n            <div class="task-explanation">Each issue contains 3-5 tasks. Complete all tasks to unlock the issue, earn rewards, and reveal a memory fragment!</div>'
)

# 4. Fix Sprint Day to Day 1
html = re.sub(
    r"const startDate = new Date\('2025-08-01'\);",
    "const startDate = new Date(); // Sprint starts today",
    html
)

html = re.sub(
    r"const daysPassed = Math\.floor\(\(today - startDate\) / \(1000 \* 60 \* 60 \* 24\)\);",
    "const daysPassed = 1; // Day 1 of Sprint",
    html
)

# 5. Add Epic Rewards update function
epic_rewards_js = """
        function updateEpicRewards(closedIssues) {
            // Epic 1: Issues 1-100
            const epic1Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return num >= 1 && num <= 100;
            }).length;
            
            // Epic 2: Issues 101-260
            const epic2Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return num >= 101 && num <= 260;
            }).length;
            
            // Epic 3: Issues 261-420
            const epic3Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return num >= 261 && num <= 420;
            }).length;
            
            // Epic 4: Issues 421-580
            const epic4Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return num >= 421 && num <= 580;
            }).length;
            
            // Epic 5: Issues 581-640 + 761-820
            const epic5Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return (num >= 581 && num <= 640) || (num >= 761 && num <= 820);
            }).length;
            
            // Epic 6: Issues 641-760
            const epic6Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return num >= 641 && num <= 760;
            }).length;
            
            // Epic 7: Issues 821-900
            const epic7Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return num >= 821 && num <= 900;
            }).length;
            
            // Epic 8: Issues 901-1000
            const epic8Closed = closedIssues.filter(i => {
                const num = parseInt(i.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return num >= 901 && num <= 1000;
            }).length;
            
            // Update reward statuses
            updateEpicRewardStatus(1, epic1Closed, 100);
            updateEpicRewardStatus(2, epic2Closed, 160);
            updateEpicRewardStatus(3, epic3Closed, 160);
            updateEpicRewardStatus(4, epic4Closed, 160);
            updateEpicRewardStatus(5, epic5Closed, 120);
            updateEpicRewardStatus(6, epic6Closed, 120);
            updateEpicRewardStatus(7, epic7Closed, 80);
            updateEpicRewardStatus(8, epic8Closed, 100);
        }
        
        function updateEpicRewardStatus(epicNum, closed, total) {
            const statusEl = document.querySelector(`#epic-${epicNum}-reward .reward-status`);
            if (statusEl) {
                if (closed >= total) {
                    statusEl.className = 'reward-status unlocked';
                    statusEl.textContent = `🎉 UNLOCKED! Claim your reward!`;
                } else {
                    statusEl.className = 'reward-status locked';
                    statusEl.textContent = `🔒 Locked (${closed}/${total} issues)`;
                }
            }
        }

"""

# Insert Epic Rewards JS before updateMemoryFragments
html = re.sub(
    r'(        function updateMemoryFragments)',
    epic_rewards_js + r'\1',
    html
)

# 6. Update processIssues to sort in ascending order and call updateEpicRewards
process_issues_update = """
            // Sort issues in ascending order by issue number
            openIssues.sort((a, b) => {
                const numA = parseInt(a.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                const numB = parseInt(b.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                return numA - numB;
            });
            
            // Display tasks with enhanced information (show first 10 in ascending order)
            displayTasksWithHierarchy(openIssues.slice(0, 10));
            
            // Update epic rewards
            updateEpicRewards(closedIssues);"""

html = re.sub(
    r'            // Display tasks with enhanced information\n            displayEnhancedTasks\(openIssues\.slice\(0, 10\)\);',
    process_issues_update,
    html
)

# 7. Update displayEnhancedTasks to displayTasksWithHierarchy
display_tasks_update = """
        function displayTasksWithHierarchy(issues) {
            const taskList = document.getElementById('task-list');
            
            if (issues.length === 0) {
                taskList.innerHTML = '<div class="loading">No open issues available</div>';
                return;
            }
            
            taskList.innerHTML = issues.map(issue => {
                const issueNum = parseInt(issue.title.match(/\\[ISSUE-(\\d+)\\]/)?.[1] || 0);
                const startTaskNum = (issueNum - 1) * 4 + 1;
                const endTaskNum = startTaskNum + 3;
                
                const xp = extractXPFromLabels(issue.labels);
                const coins = extractCoinsFromLabels(issue.labels);
                const revenue = coins * 10;
                
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
                
                // Generate tasks for this issue
                const tasks = [
                    `Task ${startTaskNum}: Initial implementation`,
                    `Task ${startTaskNum + 1}: Testing and validation`,
                    `Task ${startTaskNum + 2}: Documentation`,
                    `Task ${startTaskNum + 3}: Integration`
                ];
                
                return `
                    <div class="task-item" onclick="window.open('${issue.html_url}', '_blank')">
                        <div class="task-title">${issue.title}</div>
                        <div class="task-hierarchy">
                            <strong>Tasks to complete (${startTaskNum}-${endTaskNum}):</strong>
                            <ul class="task-checklist">
                                ${tasks.map(t => `<li>☐ ${t}</li>`).join('')}
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
                            <span class="task-label memory">🔮 Unlocks Memory #${issueNum}</span>
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

# Replace displayEnhancedTasks function
html = re.sub(
    r'        function displayEnhancedTasks\(tasks\) \{[\s\S]*?\n        \}',
    display_tasks_update,
    html,
    count=1
)

# Save updated HTML
with open('/Users/j-ashiedu/applicant_prime/__project_pivot/docs/index.html', 'w') as f:
    f.write(html)

print("Dashboard updated successfully!")
print("✅ Issues now display in ascending order (1, 2, 3...)")
print("✅ Task hierarchy shown (Issues contain Tasks)")
print("✅ Epic completion rewards added ($31,499 total value)")
print("✅ Sprint set to Day 1")
print("✅ Memory fragments unlock per issue")
print("\nView at: https://michael-placeholder.github.io/shadowed-realms/")