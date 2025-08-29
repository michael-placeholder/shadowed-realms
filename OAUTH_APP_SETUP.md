# GitHub OAuth App Configuration

## OAuth App Setup for Shadowed Realms

### 1. Create OAuth App
Go to: https://github.com/organizations/michael-placeholder/settings/applications/new

### Application Settings:
- **Application name**: Shadowed Realms Dashboard
- **Homepage URL**: https://michael-placeholder.github.io/shadowed-realms/
- **Application description**: Gamified RPG development dashboard with XP, coins, and memory fragments
- **Authorization callback URL**: https://michael-placeholder.github.io/shadowed-realms/callback

### Required Scopes:
- `repo` - Full control of private repositories
- `project` - Read and write project boards
- `workflow` - Update GitHub Action workflows
- `write:org` - Read and write org and team membership

### Environment Variables:
```javascript
// Add to dashboard's config.js
const OAUTH_CONFIG = {
  clientId: '[YOUR_CLIENT_ID]',
  clientSecret: '[DO_NOT_COMMIT_THIS]',
  redirectUri: 'https://michael-placeholder.github.io/shadowed-realms/callback',
  scope: 'repo project workflow write:org'
};
```

### OAuth Flow Implementation:
```javascript
// oauth-handler.js
class OAuthHandler {
  constructor() {
    this.clientId = OAUTH_CONFIG.clientId;
    this.redirectUri = OAUTH_CONFIG.redirectUri;
  }

  // Initiate OAuth flow
  authorize() {
    const authUrl = `https://github.com/login/oauth/authorize?` +
      `client_id=${this.clientId}&` +
      `redirect_uri=${this.redirectUri}&` +
      `scope=${OAUTH_CONFIG.scope}`;
    
    window.location.href = authUrl;
  }

  // Handle callback
  async handleCallback(code) {
    // Exchange code for token (needs backend)
    const response = await fetch('/api/oauth/token', {
      method: 'POST',
      body: JSON.stringify({ code }),
      headers: { 'Content-Type': 'application/json' }
    });
    
    const { access_token } = await response.json();
    localStorage.setItem('github_token', access_token);
    
    return access_token;
  }

  // Make authenticated API calls
  async apiCall(endpoint, options = {}) {
    const token = localStorage.getItem('github_token');
    
    return fetch(`https://api.github.com${endpoint}`, {
      ...options,
      headers: {
        ...options.headers,
        'Authorization': `Bearer ${token}`,
        'Accept': 'application/vnd.github.v3+json'
      }
    });
  }
}
```

### Dashboard Integration:
```javascript
// dashboard.js
const oauth = new OAuthHandler();

// Check if user is authenticated
if (!localStorage.getItem('github_token')) {
  document.getElementById('login-btn').addEventListener('click', () => {
    oauth.authorize();
  });
}

// Handle callback on return
if (window.location.pathname === '/callback') {
  const urlParams = new URLSearchParams(window.location.search);
  const code = urlParams.get('code');
  
  if (code) {
    oauth.handleCallback(code).then(token => {
      window.location.href = '/';
    });
  }
}
```

## Benefits:
1. ✅ User authentication
2. ✅ Access to private repos
3. ✅ Project board manipulation
4. ✅ Issue creation/updates
5. ✅ Real-time sync with GitHub

## Security Notes:
- Never commit client secret
- Use environment variables
- Implement token refresh
- Add CORS headers properly
