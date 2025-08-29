# Shadowed Realms - Final Setup Instructions

## 🔗 Complete Connection Setup

### 1. Enable GitHub Pages (Required for Dashboard)
1. Go to: https://github.com/michael-placeholder/shadowed-realms/settings/pages
2. Under "Source", select "Deploy from a branch"
3. Under "Branch", select "main"
4. Under "Folder", select "/docs"
5. Click "Save"
6. Wait 2-3 minutes for deployment
7. Dashboard will be live at: https://michael-placeholder.github.io/shadowed-realms/

### 2. Connect Project Board to Repository
1. Go to your project: https://github.com/orgs/michael-placeholder/projects
2. Click on "Shadowed Realms Sprint Board"
3. Click "..." menu → "Settings"
4. Under "Repository access", click "Add repository"
5. Search for "shadowed-realms" and add it
6. This connects issues to the project board automatically

### 3. Create Organization Token (For Issue Creation)
Since the fine-grained tokens aren't working, you need to:
1. Go to: https://github.com/settings/tokens?type=beta
2. Click "Generate new token" → "Generate new token (classic)"
3. Name: "Shadowed Realms Development"
4. Expiration: 90 days
5. Select scopes:
   - ✅ repo (all)
   - ✅ project
   - ✅ admin:org → write:org
6. Click "Generate token"
7. Copy the token

### 4. Create First Issues
Once you have the new token, run:
```bash
export GITHUB_TOKEN="your-new-token-here"

# Create first Epic
gh issue create --repo michael-placeholder/shadowed-realms \
  --title "[EPIC-001] Project Setup & Infrastructure" \
  --label "epic,sprint-1,xp-10000,coins-5000"

# Create first micro-tasks
gh issue create --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0001] Download Unity Hub" \
  --label "issue,sprint-1,xp-25,coins-10"

gh issue create --repo michael-placeholder/shadowed-realms \
  --title "[ISSUE-0002] Install Unity 2024.3 LTS" \
  --label "issue,sprint-1,xp-50,coins-25"
```

### 5. Dashboard JavaScript Integration
The dashboard at `/docs/index.html` is already configured to:
- Fetch issues from the GitHub API
- Display them in the task picker
- Calculate XP and coin rewards
- Track memory fragments
- Show financial impact

Once GitHub Pages is enabled, it will automatically:
- Connect to the repository's issues
- Display tasks by sprint
- Show progress bars
- Track completion

## ✅ What's Already Complete

### Repository Structure
```
michael-placeholder/shadowed-realms/
├── .github/ISSUE_TEMPLATE/    ✅ 4 templates ready
│   ├── 01-epic.md
│   ├── 02-user-story.md
│   ├── 03-task.md
│   └── 04-issue.md
├── docs/                       ✅ Dashboard ready
│   ├── index.html             (FromSoft-themed)
│   └── css/fromsoft-theme.css
├── README.md                   ✅ Professional docs
├── SHADOWED_REALMS_PROJECT_PIVOT.md ✅
├── ASSET_MANIFEST_5000.md     ✅ 5000+ assets
├── SPRINT_1_COMPLETE_TASKS.md ✅ 1000+ tasks
└── SPRINT_1_EPICS.md          ✅ 8 epics

All files pushed to: https://github.com/michael-placeholder/shadowed-realms
```

### Project Features
- **Gamification**: XP (25-2000), Coins, Memory Fragments (49)
- **Agile Structure**: Epic → User Story → Task → Issue
- **Task Granularity**: Down to "install python" level
- **Financial Tracking**: Every task has calculated value
- **Revenue Model**: Pure sales, no subscriptions
- **Team**: Jesse & Michael full-time
- **Timeline**: 6 months, 3 sprints
- **Goals**: 5000+ assets, $50K+ revenue

## 🚀 Next Steps

1. **Enable GitHub Pages** (2 minutes)
2. **Connect Project to Repo** (1 minute)
3. **Generate new token** (2 minutes)
4. **Create first 10 issues** (5 minutes)
5. **Visit dashboard** at https://michael-placeholder.github.io/shadowed-realms/

The dashboard will automatically pull issues and display them in the FromSoft-themed interface with:
- Task picker
- XP/Coin tracking
- Memory fragments
- Sprint progress
- Financial impact
- Skill development paths

## 📊 Verification

After setup, verify everything works:
1. Dashboard loads at GitHub Pages URL
2. Issues appear in repository
3. Project board shows issues
4. Labels are applied correctly
5. Dashboard fetches and displays tasks

Everything is ready - just need to enable GitHub Pages and create a working token!