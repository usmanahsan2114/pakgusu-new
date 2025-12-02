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
    jQuery('#mobile-side-drawer').on('click', function() {
        jQuery('.header-nav').toggleClass('show');
        jQuery('.mobile-menu-overlay').toggleClass('show');
        jQuery('body').toggleClass('menu-open');
    });
    
    jQuery('.mobile-menu-overlay').on('click', function() {
        jQuery('.header-nav').removeClass('show');
        jQuery(this).removeClass('show');
        jQuery('body').removeClass('menu-open');
    });
}

// Scroll to Top Button
function scrollToTop() {
    var btn = jQuery('.scroltop');
    
    jQuery(window).on('scroll', function() {
        if (jQuery(this).scrollTop() > 300) {
            btn.fadeIn();
        } else {
            btn.fadeOut();
        }
    });
    
    btn.on('click', function(e) {
        e.preventDefault();
        jQuery('html, body').animate({scrollTop: 0}, 600);
    });
}

// Fade In on Scroll for Elements with .fade-in-up class
function fadeInOnScroll() {
    var fadeElements = jQuery('.fade-in-up');
    
    fadeElements.each(function() {
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
jQuery(document).ready(function() {
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
jQuery(window).on('scroll', function() {
    stickyHeaderShrink();
    scrollProgress();
    fadeInOnScroll();
});

/* ============================================
   END TIER 1 GLOBAL ENHANCEMENTS JAVASCRIPT
   ============================================ */
