/* ============================================
   TIER 1: GLOBAL UI/UX ENHANCEMENTS - JavaScript
   ============================================ */

// Add to existing custom.js after line 847 (before closing IIFE)

// Sticky Header Shrink on Scroll
function stickyHeaderShrink() {
    var header = jQuery('.sticky-header');
    var scrollTop = jQuery(window).scrollTop();

    if (scrollTop > 100) {
        header.addClass('is-fixed');
    } else {
        header.removeClass('is-fixed');
    }
}

// Scroll Progress Indicator
function scrollProgress() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;

    var progressBar = document.querySelector('.scroll-progress');
    if (progressBar) {
        progressBar.style.width = scrolled + "%";
    }
}

// Mobile Menu Toggle
function mobileMenuToggle() {
    jQuery('#mobile-side-drawer').on('click', function () {
        jQuery('.header-nav').toggleClass('show');
        jQuery('.mobile-menu-overlay').toggleClass('show');
        jQuery('body').toggleClass('menu-open');
    });

    jQuery('.mobile-menu-overlay').on('click', function () {
        jQuery('.header-nav').removeClass('show');
        jQuery(this).removeClass('show');
        jQuery('body').removeClass('menu-open');
    });
}

// Scroll to Top Button
function scrollToTop() {
    var btn = jQuery('.scroltop');

    jQuery(window).on('scroll', function () {
        if (jQuery(this).scrollTop() > 300) {
            btn.fadeIn();
        } else {
            btn.fadeOut();
        }
    });

    btn.on('click', function (e) {
        e.preventDefault();
        jQuery('html, body').animate({ scrollTop: 0 }, 600);
    });
}

// Fade In on Scroll for Elements with .fade-in-up class
function fadeInOnScroll() {
    var fadeElements = jQuery('.fade-in-up');

    fadeElements.each(function () {
        var elementTop = jQuery(this).offset().top;
        var elementBottom = elementTop + jQuery(this).outerHeight();
        var viewportTop = jQuery(window).scrollTop();
        var viewportBottom = viewportTop + jQuery(window).height();

        if (elementBottom > viewportTop && elementTop < viewportBottom) {
            jQuery(this).addClass('visible');
        }
    });
}

// Initialize Functions on Document Ready
jQuery(document).ready(function () {
    // Add scroll progress bar to body
    if (!jQuery('.scroll-progress').length) {
        jQuery('body').prepend('<div class="scroll-progress"></div>');
    }

    // Add mobile menu overlay
    if (!jQuery('.mobile-menu-overlay').length) {
        jQuery('body').append('<div class="mobile-menu-overlay"></div>');
    }

    mobileMenuToggle();
    scrollToTop();
    fadeInOnScroll();
});

// Initialize Functions on Window Scroll
jQuery(window).on('scroll', function () {
    stickyHeaderShrink();
    scrollProgress();
    fadeInOnScroll();
});

/* ============================================
   END TIER 1 GLOBAL ENHANCEMENTS JAVASCRIPT
   ============================================ */

/* ============================================
   Quick Contact Widget
   ============================================ */

function injectQuickContactWidget() {
    if (document.querySelector('.quick-contact-widget')) return;

    const widgetHTML = `
        <div class="quick-contact-widget">
            <button class="quick-contact-toggle" aria-label="Quick Contact">
                <i class="fa fa-comments"></i>
            </button>
            <div class="quick-contact-menu">
                <a href="https://wa.me/923218073738" target="_blank" class="qc-item whatsapp" title="WhatsApp">
                    <i class="fa fa-whatsapp"></i>
                </a>
                <a href="tel:+923218073738" class="qc-item phone" title="Call Us">
                    <i class="fa fa-phone"></i>
                </a>
                <a href="mailto:info@pakgusu.com" class="qc-item email" title="Email Us">
                    <i class="fa fa-envelope"></i>
                </a>
            </div>
        </div>
    `;
    document.body.insertAdjacentHTML('beforeend', widgetHTML);

    // Toggle logic
    const toggleBtn = document.querySelector('.quick-contact-toggle');
    const menu = document.querySelector('.quick-contact-menu');
    const icon = toggleBtn.querySelector('i');

    toggleBtn.addEventListener('click', () => {
        menu.classList.toggle('active');
        if (menu.classList.contains('active')) {
            icon.classList.remove('fa-comments');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-comments');
        }
    });
}

// Initialize on Document Ready
jQuery(document).ready(function () {
    injectQuickContactWidget();

    // Preloader Safety Timeout
    setTimeout(function () {
        jQuery('.loading-area').fadeOut(1000);
    }, 3000);
});


