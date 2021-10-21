// Helper Functions
function updateGrid(r, c, state){
	var sel = "#" + r.toString()+ "-" + c.toString();
    if (state != 0){
    }
}

function createGrid(data){
	var result = "";

	for (var i in data){
		var cr = "<tr>";

		for (var j in data[i]){
			cr = cr + "<td id=\"" + i.toString()+ "-" + j.toString() + "\"></td>"
		}

		cr = cr + "</tr>\n";
		result = result + cr;
	}
	$("#grid").html(result);
}


// Getting the document ready
$(document).ready(function(){

    // // Changing the background and text to a dark mode theme
    // // When button is clicked
    // $("#toggle").click(function(){
    //     var element = document.body;
    //     element.classList.toggle("dark-mode");
    // });

    $.get("Generate/", {}, function(response){
		var data = JSON.parse(response);
		createGrid(data);
		for (var row in data){
			for (var col in data[row]){
				updateGrid(row, col, data[row][col]);
			}
		}
	});

});