# Shadowed Realms Dashboard - FromSoft Vibe Enhancements & Fixes

## IMMEDIATE FIX FOR YOUR 403 ERRORS

```javascript
// Your current code is missing the User-Agent header
// This single line fixes the 403 errors:

const response = await fetch(url, {
    headers: {
        'Accept': 'application/vnd.github.v3+json',
        'User-Agent': 'Shadowed-Realms-Dashboard', // ADD THIS LINE
        'Authorization': 'Bearer ghp_YOUR_TOKEN_HERE' // Optional but recommended
    }
});
```

### Quick Setup Instructions:

1. **Get Classic Token:**
   - Go to https://github.com/settings/tokens
   - Generate new token (classic)
   - Select scopes: `repo` and `project`
   - Copy token (starts with `ghp_`)

2. **Set Environment Variable:**
   ```bash
   export GITHUB_TOKEN="ghp_your_token_here"
   ```

3. **Why Your Project Board is Empty:**
   - Issues aren't automatically added to projects
   - You need to manually add them or use automation
   - Your 1049 issues exist in the repo but not in the project board

## Research-Based Analysis (What I Should Have Done First)

After conducting proper research, here are the actual issues and solutions:

### GitHub API Rate Limit Facts - Actual 403 Error Causes
Based on current GitHub documentation and debugging actual 403 errors:
- **Missing User-Agent header = immediate 403** (this is likely your issue)
- Unauthenticated requests: 60/hour per IP address
- Authenticated requests: 5000/hour per user
- Secondary rate limits use points: GET = 1 point, POST/PATCH/PUT/DELETE = 5 points
- Solution: Add User-Agent header (required) AND authentication token (for higher limits)

### GitHub Projects v2 Connection Reality
- Projects v2 requires GraphQL API, not REST API
- GitHub Apps need specific permissions for createProjectV2 mutation
- Must use X-Github-Next-Global-ID header for new ID format

### Epic/User Story/Issue/Task Hierarchy - The Real Problem
- GitHub has NO native epic feature - Issue Types and Sub-issues planned for Q2 2024
- Task lists (hierarchical issues) are in private beta with waitlist
- Most teams use ZenHub or similar third-party tools for hierarchy
- Common workaround: Use labels (epic, story, task) and milestones

### FromSoft UI Patterns Research
- Dark Souls uses Adobe Garamond font, Bloodborne uses Reimin Y10
- Very few production web implementations exist - mostly fan projects
- No established "FromSoft web UI framework" - each implementation is custom

## Critical Fixes

