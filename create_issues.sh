#!/bin/bash

# Create issues for EPIC-001: Project Setup & Infrastructure

echo "Creating EPIC-001 and associated issues..."

# Create the Epic
gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[EPIC-001] Project Setup & Infrastructure" \
  --body "## Epic Title
Project Setup & Infrastructure

## Business Value
**Estimated Revenue Impact**: \$5,000
**Asset Production**: 20 assets
**Skill Development Areas**: Git, Unity, Maya, Python

## Success Criteria
- [ ] Development environment fully configured
- [ ] Version control established
- [ ] Project documentation complete
- [ ] CI/CD pipeline operational

## User Stories
- [ ] USER-STORY-001: Initialize Development Environment
- [ ] USER-STORY-002: Configure Version Control
- [ ] USER-STORY-003: Set Up Build Pipeline
- [ ] USER-STORY-004: Create Project Documentation

## Rewards
- **XP Pool**: 10,000 XP
- **Coin Pool**: 5,000 coins
- **Memory Fragments**: 1-3" \
  --label "epic,sprint-1,xp-10000,coins-5000"

# Create User Story 001
gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[USER-STORY-001] Initialize Development Environment" \
  --body "## User Story
**As a** developer
**I want** a fully configured development environment
**So that** I can begin RPG development

## Parent Epic
EPIC-001: Project Setup & Infrastructure

## Acceptance Criteria
- [ ] All required software installed
- [ ] Unity project created
- [ ] Maya configured
- [ ] Python environment ready

## Tasks Breakdown
- [ ] TASK-001: Install Core Development Tools
- [ ] TASK-002: Initialize Git Repository
- [ ] TASK-003: Configure Unity Project

## Rewards
- **XP**: 2000
- **Coins**: 1000" \
  --label "user-story,sprint-1,xp-2000,coins-1000"

# Create first 10 micro-tasks
echo "Creating first 10 micro-tasks..."

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0001] Download Unity Hub from unity.com" \
  --body "## Action Required
Navigate to unity.com and download Unity Hub installer

## Command/Code
\`\`\`bash
# Browse to https://unity.com/download
# Click 'Download Unity Hub'
# Save installer to Downloads folder
\`\`\`

## Success Verification
- [ ] Unity Hub installer downloaded
- [ ] File size ~100MB
- [ ] Ready to install

## Time Estimate
5 minutes

## Rewards
- **XP**: 25
- **Coins**: 10
- **Progress**: 1% toward Unity mastery

## Financial Impact
- Enables \$3,900 software value
- Unlocks game development capability" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0002] Install Unity 2024.3 LTS" \
  --body "## Action Required
Install Unity 2024.3 LTS using Unity Hub

## Command/Code
\`\`\`bash
# Open Unity Hub
# Click 'Installs' tab
# Click 'Install Editor'
# Select Unity 2024.3 LTS
# Add modules: Visual Studio, Documentation
\`\`\`

## Success Verification
- [ ] Unity 2024.3 LTS installed
- [ ] Visual Studio integration ready
- [ ] Can create new project

## Time Estimate
30 minutes

## Rewards
- **XP**: 50
- **Coins**: 25
- **Progress**: 2% toward Unity mastery" \
  --label "issue,sprint-1,xp-50,coins-25"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0003] Download Visual Studio 2022" \
  --body "## Action Required
Download and install Visual Studio 2022 Community

## Command/Code
\`\`\`bash
# Browse to https://visualstudio.microsoft.com/
# Download Community edition
# Run installer
# Select 'Game development with Unity'
\`\`\`

## Success Verification
- [ ] Visual Studio installed
- [ ] Unity tools configured
- [ ] C# support enabled

## Time Estimate
20 minutes

## Rewards
- **XP**: 25
- **Coins**: 15" \
  --label "issue,sprint-1,xp-25,coins-15"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0004] Install Visual Studio Unity Tools" \
  --body "## Action Required
Configure Visual Studio for Unity development

## Command/Code
\`\`\`bash
# Open Visual Studio
# Tools > Get Tools and Features
# Check 'Game development with Unity'
# Click Modify
\`\`\`

## Success Verification
- [ ] Unity tools installed
- [ ] IntelliSense working
- [ ] Debugger configured

## Time Estimate
10 minutes

## Rewards
- **XP**: 25
- **Coins**: 10" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0005] Download Git for Windows/Mac" \
  --body "## Action Required
Install Git version control system

## Command/Code
\`\`\`bash
# Windows: https://git-scm.com/download/win
# Mac: brew install git
# Verify: git --version
\`\`\`

## Success Verification
- [ ] Git installed
- [ ] git --version shows 2.40+
- [ ] Can run git commands

## Time Estimate
5 minutes

## Rewards
- **XP**: 25
- **Coins**: 10" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0006] Install Git LFS for large files" \
  --body "## Action Required
Install Git Large File Storage for assets

## Command/Code
\`\`\`bash
# Download from https://git-lfs.github.com/
# Run installer
# Verify: git lfs version
\`\`\`

## Success Verification
- [ ] Git LFS installed
- [ ] git lfs version works
- [ ] Ready for large files

## Time Estimate
5 minutes

## Rewards
- **XP**: 25
- **Coins**: 10" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0007] Download GitHub Desktop" \
  --body "## Action Required
Install GitHub Desktop for GUI git management

## Command/Code
\`\`\`bash
# Browse to https://desktop.github.com/
# Download for your OS
# Install and sign in
\`\`\`

## Success Verification
- [ ] GitHub Desktop installed
- [ ] Signed in to account
- [ ] Can see repositories

## Time Estimate
5 minutes

## Rewards
- **XP**: 25
- **Coins**: 10" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0008] Install Node.js v20 LTS" \
  --body "## Action Required
Install Node.js for web dashboard development

## Command/Code
\`\`\`bash
# Browse to https://nodejs.org/
# Download v20 LTS
# Run installer
# Verify: node --version
\`\`\`

## Success Verification
- [ ] Node.js installed
- [ ] npm available
- [ ] node --version shows v20

## Time Estimate
5 minutes

## Rewards
- **XP**: 25
- **Coins**: 10" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0009] Install Python 3.11" \
  --body "## Action Required
Install Python for Maya scripting and tools

## Command/Code
\`\`\`bash
# Browse to https://python.org/downloads/
# Download Python 3.11
# Check 'Add to PATH' during install
# Verify: python --version
\`\`\`

## Success Verification
- [ ] Python 3.11 installed
- [ ] pip available
- [ ] python --version works

## Time Estimate
5 minutes

## Rewards
- **XP**: 25
- **Coins**: 10
- **Progress**: 1% toward Python mastery" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create \
  --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0010] Run npm install -g yarn" \
  --body "## Action Required
Install Yarn package manager globally

## Command/Code
\`\`\`bash
npm install -g yarn
yarn --version
\`\`\`

## Expected Output
\`\`\`
added 1 package in 2s
1.22.19
\`\`\`

## Success Verification
- [ ] Yarn installed globally
- [ ] yarn --version works
- [ ] Can use yarn commands

## Time Estimate
2 minutes

## Rewards
- **XP**: 25
- **Coins**: 5
- **Progress**: 1% toward web dev mastery" \
  --label "issue,sprint-1,xp-25,coins-5"

echo "First 10 issues created successfully!"
echo "Repository: https://github.com/michael-placeholder/shadowed-realms"
echo "Issues: https://github.com/michael-placeholder/shadowed-realms/issues"
echo "Project: https://github.com/orgs/michael-placeholder/projects"