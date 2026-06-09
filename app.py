from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from models import db, User

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username or not email or not password:
            return "Please fill all fields."

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            return "Email already exists!"

        hashed_password = generate_password_hash(password)

        new_user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("register.html")


@app.route("/login", methods=["POST"])
def login():

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user and check_password_hash(user.password, password):

        return render_template(
            "dashboard.html",
            username=user.username
        )

    return "Invalid Email or Password"


@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",
        username="User"
    )


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/forgot-password")
def forgot_password():
    return "Forgot Password Page Coming Soon"