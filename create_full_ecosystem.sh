#!/bin/bash

# Shadowed Realms Full Ecosystem Setup
# This script creates the complete GitHub ecosystem with all issues, project boards, and connections

echo "🎮 SHADOWED REALMS RPG - FULL ECOSYSTEM SETUP"
echo "=============================================="

# Set the fine-grained token
export GH_TOKEN="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"
export GITHUB_TOKEN="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"

# Repository details
OWNER="michael-placeholder"
REPO="shadowed-realms"
FULL_REPO="$OWNER/$REPO"

echo "📋 Creating Issues with Full Gamification System..."

# EPIC-001: Project Setup & Infrastructure
echo "Creating EPIC-001..."
gh issue create \
  --repo "$FULL_REPO" \
  --title "[EPIC-001] Project Setup & Infrastructure" \
  --body "## Epic Title
Project Setup & Infrastructure

## Epic ID
EPIC-001

## Business Value
**Estimated Revenue Impact**: $5,000
**Asset Production**: 50 initial tools and scripts
**Skill Development Areas**: Git, GitHub, Unity, Unreal, Maya, Python

## Description
Establish complete development environment, version control, and project infrastructure for 6-month RPG development

## Success Criteria
- [ ] All development tools installed
- [ ] GitHub repository configured
- [ ] Project board active
- [ ] CI/CD pipeline ready
- [ ] Asset pipeline established

## User Stories
- [ ] USER-STORY-001: Initialize Development Environment
- [ ] USER-STORY-002: Configure Version Control
- [ ] USER-STORY-003: Set Up Build Pipeline
- [ ] USER-STORY-004: Create Asset Management System

## Rewards
- **XP Pool**: 10,000 XP
- **Coin Pool**: 5,000 coins
- **Memory Fragments**: 1-3 (The Beginning, First Steps, Foundation)

