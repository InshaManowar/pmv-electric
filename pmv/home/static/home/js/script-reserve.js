$(document).ready(function() {

    $('.color-choose input').on('click', function() {
        var headphonesColor = $(this).attr('data-image');

        $('.active').removeClass('active');
        $('.left-column img[data-image = ' + headphonesColor + ']').addClass('active');
        $(this).addClass('active');
    });

});
var colour = 1;

function blackfunc() {
    colour = 3;
}

function bluefunc() {
    colour = 2;
}

function redfunc() {
    colour = 1;
}

function submitfunc() {
    if (colour == 1) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 2) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 3) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 4) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 5) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 6) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 7) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 8) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else if (colour == 9) {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    } else {
        window.location.href = "https://buy.stripe.com/test_8wM3cs4UUfkCcdaeUW";
    }
}

function savefunc() {
    console.log('success')
}