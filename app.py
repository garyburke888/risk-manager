import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)



@app.route("/get_risks")
def get_risks():
    risks = list(mongo.db.risks.find())
    return render_template("risks.html", risks=risks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    risks = list(mongo.db.risks.find({"$text": {"$search": query}}))
    return render_template("risks.html", risks=risks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return render_template("profile.html", username=username)


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_risk", methods=["GET", "POST"])
def add_risk():
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        risk = {
            "category_name": request.form.get("category_name"),
            "risk_name": request.form.get("risk_name"),
            "risk_description": request.form.get("risk_description"),
            "rating_name": request.form.get("rating_name"),
            "is_urgent": is_urgent,
            "review_date": request.form.get("review_date"),
            "created_by": session["user"]
        }
        mongo.db.risks.insert_one(risk)
        flash("Risk Successfully Added")
        return redirect(url_for("get_risks"))

    ratings = mongo.db.ratings.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_risk.html", ratings=ratings, categories=categories)


@app.route("/edit_risk/<risk_id>", methods=["GET", "POST"])
def edit_risk(risk_id):
    if request.method == "POST":
        is_urgent = "on" if request.form.get("is_urgent") else "off"
        submit = {
            "category_name": request.form.get("category_name"),
            "risk_name": request.form.get("risk_name"),
            "risk_description": request.form.get("risk_description"),
            "rating_name": request.form.get("rating_name"),
            "is_urgent": is_urgent,
            "review_date": request.form.get("review_date"),
            "created_by": session["user"]
        }
        mongo.db.risks.update({"_id": ObjectId(risk_id)}, submit)
        flash("Risk Successfully Updated")

    risk = mongo.db.risks.find_one({"_id": ObjectId(risk_id)})
    ratings = mongo.db.ratings.find()
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_risk.html", risk=risk, ratings=ratings, categories=categories)


@app.route("/delete_risk/<risk_id>")
def delete_risk(risk_id):
    mongo.db.risks.remove({"_id": ObjectId(risk_id)})
    flash("Risk Successfully Deleted")
    return redirect(url_for("get_risks"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
