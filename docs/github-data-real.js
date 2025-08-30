// GitHub Data Handler - Uses REAL GitHub Issues
// Falls back to localStorage cache, NOT simulated data

(function() {
    const CACHE_KEY = 'github_issues_cache';
    const CACHE_DURATION = 60 * 60 * 1000; // 1 hour cache
    
    // Store original fetch function
    const originalFetchGitHubData = window.fetchGitHubData;
    
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
    
    // Override fetchGitHubData to use cache intelligently
    window.fetchGitHubData = async function() {
        try {
            // Try to fetch real data
            const allIssues = [];
            let page = 1;
            let hasMore = true;
            
            while (hasMore && page <= 11) { // Max 11 pages for 1100 issues
                const response = await fetch(
                    `https://api.github.com/repos/michael-placeholder/shadowed-realms/issues?state=all&per_page=100&page=${page}`,
                    {
                        headers: {
                            'Accept': 'application/vnd.github.v3+json'
                        }
                    }
                );
                
                if (response.status === 403 || response.status === 429) {
                    throw new Error('Rate limited');
                }
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const issues = await response.json();
                allIssues.push(...issues);
                
                hasMore = issues.length === 100;
                page++;
            }
            
            console.log(`Fetched ${allIssues.length} REAL issues from GitHub`);
            
            // Cache the real data
            setCachedData(allIssues);
            
            // Process the real issues
            if (window.processIssues) {
                window.processIssues(allIssues);
            }
            
            // Update API status
            if (window.updateAPIStatus) {
                window.updateAPIStatus('Live');
            }
            
        } catch (error) {
            console.log('GitHub API error:', error.message);
            
            // Try to use cached REAL data
            const cachedIssues = getCachedData();
            
            if (cachedIssues && cachedIssues.length > 0) {
                console.log(`Using ${cachedIssues.length} cached REAL issues`);
                
                // Update API status
                if (window.updateAPIStatus) {
                    window.updateAPIStatus('Cached');
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
                    notice.innerHTML = '⚠️ Using cached REAL data (GitHub rate limit exceeded)<br>Showing actual project issues from cache';
                    taskList.parentNode.insertBefore(notice, taskList);
                }
            } else {
                // No cache available, show error
                const taskList = document.getElementById('task-list');
                if (taskList) {
                    taskList.innerHTML = `
                        <div class="error" style="color: var(--blood-red); padding: 20px; text-align: center;">
                            <h3>GitHub API Rate Limited</h3>
                            <p>Unable to fetch issues. The cache is empty.</p>
                            <p>Please wait for the rate limit to reset or try again later.</p>
                            <p style="margin-top: 10px; font-size: 0.9em;">
                                The project has 1049 real issues created.<br>
                                Once the API is available, they will load automatically.
                            </p>
                        </div>
                    `;
                }
                
                if (window.updateAPIStatus) {
                    window.updateAPIStatus('Rate Limited');
                }
            }
        }
    };
    
    // Also handle when page loads with error
    document.addEventListener('DOMContentLoaded', function() {
        setTimeout(() => {
            const errorDiv = document.querySelector('.error');
            if (errorDiv && errorDiv.textContent.includes('Failed to load GitHub data')) {
                console.log('Detected API error, attempting to use cache');
                window.fetchGitHubData();
            }
        }, 1000);
    });
    
    console.log('GitHub REAL data handler loaded - will cache real issues for 1 hour');
})();