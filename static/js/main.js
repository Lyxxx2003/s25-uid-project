$(document).ready(function () {
    // Add hover effect to drink cards
    $('.drink-card').hover(
        function () {
            $(this).css('transform', 'scale(1.05)');
            $(this).css('transition', 'transform 0.2s');
        },
        function () {
            $(this).css('transform', 'scale(1)');
        }
    );

    // Add click animation to buttons
    $('.btn').click(function () {
        $(this).css('transform', 'scale(0.95)');
        setTimeout(() => {
            $(this).css('transform', 'scale(1)');
        }, 100);
    });

    // Add animation to energy meter when filled
    $('.energy-meter img').each(function (index) {
        if ($(this).hasClass('active')) {
            setTimeout(() => {
                $(this).css('transform', 'scale(1.2)');
                setTimeout(() => {
                    $(this).css('transform', 'scale(1)');
                }, 200);
            }, index * 100);
        }
    });
    
    // Initialize typewriter effect if element exists
    if ($("#typewriter-text").length > 0) {
        initTypewriter();
    }
});

/**
 * Typewriter effect for text elements
 * @param {string} elementId - The ID of the element to apply the effect to (default: 'typewriter-text')
 * @param {string} text - The text to type (if not provided, will use data-text attribute or element content)
 * @param {number} speed - Typing speed in milliseconds (default: 50)
 * @param {number} delay - Delay before typing starts in milliseconds (default: 1000)
 */
function typewriter(elementId = 'typewriter-text', text = null, speed = 50, delay = 1000) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    // Get text from data attribute, parameter, or element content
    const textToType = text || element.getAttribute('data-text') || element.innerText;
    
    // Clear the element's text
    element.innerText = '';
    
    // Create cursor element
    const cursor = document.createElement('span');
    cursor.className = 'typewriter-cursor';
    element.after(cursor);
    
    let i = 0;
    
    function typeWriterStep() {
        if (i < textToType.length) {
            element.innerText += textToType.charAt(i);
            i++;
            setTimeout(typeWriterStep, speed);
        }
    }
    
    // Start the typewriter effect after specified delay
    setTimeout(typeWriterStep, delay);
}

// Function to initialize typewriter on the introduction page
function initTypewriter() {
    // Use null for text parameter so that the typewriter function will read from data-text
    typewriter('typewriter-text', null, 50, 1000);
} 