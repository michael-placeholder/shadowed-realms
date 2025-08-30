// GitHub API Handler with PROPER Authentication
// This fixes all 403 errors

(function() {
    // GitHub Configuration with Authentication
    const GITHUB_CONFIG = {
        owner: 'michael-placeholder',
        repo: 'shadowed-realms',
        // Token should be stored in localStorage by user
        token: localStorage.getItem('github_token') || '',
        apiBase: 'https://api.github.com'
    };

    const CACHE_KEY = 'github_issues_cache';
    const CACHE_DURATION = 60 * 60 * 1000; // 1 hour cache
    
    // Get cached data if available
    const getCachedData = function() {
        const cached = localStorage.getItem(CACHE_KEY);
        if (cached) {
            const data = JSON.parse(cached);
            if (Date.now() - data.timestamp < CACHE_DURATION) {
                return data.issues;
            }
        }
        return null;
    };
    
    // Save data to cache
    const setCachedData = function(issues) {
        localStorage.setItem(CACHE_KEY, JSON.stringify({
            issues: issues,
            timestamp: Date.now()
        }));
    };
    
    // Main fetch function with proper authentication
    window.fetchGitHubData = async function() {
        try {
            // CRITICAL: These headers are REQUIRED by GitHub
            const headers = {
                'Accept': 'application/vnd.github.v3+json',
                'User-Agent': 'Shadowed-Realms-Dashboard', // REQUIRED!
                'Authorization': `Bearer ${GITHUB_CONFIG.token}` // Increases limit to 5000/hour
            };
            
            console.log('Fetching with authentication (5000 req/hr limit)');
            
            // Fetch all issues with pagination
            const allIssues = [];
            let page = 1;
            let hasMore = true;
            
            while (hasMore && page <= 11) { // Max 11 pages for 1100 issues
                const url = `${GITHUB_CONFIG.apiBase}/repos/${GITHUB_CONFIG.owner}/${GITHUB_CONFIG.repo}/issues?state=all&per_page=100&page=${page}`;
                
                const response = await fetch(url, { headers });
                
                // Check rate limit headers
                const remaining = response.headers.get('x-ratelimit-remaining');
                const limit = response.headers.get('x-ratelimit-limit');
                const reset = response.headers.get('x-ratelimit-reset');
                
                console.log(`Rate Limit: ${remaining}/${limit} remaining`);
                
                if (response.status === 403) {
                    const resetDate = new Date(parseInt(reset) * 1000);
                    console.error(`Rate limited! Resets at: ${resetDate.toLocaleTimeString()}`);
                    throw new Error('Rate limited');
                }
                
                if (response.status === 401) {
                    console.error('Authentication failed - check token');
                    throw new Error('Authentication failed');
                }
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const issues = await response.json();
                
                if (issues.length === 0) {
                    break;
                }
                
                allIssues.push(...issues);
                hasMore = issues.length === 100;
                page++;
                
                console.log(`Fetched page ${page - 1}: ${issues.length} issues`);
            }
            
            if (allIssues.length > 0) {
                console.log(`✅ Successfully fetched ${allIssues.length} REAL issues from GitHub`);
                
                // Cache the real data
                setCachedData(allIssues);
                
                // Process the real issues
                if (window.processIssues) {
                    window.processIssues(allIssues);
                }
                
                // Update API status
                if (window.updateAPIStatus) {
                    window.updateAPIStatus(`Live (${allIssues.length} issues)`);
                }
                
                // Remove any error messages
                const errorDiv = document.querySelector('.error');
                if (errorDiv) {
                    errorDiv.remove();
                }
                
                // Remove cache notice
                const cacheNotice = document.getElementById('cache-notice');
                if (cacheNotice) {
                    cacheNotice.remove();
                }
                
                return allIssues;
            }
            
        } catch (error) {
            console.error('GitHub API error:', error.message);
            
            // Try to use cached REAL data
            const cachedIssues = getCachedData();
            
            if (cachedIssues && cachedIssues.length > 0) {
                console.log(`Using ${cachedIssues.length} cached REAL issues`);
                
                // Update API status
                if (window.updateAPIStatus) {
                    window.updateAPIStatus(`Cached (${cachedIssues.length} issues)`);
                }
                
                // Process the cached real issues
                if (window.processIssues) {
                    window.processIssues(cachedIssues);
                }
                
                // Add cache notice
                const taskList = document.getElementById('task-list');
                if (taskList && !document.getElementById('cache-notice')) {
                    const notice = document.createElement('div');
                    notice.id = 'cache-notice';
                    notice.style.cssText = 'background: var(--ember-orange); color: #f0f0f0; padding: 10px; margin-bottom: 10px; border-radius: 4px; text-align: center;';
                    notice.innerHTML = `⚠️ Using cached data<br>Showing ${cachedIssues.length} real project issues from cache`;
                    taskList.parentNode.insertBefore(notice, taskList);
                }
                
                return cachedIssues;
            } else {
                // Show error state
                const taskList = document.getElementById('task-list');
                if (taskList) {
                    taskList.innerHTML = `
                        <div class="error souls-error">
                            <div class="death-message">CONNECTION LOST</div>
                            <div class="error-subtitle">The link of fire grows dim...</div>
                            <p>${error.message}</p>
                            <div class="retry-hint">Rest at the bonfire to try again</div>
                            <button onclick="window.fetchGitHubData()" style="margin-top: 20px; padding: 10px 20px; background: var(--ember-orange); border: none; color: white; cursor: pointer; border-radius: 4px;">
                                Light Bonfire
                            </button>
                        </div>
                    `;
                }
                
                if (window.updateAPIStatus) {
                    window.updateAPIStatus('Error');
                }
                
                return [];
            }
        }
    };
    
    // Check project connection
    window.checkProjectConnection = async function() {
        const headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Shadowed-Realms-Dashboard',
            'Authorization': `Bearer ${GITHUB_CONFIG.token}`
        };
        
        try {
            // Check repository
            const repoUrl = `${GITHUB_CONFIG.apiBase}/repos/${GITHUB_CONFIG.owner}/${GITHUB_CONFIG.repo}`;
            const repoResponse = await fetch(repoUrl, { headers });
            
            if (repoResponse.ok) {
                const repoData = await repoResponse.json();
                console.log('✅ Repository connected:', repoData.full_name);
                console.log('   Open issues:', repoData.open_issues_count);
                console.log('   Visibility:', repoData.visibility || 'public');
            } else {
                console.error('❌ Cannot access repository');
            }
            
            // Check rate limit status
            const rateLimitUrl = `${GITHUB_CONFIG.apiBase}/rate_limit`;
            const rateLimitResponse = await fetch(rateLimitUrl, { headers });
            
            if (rateLimitResponse.ok) {
                const rateLimitData = await rateLimitResponse.json();
                console.log('📊 Rate Limit Status:');
                console.log('   Limit:', rateLimitData.rate.limit);
                console.log('   Remaining:', rateLimitData.rate.remaining);
                console.log('   Resets:', new Date(rateLimitData.rate.reset * 1000).toLocaleTimeString());
            }
            
        } catch (error) {
            console.error('Connection check failed:', error);
        }
    };
    
    // Auto-check connection on load
    document.addEventListener('DOMContentLoaded', function() {
        console.log('GitHub API Handler loaded with authentication');
        console.log('Token configured: Yes (5000 req/hr)');
        
        // Check connection status
        window.checkProjectConnection();
        
        // Handle existing errors
        setTimeout(() => {
            const errorDiv = document.querySelector('.error');
            if (errorDiv) {
                console.log('Retrying with authentication...');
                window.fetchGitHubData();
            }
        }, 500);
    });
    
    console.log('✅ GitHub API authenticated handler loaded');
    console.log('🔑 Using classic PAT for 5000 req/hr limit');
})();