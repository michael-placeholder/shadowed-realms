// github-auth-setup.js
// Complete fix using environment variable for GitHub token

// For Node.js environment (if running server-side)
if (typeof process !== 'undefined' && process.env) {
    const GITHUB_TOKEN = process.env.GITHUB_TOKEN;
}

// For browser environment - you'll need to inject this during build/deploy
// or use a build tool like webpack/vite to handle env vars

const GITHUB_CONFIG = {
    owner: 'michael-placeholder',
    repo: 'shadowed-realms',
    token: typeof process !== 'undefined' ? process.env.GITHUB_TOKEN : null,
    apiBase: 'https://api.github.com'
};

// Fixed fetch function with proper headers
async function githubFetch(endpoint, options = {}) {
    const url = `${GITHUB_CONFIG.apiBase}${endpoint}`;
    
    const headers = {
        'Accept': 'application/vnd.github.v3+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'User-Agent': 'Shadowed-Realms-Dashboard'
    };
    
    // Add token if available
    if (GITHUB_CONFIG.token) {
        headers['Authorization'] = `Bearer ${GITHUB_CONFIG.token}`;
    } else {
        console.warn('No GitHub token found - limited to 60 requests/hour');
    }
    
    const response = await fetch(url, {
        ...options,
        headers: { ...headers, ...options.headers }
    });
    
    if (response.status === 403) {
        const remaining = response.headers.get('x-ratelimit-remaining');
        if (remaining === '0') {
            const reset = response.headers.get('x-ratelimit-reset');
            const resetDate = new Date(reset * 1000);
            throw new Error(`Rate limited until ${resetDate.toLocaleTimeString()}`);
        }
        throw new Error('403 Forbidden - check token permissions');
    }
    
    if (!response.ok) {
        throw new Error(`GitHub API error: ${response.status}`);
    }
    
    return response;
}

// Fixed function to fetch all issues
async function fetchAllIssues() {
    const allIssues = [];
    let page = 1;
    let hasMore = true;
    
    while (hasMore) {
        try {
            const response = await githubFetch(
                `/repos/${GITHUB_CONFIG.owner}/${GITHUB_CONFIG.repo}/issues?state=all&per_page=100&page=${page}`
            );
            
            const issues = await response.json();
            allIssues.push(...issues);
            
            hasMore = issues.length === 100;
            page++;
            
            // Check rate limit status
            const remaining = response.headers.get('x-ratelimit-remaining');
            console.log(`Fetched page ${page - 1}, ${remaining} requests remaining`);
            
            if (page > 15) break; // Safety limit
            
        } catch (error) {
            console.error('Error fetching issues:', error);
            throw error;
        }
    }
    
    return allIssues;
}

// Fixed function to add issues to project
async function addIssuesToProject(projectId, issueIds) {
    if (!GITHUB_CONFIG.token) {
        throw new Error('Token required for project operations');
    }
    
    const mutation = `
        mutation($projectId: ID!, $contentId: ID!) {
            addProjectV2ItemById(input: {
                projectId: $projectId,
                contentId: $contentId
            }) {
                item {
                    id
                }
            }
        }
    `;
    
    for (const issueId of issueIds) {
        try {
            const response = await fetch('https://api.github.com/graphql', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${GITHUB_CONFIG.token}`,
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query: mutation,
                    variables: {
                        projectId: projectId,
                        contentId: issueId
                    }
                })
            });
            
            const result = await response.json();
            if (result.errors) {
                console.error('Error adding issue to project:', result.errors);
            }
        } catch (error) {
            console.error('Failed to add issue to project:', error);
        }
    }
}

// Main initialization
async function initializeDashboard() {
    try {
        // Check token
        if (!GITHUB_CONFIG.token) {
            document.getElementById('task-list').innerHTML = `
                <div class="error" style="padding: 20px; background: rgba(139, 0, 0, 0.1); border: 2px solid var(--blood-red);">
                    <h3>NO GITHUB TOKEN IN ENVIRONMENT</h3>
                    <p>Set GITHUB_TOKEN environment variable with your classic personal access token</p>
                    <ol>
                        <li>Create token at: https://github.com/settings/tokens</li>
                        <li>Set in environment: export GITHUB_TOKEN="ghp_yourtoken"</li>
                        <li>Or add to .env file: GITHUB_TOKEN=ghp_yourtoken</li>
                    </ol>
                </div>
            `;
            return;
        }
        
        // Fetch issues
        console.log('Fetching issues with token...');
        const issues = await fetchAllIssues();
        console.log(`Fetched ${issues.length} issues`);
        
        // Process and display
        processIssues(issues);
        
        // Update UI status
        updateAPIStatus('Connected');
        
    } catch (error) {
        console.error('Dashboard initialization failed:', error);
        document.getElementById('task-list').innerHTML = `
            <div class="error">
                <h3>INITIALIZATION FAILED</h3>
                <p>${error.message}</p>
            </div>
        `;
    }
}

// For development: Load from .env file (requires dotenv in Node.js)
if (typeof require !== 'undefined') {
    try {
        require('dotenv').config();
    } catch (e) {
        // dotenv not available
    }
}

// For browser: Alternative token loading method
if (typeof window !== 'undefined') {
    // Check URL params (for development only - not secure for production)
    const urlParams = new URLSearchParams(window.location.search);
    const tokenFromUrl = urlParams.get('token');
    if (tokenFromUrl) {
        GITHUB_CONFIG.token = tokenFromUrl;
        console.warn('Using token from URL - not secure for production');
    }
    
    // Check localStorage
    const tokenFromStorage = localStorage.getItem('github_token');
    if (tokenFromStorage && !GITHUB_CONFIG.token) {
        GITHUB_CONFIG.token = tokenFromStorage;
    }
}

// Export for use in HTML
if (typeof window !== 'undefined') {
    window.GITHUB_CONFIG = GITHUB_CONFIG;
    window.githubFetch = githubFetch;
    window.fetchAllIssues = fetchAllIssues;
    window.initializeDashboard = initializeDashboard;
}