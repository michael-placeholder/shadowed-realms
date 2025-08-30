// GitHub Data Handler - Fetches REAL Issues with Authentication Support
// Stores real data in localStorage, never uses fake data

(function() {
    const CACHE_KEY = 'github_issues_cache';
    const CACHE_DURATION = 60 * 60 * 1000; // 1 hour cache
    
    // IMPORTANT: Add your GitHub token here for higher rate limits
    // Get a token at: https://github.com/settings/tokens
    // Only needs 'public_repo' scope
    const GITHUB_TOKEN = ''; // Add token here if you have one
    
    // Get cached data if available and fresh
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
    
    // Fetch GitHub data with proper error handling
    window.fetchGitHubData = async function() {
        try {
            const headers = {
                'Accept': 'application/vnd.github.v3+json'
            };
            
            // Add token if available
            if (GITHUB_TOKEN) {
                headers['Authorization'] = `token ${GITHUB_TOKEN}`;
            }
            
            // First, let's check if we can access the API
            const testResponse = await fetch(
                'https://api.github.com/repos/michael-placeholder/shadowed-realms',
                { headers }
            );
            
            if (testResponse.status === 404) {
                console.log('Repository not found. Checking cached data...');
                throw new Error('Repository not accessible');
            }
            
            if (testResponse.status === 403 || testResponse.status === 429) {
                const remaining = testResponse.headers.get('x-ratelimit-remaining');
                const reset = testResponse.headers.get('x-ratelimit-reset');
                const resetDate = new Date(reset * 1000);
                console.log(`Rate limited. Remaining: ${remaining}, Resets at: ${resetDate.toLocaleTimeString()}`);
                throw new Error('Rate limited');
            }
            
            // Now fetch all issues
            const allIssues = [];
            let page = 1;
            let hasMore = true;
            
            while (hasMore && page <= 11) { // Max 11 pages for 1100 issues
                const response = await fetch(
                    `https://api.github.com/repos/michael-placeholder/shadowed-realms/issues?state=all&per_page=100&page=${page}`,
                    { headers }
                );
                
                if (response.status === 403 || response.status === 429) {
                    if (allIssues.length > 0) {
                        // We got some data before hitting the limit
                        console.log(`Rate limited after fetching ${allIssues.length} issues`);
                        break;
                    }
                    throw new Error('Rate limited');
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
            }
            
            if (allIssues.length > 0) {
                console.log(`Successfully fetched ${allIssues.length} REAL issues from GitHub`);
                
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
                
                // Remove cache notice if data is fresh
                const cacheNotice = document.getElementById('cache-notice');
                if (cacheNotice) {
                    cacheNotice.remove();
                }
            }
            
        } catch (error) {
            console.log('GitHub API error:', error.message);
            
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
                
                // Add cache notice if not already there
                const taskList = document.getElementById('task-list');
                if (taskList && !document.getElementById('cache-notice')) {
                    const notice = document.createElement('div');
                    notice.id = 'cache-notice';
                    notice.style.cssText = 'background: var(--ember-orange); color: #f0f0f0; padding: 10px; margin-bottom: 10px; border-radius: 4px; text-align: center;';
                    notice.innerHTML = `⚠️ Using cached data (GitHub rate limit exceeded)<br>Showing ${cachedIssues.length} real project issues from local cache`;
                    taskList.parentNode.insertBefore(notice, taskList);
                }
            } else {
                // No cache available
                console.log('No cached data available');
                
                const taskList = document.getElementById('task-list');
                if (taskList) {
                    taskList.innerHTML = `
                        <div class="error" style="color: var(--blood-red); padding: 20px; text-align: center;">
                            <h3>GitHub API Rate Limited - No Cache Available</h3>
                            <p>The project has 1049 real issues in the repository.</p>
                            <p>To view them, you need to either:</p>
                            <ol style="text-align: left; display: inline-block; margin: 10px auto;">
                                <li>Wait for the rate limit to reset</li>
                                <li>Add a GitHub token to github-data-authenticated.js</li>
                                <li>Visit when you have cached data available</li>
                            </ol>
                            <p style="margin-top: 15px;">
                                <a href="https://github.com/michael-placeholder/shadowed-realms/issues" 
                                   target="_blank" 
                                   style="color: var(--garden-gold);">
                                   View issues directly on GitHub →
                                </a>
                            </p>
                        </div>
                    `;
                }
                
                if (window.updateAPIStatus) {
                    window.updateAPIStatus('Rate Limited (No Cache)');
                }
            }
        }
    };
    
    // Try to fetch immediately on load
    document.addEventListener('DOMContentLoaded', function() {
        // Check if there's already an error message
        setTimeout(() => {
            const errorDiv = document.querySelector('.error');
            if (errorDiv) {
                console.log('Attempting to load GitHub data...');
                window.fetchGitHubData();
            }
        }, 500);
    });
    
    console.log('GitHub authenticated data handler loaded');
    console.log('Add a GitHub token to github-data-authenticated.js for better rate limits');
})();