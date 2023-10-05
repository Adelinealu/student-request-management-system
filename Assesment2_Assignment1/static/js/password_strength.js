// password_strength.js

document.addEventListener('DOMContentLoaded', function () {
    const passwordInput = document.querySelector('#password');
    const strengthIndicator = document.querySelector('#password-strength');

    passwordInput.addEventListener('input', function () {
        const password = passwordInput.value;

        // Perform password strength checks here and update the indicator
        const strength = checkPasswordStrength(password);

        // Update the password strength indicator
        updateStrengthIndicator(strength);
    });

    function checkPasswordStrength(password) {
        // Implement your password strength checks here and return a strength score.
        // You can use regex, length checks, or any other method to evaluate the password.
        // Return a number indicating the strength level (e.g., 0 = weak, 1 = medium, 2 = strong).
        // Modify this function to match your password policy.

        // Example: Checking password length
        if (password.length < 8) {
            return 0; // Weak
        } else if (password.length < 12) {
            return 1; // Medium
        } else {
            return 2; // Strong
        }
    }

    function updateStrengthIndicator(strength) {
        // Update the password strength indicator based on the strength value.
        // Modify this function to match your design and style.

        // Example: Updating the indicator text and color
        const indicators = ['Weak', 'Medium', 'Strong'];
        strengthIndicator.textContent = 'Password Strength: ' + indicators[strength];
        strengthIndicator.style.color = ['red', 'orange', 'green'][strength];
    }
});
