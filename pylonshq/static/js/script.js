/* Author: 

*/

// App globals
var App = window.App || {};
App.widgets = {}

$(document).ready(function() {
    $('#highlight-download').hover(
        function() {
            //$(this).addClass('auto-height');
            $('#highlight-download .options').show()
        },
        function() {
            //$(this).removeClass('auto-height');
            $('#highlight-download .options').hide()
        }
    );
    $('#company-slideshow').cycle({speed: 4000})
});





















