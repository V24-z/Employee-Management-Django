  // 1. Setup Current Date
        const dateOptions = { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' };
        document.getElementById('currentDate').textContent = new Date().toLocaleDateString('en-US', dateOptions);

        // 2. Mobile Sidebar Toggle Logic
        const menuToggle = document.getElementById('menuToggle');
        const sidebar = document.getElementById('sidebar');
        
        menuToggle.addEventListener('click', () => {
            sidebar.classList.toggle('show');
        });

        // Close sidebar if clicking outside on mobile
        document.addEventListener('click', (e) => {
            if (window.innerWidth <= 991) {
                if (!sidebar.contains(e.target) && !menuToggle.contains(e.target) && sidebar.classList.contains('show')) {
                    sidebar.classList.remove('show');
                }
            }
        });

        // 3. Prevent default on Django URL tags ONLY when viewed in standalone UI preview environments
        // This ensures the hover effects and clicks can be tested without breaking the preview window.
        // It will not affect your real Django environment.
        const links = document.querySelectorAll('.action-card, .sidebar-nav a:not(.active)');
        links.forEach(link => {
            link.addEventListener('click', function(e) {
                if (window.location.protocol === 'file:' || window.location.href.includes('preview') || this.getAttribute('href').includes('{%')) {
                    // console.log("Action triggered: " + this.getAttribute('href'));
                    // Uncomment below to stop page reload in preview mode
                    // e.preventDefault(); 
                }
            });
        });