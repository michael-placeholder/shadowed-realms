# Shadowed Realms RPG - Project Pivot Documentation
## From Abstract Garden to Commercial RPG Development

### Executive Summary
Pivoting from Abstract Garden's learning framework to Shadowed Realms RPG - a full-stack commercial game development project maintaining the same gamified Agile methodology, skill development approach, and granular task breakdown while targeting real financial returns across multiple revenue streams.

**Project Leads**: Jesse & Michael (Full-time, 6 months)  
**Investment Required**: Minimal (both working full-time, no salary needs)  
**Revenue Target**: $50,000+ across all streams  
**Timeline**: 6 months (3 sprints, 2 months each)  
**Tasks**: 5000+ granular issues  
**Skill Gaps**: 63 identified areas  

---

## 1. CORE PROJECT STRUCTURE

### 1.1 Agile Hierarchy
```
Epic (Major Feature)
  └── User Story (Feature Component)
      └── Task (Implementation Step)
          └── Issue (Granular Action)
```

**Example Breakdown:**
- **Epic**: Character Combat System
- **User Story**: Implement Melee Combat
- **Task**: Create Sword Attack Animation
- **Issue**: "Install Maya 2024", "Import base mesh", "Create keyframes 1-10"

### 1.2 Sprint Structure (6 Months Total)
- **Sprint 1** (Months 1-2): Foundation & Core Systems
- **Sprint 2** (Months 3-4): Content Creation & Assets
- **Sprint 3** (Months 5-6): Polish, Marketing & Launch

### 1.3 Task Granularity
Tasks broken down to command-level actions:
- "Install Python 3.11"
- "Create new Unity project"
- "git init"
- "Import character controller package"
- "Set terrain resolution to 2048"

---

## 2. GAMIFICATION SYSTEM (FromSoft Theme)

### 2.1 XP System
- **Basic Tasks**: 25-100 XP
- **Intermediate Tasks**: 100-500 XP
- **Advanced Tasks**: 500-2000 XP
- **Epic Completion**: 5000+ XP

### 2.2 Coin System (Financial Value)
Every task has calculated financial impact:
```javascript
coinValue = (assetValue * marketShare * completionImpact) / 100
```

### 2.3 Memory Fragments (49 Total)
Unlock story elements and development insights:
- 7 per month of development
- Tied to milestone completions
- Reveals lore, technical documentation, and market analysis

### 2.4 Skill Mastery Paths
Complete X tasks in a specialization to unlock mastery:
- **3D Modeling Path**: Maya, ZBrush, Substance (500 tasks → Master)
- **Programming Path**: C#, Python, JavaScript (500 tasks → Master)
- **Game Design Path**: Level design, systems, balance (300 tasks → Master)
- **Business Path**: Marketing, sales, analytics (200 tasks → Master)

---

## 3. REVENUE STREAMS & FINANCIAL MODEL

### 3.1 Primary Game ($197)
- **Platform**: Steam (70% revenue share)
- **Target Sales**: 100 copies in 6 months
- **Revenue**: $13,790

### 3.2 Asset Marketplace Sales
**3D Art Assets** (Unity Store, Unreal Marketplace):
- 33 unique assets identified
- Price range: $35-150
- Monthly revenue potential: $1,675 (conservative)
- Platform splits: Unity 70/30, Unreal 88/12

### 3.3 Scripts & Tools (Pure Sales Model)
**51 Development Scripts**:
- UI Systems: $45-125
- AI Systems: $75-200  
- Environment Tools: $35-95
- Combat Systems: $95-150
- VFX Tools: $50-125
- **NO SUBSCRIPTIONS** - One-time purchase
- **Optional Upgrades**: Previous buyers get 50-75% discount on new versions

### 3.4 GUI Development Tools
- Character Creator: $250
- Animation Tool: $150
- Environment Builder: $125
- VFX Creator: $95
- Material Editor: $65

### 3.5 Educational Content
- Complete Course Bundle: $197
- Character Animation Course: $97
- Environment Design Course: $77
- Programming Fundamentals: $57

### 3.6 Magic: The Gathering Style TCG
- Physical cards: $15/pack
- Digital implementation: $5/pack
- Collector editions: $50-200
- Tournament support system

### 3.7 Monthly Revenue Projections
- **Month 1**: $200 (early assets)
- **Month 2**: $500 (scripts release)
- **Month 3**: $1,200 (tools + assets)
- **Month 4**: $1,500 (educational content)
- **Month 5**: $2,000 (pre-launch sales)
- **Month 6**: $2,500 (full launch)

---

## 4. TECHNICAL IMPLEMENTATION

### 4.1 GitHub Integration
```javascript
// GitHub Issues API Integration
const fetchIssues = async () => {
  const response = await fetch('https://api.github.com/repos/[repo]/issues');
  const issues = await response.json();
  return calculateRewards(issues);
};

const calculateRewards = (issues) => {
  return issues.map(issue => ({
    ...issue,
    xp: calculateXP(issue.labels),
    coins: calculateCoins(issue.labels),
    memoryFragment: checkMemoryUnlock(issue.number)
  }));
};
```

### 4.2 Front-Facing Task Picker Dashboard
- **React** frontend with real-time GitHub sync
- **Node.js** backend for API management
- **PostgreSQL** for progress tracking
- **MongoDB** for memory fragments and lore

### 4.3 Development Stack
- **Game Engine**: Unity 2024.3 LTS / Unreal Engine 5
- **3D Pipeline**: Maya → ZBrush → Substance → Engine
- **Version Control**: Git with LFS for assets
- **CI/CD**: GitHub Actions for automated builds
- **Documentation**: Markdown with automatic site generation

---

## 5. SKILL DEVELOPMENT MATRIX (63 Gaps)

