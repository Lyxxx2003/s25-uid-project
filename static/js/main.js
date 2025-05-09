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
    
    // Handle recipe descriptions
    let currentDescIndex = 0;
    const descriptions = $('.description-slide');
    const startCraftingBtn = $('.start-crafting-btn');
    
    // Check if we've seen this content before
    const currentPath = window.location.pathname;
    const hasSeenBefore = localStorage.getItem(currentPath) === 'true';
    
    function showDescription(index) {
        // Hide all descriptions
        descriptions.removeClass('active');
        
        if (index < descriptions.length) {
            const currentSlide = $(descriptions[index]);
            currentSlide.addClass('active');
            
            if (hasSeenBefore) {
                // Skip animation for previously viewed content
                if (index === descriptions.length - 1) {
                    startCraftingBtn.addClass('visible');
                } else {
                    currentSlide.find('.continue-btn').addClass('visible');
                }
            } else {
                // Get text content and clear the element
                const textElement = currentSlide.find('.recipe-description');
                const text = textElement.text();
                textElement.text('');
                
                let charIndex = 0;
                
                // Typewriter effect for current description
                function typeChar() {
                    if (charIndex < text.length) {
                        textElement.text(textElement.text() + text[charIndex]);
                        charIndex++;
                        setTimeout(typeChar, 50);
                    } else {
                        // Show continue button or start crafting button
                        if (index === descriptions.length - 1) {
                            startCraftingBtn.addClass('visible');
                        } else {
                            currentSlide.find('.continue-btn').addClass('visible');
                        }
                    }
                }
                
                typeChar();
            }
        }
    }
    
    // Handle continue button clicks
    $('.continue-btn').click(function() {
        currentDescIndex++;
        showDescription(currentDescIndex);
    });
    
    // Start with the first description
    if (descriptions.length > 0) {
        showDescription(0);
        // Mark as seen for future visits
        localStorage.setItem(currentPath, 'true');
    }
    
    // $('#take-quiz-btn').click(function () {
    //     if (!hasInProgress) {
    //         window.location.href = "/quiz/1";
    //         return;
    //     }
    
    //     if (confirm("You have an unfinished quiz. Would you like to resume where you left off?")) {
    //         window.location.href = `/quiz/${lastQid}`;
    //     } else {
    //         fetch('/reset_quiz', { method: 'POST' }).then(() => {
    //             window.location.href = '/quiz/1';
    //         });
    //     }
    // });
    
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
    
    // Check if we've seen this page before
    const currentPath = window.location.pathname;
    const hasSeenBefore = localStorage.getItem(currentPath) === 'true';
    
    if (hasSeenBefore) {
        // Skip animation for previously viewed content
        element.innerText = textToType;
    } else {
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
        
        // Mark as seen for future visits
        localStorage.setItem(currentPath, 'true');
    }
}

// Function to initialize typewriter on the introduction page
function initTypewriter() {
    // Use null for text parameter so that the typewriter function will read from data-text
    typewriter('typewriter-text', null, 50, 1000);
} 


