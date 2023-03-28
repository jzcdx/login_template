from flask import Flask, render_template, request

application = Flask(__name__)

@application.route("/")
def main():
    return render_template("index.html")

@application.route("/makenewnccount", methods=["POST"])
def new_account():
    if request.method == "POST":
        account_data = request.get_json()
        print(account_data);
    return {'updated': 'true'}

if __name__ == "__main__":
    application.run(debug=True, use_reloader=True, threaded=True)