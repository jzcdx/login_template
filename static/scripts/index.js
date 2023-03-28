function test() {
    alert("hi");
}

var signUpDiv = document.getElementById("sign-up");
var signInDiv = document.getElementById("sign-in");
var header = document.getElementById("header");

function showSignUp() {
    console.log("here");
    signUpDiv.style.display = "block";
    signInDiv.style.display = "none";
    header.innerHTML = "sign up"
}

function submit_new_account() {
    var newEmail = document.getElementById("newEmail").value;
    var newPassword = document.getElementById("newPassword").value;
    var newPasswordC = document.getElementById("newPasswordC").value;
    
    if (newPassword != newPasswordC) {
        return;
    }

    var newAccountData = {email: newEmail, password: newPassword};

    $.ajax({
        type: "POST", //method
        url: "/makenewnccount", //this is the flask route
        data: JSON.stringify(newAccountData), //I have no idea what this is
        contentType: "application/json",
        dataType: 'json', 
        success: function(result) { //when the response comes back and it's successful, run the code below
            //This updates the description with the new value from the textarea
            console.log(result)
        } 
    });
}