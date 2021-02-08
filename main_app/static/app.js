$('#mobile-nav').click(function(event){
    $('.navbar-menu').toggleClass('is-active');
    $('.navbar-burger').toggleClass('is-active');
})

$('#open-logout-modal').click(function(event){
    $('#logout-modal').toggleClass('is-active');
})

$('.close-logout-modal').click(function(event){
    $('#logout-modal').toggleClass('is-active');
})