/**
 * Global Header Custom JS
 * Handles Mobile Menu, Dropdowns, Sticky Header, and Dark Mode
 */

(function () {
    'use strict';

    const Header = {
        init: function () {
            this.cacheDOM();
            this.bindEvents();
            this.checkTheme();
            this.handleSticky();
        },

        cacheDOM: function () {
            this.header = document.querySelector('.gh-site-header');
            this.mobileToggle = document.querySelector('.gh-mobile-toggle');
            this.mobileMenu = document.querySelector('.gh-mobile-menu');
            this.overlay = document.querySelector('.gh-overlay');
            this.submenuToggles = document.querySelectorAll('.gh-submenu-toggle');
            this.themeToggle = document.querySelector('.gh-action-btn[data-action="theme-toggle"]');
            this.body = document.body;
        },

        bindEvents: function () {
            if (this.mobileToggle) {
                this.mobileToggle.addEventListener('click', this.toggleMobileMenu.bind(this));
            }
            if (this.overlay) {
                this.overlay.addEventListener('click', this.closeMobileMenu.bind(this));
            }
            this.submenuToggles.forEach(toggle => {
                toggle.addEventListener('click', this.toggleSubmenu.bind(this));
            });
            if (this.themeToggle) {
                this.themeToggle.addEventListener('click', this.toggleTheme.bind(this));
            }
            window.addEventListener('scroll', this.handleSticky.bind(this));
        },

        toggleMobileMenu: function () {
            if (!this.mobileToggle || !this.mobileMenu) return;

            const isOpen = this.mobileMenu.classList.contains('active');

            if (isOpen) {
                this.closeMobileMenu();
            } else {
                this.mobileMenu.classList.add('active');
                this.mobileToggle.classList.add('active');
                this.overlay.classList.add('active');
                this.body.style.overflow = 'hidden'; // Prevent body scroll
            }
        },

        closeMobileMenu: function () {
            if (!this.mobileMenu) return;
            this.mobileMenu.classList.remove('active');
            this.mobileToggle.classList.remove('active');
            this.overlay.classList.remove('active');
            this.body.style.overflow = '';
        },

        toggleSubmenu: function (e) {
            const toggle = e.currentTarget;
            // Traverse up to wrapper to find the submenu sibling
            const wrapper = toggle.closest('.gh-mobile-link-wrapper');
            const submenu = wrapper ? wrapper.nextElementSibling : toggle.nextElementSibling;

            toggle.classList.toggle('active');
            if (submenu) {
                if (submenu.style.display === 'block') {
                    submenu.style.display = 'none';
                } else {
                    submenu.style.display = 'block';
                }
            }
        },

        toggleTheme: function () {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);

            // Update Icon
            const icon = this.themeToggle.querySelector('i');
            if (newTheme === 'dark') {
                icon.classList.remove('fa-moon-o');
                icon.classList.add('fa-sun-o');
            } else {
                icon.classList.remove('fa-sun-o');
                icon.classList.add('fa-moon-o');
            }

            this.updateLogo(newTheme);
        },

        updateLogo: function (theme) {
            const logo = document.querySelector('.gh-logo img');
            if (!logo) return;

            const currentSrc = logo.getAttribute('src');
            // Prevent errors if src is missing
            if (!currentSrc) return;

            let newSrc = currentSrc;

            if (theme === 'dark') {
                // Switch to logo2.png (Dark Mode Logo)
                if (currentSrc.includes('logo1.png')) {
                    newSrc = currentSrc.replace('logo1.png', 'logo2.png');
                }
            } else {
                // Switch to logo1.png (Light Mode Logo)
                if (currentSrc.includes('logo2.png')) {
                    newSrc = currentSrc.replace('logo2.png', 'logo1.png');
                }
            }

            if (newSrc !== currentSrc) {
                logo.setAttribute('src', newSrc);
            }
        },

        checkTheme: function () {
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme) {
                document.documentElement.setAttribute('data-theme', savedTheme);
                if (this.themeToggle) {
                    const icon = this.themeToggle.querySelector('i');
                    if (savedTheme === 'dark') {
                        icon.classList.remove('fa-moon-o');
                        icon.classList.add('fa-sun-o');
                    }
                }
                this.updateLogo(savedTheme);
            }
        },

        handleSticky: function () {
            if (!this.header) return;
            if (window.scrollY > 50) {
                this.header.style.padding = '0'; // Shrink effect handled by CSS height/padding if needed
                this.header.classList.add('is-sticky');
            } else {
                this.header.classList.remove('is-sticky');
            }
        }
    };

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function () {
            Header.init();
        });
    } else {
        Header.init();
    }

})();
