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
    $('#company-slideshow').cycle({speed: 4000})
});





















