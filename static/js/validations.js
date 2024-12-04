// Custom Bootstrap 5 form validation
(function() {
    'use strict';

    // Wait until the DOM is fully loaded
    window.addEventListener('load', function() {
        // Fetch all forms that require validation
        var forms = document.querySelectorAll('.needs-validation');

        // Loop over each form and apply validation
        Array.prototype.slice.call(forms).forEach(function(form) {
            form.addEventListener('submit', function(event) {
                // Prevent form submission if it's invalid
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }

                // Add the Bootstrap validation classes
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();
