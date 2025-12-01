/* ======================================
   WhatsApp Widget Injection
   ====================================== */

(function ($) {
    'use strict';

    function injectWhatsAppWidget() {
        var widgetHTML = `
            <a href="https://wa.me/923218073738" class="whatsapp-widget" target="_blank">
                <i class="fa fa-whatsapp"></i>
                <div class="wa-text">
                    <span class="wa-title">Chat with us</span>
                    <span class="wa-subtitle">Online now</span>
                </div>
            </a>
        `;
        $('body').append(widgetHTML);
    }

    $(document).ready(function () {
        injectWhatsAppWidget();
    });

})(jQuery);