/* ============================================
   Key Benefits Visual Map Logic
   Scope: #key-benefits-map
   ============================================ */
jQuery(document).ready(function ($) {
    if ($('#key-benefits-map').length) {

        // Initial State: Activate first card if none active
        if (!$('.benefit-card.active').length) {
            $('.benefit-card:first').addClass('active');
            $('.collage-tile:first').addClass('active');
        }

        // Interaction Handler
        function activateBenefit(id, $card) {
            // Remove active class from all
            $('.benefit-card').removeClass('active');
            $('.collage-tile').removeClass('active');

            // Add active class to current
            $card.addClass('active');
            $(`.collage-tile[data-target="${id}"]`).addClass('active');
        }

        // On Click or Hover (desktop)
        $('.benefit-card').on('mouseenter click', function () {
            const id = $(this).data('id');
            activateBenefit(id, $(this));
        });

        // Click on Image Tile also activates card
        $('.collage-tile').on('click', function () {
            const id = $(this).data('target');
            const $card = $(`.benefit-card[data-id="${id}"]`);
            activateBenefit(id, $card);

            // On mobile/tablet, scroll to content if needed
            if ($(window).width() < 992) {
                // Optional: Scroll to card
                // $('html, body').animate({
                //     scrollTop: $card.offset().top - 100
                // }, 500);
            }
        });

        // Auto-rotation (Optional: Pauses on hover)
        let rotationInterval;
        const autoRotate = () => {
            if ($('#key-benefits-map:hover').length) return; // Don't rotate if hovering section

            const $active = $('.benefit-card.active');
            let $next = $active.next('.benefit-card');
            if (!$next.length) $next = $('.benefit-card:first');

            activateBenefit($next.data('id'), $next);
        };

        // Start auto-rotation after 5 seconds, change every 4s
        // setTimeout(() => {
        //     rotationInterval = setInterval(autoRotate, 4000);
        // }, 1000);
    }
});

/* ============================================
   Types & Options Configurator Logic
   Scope: #types-configurator
   ============================================ */
jQuery(document).ready(function ($) {
    if ($('#types-configurator').length) {

        // Data Store
        const configData = {
            standard: {
                title: 'Standard View',
                desc: 'Cost-effective panel for non-fire-rated, non-ESD areas.',
                img: '../../images/gallery/pic1.jpg',
                stats: { fire: 'None', esd: 'None', iso: 'ISO 7-9', cost: '●○○○' },
                defaults: ['glazing-single']
            },
            fire: {
                title: 'Fire Rated (60 Min)',
                desc: 'Certified borosilicate glass and thermal insulation for fire compartments.',
                img: '../../images/gallery/pic2.jpg',
                stats: { fire: '60 Min', esd: 'None', iso: 'ISO 7-8', cost: '●●●○' },
                defaults: ['glazing-double', 'addon-tint']
            },
            esd: {
                title: 'Anti-Static / ESD',
                desc: 'Dissipative coating and grounding points for electronics assembly.',
                img: '../../images/gallery/pic3.jpg',
                stats: { fire: 'None', esd: 'Yes', iso: 'ISO 5-7', cost: '●●○○' },
                defaults: ['glazing-double']
            }
        };

        // Text Generators
        function getSummaryText(typeKey) {
            const typeName = configData[typeKey].title.split('(')[0].trim();
            const activeOptions = [];
            $('.option-pill.active').each(function () {
                activeOptions.push($(this).text());
            });
            const optsText = activeOptions.length ? activeOptions.join(' • ') : 'Standard Config';
            return `${typeName} • ${optsText}`;
        }

        // Action: Update Panel
        function updatePanel(typeKey) {
            const data = configData[typeKey];
            const $panel = $('.config-detail-panel');

            // 1. Fade out content slightly
            $panel.css('opacity', '0.7');

            setTimeout(() => {
                // 2. Update Image, Text & Chips
                $('#conf-main-img').attr('src', data.img);
                $('#conf-title').text(data.title);
                $('#conf-desc').text(data.desc);
                $('#conf-stat-fire').text(data.stats.fire);
                $('#conf-stat-esd').text(data.stats.esd);
                $('#conf-stat-iso').text(data.stats.iso);
                $('#conf-stat-cost').text(data.stats.cost);

                // 3. Reset Options to Defaults for this type
                $('.option-pill').removeClass('active');
                if (data.defaults) {
                    data.defaults.forEach(opt => {
                        $(`.option-pill[data-opt="${opt}"]`).addClass('active');
                    });
                }

                // 4. Update Summary
                $('#conf-summary-text').text(getSummaryText(typeKey));

                // 5. Fade back in
                $panel.css('opacity', '1');
            }, 200);
        }

        // Event: Click Type Card
        $('.type-card').on('click', function () {
            // UI Toggle
            $('.type-card').removeClass('active');
            $(this).addClass('active');

            // Update Logic
            const typeKey = $(this).data('type');
            updatePanel(typeKey);
        });

        // Event: Click Option Pill
        $('.option-pill').on('click', function () {
            // Toggle Self
            // If in a group like Glazing, maybe behave like radio?
            // For now, simpler toggle behavior or single-select per row

            // If it's glazing, allow only one
            if ($(this).data('opt').includes('glazing')) {
                $(this).siblings().removeClass('active');
                $(this).addClass('active');
            } else {
                $(this).toggleClass('active');
            }

            // Update Summary
            const currentType = $('.type-card.active').data('type');
            $('#conf-summary-text').text(getSummaryText(currentType));
        });
    }
});

