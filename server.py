from flask import Flask, render_template, request, redirect
from users import User
from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "Codingdojo2021!"

@app.route("/")
def redirect_to_users():
    return redirect("/users")

@app.route("/users")
def display_all():
    users = User.get_all_users()
    return render_template("index.html", users=users)

@app.route("/users/new")
def new_user():
    return render_template("form.html")

@app.route("/create_user", methods=["POST"])
def create_new_user():
    user_id = User.save(request.form)
    return redirect(f'/users/{user_id}')
            
@app.route("/users/<int:user_id>")
def user_card(user_id):
    data = {
        'id': user_id
    }
    user = User.get_user_by_id(data)
    return render_template("read_one.html", user = user)

@app.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    data = {
        'id': user_id
    }
    user = User.get_user_by_id(data)
    return render_template("edit_form.html", user = user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def update_user(user_id):
    data = {
        "id": user_id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    User.update(data)
    return redirect(f"/users/{user_id}")

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)