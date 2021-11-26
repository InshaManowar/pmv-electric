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
        window.location.href = "http://www.w3schools.com";
    } else if (colour == 2) {
        window.location.href = "http://www.google.com";
    } else {
        window.location.href = "http://www.yahoo.com";
    }
}