/* ============================================
   Key Features Console Logic
   Scope: #features-console
   ============================================ */
jQuery(document).ready(function ($) {
    if ($('#features-console').length) {

        // Data Store
        const featuresData = {
            clean: {
                id: '01',
                title: 'Easy to Clean',
                hook: 'Minimizes cleaning cycles and usage.',
                desc: 'Completely flush surfaces with no crevices for bacteria to hide. Resistant to VHP and aggressive cleaning agents used in GMP facilities.',
                metrics: ['Cleanability: 5/5', 'GMP Ready']
            },
            durable: {
                id: '02',
                title: 'Durable',
                hook: 'Impact resistant and long-lasting.',
                desc: 'Engineered with high-grade aluminum and tempered glass to withstand accidental impacts and daily wear in high-traffic zones.',
                metrics: ['Impact: IK08', 'Lifespan: 20yr']
            },
            modular: {
                id: '03',
                title: 'Modular Design',
                hook: 'Flexible design for easy expansion.',
                desc: 'Interchangeable panels and standardized joints allow for rapid layout changes without significant downtime or construction dust.',
                metrics: ['Flexibility: High', 'Dust Free']
            },
            install: {
                id: '04',
                title: 'Fast Installation',
                hook: 'Quick assembly reduces downtime.',
                desc: 'Pre-engineered components click and lock into place, reducing installation time by up to 40% compared to traditional methods.',
                metrics: ['Time Saving: 40%', 'Plug & Play']
            },
            chemical: {
                id: '05',
                title: 'Chemical Resistant',
                hook: 'Compatible with standard agents.',
                desc: 'Surface materials are tested against common sterilization agents including Spor-Klenz, VHP, and Isopropyl Alcohol.',
                metrics: ['VHP Safe', 'Resistant']
            },
            noise: {
                id: '06',
                title: 'Noise Dampening',
                hook: 'Quieter environment for operators.',
                desc: 'Double-glazed options and insulated cores significantly reduce noise transfer between technical areas and clean spaces.',
                metrics: ['Reduction: 35dB', 'Focus High']
            }
        };

        // Function: Activate Feature
        function setActiveFeature(key) {
            const data = featuresData[key];
            if (!data) return;

            // 1. Nav Pills
            $('.feature-nav-pill').removeClass('active');
            $(`.feature-nav-pill[data-feature="${key}"]`).addClass('active');

            // 2. Schematic Nodes
            $('.feature-node').removeClass('active');
            $(`.feature-node[data-feature="${key}"]`).addClass('active');

            // 3. Story Panel Update (with fade)
            const $panel = $('.feature-story-panel .panel-body');
            $panel.css('opacity', '0.5');

            setTimeout(() => {
                $('.feature-story-panel .panel-header span').text(`Feature ${data.id} / 06`);
                $('#feat-title').text(data.title);
                $('#feat-hook').text(data.hook);
                $('#feat-desc').text(data.desc);

                // Metrics
                let metricHtml = '';
                data.metrics.forEach(m => {
                    metricHtml += `<div class="metric-pill m-b5"><span class="font-11 font-weight-600 text-dark-blue">${m}</span></div> `;
                });
                $('.metrics-grid').html(metricHtml);

                $panel.css('opacity', '1');
            }, 200);
        }

        // Interaction: Click Nav Pill
        $('.feature-nav-pill').on('click', function () {
            const key = $(this).data('feature');
            setActiveFeature(key);
            stopAutoPlay();
        });

        // Interaction: Click Node
        $('.feature-node').on('click', function () {
            const key = $(this).data('feature');
            setActiveFeature(key);
            stopAutoPlay();
        });

        // Auto-Play Logic
        let autoPlayInterval;
        let features = Object.keys(featuresData);
        let currentIndex = 0;

        function startAutoPlay() {
            autoPlayInterval = setInterval(() => {
                currentIndex = (currentIndex + 1) % features.length;
                setActiveFeature(features[currentIndex]);
            }, 5000);
        }

        function stopAutoPlay() {
            clearInterval(autoPlayInterval);
        }

        // Start Auto-Play initially
        // startAutoPlay(); // Optional: Uncomment to enable auto-rotation

        // Stop on hover
        $('#features-console').hover(function () {
            stopAutoPlay();
        }, function () {
            // startAutoPlay(); // Resume?
        });

    }
});

