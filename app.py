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


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/get_risks")
def get_risks():
    """
    Main 'Risk Register' from 'risks'
    collection in MongoDB.
    """
    risks = list(mongo.db.risks.find())
    return render_template("risks.html", risks=risks)


@app.route("/search", methods=["GET", "POST"])
def search():
    # grab from search form input.
    query = request.form.get("query")
    """
    Search function on 'Risk Register' page.
    Indexes are set within MongoDB and match all fields in the 'Risk' form.
    """
    risks = list(mongo.db.risks.find({"$text": {"$search": query}}))
    return render_template("risks.html", risks=risks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        """
        Check if 'username' already exists within
        'users' collection in MongoDB. If so,
        give a flash message and reload the form.
        """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        """
        Register user with 'username' and 'password'.
        Add to 'users' collection in MongoDB and
        implement Werkzeug generate_password_hash
        helper which takes a plaintext password,
        hashing method and salt length as an input
        to produce hashed password, then stored in
        MongoDB.
        """
        register = {
            "username": request.form.get("username").lower(),
            # Werkzeug generate_password_hash helper
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        """
        Check if 'username' already exists within
        'users' collection in MongoDB. If so,
        check the password using Werkzeug
        check_password_hash helper.
        """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # password match
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # password doesn't match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Get the sessions user's username from 'users'
    collection in MongoDB and return 'Profile' page.
    """
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
    return redirect(url_for("index"))


@app.route("/add_risk", methods=["GET", "POST"])
def add_risk():
    if request.method == "POST":
        """
        Input form to add a new 'Risk' to the
        'Risk Register' which is held in the 'risks'
        collection in MongoDB.
        """
        is_open = "on" if request.form.get("is_open") else "off"
        risk = {
            "owner_name": request.form.get("owner_name"),
            "risk_name": request.form.get("risk_name"),
            "risk_description": request.form.get("risk_description"),
            "likelihood_name": request.form.get("likelihood_name"),
            "impact_name": request.form.get("impact_name"),
            "rating_name": request.form.get("rating_name"),
            "mitigating_action": request.form.get("mitigating_action"),
            "contingent_action": request.form.get("contingent_action"),
            "progress_on_actions": request.form.get("progress_on_actions"),
            "date_raised": request.form.get("date_raised"),
            "is_open": is_open,
            """
            Current logged-in user = created_by,
            which will be used to allow (or not)
            certain users to edit/delete certain 'Risks'
            """
            "created_by": session["user"]
        }
        mongo.db.risks.insert_one(risk)
        flash("Risk Successfully Added")
        return redirect(url_for("get_risks"))

    owners = mongo.db.owners.find()
    likelihoods = mongo.db.likelihoods.find()
    impacts = mongo.db.impacts.find()
    ratings = mongo.db.ratings.find()
    return render_template(
        "add_risk.html", owners=owners,
        likelihoods=likelihoods, impacts=impacts,
        ratings=ratings)


@app.route("/edit_risk/<risk_id>", methods=["GET", "POST"])
def edit_risk(risk_id):
    if request.method == "POST":
        # edit a current 'Risk'.
        is_open = "on" if request.form.get("is_open") else "off"
        submit = {
            "owner_name": request.form.get("owner_name"),
            "risk_name": request.form.get("risk_name"),
            "risk_description": request.form.get("risk_description"),
            "likelihood_name": request.form.get("likelihood_name"),
            "impact_name": request.form.get("impact_name"),
            "rating_name": request.form.get("rating_name"),
            "mitigating_action": request.form.get("mitigating_action"),
            "contingent_action": request.form.get("contingent_action"),
            "progress_on_actions": request.form.get("progress_on_actions"),
            "date_raised": request.form.get("date_raised"),
            "is_open": is_open,
            "created_by": session["user"]
        }
        mongo.db.risks.update({"_id": ObjectId(risk_id)}, submit)
        flash("Risk Successfully Updated")
        return redirect(url_for("get_risks"))

    risk = mongo.db.risks.find_one({"_id": ObjectId(risk_id)})
    owners = mongo.db.owners.find()
    likelihoods = mongo.db.likelihoods.find()
    impacts = mongo.db.impacts.find()
    ratings = mongo.db.ratings.find()
    return render_template(
        "edit_risk.html", risk=risk, owners=owners,
        likelihoods=likelihoods, impacts=impacts,
        ratings=ratings)


@app.route("/delete_risk/<risk_id>")
def delete_risk(risk_id):
    """
    Delete 'Risk' from 'risks'
    collection in MongoDB using the python
    remove() method.
    """
    mongo.db.risks.remove({"_id": ObjectId(risk_id)})
    flash("Risk Successfully Deleted")
    return redirect(url_for("get_risks"))


@app.route("/get_owners")
def get_owners():
    """
    Get list of owners from collection in MongoDB
    and sort them alphabetically for display.
    """
    owners = list(mongo.db.owners.find().sort("owner_name", 1))
    return render_template("owners.html", owners=owners)


@app.route("/add_owner", methods=["GET", "POST"])
def add_owner():
    """
    Add a new owner to the 'owners' collection
    in MongoDB under 'owner_name'.
    """
    if request.method == "POST":
        owner = {
            "owner_name": request.form.get("owner_name")
        }
        mongo.db.owners.insert_one(owner)
        flash("Risk Owner Added")
        return redirect(url_for("get_owners"))

    return render_template("add_owner.html")


@app.route("/edit_owner/<owner_id>", methods=["GET", "POST"])
def edit_owner(owner_id):
    # edit an 'owner'
    if request.method == "POST":
        submit = {
            "owner_name": request.form.get("owner_name")
        }
        mongo.db.owners.update({"_id": ObjectId(owner_id)}, submit)
        flash("Risk Owner Successfully Updated")
        return redirect(url_for("get_owners"))

    owner = mongo.db.owners.find_one({"_id": ObjectId(owner_id)})
    return render_template("edit_owner.html", owner=owner)


@app.route("/delete_owner/<owner_id>")
def delete_owner(owner_id):
    # delete owner using python remove()
    mongo.db.owners.remove({"_id": ObjectId(owner_id)})
    flash("Risk Owner Successfully Deleted")
    return redirect(url_for("get_owners"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
