from app import app
from flask import render_template, request, redirect, url_for
import messages, users

@app.route("/")
def index():
    admin = users.check_admin()
    list_categories = messages.get_categories()
    return render_template("index.html", categories=list_categories,
                           count_categories=len(list_categories), admin=admin, current_page='index')

@app.route("/new_category", methods=["POST"])
def new_category():
    category_name = request.form["category_name"]
    if messages.check_categories(category_name):
        return render_template("error.html", message="nimi ei saa olla sama")
    is_secret = request.form["is_secret"]
    if is_secret == "1":
        is_secret == True
    else:
        is_secret == False
    if messages.create_category(category_name, is_secret):
        return redirect("/")
    else:
        return render_template("error.html", message="alueen luonti ei onnistunut")

@app.route("/delete_category", methods=["POST"])
def delete_category():
    category_id = request.form["category_id"]
    if messages.delete_category(category_id):
        return redirect("/")
    else:
        return render_template("error.html", message="alueen poisto ei onnistunut")

@app.route("/<category_name>")
def category_page(category_name):
    category = messages.check_categories(category_name)
    if category is None or not users.check_rights(category[1]):
        return redirect("/")
    list_threads = messages.get_threads(category[1])
    return render_template("category.html", 
                           category=category, 
                           threads=list_threads,
                           count_threads=len(list_threads), 
                           current_page='category')

@app.route("/<category_name>/new_thread", methods=["POST"])
def new_thread(category_name):
    category_name = request.form["category_name"]
    category_id = request.form["category_id"]
    thread_name = request.form["thread_name"]
    content = request.form["content"]
    thread_id = messages.create_thread(category_id, thread_name)
    if messages.send_message(content, category_id, thread_id):
        return redirect(f"/{category_name}/{thread_id}")
    else:
        return render_template("error.html", message="ketjun luonti ei onnistunut")

@app.route("/<category_name>/edit_thread", methods=["POST"])
def edit_thread(category_name):
    category_name = request.form["category_name"]
    thread_id = request.form["thread_id"]
    thread_name = request.form["thread_name"]
    if messages.edit_thread(thread_name, thread_id):
        return redirect(f"/{category_name}")
    else:
        return render_template("error.html", message="ketjun luonti ei onnistunut")
    
@app.route("/<category_name>/delete_thread", methods=["POST"])
def delete_thread(category_name):
    thread_id = request.form["thread_id"]
    if messages.delete_thread(thread_id):
        return redirect(f"/{category_name}")
    else:
        return render_template("error.html", message="ketjun poisto ei onnistunut")

@app.route("/<category_name>/<int:thread_id>")
def thread_page(category_name, thread_id):
    category = messages.check_categories(category_name)
    thread = messages.check_threads(thread_id, category[1])
    list_messages = messages.get_messages(thread_id)
    if category is None or thread is None:
        return redirect("/")
    return render_template("thread.html", 
                           category=category, 
                           thread=thread, 
                           messages=list_messages,
                           count_messages=len(list_messages), 
                           current_page='thread')

@app.route("/<category_name>/<int:thread_id>/send_message", methods=["POST"])
def send_message(category_name, thread_id):
    category_id = request.form["category_id"]
    thread_id = request.form["thread_id"]
    content = request.form["content"]
    if messages.send_message(content, category_id, thread_id):
        return redirect(f"/{category_name}/{thread_id}")
    else:
        return render_template("error.html", 
                               message="viestin lähetys ei onnistunut", 
                               current_page='error')

@app.route("/<category_name>/<int:thread_id>/edit_message", methods=["POST"])
def edit_message(category_name, thread_id):
    thread_id = request.form["thread_id"]
    content = request.form["content"]
    message_id = request.form["message_id"]
    if messages.edit_message(content, message_id):
        return redirect(f"/{category_name}/{thread_id}")
    else:
        return render_template("error.html", message="viestin lähetys ei onnistunut", current_page='error')
    
@app.route("/<category_name>/<int:thread_id>/delete_message", methods=["POST"])
def delete_message(category_name, thread_id):
    message_id = request.form["message_id"]
    if messages.delete_message(message_id):
        return redirect(f"/{category_name}/{thread_id}")
    else:
        return render_template("error.html", message="viestin poisto ei onnistunut", current_page='error')

@app.route("/login", methods=["GET", "POST"])
def login():
    redirect_url = request.args.get('redirect', url_for('index'))
    if request.method == "GET":
        return render_template("login.html", 
                               redirect_url=redirect_url, 
                               current_page='login')
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        redirect_url = request.form.get('redirect_url', url_for('index'))
        if users.login(username, password):
            return redirect(redirect_url)
        else:
            return render_template("error.html", 
                                   message="väärä tunnus tai salasana", 
                                   current_page='error')

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    redirect_url = request.args.get('redirect', url_for('index'))
    if request.method == "GET":
        return render_template("register.html", 
                               redirect_url=redirect_url, 
                               current_page='register')
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        redirect_url = request.form.get('redirect_url', url_for('index'))
        if len(username) < 1 or " " in username:
            return redirect("/register")
        if len(password1) < 1 or " " in password1:
            return redirect("/register")
        if password1 != password2:
            return render_template("error.html", 
                                   message="salasanat eroavat", 
                                   current_page='error')
        if users.register(username, password1):
            return redirect(redirect_url)
        else:
            return render_template("error.html", 
                                   message="rekisteröinti ei onnistunut", 
                                   current_page='error')