# Setup Instructions for GitHub Token

## 1. Create Classic Personal Access Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name: "Shadowed Realms Dashboard"
4. Select scopes:
   - `repo` (full control of private repositories)
   - `project` (read/write access to projects)
5. Generate and copy token (starts with `ghp_`)

## 2. Set Environment Variable

### macOS/Linux Terminal:
```bash
# Temporary (current session only)
export GITHUB_TOKEN="ghp_your_token_here"

# Permanent (add to ~/.bashrc or ~/.zshrc)
echo 'export GITHUB_TOKEN="ghp_your_token_here"' >> ~/.zshrc
source ~/.zshrc
```

### Using .env file (recommended for development):
Create file `.env` in project root:
```
GITHUB_TOKEN=ghp_your_token_here
```

### For GitHub Pages deployment:
Go to repo Settings > Secrets and variables > Actions
Add repository secret: `GITHUB_TOKEN`

## 3. Updated HTML with Environment Token Support

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shadowed Realms - Professional RPG Development Platform</title>
    <!-- Keep your existing styles -->
</head>
<body>
    <!-- Your existing HTML structure -->
    
    <script>
        // GitHub configuration with token from environment
        const GITHUB_OWNER = 'michael-placeholder';
        const GITHUB_REPO = 'shadowed-realms';
        
        // In production, this would be injected during build
        // For local testing, use localStorage or URL param
        let GITHUB_TOKEN = null;
        
        // Try to get token from various sources
        if (typeof process !== 'undefined' && process.env && process.env.GITHUB_TOKEN) {
            GITHUB_TOKEN = process.env.GITHUB_TOKEN;
        } else if (localStorage.getItem('github_token')) {
            GITHUB_TOKEN = localStorage.getItem('github_token');
        }
        
        // Fixed fetch function with proper authentication
        async function fetchGitHubData() {
            try {
                const headers = {
                    'Accept': 'application/vnd.github.v3+json',
                    'X-GitHub-Api-Version': '2022-11-28',
                    'User-Agent': 'Shadowed-Realms-Dashboard'
                };
                
                if (GITHUB_TOKEN) {
                    headers['Authorization'] = `Bearer ${GITHUB_TOKEN}`;
                    console.log('Using GitHub token for authentication');
                } else {
                    console.warn('No token found - limited to 60 requests/hour');
                    showTokenPrompt();
                }
                
                let allIssues = [];
                let page = 1;
                let hasMore = true;
                
                while (hasMore && page <= 15) {
                    const response = await fetch(
                        `https://api.github.com/repos/${GITHUB_OWNER}/${GITHUB_REPO}/issues?state=all&per_page=100&page=${page}`,
                        { headers }
                    );
                    
                    if (response.status === 403) {
                        const remaining = response.headers.get('x-ratelimit-remaining');
                        const reset = response.headers.get('x-ratelimit-reset');
                        
                        if (remaining === '0') {
                            const resetTime = new Date(reset * 1000);
                            throw new Error(`Rate limited until ${resetTime.toLocaleTimeString()}`);
                        }
                        
                        const errorData = await response.json();
                        throw new Error(errorData.message || 'Access forbidden');
                    }
                    
                    if (!response.ok) {
                        throw new Error(`GitHub API error: ${response.status}`);
                    }
                    
                    const pageIssues = await response.json();
                    allIssues = allIssues.concat(pageIssues);
                    
                    hasMore = pageIssues.length === 100;
                    page++;
                    
                    // Show progress
                    const remaining = response.headers.get('x-ratelimit-remaining');
                    console.log(`Fetched ${allIssues.length} issues, ${remaining} requests remaining`);
                }
                
                updateAPIStatus('Connected');
                processIssues(allIssues);
                
            } catch (error) {
                console.error('Error fetching GitHub data:', error);
                updateAPIStatus('Error');
                showError(`Failed to load: ${error.message}`);
            }
        }
        
        function showTokenPrompt() {
            const container = document.createElement('div');
            container.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: rgba(10, 10, 10, 0.95);
                border: 2px solid var(--ember-orange);
                padding: 30px;
                z-index: 10000;
                max-width: 500px;
            `;
            
            container.innerHTML = `
                <h2 style="color: var(--garden-gold); font-family: 'Cinzel', serif;">BEARER SEEK GUIDANCE</h2>
                <p style="color: #d0d0d0; margin: 20px 0;">No GitHub token detected. Add token to access full power:</p>
                <input type="password" id="token-input" placeholder="ghp_..." style="
                    width: 100%;
                    padding: 10px;
                    background: rgba(42, 42, 42, 0.8);
                    border: 1px solid var(--abstract-purple);
                    color: white;
                    margin-bottom: 20px;
                ">
                <button onclick="saveToken()" style="
                    background: var(--ember-orange);
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    cursor: pointer;
                    font-family: 'Cinzel', serif;
                ">LIGHT THE BONFIRE</button>
                <button onclick="this.parentElement.remove()" style="
                    background: var(--fog-gray);
                    color: #999;
                    border: none;
                    padding: 10px 20px;
                    cursor: pointer;
                    margin-left: 10px;
                ">Continue Hollow</button>
            `;
            
            document.body.appendChild(container);
        }
        
        function saveToken() {
            const token = document.getElementById('token-input').value;
            if (token) {
                localStorage.setItem('github_token', token);
                GITHUB_TOKEN = token;
                location.reload();
            }
        }
        
        function updateAPIStatus(status) {
            const statusElement = document.getElementById('api-status');
            const statusText = document.getElementById('api-status-text');
            
            if (!statusElement || !statusText) return;
            
            if (status === 'Connected') {
                statusElement.style.background = 'var(--estus-green)';
                statusText.textContent = GITHUB_TOKEN ? 
                    'Authenticated (5000/hr)' : 
                    'Limited (60/hr)';
            } else {
                statusElement.style.background = 'var(--blood-red)';
                statusText.textContent = status;
            }
        }
        
        function showError(message) {
            const taskList = document.getElementById('task-list');
            if (taskList) {
                taskList.innerHTML = `
                    <div class="error" style="color: var(--blood-red); padding: 20px; text-align: center;">
                        <h3>CONNECTION LOST</h3>
                        <p>${message}</p>
                        <button onclick="location.reload()" style="
                            margin-top: 20px;
                            padding: 10px 20px;
                            background: var(--ember-orange);
                            color: white;
                            border: none;
                            cursor: pointer;
                        ">Try Again</button>
                    </div>
                `;
            }
        }
        
        // Your existing processIssues function stays the same
        
        // Initialize on load
        document.addEventListener('DOMContentLoaded', () => {
            fetchGitHubData();
            
            // Refresh every 5 minutes if authenticated
            if (GITHUB_TOKEN) {
                setInterval(fetchGitHubData, 5 * 60 * 1000);
            }
        });
    </script>
</body>
</html>
```

## 4. For GitHub Actions (Automated Deployment)

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy Dashboard
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build with token
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          # Inject token into build
          sed -i "s/GITHUB_TOKEN = null/GITHUB_TOKEN = '$GITHUB_TOKEN'/g" index.html
      
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

## 5. Test Your Setup

```bash
# Check if token is set
echo $GITHUB_TOKEN

# Test API access with curl
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/rate_limit
```

Token should now work everywhere in your dashboard.