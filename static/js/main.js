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
}); 