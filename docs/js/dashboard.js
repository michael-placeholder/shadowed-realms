// GitHub Integration for Shadowed Realms Dashboard
// Complete gamification system with XP, coins, and memory fragments

class ShadowedRealmsDashboard {
  constructor() {
    this.repo = 'michael-placeholder/shadowed-realms';
    this.currentUser = null;
    this.stats = {
      xp: 0,
      coins: 0,
      level: 1,
      issuesClosed: 0,
      memories: [],
      skills: {}
    };
    this.init();
  }

  async init() {
    await this.loadUserData();
    await this.fetchIssues();
    await this.updateDashboard();
    this.setupEventListeners();
  }

  // Load user data from localStorage or API
  async loadUserData() {
    const savedStats = localStorage.getItem('shadowedRealmsStats');
    if (savedStats) {
      this.stats = JSON.parse(savedStats);
    }
    
    // Get GitHub username
    const token = localStorage.getItem('github_token');
    if (token) {
      const response = await fetch('https://api.github.com/user', {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Accept': 'application/vnd.github.v3+json'
        }
      });
      const user = await response.json();
      this.currentUser = user.login;
    }
  }

  // Fetch issues and calculate available XP/coins
  async fetchIssues() {
    const response = await fetch(`https://api.github.com/repos/${this.repo}/issues?state=open&per_page=100`, {
      headers: {
        'Accept': 'application/vnd.github.v3+json'
      }
    });
    
    const issues = await response.json();
    this.displayTasks(issues);
    this.calculateTotalRewards(issues);
  }

  // Display tasks in the dashboard
  displayTasks(issues) {
    const taskContainer = document.getElementById('task-list');
    if (!taskContainer) return;
    
    taskContainer.innerHTML = '';
    
    // Group by type
    const epics = issues.filter(i => i.labels.some(l => l.name === 'epic'));
    const userStories = issues.filter(i => i.labels.some(l => l.name === 'user-story'));
    const tasks = issues.filter(i => i.labels.some(l => l.name === 'task'));
    const microTasks = issues.filter(i => i.labels.some(l => l.name === 'micro-task'));
    
    // Display by category
    this.renderTaskSection('Epics', epics, 'epic-section');
    this.renderTaskSection('User Stories', userStories, 'story-section');
    this.renderTaskSection('Tasks', tasks, 'task-section');
    this.renderTaskSection('Micro-Tasks', microTasks, 'micro-section');
  }

  renderTaskSection(title, issues, className) {
    const container = document.getElementById('task-list');
    if (!container) return;
    
    const section = document.createElement('div');
    section.className = `task-section ${className}`;
    section.innerHTML = `
      <h3 class="section-title">${title} (${issues.length})</h3>
      <div class="task-grid">
        ${issues.map(issue => this.renderTaskCard(issue)).join('')}
      </div>
    `;
    
    container.appendChild(section);
  }

  renderTaskCard(issue) {
    const xp = this.extractXP(issue.labels);
    const coins = this.extractCoins(issue.labels);
    const sprint = this.extractSprint(issue.labels);
    
    return `
      <div class="task-card" data-issue-id="${issue.number}">
        <div class="task-header">
          <span class="task-number">#${issue.number}</span>
          <span class="task-sprint sprint-${sprint}">Sprint ${sprint}</span>
        </div>
        <h4 class="task-title">${issue.title}</h4>
        <div class="task-rewards">
          <span class="xp-reward">🌟 ${xp} XP</span>
          <span class="coin-reward">🪙 ${coins} coins</span>
        </div>
        <div class="task-labels">
          ${issue.labels.map(l => `<span class="label" style="background-color: #${l.color}">${l.name}</span>`).join('')}
        </div>
        <div class="task-actions">
          <button class="btn-claim" onclick="dashboard.claimTask(${issue.number})">Claim Task</button>
          <a href="${issue.html_url}" target="_blank" class="btn-view">View on GitHub</a>
        </div>
      </div>
    `;
  }

  extractXP(labels) {
    const xpLabel = labels.find(l => l.name.startsWith('xp-'));
    return xpLabel ? parseInt(xpLabel.name.replace('xp-', '')) : 25;
  }

  extractCoins(labels) {
    const coinsLabel = labels.find(l => l.name.startsWith('coins-'));
    return coinsLabel ? parseInt(coinsLabel.name.replace('coins-', '')) : 10;
  }

  extractSprint(labels) {
    const sprintLabel = labels.find(l => l.name.startsWith('sprint-'));
    return sprintLabel ? parseInt(sprintLabel.name.replace('sprint-', '')) : 1;
  }

  // Calculate total available rewards
  calculateTotalRewards(issues) {
    let totalXP = 0;
    let totalCoins = 0;
    
    issues.forEach(issue => {
      totalXP += this.extractXP(issue.labels);
      totalCoins += this.extractCoins(issue.labels);
    });
    
    const xpElement = document.getElementById('total-xp');
    const coinsElement = document.getElementById('total-coins');
    const issuesElement = document.getElementById('open-issues');
    
    if (xpElement) xpElement.textContent = totalXP.toLocaleString();
    if (coinsElement) coinsElement.textContent = totalCoins.toLocaleString();
    if (issuesElement) issuesElement.textContent = issues.length;
  }

  // Update dashboard UI
  async updateDashboard() {
    // Update XP bar
    const level = Math.floor(this.stats.xp / 1000);
    const progress = (this.stats.xp % 1000) / 10;
    
    const levelElement = document.getElementById('user-level');
    const xpElement = document.getElementById('user-xp');
    const progressElement = document.getElementById('xp-progress');
    
    if (levelElement) levelElement.textContent = level;
    if (xpElement) xpElement.textContent = this.stats.xp.toLocaleString();
    if (progressElement) progressElement.style.width = `${progress}%`;
    
    // Update coins
    const coinsElement = document.getElementById('user-coins');
    if (coinsElement) coinsElement.textContent = this.stats.coins.toLocaleString();
    
    // Update memory fragments
    this.displayMemoryFragments();
    
    // Update skill specializations
    this.displaySkills();
    
    // Calculate portfolio value
    this.calculatePortfolioValue();
  }

  // Display unlocked memory fragments
  displayMemoryFragments() {
    const container = document.getElementById('memory-container');
    if (!container) return;
    
    container.innerHTML = '';
    
    for (let i = 1; i <= 49; i++) {
      const fragment = document.createElement('div');
      fragment.className = `memory-fragment ${this.stats.memories.includes(i) ? 'unlocked' : 'locked'}`;
      fragment.innerHTML = `
        <div class="memory-number">${i}</div>
        ${this.stats.memories.includes(i) ? 
          `<div class="memory-title">Memory #${i}</div>` : 
          `<div class="memory-locked">🔒</div>`
        }
      `;
      
      if (this.stats.memories.includes(i)) {
        fragment.onclick = () => this.showMemoryStory(i);
      }
      
      container.appendChild(fragment);
    }
  }

  // Show memory story modal
  showMemoryStory(memoryId) {
    const stories = {
      1: "The Beginning - You stand at the threshold of creation...",
      2: "First Steps - The path forward becomes clear...",
      3: "Foundation - Stone by stone, the edifice rises...",
      // Add all 49 memory stories
    };
    
    const modal = document.getElementById('memory-modal');
    if (!modal) return;
    
    modal.innerHTML = `
      <div class="modal-content">
        <h2>Memory Fragment #${memoryId}</h2>
        <p class="memory-story">${stories[memoryId] || 'Story to be revealed...'}</p>
        <button onclick="this.parentElement.parentElement.style.display='none'">Close</button>
      </div>
    `;
    modal.style.display = 'block';
  }

  // Display skill specializations
  displaySkills() {
    const container = document.getElementById('skills-container');
    if (!container) return;
    
    const skills = ['Maya', 'Unity', 'Unreal', 'Python', 'React', 'TCG Design'];
    
    container.innerHTML = skills.map(skill => `
      <div class="skill-track">
        <h4>${skill}</h4>
        <div class="skill-progress">
          <div class="skill-bar" style="width: ${(this.stats.skills[skill] || 0)}%"></div>
        </div>
        <span class="skill-level">${this.getSkillLevel(this.stats.skills[skill] || 0)}</span>
      </div>
    `).join('');
  }

  getSkillLevel(progress) {
    if (progress < 25) return 'Novice';
    if (progress < 50) return 'Apprentice';
    if (progress < 75) return 'Journeyman';
    if (progress < 100) return 'Expert';
    return 'Master';
  }

  // Calculate portfolio value based on completed assets
  calculatePortfolioValue() {
    const assetValues = {
      'character-model': 120,
      'environment': 150,
      'animation': 95,
      'script': 125,
      'gui-tool': 180,
      'tutorial': 97,
      'tcg-card': 5
    };
    
    let totalValue = 0;
    // Calculate based on completed issues
    // This would query completed issues and sum their asset values
    
    const valueElement = document.getElementById('portfolio-value');
    if (valueElement) valueElement.textContent = `$${totalValue.toLocaleString()}`;
  }

  // Claim a task (assign to user)
  async claimTask(issueNumber) {
    const token = localStorage.getItem('github_token');
    if (!token) {
      alert('Please log in with GitHub to claim tasks');
      return;
    }
    
    try {
      const response = await fetch(`https://api.github.com/repos/${this.repo}/issues/${issueNumber}/assignees`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Accept': 'application/vnd.github.v3+json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          assignees: [this.currentUser]
        })
      });
      
      if (response.ok) {
        alert(`Task #${issueNumber} claimed! Get to work, chosen undead!`);
        this.fetchIssues(); // Refresh
      }
    } catch (error) {
      console.error('Error claiming task:', error);
    }
  }

  // Complete a task (close issue and award XP/coins)
  async completeTask(issueNumber) {
    const token = localStorage.getItem('github_token');
    if (!token) return;
    
    // Close the issue
    const response = await fetch(`https://api.github.com/repos/${this.repo}/issues/${issueNumber}`, {
      method: 'PATCH',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Accept': 'application/vnd.github.v3+json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        state: 'closed'
      })
    });
    
    if (response.ok) {
      // Award XP and coins (would be handled by GitHub App webhook in production)
      const issue = await response.json();
      const xp = this.extractXP(issue.labels);
      const coins = this.extractCoins(issue.labels);
      
      this.stats.xp += xp;
      this.stats.coins += coins;
      this.stats.issuesClosed += 1;
      
      // Check for memory unlocks
      this.checkMemoryUnlocks();
      
      // Save stats
      localStorage.setItem('shadowedRealmsStats', JSON.stringify(this.stats));
      
      // Update UI
      this.updateDashboard();
      
      // Show reward notification
      this.showRewardNotification(xp, coins);
    }
  }

  // Check if new memory fragments should be unlocked
  checkMemoryUnlocks() {
    const memoryThresholds = {
      1: 100,    // First memory at 100 XP
      2: 500,
      3: 1000,
      4: 2000,
      5: 3500,
      // ... add all 49 thresholds
    };
    
    Object.entries(memoryThresholds).forEach(([id, threshold]) => {
      if (this.stats.xp >= threshold && !this.stats.memories.includes(parseInt(id))) {
        this.stats.memories.push(parseInt(id));
        this.showMemoryUnlockNotification(id);
      }
    });
  }

  // Show reward notification
  showRewardNotification(xp, coins) {
    const notification = document.createElement('div');
    notification.className = 'reward-notification';
    notification.innerHTML = `
      <h3>Quest Complete!</h3>
      <div class="rewards">
        <span>+${xp} XP</span>
        <span>+${coins} coins</span>
      </div>
    `;
    
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 3000);
  }

  // Show memory unlock notification
  showMemoryUnlockNotification(memoryId) {
    const notification = document.createElement('div');
    notification.className = 'memory-unlock-notification';
    notification.innerHTML = `
      <h3>Memory Fragment Unlocked!</h3>
      <div class="memory-icon">🧩</div>
      <p>Memory #${memoryId} has been restored</p>
    `;
    
    document.body.appendChild(notification);
    setTimeout(() => notification.remove(), 5000);
  }

  // Setup event listeners
  setupEventListeners() {
    // Sprint filter
    document.getElementById('sprint-filter')?.addEventListener('change', (e) => {
      this.filterBySprint(e.target.value);
    });
    
    // Task type filter
    document.getElementById('type-filter')?.addEventListener('change', (e) => {
      this.filterByType(e.target.value);
    });
    
    // Search
    document.getElementById('task-search')?.addEventListener('input', (e) => {
      this.searchTasks(e.target.value);
    });
  }

  // Filter tasks by sprint
  filterBySprint(sprint) {
    const cards = document.querySelectorAll('.task-card');
    cards.forEach(card => {
      const cardSprint = card.querySelector('.task-sprint').textContent;
      card.style.display = sprint === 'all' || cardSprint.includes(sprint) ? 'block' : 'none';
    });
  }

  // Filter tasks by type
  filterByType(type) {
    const sections = document.querySelectorAll('.task-section');
    sections.forEach(section => {
      section.style.display = type === 'all' || section.classList.contains(type) ? 'block' : 'none';
    });
  }

  // Search tasks
  searchTasks(query) {
    const cards = document.querySelectorAll('.task-card');
    const lowerQuery = query.toLowerCase();
    
    cards.forEach(card => {
      const title = card.querySelector('.task-title').textContent.toLowerCase();
      card.style.display = title.includes(lowerQuery) ? 'block' : 'none';
    });
  }
}

// Initialize dashboard on load
const dashboard = new ShadowedRealmsDashboard();

// Export for use in other modules
window.ShadowedRealmsDashboard = ShadowedRealmsDashboard;
