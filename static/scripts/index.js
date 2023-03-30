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
    console.log("heeeeere");
    var newEmail = document.getElementById("newEmail").value;
    var newPassword = document.getElementById("newPassword").value;
    var newPasswordC = document.getElementById("newPasswordC").value;
    
    if (newPassword != newPasswordC) {
        return;
    }

    var newAccountData = {
        email: newEmail, 
        password: newPassword
    };

    $.ajax({
        type: "POST", //method
        url: "/signup", //this is the flask route
        data: JSON.stringify(newAccountData), //I have no idea what this is
        contentType: "application/json",
        dataType: 'json', 
        success: function(result) { //when the response comes back and it's successful, run the code below
            //This updates the description with the new value from the textarea
            console.log(result)
            backToLogin()
        } 
    });
}

function backToLogin() {
    signUpDiv.style.display = "none";
    signInDiv.style.display = "block";
    header.innerHTML = "login"
}

function submitLoginDetails() {
    var loginAttempt = {
        email: document.getElementById("attemptEmail").value,
        password: document.getElementById("attemptPassword").value 
    }

    $.ajax({
        type: "POST", //method
        url: "/login", //this is the flask route
        data: JSON.stringify(loginAttempt), //I have no idea what this is
        contentType: "application/json",
        dataType: 'json', 
        success: function(result) { //when the response comes back and it's successful, run the code below
            //This updates the description with the new value from the textarea
            
            loginLabel = document.getElementById("login-indicator");
            if (result["password correct"]) {
                console.log("password right");
                loginLabel.innerHTML = "Logging in";
            } else {
                console.log("password wrong")
                if (result["email exists"]) {
                    loginLabel.innerHTML = "Password Incorrect";
                } else {
                    loginLabel.innerHTML = "Email Incorrect";
                }
            }
        } 
    });
}