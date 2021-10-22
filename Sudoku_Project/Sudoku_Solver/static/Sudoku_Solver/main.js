// Helper Functions
//  Should be ran when we generate a new board
function updateGrid(r, c, state){
	var sel = r.toString()+ "-" + c.toString();
	if (state != 0){
		var newInput = document.createElement("input");
		newInput.type = "text";
		newInput.id = "s" + r.toString() + "-" + c.toString();
		newInput.className = "s0"; 
		newInput.size = "1";
		newInput.autocomplete = "off";
		newInput.readOnly = "readonly";
		newInput.value = state.toString();
		document.getElementById(sel).appendChild(newInput);
	}
	else{
		var newInput = document.createElement("input");
		newInput.type = "text";
		newInput.id = "s" + r.toString() + "-" + c.toString();
		newInput.className = "s0"; 
		newInput.size = "1";
		newInput.autocomplete = "off";
		newInput.value = "";
		document.getElementById(sel).appendChild(newInput)
	}
}

// Should only be ran once!!!
// Should create the grid only
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

	// Initialize the starting board when the app is first spun up
    $.get("Start/", {}, function(response){
		var data = JSON.parse(response);
		createGrid(data);
		for (var row in data){
			for (var col in data[row]){
				updateGrid(row, col, data[row][col]);
			}
		}
	});

	$("#GenerateBoard").click(function(){
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

	$("#SolveBoard").click(function(){
		$.get("Solve/", {}, function(response){
			var data = JSON.parse(response);
			createGrid(data);
			for (var row in data){
				for (var col in data[row]){
					updateGrid(row, col, data[row][col]);
				}
			}
		});
		window.alert("Solved Sudoku!");
	});

});