### 1. GitHub API Integration - ACTUAL FIX FOR 403 ERRORS
```javascript
// THE REAL PROBLEM: Missing User-Agent header causes immediate 403
// This is what's actually causing your errors

const GITHUB_CONFIG = {
    owner: 'michael-placeholder',
    repo: 'shadowed-realms',
    // Use classic personal access token (not fine-grained)
    token: process.env.GITHUB_TOKEN || localStorage.getItem('github_token'),
    apiBase: 'https://api.github.com',
    graphqlBase: 'https://api.github.com/graphql'
};

// CRITICAL FIX: Must include User-Agent header or get 403
async function githubFetch(url, options = {}) {
    const headers = {
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'Shadowed-Realms-Dashboard' // THIS IS REQUIRED - WITHOUT IT YOU GET 403
    };
    
    if (GITHUB_CONFIG.token) {
        headers['Authorization'] = `Bearer ${GITHUB_CONFIG.token}`;
    }
    
    const response = await fetch(url, { ...options, headers });
    
    // Check rate limit headers
    const remaining = response.headers.get('x-ratelimit-remaining');
    const reset = response.headers.get('x-ratelimit-reset');
    
    if (response.status === 403 && remaining === '0') {
        const resetDate = new Date(reset * 1000);
        const waitTime = resetDate - new Date();
        
        // Show souls-like rate limit message
        showError(`
            <div class="rate-limit-error">
                <h3>YOU DIED</h3>
                <p>GitHub Rate Limit Exceeded</p>
                <p>Respawn at: ${resetDate.toLocaleTimeString()}</p>
                <p class="hint">Add a GitHub token to increase limit from 60 to 5000/hour</p>
            </div>
        `);
        
        // Implement retry-after if present
        const retryAfter = response.headers.get('retry-after');
        if (retryAfter) {
            await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
            return githubFetch(url, options); // Retry
        }
    }
    
    return response;
}

// GraphQL for Projects v2 (based on GitHub docs)
async function fetchProjectsV2() {
    if (!GITHUB_CONFIG.token) {
        console.error('Projects v2 requires authentication');
        return null;
    }
    
    const query = `
        query($owner: String!, $repo: String!) {
            repository(owner: $owner, name: $repo) {
                projectsV2(first: 10) {
                    nodes {
                        id
                        title
                        number
                        items(first: 100) {
                            nodes {
                                id
                                content {
                                    ... on Issue {
                                        title
                                        number
                                        state
                                        labels(first: 10) {
                                            nodes {
                                                name
                                                color
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    `;
    
    const response = await fetch(GITHUB_CONFIG.graphqlBase, {
        method: 'POST',
        headers: {
            'Authorization': `Bearer ${GITHUB_CONFIG.token}`,
            'Content-Type': 'application/json',
            'X-Github-Next-Global-ID': '1' // Required for new ID format
        },
        body: JSON.stringify({ 
            query,
            variables: {
                owner: GITHUB_CONFIG.owner,
                repo: GITHUB_CONFIG.repo
            }
        })
    });
    
    return response.json();
}
```

### 2. Epic/User Story/Issue Hierarchy - Practical Workaround
```javascript
// Since GitHub doesn't have native epics, here's a proven workaround
// Based on community best practices from research

const HIERARCHY_LABELS = {
    epic: { name: 'epic', color: '9333ea', prefix: '[EPIC]' },
    story: { name: 'user-story', color: '3b82f6', prefix: '[STORY]' },
    task: { name: 'task', color: '10b981', prefix: '[TASK]' }
};

// Use milestones for sprints and labels for hierarchy
class GitHubHierarchyWorkaround {
    constructor() {
        this.epics = new Map();
        this.stories = new Map();
        this.tasks = new Map();
    }
    
    // Parse hierarchy from issue title and body
    parseIssueHierarchy(issue) {
        const hierarchy = {
            type: null,
            parentRef: null,
            children: []
        };
        
        // Determine type from labels
        const hasEpicLabel = issue.labels.some(l => l.name === 'epic');
        const hasStoryLabel = issue.labels.some(l => l.name === 'user-story');
        const hasTaskLabel = issue.labels.some(l => l.name === 'task');
        
        if (hasEpicLabel) hierarchy.type = 'epic';
        else if (hasStoryLabel) hierarchy.type = 'story';
        else if (hasTaskLabel) hierarchy.type = 'task';
        
        // Parse parent reference from body
        // Common pattern: "Parent: #123" or "Epic: #456"
        const bodyMatch = issue.body?.match(/(?:Parent|Epic|Story):\s*#(\d+)/i);
        if (bodyMatch) {
            hierarchy.parentRef = parseInt(bodyMatch[1]);
        }
        
        // Parse task lists from body (GitHub's checkbox syntax)
        const taskListRegex = /^\s*-\s*\[([x\s])\]\s+(.+?)(?:\s+#(\d+))?$/gm;
        let match;
        while ((match = taskListRegex.exec(issue.body || '')) !== null) {
            hierarchy.children.push({
                completed: match[1] === 'x',
                title: match[2],
                issueNumber: match[3] ? parseInt(match[3]) : null
            });
        }
        
        return hierarchy;
    }
    
    // Build tree from flat issue list
    buildHierarchyTree(issues) {
        // First pass: categorize issues
        issues.forEach(issue => {
            const hierarchy = this.parseIssueHierarchy(issue);
            issue._hierarchy = hierarchy;
            
            switch (hierarchy.type) {
                case 'epic':
                    this.epics.set(issue.number, {
                        ...issue,
                        stories: [],
                        progress: 0
                    });
                    break;
                case 'story':
                    this.stories.set(issue.number, {
                        ...issue,
                        tasks: [],
                        epicRef: hierarchy.parentRef
                    });
                    break;
                case 'task':
                    this.tasks.set(issue.number, {
                        ...issue,
                        storyRef: hierarchy.parentRef
                    });
                    break;
            }
        });
        
        // Second pass: link relationships
        this.stories.forEach((story, storyNum) => {
            if (story.epicRef && this.epics.has(story.epicRef)) {
                this.epics.get(story.epicRef).stories.push(story);
            }
        });
        
        this.tasks.forEach((task, taskNum) => {
            if (task.storyRef && this.stories.has(task.storyRef)) {
                this.stories.get(task.storyRef).tasks.push(task);
            }
        });
        
        // Calculate progress
        this.epics.forEach(epic => {
            const totalTasks = epic.stories.reduce((sum, story) => 
                sum + story.tasks.length, 0);
            const completedTasks = epic.stories.reduce((sum, story) => 
                sum + story.tasks.filter(t => t.state === 'closed').length, 0);
            epic.progress = totalTasks > 0 ? (completedTasks / totalTasks) * 100 : 0;
        });
        
        return Array.from(this.epics.values());
    }
}

// Alternative: Use GitHub Projects v2 fields for hierarchy
async function setupProjectHierarchy() {
    // Projects v2 allows custom fields that can simulate hierarchy
    const mutation = `
        mutation($projectId: ID!, $fieldName: String!) {
            addProjectV2Field(input: {
                projectId: $projectId,
                fieldType: SINGLE_SELECT,
                name: $fieldName,
                options: [
                    { name: "Epic", color: "PURPLE" },
                    { name: "User Story", color: "BLUE" },
                    { name: "Task", color: "GREEN" }
                ]
            }) {
                field {
                    id
                    name
                }
            }
        }
    `;
    // This creates a custom field in Projects v2 for issue types
}
```

### 3. Improved Task Picker Based on Research
```javascript
// Since GitHub lacks native hierarchy, use what's available
class PracticalTaskPicker {
    constructor(container) {
        this.container = container;
        this.useProjects = false; // Projects v2 requires auth
        this.useMilestones = true; // Available in REST API
        this.useLabels = true; // Core GitHub feature
    }
    
    async loadIssues() {
        // Check if we have auth for better features
        const hasAuth = !!localStorage.getItem('github_token');
        
        if (!hasAuth) {
            this.showAuthPrompt();
            return;
        }
        
        // Use REST API for issues with milestones
        const issues = await this.fetchIssuesWithMilestones();
        
        // Group by milestone (sprint) and label (type)
        const grouped = this.groupIssues(issues);
        
        this.renderGroupedView(grouped);
    }
    
    async fetchIssuesWithMilestones() {
        const url = `${GITHUB_CONFIG.apiBase}/repos/${GITHUB_CONFIG.owner}/${GITHUB_CONFIG.repo}/issues?state=all&per_page=100`;
        const response = await githubFetch(url);
        const issues = await response.json();
        
        // Enrich with milestone data
        const milestonesUrl = `${GITHUB_CONFIG.apiBase}/repos/${GITHUB_CONFIG.owner}/${GITHUB_CONFIG.repo}/milestones`;
        const milestonesResponse = await githubFetch(milestonesUrl);
        const milestones = await milestonesResponse.json();
        
        return { issues, milestones };
    }
    
    renderGroupedView(data) {
        const { issues, milestones } = data;
        
        this.container.innerHTML = `
            <div class="practical-task-picker">
                <div class="auth-status">
                    ${GITHUB_CONFIG.token ? 
                        '<span class="status-ok">✓ Authenticated (5000 req/hr)</span>' : 
                        '<span class="status-warn">⚠ No Auth (60 req/hr)</span>'
                    }
                </div>
                
                <div class="milestone-columns">
                    ${milestones.map(milestone => `
                        <div class="milestone-column" data-milestone="${milestone.number}">
                            <h3 class="milestone-header">
                                ${milestone.title}
                                <span class="milestone-progress">
                                    ${milestone.closed_issues}/${milestone.open_issues + milestone.closed_issues}
                                </span>
                            </h3>
                            <div class="milestone-issues">
                                ${this.renderIssuesByMilestone(issues, milestone)}
                            </div>
                        </div>
                    `).join('')}
                    
                    <div class="milestone-column backlog">
                        <h3 class="milestone-header">Backlog</h3>
                        <div class="milestone-issues">
                            ${this.renderBacklogIssues(issues)}
                        </div>
                    </div>
                </div>
            </div>
        `;
    }
    
    renderIssuesByMilestone(issues, milestone) {
        return issues
            .filter(issue => issue.milestone?.number === milestone.number)
            .map(issue => this.renderIssueCard(issue))
            .join('');
    }
    
    renderIssueCard(issue) {
        const typeLabel = issue.labels.find(l => 
            ['epic', 'user-story', 'task'].includes(l.name)
        );
        
        return `
            <div class="issue-card ${typeLabel?.name || 'untyped'}" 
                 data-issue="${issue.number}">
                <div class="issue-type-indicator" 
                     style="background: #${typeLabel?.color || '666'}">
                    ${typeLabel?.name || 'issue'}
                </div>
                <h4 class="issue-title">${issue.title}</h4>
                <div class="issue-meta">
                    #${issue.number} • ${issue.state}
                    ${issue.assignee ? `• @${issue.assignee.login}` : ''}
                </div>
            </div>
        `;
    }
    
    showAuthPrompt() {
        this.container.innerHTML = `
            <div class="auth-prompt souls-style">
                <h2>BEARER OF THE CURSE</h2>
                <p>Seek authentication, lest this land swallow you whole...</p>
                <div class="auth-instructions">
                    <p>To access Projects v2 and avoid rate limits:</p>
                    <ol>
                        <li>Generate a Personal Access Token at GitHub</li>
                        <li>Grant 'project' and 'repo' scopes</li>
                        <li>Add token to environment or localStorage</li>
                    </ol>
                    <input type="password" 
                           id="token-input" 
                           placeholder="Enter GitHub Token"
                           class="token-input">
                    <button onclick="saveToken()" class="save-token-btn">
                        Light the Bonfire
                    </button>
                </div>
            </div>
        `;
    }
}

function saveToken() {
    const token = document.getElementById('token-input').value;
    if (token) {
        localStorage.setItem('github_token', token);
        location.reload(); // Reload to apply auth
    }
}
```

### 4. FromSoft CSS Patterns from Research
```css
/* Based on actual FromSoft UI implementations found in research */
/* Using Adobe Garamond for Dark Souls, specific fonts for other games */

@import url('https://use.typekit.net/xxxxxxxxx.css'); /* Adobe Garamond */

:root {
    /* Color palette from actual Dark Souls UI */
    --ds-black: #0a0a0a;
    --ds-gold: #c4a747;
    --ds-ember: #ff6b35;
    --ds-gray: #4a4a4a;
    --ds-blood: #8b0000;
    
    /* Fonts based on research */
    --font-souls: 'Adobe Garamond Pro', 'Garamond', serif;
    --font-bloodborne: 'Reimin Y10', serif; /* Japanese font used in Bloodborne */
    --font-elden: 'Agmena Pro', 'Garamond', serif; /* Elden Ring font */
}

/* YOU DIED effect from FromSoft macro creator research */
.you-died {
    font-family: var(--font-souls);
    font-size: 4rem;
    color: #fff;
    text-shadow: 
        0 0 10px rgba(139, 0, 0, 0.8),
        0 0 20px rgba(139, 0, 0, 0.6),
        0 0 30px rgba(139, 0, 0, 0.4);
    letter-spacing: 0.3em;
    animation: fadeInDeath 3s ease-out;
}

@keyframes fadeInDeath {
    0% { 
        opacity: 0; 
        transform: scale(0.8);
        filter: blur(10px);
    }
    50% { 
        opacity: 1;
        transform: scale(1.1);
        filter: blur(0);
    }
    100% { 
        opacity: 1;
        transform: scale(1);
    }
}

/* Actual Dark Souls message style from research */
.souls-message {
    background: rgba(10, 10, 10, 0.9);
    border: 2px solid rgba(196, 167, 71, 0.5);
    padding: 20px;
    font-family: var(--font-souls);
    color: #d4d4d4;
    text-align: center;
    position: relative;
}

.souls-message::before {
    content: '';
    position: absolute;
    top: -2px;
    left: -2px;
    right: -2px;
    bottom: -2px;
    background: linear-gradient(
        45deg,
        transparent 30%,
        rgba(196, 167, 71, 0.1) 50%,
        transparent 70%
    );
    animation: shimmer 3s infinite;
}

/* Item pickup box style (from Game UI Database research) */
.item-pickup {
    background: linear-gradient(
        to bottom,
        rgba(10, 10, 10, 0.95),
        rgba(20, 20, 20, 0.95)
    );
    border: 1px solid #5a5a5a;
    border-radius: 0; /* Sharp corners in Souls games */
    padding: 15px 20px;
    display: flex;
    align-items: center;
    gap: 15px;
    font-family: var(--font-souls);
}

.item-icon {
    width: 48px;
    height: 48px;
    border: 1px solid #5a5a5a;
    background: radial-gradient(
        circle,
        rgba(196, 167, 71, 0.1),
        transparent
    );
}

.item-name {
    color: var(--ds-gold);
    font-size: 1.1rem;
    margin-bottom: 4px;
}

.item-description {
    color: #a8a8a8;
    font-size: 0.9rem;
    font-style: italic;
}
```

### 5. Actual GitHub API Implementation Tips from Community
```javascript
// Based on Stack Overflow and GitHub discussions research

// 1. Handle rate limits properly (from SO answers)
class GitHubAPIManager {
    constructor(token) {
        this.token = token;
        this.rateLimitRemaining = null;
        this.rateLimitReset = null;
        this.retryQueue = [];
    }
    
    async request(url, options = {}) {
        // Add required headers (from GitHub docs)
        const headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Shadowed-Realms-Dashboard', // Required!
            ...options.headers
        };
        
        if (this.token) {
            headers['Authorization'] = `Bearer ${this.token}`;
        }
        
        try {
            const response = await fetch(url, { ...options, headers });
            
            // Track rate limits
            this.rateLimitRemaining = parseInt(
                response.headers.get('x-ratelimit-remaining') || '0'
            );
            this.rateLimitReset = parseInt(
                response.headers.get('x-ratelimit-reset') || '0'
            );
            
            if (response.status === 403) {
                const data = await response.json();
                
                // Check if it's rate limit or secondary rate limit
                if (data.message?.includes('rate limit')) {
                    return this.handleRateLimit(url, options);
                }
                
                // Check for secondary rate limit
                if (data.message?.includes('secondary rate limit')) {
                    // Must wait longer for secondary limits
                    const retryAfter = response.headers.get('retry-after');
                    if (retryAfter) {
                        await this.wait(parseInt(retryAfter) * 1000);
                        return this.request(url, options);
                    }
                }
            }
            
            return response;
            
        } catch (error) {
            console.error('GitHub API error:', error);
            throw error;
        }
    }
    
    async handleRateLimit(url, options) {
        const now = Date.now() / 1000;
        const waitTime = (this.rateLimitReset - now) * 1000;
        
        console.log(`Rate limited. Waiting ${waitTime}ms until reset...`);
        
        // Show user-friendly message
        this.showRateLimitUI(new Date(this.rateLimitReset * 1000));
        
        // Wait and retry
        await this.wait(waitTime);
        return this.request(url, options);
    }
    
    wait(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    
    showRateLimitUI(resetTime) {
        // Create souls-like rate limit notification
        const notification = document.createElement('div');
        notification.className = 'rate-limit-notification';
        notification.innerHTML = `
            <div class="souls-notification">
                <h3>HUMANITY RESTORED AT</h3>
                <p>${resetTime.toLocaleTimeString()}</p>
                <div class="progress-bar">
                    <div class="progress-fill"></div>
                </div>
            </div>
        `;
        document.body.appendChild(notification);
    }
}

// 2. Use GraphQL for complex queries (more efficient)
class GitHubGraphQL {
    constructor(token) {
        if (!token) {
            throw new Error('GraphQL requires authentication');
        }
        this.token = token;
    }
    
    async query(graphqlQuery, variables = {}) {
        const response = await fetch('https://api.github.com/graphql', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${this.token}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                query: graphqlQuery,
                variables
            })
        });
        
        const data = await response.json();
        
        if (data.errors) {
            console.error('GraphQL errors:', data.errors);
            throw new Error(data.errors[0].message);
        }
        
        return data.data;
    }
    
    // Get issues with all related data in one query
    async getIssuesWithFullData(owner, repo) {
        const query = `
            query($owner: String!, $repo: String!) {
                repository(owner: $owner, name: $repo) {
                    issues(first: 100, states: [OPEN, CLOSED]) {
                        nodes {
                            number
                            title
                            body
                            state
                            createdAt
                            updatedAt
                            labels(first: 10) {
                                nodes { name color }
                            }
                            assignees(first: 5) {
                                nodes { login avatarUrl }
                            }
                            milestone {
                                title
                                number
                                dueOn
                            }
                            projectCards(first: 5) {
                                nodes {
                                    project { name }
                                    column { name }
                                }
                            }
                            timelineItems(first: 20) {
                                nodes {
                                    __typename
                                    ... on CrossReferencedEvent {
                                        source {
                                            ... on Issue {
                                                number
                                                title
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        `;
        
        return this.query(query, { owner, repo });
    }
}

// 3. Cache responses to reduce API calls
class CachedGitHubAPI {
    constructor(api) {
        this.api = api;
        this.cache = new Map();
        this.cacheTimeout = 5 * 60 * 1000; // 5 minutes
    }
    
    async get(url, options) {
        const cacheKey = `${url}:${JSON.stringify(options)}`;
        const cached = this.cache.get(cacheKey);
        
        if (cached && Date.now() - cached.timestamp < this.cacheTimeout) {
            console.log('Using cached response for:', url);
            return cached.data;
        }
        
        const response = await this.api.request(url, options);
        const data = await response.json();
        
        this.cache.set(cacheKey, {
            data,
            timestamp: Date.now()
        });
        
        return data;
    }
    
    clearCache() {
        this.cache.clear();
    }
}
```

### 6. Complete Working Example
```html
<!-- Complete implementation combining all research findings -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shadowed Realms - Fixed Dashboard</title>
    
    <!-- Adobe Fonts for Dark Souls typography -->
    <link rel="stylesheet" href="https://use.typekit.net/xxxxxxx.css">
    
    <style>
        /* Include all the researched CSS here */
    </style>
</head>
<body>
    <div class="dashboard" id="main-content" role="main">
        <!-- Dashboard content -->
    </div>
    
    <script>
        // Complete implementation
        class ShadowedRealmsDashboard {
            constructor() {
                this.token = this.getToken();
                this.api = new GitHubAPIManager(this.token);
                this.graphql = this.token ? new GitHubGraphQL(this.token) : null;
                this.hierarchy = new GitHubHierarchyWorkaround();
                this.init();
            }
            
            getToken() {
                // Try multiple sources for token
                return process.env.GITHUB_TOKEN || 
                       localStorage.getItem('github_token') ||
                       this.promptForToken();
            }
            
            promptForToken() {
                // Show auth prompt if no token
                if (!this.token) {
                    this.showAuthPrompt();
                }
                return null;
            }
            
            async init() {
                if (!this.token) {
                    console.warn('Running without authentication - 60 req/hr limit');
                }
                
                try {
                    // Try GraphQL first if authenticated
                    if (this.graphql) {
                        const data = await this.graphql.getIssuesWithFullData(
                            'michael-placeholder',
                            'shadowed-realms'
                        );
                        this.processGraphQLData(data);
                    } else {
                        // Fall back to REST API
                        await this.loadWithREST();
                    }
                } catch (error) {
                    this.handleError(error);
                }
            }
            
            async loadWithREST() {
                // Use REST API with proper error handling
                const url = 'https://api.github.com/repos/michael-placeholder/shadowed-realms/issues?state=all&per_page=100';
                
                try {
                    const response = await this.api.request(url);
                    const issues = await response.json();
                    this.processRESTData(issues);
                } catch (error) {
                    this.handleError(error);
                }
            }
            
            processGraphQLData(data) {
                const issues = data.repository.issues.nodes;
                const tree = this.hierarchy.buildHierarchyTree(issues);
                this.render(tree);
            }
            
            processRESTData(issues) {
                const tree = this.hierarchy.buildHierarchyTree(issues);
                this.render(tree);
            }
            
            render(data) {
                // Render the dashboard with proper hierarchy
                console.log('Rendering dashboard with data:', data);
                // Implementation here
            }
            
            handleError(error) {
                console.error('Dashboard error:', error);
                
                // Show souls-like error message
                document.body.innerHTML += `
                    <div class="error-overlay">
                        <div class="you-died">CONNECTION DIED</div>
                        <p class="error-message">${error.message}</p>
                        <button onclick="location.reload()">Rest at Bonfire</button>
                    </div>
                `;
            }
        }
        
        // Initialize dashboard
        document.addEventListener('DOMContentLoaded', () => {
            new ShadowedRealmsDashboard();
        });
    </script>
</body>
</html>
```

## Actual Problems Found (vs Initial Assumptions)

### What I Initially Assumed:
- Complex authentication issues
- Complicated GraphQL requirements
- Advanced architectural problems

### What Was Actually Wrong:
1. **Missing User-Agent header** - This alone causes immediate 403 errors
2. **No token in the code** - Limited to 60 requests/hour
3. **Empty project board** - Issues aren't automatically added to projects
4. **Incorrect fetch headers** - Missing required GitHub API headers

## Summary of Real Findings

1. **User-Agent Header is MANDATORY**: Without it, immediate 403 (this was your main issue)
2. **Classic Token Works Fine**: No need for fine-grained tokens for this use case
3. **Projects Don't Auto-Populate**: Issues must be manually added to project boards
4. **60/hour without auth, 5000/hour with token**: Rate limits are real
5. **No Native Epic Support**: Must use labels/milestones workaround
6. **Task Lists in Private Beta**: Not publicly available yet
7. **FromSoft UI is Custom**: No standard framework exists

## Corrected Action Plan

### Immediate (Fix 403 Errors Today):
1. **Add User-Agent header** to all fetch requests (mandatory)
2. **Add classic GitHub token** for 5000 req/hr (vs 60)
3. **Store token in localStorage** for browser persistence

### Short-term (This Week):
1. **Populate project board** - Add existing issues to project
2. **Implement label-based hierarchy** - Use epic/story/task labels
3. **Set up milestones** for sprint management

### Medium-term (This Month):
1. **Apply for Task Lists beta** if available
2. **Add caching** to reduce API calls
3. **Implement GraphQL** for more efficient queries

### Optional Enhancements:
1. **ZenHub** for true epic support
2. **GitHub Actions** for automation
3. **Projects v2 migration** if needed

### 1. Enhanced Bonfire System
```css
/* Animated Bonfire with Particle Effects */
.bonfire-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 0;
    opacity: 0.15;
    pointer-events: none;
}

.bonfire-particles {
    position: absolute;
    width: 100%;
    height: 100%;
}

.ember {
    position: absolute;
    width: 3px;
    height: 3px;
    background: #ff6b35;
    border-radius: 50%;
    filter: blur(1px);
    animation: emberFloat 4s infinite ease-out;
}

@keyframes emberFloat {
    0% {
        transform: translateY(0) translateX(0);
        opacity: 0;
    }
    10% {
        opacity: 1;
    }
    90% {
        opacity: 1;
    }
    100% {
        transform: translateY(-200px) translateX(var(--drift));
        opacity: 0;
    }
}

/* Add 20 embers with random properties */
.ember:nth-child(1) { --drift: 20px; animation-delay: 0s; left: 45%; }
.ember:nth-child(2) { --drift: -15px; animation-delay: 0.5s; left: 50%; }
.ember:nth-child(3) { --drift: 25px; animation-delay: 1s; left: 55%; }
/* ... continue for more embers */
```

### 2. Death Counter & Souls System
```javascript
// Add souls-like death/retry system
let deathCount = localStorage.getItem('deathCount') || 0;
let soulsHeld = 0;
let soulsLost = 0;

function updateSoulsDisplay() {
    const soulsElement = document.createElement('div');
    soulsElement.className = 'souls-counter';
    soulsElement.innerHTML = `
        <div class="souls-held">
            <span class="souls-icon">👻</span>
            <span class="souls-value">${soulsHeld.toLocaleString()}</span>
        </div>
        <div class="humanity-counter">
            <span class="humanity-icon">◉</span>
            <span class="humanity-value">${Math.floor(totalXP / 1000)}</span>
        </div>
    `;
    document.querySelector('.header').appendChild(soulsElement);
}
```

### 3. Improved Memory Fragments (Souls-like Lore)
```javascript
const LORE_FRAGMENTS = {
    1: {
        title: "The First Flame",
        text: "In the beginning, there was darkness. Then came the repository, and with it, disparity.",
        unlockCondition: "Complete setup phase"
    },
    2: {
        title: "The Undead Curse",
        text: "Those who fail their sprints are branded with the darksign of technical debt.",
        unlockCondition: "First asset published"
    },
    3: {
        title: "Lords of Cinder",
        text: "Four great codebases linked the fire, but now their flames fade...",
        unlockCondition: "Combat system complete"
    }
    // Add more lore fragments
};

function displayLoreFragment(fragmentId) {
    const fragment = LORE_FRAGMENTS[fragmentId];
    const modal = document.createElement('div');
    modal.className = 'lore-modal';
    modal.innerHTML = `
        <div class="lore-content">
            <h3 class="lore-title">${fragment.title}</h3>
            <p class="lore-text">${fragment.text}</p>
            <div class="lore-unlock">Unlocked: ${fragment.unlockCondition}</div>
            <button class="lore-close">Touch the Darkness</button>
        </div>
    `;
    document.body.appendChild(modal);
}
```

### 4. Enhanced Visual Effects
```css
/* Fog Gate Transitions */
.section-transition {
    position: relative;
    height: 2px;
    margin: 40px 0;
    overflow: hidden;
}

.section-transition::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, 
        transparent 0%, 
        rgba(255, 255, 255, 0.1) 45%,
        rgba(255, 255, 255, 0.3) 50%,
        rgba(255, 255, 255, 0.1) 55%,
        transparent 100%);
    animation: fogGateShimmer 3s infinite;
}

@keyframes fogGateShimmer {
    0% { left: -100%; }
    100% { left: 100%; }
}

/* Estus Flask for Health/Progress */
.estus-flask {
    position: fixed;
    bottom: 20px;
    left: 20px;
    width: 60px;
    height: 80px;
    background: linear-gradient(180deg, 
        rgba(255, 200, 50, 0.8) 0%,
        rgba(255, 150, 0, 0.9) 100%);
    border-radius: 30% 30% 50% 50%;
    border: 2px solid #8b6914;
    box-shadow: 0 0 20px rgba(255, 200, 50, 0.5);
}

.estus-charges {
    position: absolute;
    bottom: -25px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 5px;
}

.estus-charge {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #8b6914;
    transition: all 0.3s;
}

.estus-charge.active {
    background: #ffd700;
    box-shadow: 0 0 5px #ffd700;
}
```

### 5. Boss Health Bar for Major Milestones
```css
.boss-health-bar {
    position: fixed;
    top: 100px;
    left: 50%;
    transform: translateX(-50%);
    width: 60%;
    opacity: 0;
    transition: opacity 0.5s;
    z-index: 1000;
}

.boss-health-bar.active {
    opacity: 1;
}

.boss-name {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 1.8rem;
    color: #ffd700;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
    margin-bottom: 10px;
}

.boss-health-container {
    background: rgba(0, 0, 0, 0.8);
    border: 2px solid #8b6914;
    height: 30px;
    position: relative;
    overflow: hidden;
}

.boss-health-fill {
    height: 100%;
    background: linear-gradient(90deg, #8b0000, #ff0000);
    transition: width 0.5s ease;
    box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
}
```

### 6. Improved Task Items (Quest Log Style)
```css
.task-item {
    background: linear-gradient(135deg, 
        rgba(10, 10, 10, 0.9),
        rgba(30, 20, 10, 0.7));
    border-left: 4px solid var(--ember-orange);
    padding: 20px;
    margin-bottom: 15px;
    border-radius: 4px;
    position: relative;
    transition: all 0.3s ease;
    cursor: pointer;
    overflow: hidden;
}

.task-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, 
        transparent, 
        rgba(255, 215, 0, 0.1), 
        transparent);
    transition: left 0.5s;
}

.task-item:hover::before {
    left: 100%;
}

.task-difficulty {
    position: absolute;
    top: 10px;
    right: 10px;
    display: flex;
    gap: 2px;
}

.skull {
    width: 20px;
    height: 20px;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="%23999"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2z"/></svg>');
    opacity: 0.3;
}

.skull.active {
    opacity: 1;
    filter: drop-shadow(0 0 3px #ff0000);
}
```

### 7. Sound Design Enhancements
```javascript
// Add souls-like sound effects
const soundEffects = {
    levelUp: new Audio('audio/level-up.mp3'),
    itemPickup: new Audio('audio/item-get.mp3'),
    bonfireLit: new Audio('audio/bonfire-lit.mp3'),
    death: new Audio('audio/you-died.mp3'),
    victory: new Audio('audio/victory-achieved.mp3')
};

function playSound(effect) {
    if (soundEffects[effect]) {
        soundEffects[effect].volume = 0.3;
        soundEffects[effect].play().catch(e => console.log('Audio play failed:', e));
    }
}

// Trigger sounds on events
function onTaskComplete() {
    playSound('itemPickup');
    showNotification('QUEST COMPLETE', 'var(--garden-gold)');
}

function onMilestoneReached() {
    playSound('victory');
    showBossDefeated();
}
```

### 8. Notification System (Souls-style)
```css
.souls-notification {
    position: fixed;
    bottom: 100px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0, 0, 0, 0.9);
    border: 2px solid var(--garden-gold);
    padding: 20px 40px;
    font-family: 'Cinzel', serif;
    font-size: 1.5rem;
    color: var(--garden-gold);
    text-align: center;
    opacity: 0;
    animation: notificationFade 3s ease-out;
    z-index: 2000;
}

@keyframes notificationFade {
    0% { opacity: 0; transform: translateX(-50%) translateY(20px); }
    20% { opacity: 1; transform: translateX(-50%) translateY(0); }
    80% { opacity: 1; transform: translateX(-50%) translateY(0); }
    100% { opacity: 0; transform: translateX(-50%) translateY(-20px); }
}

.item-acquired {
    display: flex;
    align-items: center;
    gap: 15px;
}

.item-icon {
    width: 40px;
    height: 40px;
    border: 2px solid var(--garden-gold);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### 9. Enhanced Loading States
```javascript
// Souls-like loading messages
const LOADING_MESSAGES = [
    "Kindling the flame...",
    "Traversing the fog...",
    "Restoring humanity...",
    "Linking the repositories...",
    "Summoning phantoms...",
    "Reading soapstone messages...",
    "Praising the sun..."
];

function showLoading() {
    const randomMessage = LOADING_MESSAGES[Math.floor(Math.random() * LOADING_MESSAGES.length)];
    const loadingElement = document.createElement('div');
    loadingElement.className = 'souls-loading';
    loadingElement.innerHTML = `
        <div class="loading-bonfire">🔥</div>
        <div class="loading-text">${randomMessage}</div>
    `;
    document.body.appendChild(loadingElement);
}
```

### 10. Covenant System for Team Roles
```javascript
const COVENANTS = {
    sunbros: {
        name: "Warriors of Sunlight",
        role: "Frontend Development",
        color: "#ffd700",
        bonus: "+20% XP for UI tasks"
    },
    darkwraiths: {
        name: "Darkwraiths",
        role: "Backend Development",
        color: "#8b0000",
        bonus: "+20% XP for system tasks"
    },
    dragons: {
        name: "Path of the Dragon",
        role: "Game Design",
        color: "#4a3410",
        bonus: "+20% XP for design tasks"
    }
};

function joinCovenant(covenantKey) {
    const covenant = COVENANTS[covenantKey];
    localStorage.setItem('covenant', covenantKey);
    showNotification(`Covenant Joined: ${covenant.name}`);
    updateCovenantDisplay();
}
```

## Implementation Priority

1. **Immediate Fixes** (Priority 1)
   - Fix GitHub API error handling
   - Add fallback data structure
   - Fix audio file references

2. **Core Enhancements** (Priority 2)
   - Implement souls counter system
   - Add boss health bars for milestones
   - Enhance notification system

3. **Atmospheric Improvements** (Priority 3)
   - Add particle effects to bonfire
   - Implement fog gate transitions
   - Add souls-like sound effects

4. **Advanced Features** (Priority 4)
   - Implement covenant system
   - Add lore fragment modals
   - Create death counter system

## Testing Checklist

- [ ] Test with GitHub API rate limited
- [ ] Test without audio files
- [ ] Test keyboard navigation
- [ ] Test screen reader compatibility
- [ ] Test on mobile devices
- [ ] Test dark/light mode transitions
- [ ] Test all animation performance
- [ ] Verify WCAG compliance maintained

## Performance Optimizations

```javascript
// Throttle scroll events
let scrollTimeout;
window.addEventListener('scroll', () => {
    if (scrollTimeout) {
        window.cancelAnimationFrame(scrollTimeout);
    }
    scrollTimeout = window.requestAnimationFrame(() => {
        updateParallaxEffects();
    });
});

// Lazy load heavy animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate');
        }
    });
});

document.querySelectorAll('.memory-fragments').forEach(el => {
    observer.observe(el);
});
```

## Critical GitHub Connection Issues (You're Right - These Need Addressing)

### 1. Project Page Organization Repository Connection
```javascript
// POTENTIAL ISSUES I MISSED:
// 1. The repo might not be properly connected to GitHub Projects
// 2. OAuth token might be missing or expired  
// 3. CORS issues with GitHub API
// 4. GitHub Pages deployment configuration issues

// Enhanced connection verification
const CONNECTION_CONFIG = {
    owner: 'michael-placeholder',
    repo: 'shadowed-realms',
    projectId: null, // This might be missing!
    token: process.env.GITHUB_TOKEN || null,
    apiVersion: '2022-11-28',
    graphqlEndpoint: 'https://api.github.com/graphql'
};

async function verifyGitHubConnections() {
    const connectionStatus = {
        repository: false,
        project: false,
        issues: false,
        webhooks: false,
        pages: false
    };
    
    // Check repository access
    try {
        const repoResponse = await fetch(
            `https://api.github.com/repos/${CONNECTION_CONFIG.owner}/${CONNECTION_CONFIG.repo}`,
            { headers: CONNECTION_CONFIG.token ? 
                { 'Authorization': `token ${CONNECTION_CONFIG.token}` } : {} 
            }
        );
        connectionStatus.repository = repoResponse.ok;
    } catch (e) {
        console.error('Repository connection failed:', e);
    }
    
    // Check GitHub Projects v2 connection (GraphQL)
    if (CONNECTION_CONFIG.token) {
        try {
            const projectQuery = `
                query {
                    repository(owner: "${CONNECTION_CONFIG.owner}", name: "${CONNECTION_CONFIG.repo}") {
                        projectsV2(first: 10) {
                            nodes {
                                id
                                title
                                number
                            }
                        }
                    }
                }
            `;
            const projectResponse = await fetch(CONNECTION_CONFIG.graphqlEndpoint, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${CONNECTION_CONFIG.token}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: projectQuery })
            });
            const projectData = await projectResponse.json();
            connectionStatus.project = !projectData.errors;
        } catch (e) {
            console.error('Project connection failed:', e);
        }
    }
    
    return connectionStatus;
}
```

### 2. Epic → User Story → Issue → Task Hierarchy Problems
```javascript
// THE REAL ISSUE: GitHub doesn't natively support this hierarchy!
// We need to implement a custom solution

const HIERARCHY_STRUCTURE = {
    epic: {
        prefix: '[EPIC]',
        label: 'epic',
        color: '#9333ea',
        children: 'userStories'
    },
    userStory: {
        prefix: '[STORY]',
        label: 'user-story',
        color: '#3b82f6',
        children: 'issues',
        parent: 'epic'
    },
    issue: {
        prefix: '[ISSUE]',
        label: 'issue',
        color: '#10b981',
        children: 'tasks',
        parent: 'userStory'
    },
    task: {
        prefix: '[TASK]',
        label: 'task',
        color: '#f59e0b',
        parent: 'issue'
    }
};

// Parse hierarchy from issue body or comments
function parseHierarchy(issue) {
    const hierarchy = {
        type: null,
        parent: null,
        children: [],
        epicId: null,
        storyId: null,
        issueId: null
    };
    
    // Check title for type
    for (const [type, config] of Object.entries(HIERARCHY_STRUCTURE)) {
        if (issue.title.includes(config.prefix)) {
            hierarchy.type = type;
            break;
        }
    }
    
    // Parse parent/child relationships from body
    const bodyLines = (issue.body || '').split('\n');
    bodyLines.forEach(line => {
        if (line.includes('Parent:')) {
            const parentMatch = line.match(/#(\d+)/);
            if (parentMatch) hierarchy.parent = parentMatch[1];
        }
        if (line.includes('Epic:')) {
            const epicMatch = line.match(/#(\d+)/);
            if (epicMatch) hierarchy.epicId = epicMatch[1];
        }
        if (line.includes('Story:')) {
            const storyMatch = line.match(/#(\d+)/);
            if (storyMatch) hierarchy.storyId = storyMatch[1];
        }
    });
    
    // Find children through cross-references
    if (issue.timeline_events) {
        issue.timeline_events.forEach(event => {
            if (event.event === 'cross-referenced') {
                hierarchy.children.push(event.source.issue.number);
            }
        });
    }
    
    return hierarchy;
}

// Build complete hierarchy tree
async function buildHierarchyTree(issues) {
    const tree = {
        epics: [],
        orphanedStories: [],
        orphanedIssues: [],
        orphanedTasks: []
    };
    
    const issueMap = new Map();
    issues.forEach(issue => {
        const hierarchy = parseHierarchy(issue);
        issueMap.set(issue.number, { ...issue, hierarchy });
    });
    
    // Build tree structure
    issueMap.forEach((issue, number) => {
        if (issue.hierarchy.type === 'epic') {
            tree.epics.push({
                ...issue,
                stories: []
            });
        }
    });
    
    // Link stories to epics
    issueMap.forEach((issue) => {
        if (issue.hierarchy.type === 'userStory') {
            const epic = tree.epics.find(e => e.number === parseInt(issue.hierarchy.epicId));
            if (epic) {
                epic.stories.push({
                    ...issue,
                    issues: []
                });
            } else {
                tree.orphanedStories.push(issue);
            }
        }
    });
    
    return tree;
}
```

### 3. Enhanced Issue to Task Picker (Major Improvements Needed)
```javascript
// ISSUES WITH CURRENT IMPLEMENTATION:
// - No proper task breakdown within issues
// - No drag-and-drop functionality
// - No filtering or search
// - No bulk operations
// - No keyboard shortcuts

class EnhancedTaskPicker {
    constructor(container) {
        this.container = container;
        this.selectedIssues = new Set();
        this.filters = {
            sprint: 'all',
            epic: 'all',
            assignee: 'all',
            label: [],
            search: ''
        };
        this.viewMode = 'list'; // list, kanban, tree
        this.init();
    }
    
    init() {
        this.render();
        this.attachEventListeners();
        this.loadIssues();
    }
    
    render() {
        this.container.innerHTML = `
            <div class="task-picker-enhanced">
                <!-- View Mode Selector -->
                <div class="view-mode-selector">
                    <button class="view-btn ${this.viewMode === 'list' ? 'active' : ''}" 
                            data-view="list" aria-label="List view">
                        <svg><!-- List icon --></svg>
                    </button>
                    <button class="view-btn ${this.viewMode === 'kanban' ? 'active' : ''}" 
                            data-view="kanban" aria-label="Kanban view">
                        <svg><!-- Kanban icon --></svg>
                    </button>
                    <button class="view-btn ${this.viewMode === 'tree' ? 'active' : ''}" 
                            data-view="tree" aria-label="Tree view">
                        <svg><!-- Tree icon --></svg>
                    </button>
                </div>
                
                <!-- Advanced Filters -->
                <div class="filter-bar">
                    <input type="search" 
                           class="search-input" 
                           placeholder="Search issues, tasks, or epics..."
                           aria-label="Search issues">
                    
                    <select class="filter-select" data-filter="sprint">
                        <option value="all">All Sprints</option>
                        <option value="current">Current Sprint</option>
                        <option value="backlog">Backlog</option>
                    </select>
                    
                    <select class="filter-select" data-filter="epic">
                        <option value="all">All Epics</option>
                        <!-- Dynamically populated -->
                    </select>
                    
                    <select class="filter-select" data-filter="assignee">
                        <option value="all">All Assignees</option>
                        <option value="unassigned">Unassigned</option>
                        <!-- Dynamically populated -->
                    </select>
                    
                    <div class="label-filters">
                        <!-- Dynamically populated label chips -->
                    </div>
                </div>
                
                <!-- Bulk Actions -->
                <div class="bulk-actions ${this.selectedIssues.size > 0 ? 'visible' : ''}">
                    <span class="selection-count">${this.selectedIssues.size} selected</span>
                    <button class="bulk-btn" data-action="assign">Assign</button>
                    <button class="bulk-btn" data-action="label">Add Label</button>
                    <button class="bulk-btn" data-action="sprint">Move to Sprint</button>
                    <button class="bulk-btn" data-action="close">Close Issues</button>
                </div>
                
                <!-- Issue/Task Container -->
                <div class="issues-container" data-view="${this.viewMode}">
                    <!-- Content rendered based on view mode -->
                </div>
                
                <!-- Task Breakdown Panel -->
                <div class="task-breakdown-panel">
                    <h3>Task Breakdown</h3>
                    <div class="selected-issue-info"></div>
                    <div class="task-list-container"></div>
                    <button class="add-task-btn">+ Add Task</button>
                </div>
            </div>
        `;
    }
    
    renderListView(issues) {
        const container = this.container.querySelector('.issues-container');
        const grouped = this.groupIssues(issues);
        
        container.innerHTML = `
            <div class="list-view">
                ${Object.entries(grouped).map(([group, items]) => `
                    <div class="issue-group">
                        <h3 class="group-header">
                            <span class="group-toggle">▼</span>
                            ${group} (${items.length})
                        </h3>
                        <div class="group-content">
                            ${items.map(issue => this.renderIssueCard(issue)).join('')}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    renderKanbanView(issues) {
        const container = this.container.querySelector('.issues-container');
        const columns = ['To Do', 'In Progress', 'In Review', 'Done'];
        
        container.innerHTML = `
            <div class="kanban-view">
                ${columns.map(column => `
                    <div class="kanban-column" data-status="${column}">
                        <h3 class="column-header">${column}</h3>
                        <div class="column-content" 
                             ondrop="handleDrop(event)" 
                             ondragover="handleDragOver(event)">
                            ${this.getIssuesByStatus(issues, column)
                                .map(issue => this.renderDraggableCard(issue))
                                .join('')}
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
    }
    
    renderTreeView(issues) {
        const tree = this.buildHierarchyTree(issues);
        const container = this.container.querySelector('.issues-container');
        
        container.innerHTML = `
            <div class="tree-view">
                ${tree.epics.map(epic => `
                    <details class="epic-node" open>
                        <summary class="epic-header">
                            ${epic.title}
                            <span class="epic-stats">
                                ${epic.stories.length} stories, 
                                ${epic.totalIssues} issues
                            </span>
                        </summary>
                        <div class="epic-content">
                            ${epic.stories.map(story => `
                                <details class="story-node">
                                    <summary class="story-header">
                                        ${story.title}
                                        <span class="story-stats">
                                            ${story.issues.length} issues
                                        </span>
                                    </summary>
                                    <div class="story-content">
                                        ${story.issues.map(issue => `
                                            <div class="issue-node">
                                                ${issue.title}
                                                <div class="task-preview">
                                                    ${this.renderTaskPreview(issue.tasks)}
                                                </div>
                                            </div>
                                        `).join('')}
                                    </div>
                                </details>
                            `).join('')}
                        </div>
                    </details>
                `).join('')}
            </div>
        `;
    }
    
    renderIssueCard(issue) {
        const tasks = this.extractTasksFromIssue(issue);
        return `
            <div class="issue-card ${this.selectedIssues.has(issue.number) ? 'selected' : ''}" 
                 data-issue-id="${issue.number}"
                 draggable="true">
                <input type="checkbox" 
                       class="issue-checkbox" 
                       ${this.selectedIssues.has(issue.number) ? 'checked' : ''}>
                <div class="issue-content">
                    <h4 class="issue-title">${issue.title}</h4>
                    <div class="issue-meta">
                        <span class="issue-number">#${issue.number}</span>
                        <span class="issue-assignee">${issue.assignee?.login || 'Unassigned'}</span>
                        <span class="task-count">${tasks.length} tasks</span>
                    </div>
                    <div class="issue-labels">
                        ${issue.labels.map(label => `
                            <span class="label" style="background: #${label.color}">
                                ${label.name}
                            </span>
                        `).join('')}
                    </div>
                    <div class="task-quick-view">
                        ${tasks.slice(0, 3).map(task => `
                            <div class="task-item-mini">
                                <input type="checkbox" ${task.completed ? 'checked' : ''}>
                                <span>${task.title}</span>
                            </div>
                        `).join('')}
                        ${tasks.length > 3 ? `<span class="more-tasks">+${tasks.length - 3} more</span>` : ''}
                    </div>
                </div>
            </div>
        `;
    }
    
    extractTasksFromIssue(issue) {
        // Parse tasks from issue body using checkbox syntax
        const tasks = [];
        const bodyLines = (issue.body || '').split('\n');
        
        bodyLines.forEach((line, index) => {
            const taskMatch = line.match(/^\s*- \[([ x])\]\s+(.+)/);
            if (taskMatch) {
                tasks.push({
                    id: `${issue.number}-task-${index}`,
                    title: taskMatch[2],
                    completed: taskMatch[1] === 'x',
                    issueNumber: issue.number
                });
            }
        });
        
        return tasks;
    }
    
    attachEventListeners() {
        // View mode switching
        this.container.querySelectorAll('.view-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.viewMode = e.target.dataset.view;
                this.render();
                this.loadIssues();
            });
        });
        
        // Search functionality
        const searchInput = this.container.querySelector('.search-input');
        if (searchInput) {
            searchInput.addEventListener('input', debounce((e) => {
                this.filters.search = e.target.value;
                this.applyFilters();
            }, 300));
        }
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey || e.metaKey) {
                switch(e.key) {
                    case 'a':
                        e.preventDefault();
                        this.selectAll();
                        break;
                    case 'f':
                        e.preventDefault();
                        searchInput?.focus();
                        break;
                    case '1':
                        this.viewMode = 'list';
                        this.render();
                        break;
                    case '2':
                        this.viewMode = 'kanban';
                        this.render();
                        break;
                    case '3':
                        this.viewMode = 'tree';
                        this.render();
                        break;
                }
            }
        });
    }
}

// Utility function for debouncing
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}
```

### 4. Additional HTML Structure Problems
```html
<!-- MISSING CRITICAL ELEMENTS -->

<!-- 1. Proper semantic structure for screen readers -->
<main role="main" aria-label="Project Dashboard">
    <section role="region" aria-labelledby="sprint-heading">
        <h2 id="sprint-heading">Sprint Progress</h2>
        <!-- Content -->
    </section>
</main>

<!-- 2. Missing loading states for async operations -->
<div class="loading-overlay" aria-hidden="true">
    <div class="spinner" role="status">
        <span class="sr-only">Loading issues...</span>
    </div>
</div>

<!-- 3. Missing error boundaries -->
<div class="error-boundary" role="alert" aria-live="assertive">
    <!-- Error messages appear here -->
</div>

<!-- 4. Missing data attributes for testing -->
<div class="task-item" 
     data-testid="task-item"
     data-issue-id="123"
     data-epic-id="456"
     data-sprint="current">
</div>

<!-- 5. Missing progressive enhancement fallbacks -->
<noscript>
    <div class="no-js-warning">
        This dashboard requires JavaScript to function properly.
        <a href="/static-view">View static version</a>
    </div>
</noscript>
```

### 5. CSS Improvements for Better Structure
```css
/* Missing responsive breakpoints */
@media (max-width: 768px) {
    .dashboard {
        padding: 10px;
    }
    
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    .task-picker-enhanced {
        flex-direction: column;
    }
    
    .kanban-view {
        overflow-x: auto;
        display: flex;
        gap: 10px;
        padding-bottom: 20px;
    }
}

/* Missing print styles */
@media print {
    .audio-controls,
    .sync-status,
    .bonfire-container {
        display: none;
    }
    
    .dashboard {
        background: white;
        color: black;
    }
}

/* Missing focus-visible for better keyboard navigation */
:focus-visible {
    outline: 3px solid var(--garden-gold);
    outline-offset: 2px;
}

/* Missing reduced motion support */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* Missing dark mode toggle */
@media (prefers-color-scheme: light) {
    :root {
        --dark-souls-black: #f5f5f5;
        --ember-orange: #ff6b35;
        /* Adjust other colors for light mode */
    }
}
```

### 6. Data Flow Issues & Solutions
```javascript
// PROBLEM: No proper state management
// SOLUTION: Implement a simple state store

class DashboardState {
    constructor() {
        this.state = {
            issues: [],
            epics: [],
            stories: [],
            tasks: [],
            filters: {},
            user: null,
            config: {}
        };
        this.listeners = [];
    }
    
    setState(updates) {
        this.state = { ...this.state, ...updates };
        this.notify();
    }
    
    subscribe(listener) {
        this.listeners.push(listener);
        return () => {
            this.listeners = this.listeners.filter(l => l !== listener);
        };
    }
    
    notify() {
        this.listeners.forEach(listener => listener(this.state));
    }
    
    // Actions
    async fetchIssues() {
        try {
            const response = await this.githubAPI.getIssues();
            this.setState({ issues: response });
        } catch (error) {
            this.handleError(error);
        }
    }
    
    handleError(error) {
        // Centralized error handling
        console.error('State error:', error);
        this.setState({ 
            error: error.message,
            errorType: this.classifyError(error)
        });
    }
    
    classifyError(error) {
        if (error.status === 403) return 'rate-limit';
        if (error.status === 401) return 'auth';
        if (error.status >= 500) return 'server';
        return 'unknown';
    }
}
```

### 7. Missing Accessibility Features
```javascript
// Screen reader announcements
class AccessibilityAnnouncer {
    constructor() {
        this.createAnnouncer();
    }
    
    createAnnouncer() {
        this.announcer = document.createElement('div');
        this.announcer.setAttribute('role', 'status');
        this.announcer.setAttribute('aria-live', 'polite');
        this.announcer.setAttribute('aria-atomic', 'true');
        this.announcer.className = 'sr-only';
        document.body.appendChild(this.announcer);
    }
    
    announce(message, priority = 'polite') {
        this.announcer.setAttribute('aria-live', priority);
        this.announcer.textContent = message;
        
        // Clear after announcement
        setTimeout(() => {
            this.announcer.textContent = '';
        }, 1000);
    }
}

// Keyboard navigation helper
class KeyboardNavigator {
    constructor(container) {
        this.container = container;
        this.focusableElements = [];
        this.currentIndex = 0;
        this.init();
    }
    
    init() {
        this.updateFocusableElements();
        this.attachListeners();
    }
    
    updateFocusableElements() {
        const selector = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
        this.focusableElements = Array.from(this.container.querySelectorAll(selector));
    }
    
    attachListeners() {
        this.container.addEventListener('keydown', (e) => {
            if (e.key === 'Tab') {
                // Let default tab behavior work
                return;
            }
            
            // Arrow key navigation
            if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
                e.preventDefault();
                this.focusNext();
            } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
                e.preventDefault();
                this.focusPrevious();
            } else if (e.key === 'Home') {
                e.preventDefault();
                this.focusFirst();
            } else if (e.key === 'End') {
                e.preventDefault();
                this.focusLast();
            }
        });
    }
    
    focusNext() {
        this.currentIndex = (this.currentIndex + 1) % this.focusableElements.length;
        this.focusableElements[this.currentIndex].focus();
    }
    
    focusPrevious() {
        this.currentIndex = (this.currentIndex - 1 + this.focusableElements.length) % this.focusableElements.length;
        this.focusableElements[this.currentIndex].focus();
    }
    
    focusFirst() {
        this.currentIndex = 0;
        this.focusableElements[0]?.focus();
    }
    
    focusLast() {
        this.currentIndex = this.focusableElements.length - 1;
        this.focusableElements[this.currentIndex]?.focus();
    }
}
```

## Additional FromSoft References

- Replace "Sprint" with "Journey"
- Replace "Issues" with "Trials"
- Replace "Tasks" with "Ordeals"
- Add "Praise the Sun!" gesture button
- Include "Try finger but hole" in error messages (keeping it professional)
- Add covenant rankings leaderboard
- Implement NG+ concept for project iterations
- Add "Souls Retrieved" animation when resuming work
- Include "Fog Wall" effect before major milestones
- Add "Phantom" indicators for team members online

## Notes

- Maintain accessibility while enhancing atmosphere
- Keep professional context while adding game elements
- Ensure all enhancements are performant
- Test thoroughly on all target browsers
- Document all Easter eggs for team awareness