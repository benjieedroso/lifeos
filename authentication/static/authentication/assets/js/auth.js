/* 
========================================================================
   BOOTSTRAP 5 ADMIN TEMPLATE - LIFEOS
   AUTHENTICATION MODULE JAVASCRIPT
   Developed with premium UI/UX standards

   Template Name: LifeOS
   Version: 1.0 
   Author: LifeOS Team
========================================================================
*/

document.addEventListener('DOMContentLoaded', function () {
    /**
     * Password Visibility Toggle Logic
     * Enables toggling password input between obscured dots and plain text.
     * Each .password-toggle-btn targets its input via a data-target id.
     */
    document.querySelectorAll('.password-toggle-btn').forEach(function (toggleButton) {
        toggleButton.addEventListener('click', function () {
            const passwordInput = document.getElementById(this.dataset.target);
            if (!passwordInput) return;

            // Toggle input type attribute
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);

            // Toggle eye icon class & aria-label
            const icon = this.querySelector('i');
            if (type === 'text') {
                if (icon) {
                    icon.classList.remove('bi-eye');
                    icon.classList.add('bi-eye-slash');
                }
                this.setAttribute('aria-label', 'Hide password');
            } else {
                if (icon) {
                    icon.classList.remove('bi-eye-slash');
                    icon.classList.add('bi-eye');
                }
                this.setAttribute('aria-label', 'Show password');
            }
        });
    });

    // NOTE: No client-side submit blocking on purpose — the form always
    // POSTs (it carries `novalidate`) so Django validates and renders messages.
});
