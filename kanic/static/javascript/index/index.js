$(document).ready(function() {

    var top = $(document).scrollTop();
    if(top > 50) {
        $('.navbar').removeClass('navbar-transparent');
        $('.navbar-default .navbar-nav > li > a').css('color', 'black');
        $('.navbar-default .navbar-brand').css('color', 'black');
    } else {
        $('.navbar').addClass('navbar-transparent');
        $('.navbar-default .navbar-nav > li > a').css('color', 'white');
        $('.navbar-default .navbar-brand').css('color', 'white');
    }
    // listening to scrolling action
    $(window).scroll(function () {
        var top = $(document).scrollTop();

        if(top > 50) {
            $('.navbar').removeClass('navbar-transparent');
            $('.navbar-default .navbar-nav > li > a').css('color', 'black');
            $('.navbar-default .navbar-brand').css('color', 'black');
        } else {
            $('.navbar').addClass('navbar-transparent');
            $('.navbar-default .navbar-nav > li > a').css('color', 'white');
            $('.navbar-default .navbar-brand').css('color', 'white');
        }
    });

    // trigger css in main section to animate(eg. transition)
    $('.landing-section').css('top', '40%');
    $('.main-line, .main-title').css('color', 'rgba(255, 255, 255, 1)')
    $('button.signup').css('color', 'rgba(0, 0, 0, 0.4)')
    $('button.signup').css('background-color', 'rgba(255, 255, 255, 1)')
});