/* ============================================
   Typical Applications Logic
   Scope: #typical-applications
   ============================================ */
jQuery(document).ready(function ($) {
    if ($('#typical-applications').length) {

        function moveIndicator($tab) {
            const $wrapper = $('.app-tabs-nav');
            const $indicator = $('.nav-indicator');

            const left = $tab.position().left;
            const width = $tab.outerWidth();

            $indicator.css({
                left: left + 'px',
                width: width + 'px'
            });
        }

        // Init Indicator
        const $activeTab = $('.app-tab-link.active');
        if ($activeTab.length) {
            // Need a slight delay or window load to get correct widths if fonts loading
            setTimeout(() => moveIndicator($activeTab), 100);
        }

        // Tab Click
        $('.app-tab-link').on('click', function () {
            const $this = $(this);
            const target = $this.data('tab');

            // 1. Update Tabs
            $('.app-tab-link').removeClass('active').attr('aria-selected', 'false');
            $this.addClass('active').attr('aria-selected', 'true');
            moveIndicator($this);

            // 2. Update Content
            $('.app-tab-pane').removeClass('active');
            // Slight delay for animation feel? CSS transition handles opacity
            setTimeout(() => {
                $('#tab-' + target).addClass('active');
            }, 50);
        });

        // Row Card Expansion
        $('.app-row-card').on('click', function () {
            const $details = $(this).find('.card-expand-details');

            if ($details.hasClass('expanded')) {
                $details.removeClass('expanded').slideUp(200);
            } else {
                // Optional: Close others?
                // $('.card-expand-details').removeClass('expanded').slideUp(200);

                $details.addClass('expanded').slideDown(200); // Using slideDown for smooth height
            }
        });

    }
});

/* ============================================
   Visual Story Wall Logic
   Scope: #visual-story-wall
   ============================================ */
jQuery(window).on('load', function () { // Wait for images to load for Isotope
    const $wall = $('#visual-story-wall');
    if ($wall.length && jQuery().isotope) {

        // 1. Init Isotope
        const $grid = $wall.find('.gallery-grid').isotope({
            itemSelector: '.media-tile',
            percentPosition: true,
            masonry: {
                columnWidth: '.grid-sizer'
            }
        });

        // 2. Filters
        $wall.find('.filter-chip').on('click', function () {
            const filterValue = $(this).attr('data-filter');

            // UI Update
            $wall.find('.filter-chip').removeClass('active');
            $(this).addClass('active');

            // Isotope Filter
            $grid.isotope({ filter: filterValue });
        });

        // 3. Lightbox (Ensure it's init for new items if not global)
        if (jQuery().magnificPopup) {
            $wall.find('.mfp-gallery').magnificPopup({
                delegate: '.mfp-link',
                type: 'image',
                tLoading: 'Loading image #%curr%...',
                mainClass: 'mfp-img-mobile',
                gallery: {
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
                },
                image: {
                    tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
                    titleSrc: function (item) {
                        return item.el.attr('title') + '<small>Visual Story Wall</small>';
                    }
                }
            });
        }
    }
});

/* ============================================
   Ecosystem Map Logic
   Scope: #ecosystem-section
   ============================================ */
