function validate() {
    var x = document.getElementById('first_name').value;
    var y = document.getElementById('last_name').value;
    var z = document.getElementById('email').value;
        if (x == "") { 
            alert("First Name is Empty!"); }
        if (y == "") { 
            alert("Last Name is Empty!"); }
        if (z == "") { 
            alert("Email is Empty!"); }
        if (x && y && z != "" ) { 
            alert("Thank for for filling up the form!"); }    
    }


function reset() {
    document.getElementById('first_name').value = "";
    document.getElementById('last_name').value = "";
    document.getElementById('email').value = "";
}

