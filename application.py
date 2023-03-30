from flask import Flask, render_template, request, session
from db_utils import DBH
import bcrypt
import secrets

application = Flask(__name__)
application.secret_key = secrets.token_urlsafe(16)

@application.route("/")
def main():
    return render_template("index.html")

@application.route("/signup", methods=["POST"])
def new_account():
    if request.method == "POST":
        account_data = request.get_json()
        print(account_data)
        dbh = DBH()
        account_made = dbh.create_account(account_data["email"], account_data["password"]);
        #should probably update the frontend from here lol
        if account_made:
            print("account has been made successfully")
        else:
            print("email is already taken")
    return {'updated': 'true'}

@application.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        login_details = request.get_json()
        dbh = DBH()
        password_attempt = login_details["password"]
        correct_password = dbh.read_password(login_details["email"])
        if correct_password: #email exists in db
            #now we check if the password hashes match
            passwords_match = bcrypt.checkpw(password_attempt.encode('utf8'), correct_password.encode('utf8'))
            
            #print("passwords match: " , passwords_match);
            if passwords_match:
                session["logged_in"] = True
                session["email"] = login_details["email"]
                return {"email exists": 'true', "password correct:": 'true'}
            else:
                return {"password correct:": 'false'}
        else:
            print("email does not exist in database")
            return {"email exists": 'false', "password correct:": 'false'}
    
    return {"correct request":'false', "email exists": 'false', "password correct:": 'false'}
if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)