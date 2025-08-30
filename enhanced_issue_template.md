# Enhanced Issue Template for Shadowed Realms RPG

## Issue Structure Requirements

### 1. DELIVERABLE REQUIREMENTS
Every issue MUST have a clear deliverable that can be uploaded/verified:
- Code files (.cs, .py, .js)
- Asset files (.fbx, .png, .prefab)
- Documentation (.md, .txt)
- Screenshots/Videos (proof of completion)
- Configuration files (.json, .yaml)

### 2. MONETARY VALUE EXPLANATION
Each issue must explain WHY it has its coin value:
- How it contributes to the $50,000 revenue target
- Which revenue stream it impacts (Game, Assets, Scripts, Education, TCG)
- Market value of similar work
- Time investment vs. return calculation

### 3. XP JUSTIFICATION
Explain why the XP value is assigned:
- Skill difficulty level
- Learning curve involved
- Prerequisites required
- Mastery path contribution

### 4. USER STORY INTEGRATION
Every issue must link to:
- Parent Epic
- User Story
- Acceptance Criteria
- Definition of Done

### 5. MEMORY FRAGMENT MILESTONES
Issues contribute to milestone-based fragments:
- Fragments 1-7: Complete Sprint 1 Setup (Issues 1-160)
- Fragments 8-14: First Asset Published (Issues 161-300)
- Fragments 15-21: Combat System Complete (Issues 301-480)
- Fragments 22-28: Environment System Done (Issues 481-640)
- Fragments 29-35: UI/UX Complete (Issues 641-780)
- Fragments 36-42: Save System Implemented (Issues 781-900)
- Fragments 43-49: Audio System & Polish (Issues 901-1000)

## EXAMPLE ENHANCED ISSUE:

```markdown
# [ISSUE-0231] Export Character Model to Unity FBX Format

## 🎯 Epic & User Story
- **Epic**: EPIC-002 - Character System Foundation
- **User Story**: US-013 - As a developer, I need game-ready character models
- **Sprint**: Sprint 1 - Foundation & Core Systems
- **Priority**: High

## 📦 Deliverable Requirements
**What you must upload:**
1. Character_Base.fbx file (exported from Maya)
2. Screenshot of Unity import settings
3. Test scene showing character in Unity
4. Export settings documentation (.txt)

**Verification Criteria:**
- [ ] FBX file size < 10MB
- [ ] Polycount < 15,000 triangles
- [ ] Proper UV mapping intact
- [ ] Bones correctly imported
- [ ] No missing textures

## 💰 Monetary Value Explanation
**Coin Value: 120 coins = $1,200 project value**

This task directly contributes to:
- **3D Asset Marketplace**: Character models sell for $45-95 each
- **Game Development**: Core character is essential for gameplay ($197 game price)
- **Educational Content**: This process becomes a tutorial ($97 course value)

Market comparison:
- Freelance 3D artist charges $150-300 for similar export/optimization
- Unity Asset Store similar models: $35-75
- Time saved by proper export: 2-3 hours = $100-150 developer time

## 🎮 XP Justification
**XP Value: 200 XP (Intermediate-Advanced)**

Why this XP value:
- Requires knowledge of both Maya and Unity pipelines
- Understanding of optimization techniques needed
- Critical skill for 3D artist career path
- Builds on 10+ previous tasks
- Unlocks ability to create sellable assets

**Skill Development:**
- 3D Pipeline Mastery: +15%
- Unity Integration: +10%
- Asset Optimization: +20%

## 📊 Full Agile Integration

### Acceptance Criteria
1. Model imports into Unity without errors
2. All animations remain functional
3. Materials properly assigned
4. Performance metrics met (60 FPS)

### Definition of Done
- [ ] Code reviewed by team
- [ ] Tested on 3 different machines
- [ ] Documentation updated
- [ ] Committed to repository
- [ ] Added to asset manifest

### Dependencies
- Blocked by: ISSUE-0210 (Complete character modeling)
- Blocks: ISSUE-0251 (Setup character rig in Unity)

## 🔮 Memory Fragment Progress
**Contributes to Fragments 8-14: First Asset Published**

Completing this issue brings you 5% closer to unlocking:
- Fragment 8: "The Artist's Journey" - Lore about the game's art style
- Fragment 9: "Pipeline Mastery" - Technical documentation unlock
- Fragment 10: "Market Insights" - Asset pricing strategies revealed

## 📈 Business Impact Metrics
- **Revenue Impact**: Direct path to first $1,000 in asset sales
- **Time to Market**: Reduces character pipeline by 40%
- **Quality Score**: Improves asset rating potential to 4.5+ stars
- **Reusability**: This process applies to all 200+ character models

## 🛠️ Technical Specifications
```yaml
export_settings:
  format: FBX 2020
  units: Meters
  up_axis: Y
  include:
    - mesh
    - skeleton
    - blend_shapes
    - materials
  exclude:
    - cameras
    - lights
    - animation_clips
  optimization:
    mesh_compression: true
    remove_doubles: true
    triangulate: true