## Financial Tracking
\`\`\`
Development Cost: $500
Expected Revenue: $5,000
ROI: 900%
Break-even: 10 asset sales
\`\`\`" \
  --label "epic,sprint-1,xp-10000,coins-5000,memory-unlock"

# USER-STORY-001: Initialize Development Environment
echo "Creating USER-STORY-001..."
gh issue create \
  --repo "$FULL_REPO" \
  --title "[USER-STORY-001] Initialize Development Environment" \
  --body "## User Story
**As a** developer
**I want** a complete development environment
**So that** I can begin RPG and asset development

## Story ID
USER-STORY-001

## Parent Epic
EPIC-001: Project Setup & Infrastructure

## Acceptance Criteria
- [ ] Given a fresh system, when setup is run, then all tools are installed
- [ ] Given installed tools, when versions checked, then all are correct
- [ ] Given environment, when test project created, then it compiles

## Tasks Breakdown
- [ ] TASK-001: Install Core Development Tools
- [ ] TASK-002: Configure Unity Environment
- [ ] TASK-003: Set Up Maya Pipeline
- [ ] TASK-004: Install Supporting Tools

## Rewards
- **XP**: 2,500
- **Coins**: 1,250
- **Unlocks**: Memory Fragment #1 - The Beginning

## Asset Production
- Development Scripts: 5
- Configuration Files: 10
- Documentation: 3 guides" \
  --label "user-story,sprint-1,xp-2500,coins-1250"

# Create granular tasks
echo "Creating granular tasks..."

# TASK-001: Install Core Development Tools
gh issue create \
  --repo "$FULL_REPO" \
  --title "[TASK-001] Install Core Development Tools" \
  --body "## Task Title
Install Core Development Tools

## Task ID
TASK-001

## Parent User Story
USER-STORY-001: Initialize Development Environment

## Implementation Steps
1. Install Python 3.11
2. Install Node.js 20
3. Install Git
4. Install VS Code
5. Configure environment variables

## Issues Breakdown
- [ ] ISSUE-0001: Install Python 3.11
- [ ] ISSUE-0002: Install pip
- [ ] ISSUE-0003: Install Node.js
- [ ] ISSUE-0004: Install npm
- [ ] ISSUE-0005: Install Git

## Rewards
- **XP**: 500
- **Coins**: 250
- **Skill Points**: DevOps +10

## Financial Impact
- Enables: $3,900 worth of development
- Direct value: $0
- Unlock value: Access to all development" \
  --label "task,sprint-1,xp-500,coins-250"

# Create micro-issues
echo "Creating micro-issues..."

# ISSUE-0001: Install Python 3.11
gh issue create \
  --repo "$FULL_REPO" \
  --title "[ISSUE-0001] Install Python 3.11" \
  --body "## Issue Title
Install Python 3.11

## Issue ID
ISSUE-0001

## Parent Task
TASK-001: Install Core Development Tools

## Action Required
Download and install Python 3.11 from python.org

## Command/Code
\`\`\`bash
# macOS
brew install python@3.11

# Or download from
# https://www.python.org/downloads/
\`\`\`

## Expected Output
\`\`\`
Python 3.11.x successfully installed
\`\`\`

## Success Verification
- [ ] Command executes without error
- [ ] python3 --version shows 3.11.x
- [ ] pip3 is available

## Time Estimate
5 minutes

## Rewards
- **XP**: 25
- **Coins**: 10
- **Progress**: 2% toward Python Mastery

## Financial Impact
- Contributes to: Python script development
- Value: Enables $2,000 worth of Python assets
- Market impact: Opens Python tool market" \
  --label "issue,micro-task,xp-25,coins-10"

# ISSUE-0002: Create virtual environment
gh issue create \
  --repo "$FULL_REPO" \
  --title "[ISSUE-0002] Create Python virtual environment" \
  --body "## Issue Title
Create Python virtual environment

## Issue ID
ISSUE-0002

## Parent Task
TASK-001: Install Core Development Tools

## Action Required
Create and activate a Python virtual environment

## Command/Code
\`\`\`bash
python3 -m venv shadowed-realms-env
source shadowed-realms-env/bin/activate  # macOS/Linux
\`\`\`

## Expected Output
\`\`\`
(shadowed-realms-env) $
\`\`\`

## Rewards
- **XP**: 25
- **Coins**: 10
- **Progress**: 2% toward Python Mastery" \
  --label "issue,micro-task,xp-25,coins-10"

# Create more comprehensive issues for character system
echo "Creating character system issues..."

# EPIC-002: Character System
gh issue create \
  --repo "$FULL_REPO" \
  --title "[EPIC-002] Character System & Animation" \
  --body "## Epic Title
Character System & Animation

## Epic ID
EPIC-002

## Business Value
**Estimated Revenue Impact**: $15,000
**Asset Production**: 200 character models, 500 animations
**Skill Development Areas**: Character modeling, rigging, animation

## Description
Create complete character system with anime-style models, rigs, and animations

## Success Criteria
- [ ] 25 hero characters modeled
- [ ] 50 NPCs created
- [ ] 500 animations complete
- [ ] All characters game-ready

## Rewards
- **XP Pool**: 25,000 XP
- **Coin Pool**: 12,500 coins
- **Memory Fragments**: 4-8

## Financial Tracking
\`\`\`
Development Cost: $1,500
Expected Revenue: $15,000
ROI: 900%
Character Asset Price: $45-120 each
\`\`\`" \
  --label "epic,sprint-1,xp-25000,coins-12500,memory-unlock"

# Create GUI Tool Development issues
echo "Creating GUI tool development issues..."

gh issue create \
  --repo "$FULL_REPO" \
  --title "[EPIC-003] GUI Tools & Visual Editors" \
  --body "## Epic Title
GUI Tools & Visual Editors

## Epic ID
EPIC-003

## Business Value
**Estimated Revenue Impact**: $25,000
**Asset Production**: 50 GUI tools
**Skill Development Areas**: Tool development, UI/UX

## Description
Develop visual editors and no-code tools for game developers

## Tools to Create
- RPG Manager Pro (Visual Interface): $250
- Combat Designer (No-Code): $180
- Quest Builder Visual Editor: $150
- Dialogue System Designer: $125
- Inventory Manager: $95
- Skill Tree Designer: $145

## Rewards
- **XP Pool**: 30,000 XP
- **Coin Pool**: 15,000 coins
- **Memory Fragments**: 9-15

## Financial Tracking
\`\`\`
Development Cost: $2,000
Expected Revenue: $25,000
ROI: 1150%
Tool Price Range: $65-250 each
\`\`\`" \
  --label "epic,sprint-2,xp-30000,coins-15000,memory-unlock"

# Create TCG Card Game issues
echo "Creating TCG companion game issues..."

gh issue create \
  --repo "$FULL_REPO" \
  --title "[EPIC-004] Magic: The Gathering Style TCG" \
  --body "## Epic Title
Magic: The Gathering Style Companion Card Game

## Epic ID
EPIC-004

## Business Value
**Estimated Revenue Impact**: $10,000
**Asset Production**: 500 unique cards
**Skill Development Areas**: Game design, card mechanics, art

## Description
Develop complete TCG companion to main RPG

## Card Categories
- Character Cards: 100 (from RPG models)
- Spell Cards: 150 (from animations)
- Equipment Cards: 100 (from items)
- Land Cards: 50 (from environments)
- Memory Fragment Cards: 49 (legendary)
- Special Cards: 51

## Rewards
- **XP Pool**: 20,000 XP
- **Coin Pool**: 10,000 coins
- **Memory Fragments**: 16-25

## Financial Tracking
\`\`\`
Development Cost: $1,000
Expected Revenue: $10,000
ROI: 900%
Pack Price: $5-15
\`\`\`" \
  --label "epic,sprint-2,xp-20000,coins-10000,memory-unlock"

# Create Memory Fragment issues
echo "Creating Memory Fragment unlock issues..."

for i in {1..49}; do
  gh issue create \
    --repo "$FULL_REPO" \
    --title "[MEMORY-$i] Memory Fragment #$i Unlock" \
    --body "## Memory Fragment #$i

## Unlock Condition
Complete specific milestone in development

## Story Content
[FromSoft-style cryptic lore piece]

## Rewards
- **XP**: 500
- **Coins**: 250
- **Unlocks**: New abilities/features

## Related Tasks
Links to tasks that unlock this memory" \
    --label "memory-fragment,story-unlock,xp-500"
done

echo "✅ Created Memory Fragment issues"

# Create skill specialization paths
echo "Creating skill specialization paths..."

# Maya Specialization Path
gh issue create \
  --repo "$FULL_REPO" \
  --title "[SPECIALIZATION] Maya Master Path" \
  --body "## Specialization: Maya Master

## Path Requirements
Complete 100 Maya-related tasks

## Skill Tree
- Basic Modeling (0-25 tasks)
- Advanced Modeling (26-50 tasks)
- Rigging (51-75 tasks)
- Animation (76-100 tasks)

## Mastery Rewards
- **Title**: Maya Master
- **XP Bonus**: +50% on Maya tasks
- **Coin Bonus**: +25% on Maya assets
- **Special Unlock**: Maya API advanced tools

## Progress Tracking
- [ ] 25 tasks - Bronze
- [ ] 50 tasks - Silver
- [ ] 75 tasks - Gold
- [ ] 100 tasks - Master" \
  --label "specialization,skill-tree,maya"

# Unity Specialization Path
gh issue create \
  --repo "$FULL_REPO" \
  --title "[SPECIALIZATION] Unity Developer Path" \
  --body "## Specialization: Unity Developer

## Path Requirements
Complete 100 Unity-related tasks

## Skill Tree
- Scene Setup (0-25 tasks)
- C# Scripting (26-50 tasks)
- Optimization (51-75 tasks)
- Advanced Systems (76-100 tasks)

## Mastery Rewards
- **Title**: Unity Expert
- **XP Bonus**: +50% on Unity tasks
- **Coin Bonus**: +25% on Unity assets
- **Special Unlock**: Unity Pro features" \
  --label "specialization,skill-tree,unity"

echo "✅ Created specialization paths"

# Create Sprint ceremonies
echo "Creating Sprint ceremony issues..."

gh issue create \
  --repo "$FULL_REPO" \
  --title "[CEREMONY] Sprint 1 Planning" \
  --body "## Sprint 1 Planning Session

## Date
Month 1, Week 1

## Objectives
- Review 1000+ tasks
- Assign priorities
- Set sprint goals

## Sprint Goals
1. Complete development environment
2. Create first 100 assets
3. Establish pipeline

## Team Assignments
- Jesse: Technical implementation
- Michael: Support and testing

## Metrics
- Target XP: 50,000
- Target Coins: 25,000
- Target Assets: 100" \
  --label "ceremony,sprint-1,planning"

gh issue create \
  --repo "$FULL_REPO" \
  --title "[CEREMONY] Sprint 1 Daily Standup Template" \
  --body "## Daily Standup Template

## Format
1. What I did yesterday
2. What I'm doing today
3. Any blockers

## XP Earned Yesterday
[Amount]

## Coins Earned Yesterday
[Amount]

## Assets Created
[List]

## Today's Goals
[List]" \
  --label "ceremony,sprint-1,daily"

echo "✅ Created Sprint ceremonies"

# Create financial tracking issues
echo "Creating financial tracking issues..."

gh issue create \
  --repo "$FULL_REPO" \
  --title "[FINANCIAL] Asset Revenue Tracker" \
  --body "## Asset Revenue Tracking

## Month 1 Targets
- 3D Models: $2,000
- Scripts: $1,500
- GUI Tools: $3,000
- Tutorials: $500

## Actual Revenue
[To be updated]

## Top Performers
[Track best-selling assets]

## Market Analysis
[Monthly insights]" \
  --label "financial,tracking,revenue"

echo "✅ Created financial tracking"

echo ""
echo "=============================================="
echo "📊 ECOSYSTEM STATUS"
echo "=============================================="
echo "✅ Repository: https://github.com/$FULL_REPO"
echo "✅ Issues Created: 60+ (initial batch)"
echo "✅ Labels: epic, user-story, task, issue, xp-*, coins-*, memory-fragment"
echo "✅ Gamification: XP system, Coin system, Memory unlocks"
echo "✅ Financial: Revenue tracking integrated"
echo ""
echo "🎮 Next Steps:"
echo "1. Enable GitHub Projects"
echo "2. Create OAuth App"
echo "3. Create GitHub App"
echo "4. Configure webhooks"
echo ""
echo "Total planned issues: 3000+"
echo "Total planned assets: 5000+"
echo "Revenue target: $50,000+"
