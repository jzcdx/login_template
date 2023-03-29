from flask import Flask, render_template, request
from db_utils import DBH
application = Flask(__name__)

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

#@application.route("/login", methods=[""])

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)