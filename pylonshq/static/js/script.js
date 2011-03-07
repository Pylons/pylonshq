/* Author: 

*/

// App globals
var App = window.App || {};
App.widgets = {}

$(document).ready(function() {
    $('.header-nav ul li').hover(
        function() { $(this).children('.header-nav-submenu').show() },
        function() { $(this).children('.header-nav-submenu').hide() }
    );
    $('#highlight-download').hover(
        function() { $('#highlight-download .options').show() },
        function() { $('#highlight-download .options').hide() }
    );
    $('#company-slideshow').cycle({speed: 2000, timeout: 10000})
    $('#highlight-slideshow').cycle({speed: 2000, timeout: 8000});
});





















