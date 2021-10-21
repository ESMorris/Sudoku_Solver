$(document).ready(function(){

    // Jquery code added here
    $("#toggle").click(function(){
        console.log("Success!!!");
        var element = document.body;
        element.classList.toggle("dark-mode");
    });

});