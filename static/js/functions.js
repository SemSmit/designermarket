$('#menu').on('click', function(){
    $('.navbar-nav').slideToggle();
});

var x = window.matchMedia("(min-width: 769px)");

$(function(){
        QueryFunction(x);
});



function QueryFunction(x) {
  if (x.matches) {
    $('.navbar-nav').show();
    $('#menu').hide();
  } else {
    $('.navbar-nav').hide();
    $('#menu').show();
  }
}

window.addEventListener('resize', function(){
    x.addListener(QueryFunction);
});

$(document).ready(function() {
  $('li.active').removeClass('active');
  $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
});