```

## 📚 Learning Resources
- [Unity FBX Import Best Practices](https://docs.unity.com)
- [Maya to Unity Pipeline Guide](internal-docs)
- Video Tutorial: "Export Like a Pro" (10 min)

## 🏆 Achievements Unlocked
Completing this issue unlocks:
- "Pipeline Professional" badge
- Access to advanced export scripts
- Eligibility for "3D Asset Creator" certification

## 💬 Discussion & Support
- Slack Channel: #3d-pipeline
- Expert Contact: @maya-specialist
- Common Issues: [Troubleshooting Guide](link)

---
**Estimated Time**: 2-3 hours
**Actual Time**: [To be filled]
**Post-Mortem**: [Lessons learned after completion]
```

## FULL SPRINT AGILE WORKFLOW

### Sprint Structure (2 months each)
```
Sprint Planning (Day 1-2)
  ├── Review Product Backlog
  ├── Story Point Estimation
  ├── Sprint Goal Setting
  └── Task Assignment

Daily Standups (Every Day)
  ├── Yesterday's Progress
  ├── Today's Goals
  └── Blockers

Sprint Review (Day 55)
  ├── Demo Deliverables
  ├── Stakeholder Feedback
  └── Metrics Review

Sprint Retrospective (Day 58-60)
  ├── What Went Well
  ├── What Could Improve
  └── Action Items
```

### Velocity Tracking
- Target: 28 tasks/day = 1,680 tasks per sprint
- Actual tracking in GitHub Projects
- Burndown charts automated
- Story points properly assigned

### Definition of Ready
Before an issue can be worked on:
1. Clear acceptance criteria
2. Estimated story points
3. No blocking dependencies
4. Deliverables defined
5. Resources available

### Definition of Done
An issue is only complete when:
1. Code/Asset created and tested
2. Documentation updated
3. Peer reviewed
4. Merged to main branch
5. Deliverable uploaded
6. Metrics recorded

## RELATIONAL DATABASE STRUCTURE

### Issue Relations
```sql
Issues Table:
- issue_id (PRIMARY KEY)
- epic_id (FOREIGN KEY)
- user_story_id (FOREIGN KEY)
- sprint_id (FOREIGN KEY)
- memory_fragment_id (FOREIGN KEY)
- xp_value
- coin_value
- monetary_impact
- deliverable_url
- status

Epics Table:
- epic_id (PRIMARY KEY)
- epic_name
- business_value
- target_revenue

User_Stories Table:
- story_id (PRIMARY KEY)
- epic_id (FOREIGN KEY)
- story_description
- acceptance_criteria

Memory_Fragments Table:
- fragment_id (PRIMARY KEY)
- unlock_condition
- lore_content
- technical_unlock

Deliverables Table:
- deliverable_id (PRIMARY KEY)
- issue_id (FOREIGN KEY)
- file_type
- file_url
- validation_status
```

This creates a fully integrated system where every issue is connected to the larger project goals, has clear value propositions, and contributes to both immediate deliverables and long-term career objectives.