jQuery(document).ready(function ($) {
    if ($('#ecosystem-section').length) {

        const ecoData = {
            'pharma': {
                tag: 'PHARMACEUTICAL',
                title: 'GMP-Compliant Solutions',
                desc: 'Designed for ISO 5-8 cleanrooms with flush surfaces to prevent particle accumulation and simplify cleaning regiments.',
                stat1: { check: '35+', label: 'Projects' },
                stat2: { check: '100%', label: 'Compliance' },
                link: '../../industries/pharmaceutical-nutraceutical/'
            },
            'electronics': {
                tag: 'ELECTRONICS',
                title: 'Anti-Static ESD Control',
                desc: 'Conductive and static-dissipative materials prevent electrostatic discharge, protecting sensitive components.',
                stat1: { check: '50+', label: 'Fabs' },
                stat2: { check: 'ISO 4', label: 'Class Ready' },
                link: '../../industries/electronics-manufacturing/'
            },
            'food': {
                tag: 'FOOD & BEVERAGE',
                title: 'Hygienic Washdown Ready',
                desc: 'Resistant to harsh cleaning chemicals and high-pressure washdowns, ensuring food safety compliance.',
                stat1: { check: 'FDA', label: 'Compliant' },
                stat2: { check: 'IP65', label: 'Rated' },
                link: '#'
            },
            'healthcare': {
                tag: 'HEALTHCARE',
                title: 'Clinical Grade Hygiene',
                desc: 'Hermetically sealed solutions for operating theaters and isolation rooms, minimizing infection risk.',
                stat1: { check: '200+', label: 'Hospitals' },
                stat2: { check: '99.9%', label: 'Seal' },
                link: '../../industries/healthcare-hospitals/'
            },
            'labs': {
                tag: 'R&D LABS',
                title: 'Maximum Visibility',
                desc: 'High-clarity glazing for observation and safety in research environments, with integrated blinds options.',
                stat1: { check: 'High', label: 'Visibility' },
                stat2: { check: 'Safe', label: 'Glazing' },
                link: '#'
            }
        };

        function updateEcoCard(key) {
            const data = ecoData[key];
            if (!data) return;

            const $container = $('#eco-card-container');
            const $card = $container.find('.eco-card');

            // 1. Animate Out
            $card.css('opacity', '0.5'); // Quick visible feedback

            // 2. Build New HTML
            const newHtml = `
                <div class="eco-card bg-white p-a30 shadow-lg border-radius-12 border-left-theme animate-in">
                    <span class="d-inline-block p-a5 p-lr15 bg-light-blue text-white font-11 font-weight-700 border-radius-30 m-b15">${data.tag}</span>
                    <h3 class="font-24 font-weight-700 text-dark-blue m-t0 m-b10">${data.title}</h3>
                    <p class="text-muted m-b20">${data.desc}</p>
                    <div class="eco-stats d-flex m-b25">
                        <div class="m-r20">
                            <span class="d-block font-20 font-weight-700 text-dark-blue">${data.stat1.check}</span>
                            <span class="font-12 text-muted">${data.stat1.label}</span>
                        </div>
                        <div>
                            <span class="d-block font-20 font-weight-700 text-dark-blue">${data.stat2.check}</span>
                            <span class="font-12 text-muted">${data.stat2.label}</span>
                        </div>
                    </div>
                    <a href="${data.link}" class="site-button-link font-weight-700">View Solutions <i class="fa fa-angle-right"></i></a>
                </div>
            `;

            // 3. Replace & Animate In
            setTimeout(() => {
                $container.html(newHtml);
            }, 100);
        }

        // Click Handler
        $('.eco-node').on('mouseenter click', function (e) {
            // Logic to prevent double firing on touch devices can be added if needed
            if (e.type === 'mouseenter' && $(window).width() < 991) return; // Don't hover on mobile

            const target = $(this).attr('data-industry');
            if ($(this).hasClass('active')) return;

            // UI Updates
            $('.eco-node').removeClass('active');
            $(this).addClass('active');

            // Lines
            $('.eco-line').removeClass('active-line');
            $('.line-' + target).addClass('active-line');

            // Card
            updateEcoCard(target);
        });

        // Auto-Play Logic
        let rotationInterval;
        const rotateSpeed = 4000; // 4 seconds
        const industries = ['pharma', 'electronics', 'food', 'healthcare', 'labs'];
        let currentIndex = 0;

        function startRotation() {
            stopRotation();
            rotationInterval = setInterval(() => {
                currentIndex = (currentIndex + 1) % industries.length;
                const nextKey = industries[currentIndex];

                // Trigger update
                $('.eco-node[data-industry="' + nextKey + '"]').trigger('fake-click');
            }, rotateSpeed);
        }

        function stopRotation() {
            if (rotationInterval) clearInterval(rotationInterval);
        }

        // Custom Event for auto-play (simulates click without user interaction logic like scrolling)
        $('.eco-node').on('fake-click', function () {
            const target = $(this).attr('data-industry');

            $('.eco-node').removeClass('active');
            $(this).addClass('active');

            $('.eco-line').removeClass('active-line');
            $('.line-' + target).addClass('active-line');

            updateEcoCard(target);
        });

        // Start cycling
        startRotation();

        // Pause on interaction
        $('#ecosystem-section').on('mouseenter', stopRotation).on('mouseleave', startRotation);
    }
});



