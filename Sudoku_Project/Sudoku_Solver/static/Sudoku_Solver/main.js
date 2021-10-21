// Getting the document ready
$(document).ready(function(){

    // Changing the background and text to a dark mode theme
    // When button is clicked
    $("#toggle").click(function(){
        var element = document.body;
        element.classList.toggle("dark-mode");
    });

});