### 5.1 Technical Skills
- **3D Modeling**: Maya, Blender, 3ds Max
- **Sculpting**: ZBrush, Mudbox
- **Texturing**: Substance Painter, Designer, Mari
- **Animation**: Maya, MotionBuilder, Cascadeur
- **VFX**: Houdini, PopcornFX, Niagara
- **Programming**: C#, C++, Python, JavaScript
- **Shaders**: HLSL, GLSL, ShaderGraph

### 5.2 Business Skills
- **Marketing**: Social media, content creation, SEO
- **Sales**: Asset store optimization, pricing strategy
- **Analytics**: Player metrics, revenue tracking
- **Community**: Discord management, forum moderation

---

## 6. TASK CALCULATION METHODOLOGY

### 6.1 Financial Value Assignment
Every task contributes to overall project value:
```python
def calculate_task_value(task):
    base_value = skill_level_multiplier[task.difficulty]
    market_impact = asset_market_value * completion_percentage
    skill_growth = experience_value * learning_coefficient
    return base_value + market_impact + skill_growth
```

### 6.2 Example Task Valuation
**Task**: "Create Sword Slash VFX"
- Base Value: $50 (intermediate task)
- Market Impact: $30 (contributes to $150 VFX pack)
- Skill Growth: $20 (Houdini experience)
- **Total Coin Value**: 100 coins

---

## 7. SPRINT ENFORCEMENT & DEPENDENCIES

### 7.1 Sequential Task Completion
```javascript
const sprintTasks = {
  sprint1: {
    required: ['setup-unity', 'git-init', 'create-gdd'],
    unlocks: 'sprint1-advanced'
  },
  sprint2: {
    required: ['character-model', 'animation-rig', 'base-textures'],
    prerequisite: 'sprint1-complete'
  }
};
```

### 7.2 Memory Fragment Unlocks
- Fragment 1-7: Sprint 1 completion
- Fragment 8-14: First asset published
- Fragment 15-21: First sale achieved
- Fragment 22-28: TCG prototype complete
- Fragment 29-35: Beta launch
- Fragment 36-42: Full launch
- Fragment 43-49: Post-launch content

---

## 8. INVESTMENT & RESOURCE OPTIMIZATION

### 8.1 Minimal Investment Strategy
Since Jesse & Michael are full-time for 6 months:
- **Software**: $500 (student/indie licenses)
- **Assets**: $300 (base assets to modify)
- **Marketing**: $200 (initial promotion)
- **Total**: $1,000 (vs. original $9,000 projection)

### 8.2 Revenue Reinvestment
- Month 1-2 revenue → Marketing budget
- Month 3-4 revenue → Better tools/assets
- Month 5-6 revenue → Launch promotion

---

## 9. GITHUB PROJECT STRUCTURE

### 9.1 Repository Organization
```
shadowed-realms/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── epic.md
│   │   ├── user-story.md
│   │   ├── task.md
│   │   └── issue.md
│   └── workflows/
├── game/
│   ├── Unity/
│   └── Unreal/
├── assets/
│   ├── 3d-models/
│   ├── textures/
│   ├── animations/
│   └── vfx/
├── scripts/
│   ├── unity/
│   ├── unreal/
│   └── tools/
├── tcg/
│   ├── cards/
│   └── rules/
├── docs/
│   ├── js/
│   │   ├── github-data-service.js
│   │   ├── sprint-enforcer.js
│   │   └── task-picker.js
│   └── dashboard/
└── education/
```

### 9.2 Issue Labels System
- **difficulty**: `easy`, `medium`, `hard`, `epic`
- **xp-value**: `xp-25`, `xp-100`, `xp-500`, `xp-2000`
- **coins**: `coins-10`, `coins-50`, `coins-100`, `coins-500`
- **sprint**: `sprint-1`, `sprint-2`, `sprint-3`
- **skill**: `3d`, `programming`, `design`, `business`
- **memory**: `fragment-1` through `fragment-49`

---

## 10. NEXT IMMEDIATE ACTIONS

1. **Create GitHub repository** with issue templates
2. **Set up project board** with sprint columns
3. **Initialize first 100 granular issues** for Sprint 1
4. **Deploy task picker dashboard** (React + GitHub API)
5. **Configure automated XP/coin tracking**
6. **Document first 7 memory fragments**
7. **Create skill mastery tracking system**
8. **Establish daily standup structure**

---

## 11. SUCCESS METRICS

### 11.1 Development Metrics
- Tasks completed per day: 28+ (5000 tasks / 180 days)
- XP earned per week: 5000+
- Memory fragments unlocked: 7/month
- Skill masteries achieved: 2+ per developer

### 11.2 Financial Metrics
- Month 1-2: $700 revenue
- Month 3-4: $2,700 revenue
- Month 5-6: $4,500 revenue
- 6-month total: $7,900+
- Post-launch monthly: $2,500+

### 11.3 Asset Production
- 3D models: 33+ market-ready
- Scripts: 51+ production tools
- GUI tools: 5+ development aids
- Educational modules: 4+ courses
- TCG cards: 200+ unique designs

---

## 12. RISK MITIGATION

### 12.1 Technical Risks
- **Mitigation**: Granular tasks prevent large failures
- **Backup**: Multiple revenue streams reduce dependency

### 12.2 Market Risks
- **Mitigation**: Pre-validated through financial analysis
- **Backup**: Pivot individual assets based on early sales

### 12.3 Time Risks
- **Mitigation**: Sprint structure enforces progress
- **Backup**: Core systems prioritized for MVP

---

This pivot maintains Abstract Garden's proven methodology while targeting real commercial success. Every task contributes to both skill development and financial value, creating a sustainable development model that can extend beyond the initial 6-month timeline.