# GitHub App Configuration

## GitHub App Setup for Shadowed Realms

### 1. Create GitHub App
Go to: https://github.com/organizations/michael-placeholder/settings/apps/new

### App Configuration:

#### Basic Information:
- **GitHub App name**: Shadowed Realms Bot
- **Homepage URL**: https://michael-placeholder.github.io/shadowed-realms/
- **Description**: Automated issue management, XP tracking, and gamification bot for Shadowed Realms RPG development

#### Webhook:
- **Webhook URL**: https://your-backend-url.com/webhooks/github
- **Webhook secret**: [Generate a strong secret]
- **SSL verification**: Enable

#### Permissions:

##### Repository permissions:
- **Actions**: Read & Write (manage workflows)
- **Checks**: Read & Write (CI/CD status)
- **Contents**: Read & Write (update files)
- **Issues**: Read & Write (create/update issues)
- **Metadata**: Read (required)
- **Projects**: Read & Write (manage project boards)
- **Pull requests**: Read & Write

##### Organization permissions:
- **Members**: Read (team access)
- **Projects**: Read & Write (org-level projects)

#### Subscribe to events:
- ✅ Issues
- ✅ Issue comment
- ✅ Project
- ✅ Project card
- ✅ Project column
- ✅ Pull request
- ✅ Pull request review
- ✅ Push
- ✅ Workflow run

#### Where can this GitHub App be installed?
- Only on this account

### 2. Generate Private Key
After creating, download the private key (.pem file)

### 3. Installation
Install the app on the michael-placeholder/shadowed-realms repository

### 4. Backend Implementation

```javascript
// github-app.js
const { App } = require('@octokit/app');
const { Octokit } = require('@octokit/rest');

class ShadowedRealmsBot {
  constructor() {
    this.app = new App({
      appId: process.env.GITHUB_APP_ID,
      privateKey: process.env.GITHUB_APP_PRIVATE_KEY,
      webhooks: {
        secret: process.env.GITHUB_WEBHOOK_SECRET
      }
    });
  }

  // Handle webhook events
  async handleWebhook(event, payload) {
    switch(event) {
      case 'issues.closed':
        await this.onIssueClosed(payload);
        break;
      case 'issues.opened':
        await this.onIssueOpened(payload);
        break;
      case 'project_card.moved':
        await this.onCardMoved(payload);
        break;
    }
  }

  // Award XP when issue is closed
  async onIssueClosed(payload) {
    const issue = payload.issue;
    const labels = issue.labels.map(l => l.name);
    
    // Extract XP from labels
    const xpLabel = labels.find(l => l.startsWith('xp-'));
    const xp = xpLabel ? parseInt(xpLabel.replace('xp-', '')) : 0;
    
    // Extract coins from labels
    const coinsLabel = labels.find(l => l.startsWith('coins-'));
    const coins = coinsLabel ? parseInt(coinsLabel.replace('coins-', '')) : 0;
    
    // Update user stats (stored in database)
    await this.updateUserStats(payload.sender.login, {
      xp: xp,
      coins: coins,
      issuesClosed: 1
    });
    
    // Check for memory fragment unlocks
    await this.checkMemoryUnlocks(payload.sender.login);
    
    // Post congratulations comment
    const octokit = await this.app.getInstallationOctokit(payload.installation.id);
    await octokit.issues.createComment({
      owner: payload.repository.owner.login,
      repo: payload.repository.name,
      issue_number: issue.number,
      body: `🎮 **Quest Complete!**\n\n` +
            `**${payload.sender.login}** earned:\n` +
            `- 🌟 **${xp} XP**\n` +
            `- 🪙 **${coins} coins**\n\n` +
            `*Keep pushing forward, chosen undead!*`
    });
  }

  // Auto-label new issues
  async onIssueOpened(payload) {
    const issue = payload.issue;
    const title = issue.title;
    
    const labels = [];
    
    // Detect issue type from title
    if (title.includes('[EPIC]')) labels.push('epic');
    if (title.includes('[USER-STORY]')) labels.push('user-story');
    if (title.includes('[TASK]')) labels.push('task');
    if (title.includes('[ISSUE]')) labels.push('issue', 'micro-task');
    
    // Detect sprint from title
    if (title.includes('Sprint 1')) labels.push('sprint-1');
    if (title.includes('Sprint 2')) labels.push('sprint-2');
    if (title.includes('Sprint 3')) labels.push('sprint-3');
    
    // Apply labels
    const octokit = await this.app.getInstallationOctokit(payload.installation.id);
    await octokit.issues.addLabels({
      owner: payload.repository.owner.login,
      repo: payload.repository.name,
      issue_number: issue.number,
      labels: labels
    });
  }

  // Track project board movements
  async onCardMoved(payload) {
    const card = payload.project_card;
    const column = payload.project_column;
    
    // Award bonus XP for moving to "Done" column
    if (column.name === 'Done') {
      // Extract issue from card
      const issueUrl = card.content_url;
      const issueNumber = issueUrl.split('/').pop();
      
      // Award completion bonus
      await this.awardCompletionBonus(issueNumber);
    }
  }

  // Update user statistics
  async updateUserStats(username, stats) {
    // Store in database (PostgreSQL/MongoDB)
    // Track: total XP, coins, issues closed, current level, etc.
  }

  // Check for memory fragment unlocks
  async checkMemoryUnlocks(username) {
    // Check if user has reached XP thresholds
    // Unlock memory fragments at specific milestones
    // Post special announcement when unlocked
  }
}

// Express webhook handler
app.post('/webhooks/github', (req, res) => {
  const event = req.headers['x-github-event'];
  const payload = req.body;
  
  bot.handleWebhook(event, payload);
  
  res.status(200).send('OK');
});
```

