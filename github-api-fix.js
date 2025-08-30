// github-api-fix.js
// Add this to your HTML to fix the 403 errors

const GITHUB_CONFIG = {
    owner: 'michael-placeholder',
    repo: 'shadowed-realms',
    // CRITICAL: Add your token here to fix 403 errors
    token: null // Replace with your actual token: 'ghp_xxxxxxxxxxxx'
};

async function fetchGitHubData() {
    try {
        // Build URL with authentication if available
        const baseUrl = `https://api.github.com/repos/${GITHUB_CONFIG.owner}/${GITHUB_CONFIG.repo}/issues`;
        
        // Required headers to prevent 403
        const headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Shadowed-Realms-Dashboard' // REQUIRED or you get 403
        };
        
        // Add auth if token exists
        if (GITHUB_CONFIG.token) {
            headers['Authorization'] = `Bearer ${GITHUB_CONFIG.token}`;
        }
        
        // Try to fetch
        const response = await fetch(baseUrl + '?state=all&per_page=100', {
            headers: headers
        });
        
        if (response.status === 403) {
            const remaining = response.headers.get('x-ratelimit-remaining');
            const reset = response.headers.get('x-ratelimit-reset');
            
            if (remaining === '0') {
                // Rate limited
                const resetTime = new Date(reset * 1000);
                showError(`
                    <div class="error" style="color: var(--blood-red); padding: 20px;">
                        <h3>YOU DIED</h3>
                        <p>GitHub Rate Limit: 0/${GITHUB_CONFIG.token ? '5000' : '60'}</p>
                        <p>Respawn at: ${resetTime.toLocaleTimeString()}</p>
                        <p>${!GITHUB_CONFIG.token ? 'Add a GitHub token to increase limit to 5000/hour' : ''}</p>
                        <div style="margin-top: 20px;">
                            <input type="password" id="token-input" placeholder="Paste GitHub token here" style="padding: 10px; width: 300px;">
                            <button onclick="saveAndReload()" style="padding: 10px;">Save Token</button>
                        </div>
                    </div>
                `);
                return;
            }
            
            // Other 403 error
            const errorData = await response.json();
            showError(`
                <div class="error">
                    <h3>FORBIDDEN</h3>
                    <p>${errorData.message || 'Access denied'}</p>
                    <p>Likely missing User-Agent header or authentication</p>
                </div>
            `);
            return;
        }
        
        if (!response.ok) {
            throw new Error(`GitHub API error: ${response.status}`);
        }
        
        const issues = await response.json();
        processIssues(issues);
        
    } catch (error) {
        console.error('GitHub fetch error:', error);
        showError(`
            <div class="error">
                <h3>CONNECTION LOST</h3>
                <p>${error.message}</p>
                <p>Check console for details</p>
            </div>
        `);
    }
}

function saveAndReload() {
    const token = document.getElementById('token-input').value;
    if (token) {
        localStorage.setItem('github_token', token);
        location.reload();
    }
}

// Check for saved token on load
document.addEventListener('DOMContentLoaded', () => {
    const savedToken = localStorage.getItem('github_token');
    if (savedToken) {
        GITHUB_CONFIG.token = savedToken;
    }
    
    // Show token status
    const statusElement = document.createElement('div');
    statusElement.style.cssText = 'position: fixed; top: 10px; right: 10px; padding: 10px; background: rgba(0,0,0,0.8); color: white; z-index: 9999;';
    statusElement.innerHTML = GITHUB_CONFIG.token ? 
        '<span style="color: #6b9b7e;">Authenticated (5000/hr)</span>' : 
        '<span style="color: #994444;">No Auth (60/hr)</span>';
    document.body.appendChild(statusElement);
});

function showError(html) {
    const taskList = document.getElementById('task-list');
    if (taskList) {
        taskList.innerHTML = html;
    }
}

// Replace your existing fetchGitHubData call with this fixed version