### 5. Automation Features

#### Automatic Features:
1. **XP & Coin Distribution**: Automatically award when issues close
2. **Level Progression**: Calculate and update user levels
3. **Memory Unlocks**: Trigger story fragments at milestones
4. **Sprint Tracking**: Move issues between sprints automatically
5. **Daily Standups**: Create daily standup issues
6. **Revenue Tracking**: Update financial metrics from completed assets
7. **Skill Progress**: Track specialization paths
8. **Leaderboards**: Update rankings in real-time

#### Bot Commands (via comments):
- `/xp @user 100` - Award bonus XP
- `/coins @user 50` - Award bonus coins
- `/memory unlock 5` - Unlock memory fragment
- `/sprint move 2` - Move issue to Sprint 2
- `/estimate 4h` - Set time estimate
- `/assign @user` - Assign issue
- `/block #123` - Mark as blocked by issue
- `/asset-value $150` - Set asset market value

### 6. Dashboard Integration

```javascript
// dashboard-integration.js
class DashboardGitHubApp {
  constructor(installationId) {
    this.installationId = installationId;
  }
  
  // Get real-time stats
  async getUserStats(username) {
    const response = await fetch(`/api/stats/${username}`);
    return response.json();
  }
  
  // Display XP progress
  async updateXPBar() {
    const stats = await this.getUserStats(currentUser);
    const xpBar = document.getElementById('xp-progress');
    const level = Math.floor(stats.xp / 1000);
    const progress = (stats.xp % 1000) / 10;
    
    xpBar.style.width = `${progress}%`;
    xpBar.textContent = `Level ${level} - ${stats.xp} XP`;
  }
  
  // Show memory fragments
  async displayMemories() {
    const memories = await fetch('/api/memories/unlocked');
    const memoryContainer = document.getElementById('memories');
    
    memories.forEach(memory => {
      const fragment = document.createElement('div');
      fragment.className = 'memory-fragment unlocked';
      fragment.innerHTML = `
        <h3>Memory #${memory.id}: ${memory.title}</h3>
        <p>${memory.content}</p>
        <span class="unlock-date">${memory.unlockedAt}</span>
      `;
      memoryContainer.appendChild(fragment);
    });
  }
}
```

## Benefits of GitHub App:
1. ✅ Automated XP/coin distribution
2. ✅ Real-time progress tracking
3. ✅ Memory fragment unlocks
4. ✅ Sprint automation
5. ✅ Revenue tracking
6. ✅ Skill specialization paths
7. ✅ Team collaboration features
8. ✅ Leaderboards and achievements
9. ✅ Daily standup automation
10. ✅ Financial metrics dashboard

## Installation URL:
Once created, share: https://github.com/apps/shadowed-realms-bot

## Required Backend Services:
- Node.js server for webhooks
- PostgreSQL for user stats
- Redis for caching
- Express API endpoints
