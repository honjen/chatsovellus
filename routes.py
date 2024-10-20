from app import app
from flask import render_template, request, redirect, abort
import messages, users, re

@app.route("/")
def index():
    admin = users.check_admin()
    list_users = users.get_users()
    list_categories = messages.get_categories()
    return render_template("index.html", categories=list_categories,
                                        count_categories=len(list_categories), 
                                        admin=admin, 
                                        users=list_users, 
                                        current_page="index")


@app.route("/new_category", methods=["GET", "POST"])
def new_category():
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    category_name = request.form["category_name"]
    if messages.check_categories(category_name):
        return render_template("error.html", message="saman niminen keskustelualue on jo olemassa")
    if not messages.check_category_title(category_name):
        return render_template("error.html", message="1-50 merkkiä pitkä nimi ei saa sisältää / merkkiä tai pelkkiä välilyöntejä")
    option = request.form["is_secret"]
    if option == "0":
        is_secret = False
    else:
        is_secret = True
    if messages.create_category(category_name, is_secret):
        return redirect("/")
    else:
        return render_template("error.html", message="keskustelualuetta ei voitu luoda")
    
@app.route("/edit_category", methods=["POST"])
def edit_category():
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    category_id = request.form["category_id"]
    category_name = request.form["category_name"]
    option = request.form["is_secret"]
    allowed_users = request.form.getlist("user_ids")
    allowed_users = [int(user_id) for user_id in allowed_users]
    if messages.check_categories_unique(category_name, category_id):
        return render_template("error.html", message="saman niminen keskustelualue on jo olemassa")
    if not messages.check_category_title(category_name):
        return render_template("error.html", message="1-50 merkkiä pitkä nimi ei saa sisältää / merkkiä")
    if option == "0":
        is_secret = False
    else:
        is_secret = True
    if messages.edit_category(category_id, category_name, is_secret, allowed_users):
        return redirect("/")
    return render_template("error.html", message="keskustelualueen päivitys epäonnistui")
    
@app.route("/delete_category", methods=["POST"])
def delete_category():
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    category_id = request.form["category_id"]
    if messages.delete_category(category_id):
        return redirect("/")
    else:
        return render_template("error.html", message="keskustelualueen poisto epäonnistui")

@app.route("/<category_name>")
def category_page(category_name):
    category = messages.check_categories(category_name)
    if category is None or not users.check_rights(category[1]):
        return redirect("/")
    if category[2] == True and not users.user_id():
        return redirect("/")
    list_threads = messages.get_threads(category[1])
    return render_template("category.html", category=category, 
                                            threads=list_threads,
                                            count_threads=len(list_threads),
                                            current_page="category")
                            
@app.route("/<category_name>/new_thread", methods=["POST"])
def new_thread(category_name):
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    category_name = request.form["category_name"]
    category_id = request.form["category_id"]
    thread_name = request.form["thread_name"]
    content = request.form["content"]
    if messages.check_thread_title(thread_name) and messages.check_message(content):
        thread_id = messages.create_thread(content, category_id, thread_name)
        if thread_id:    
            return redirect(f"/{category_name}/{thread_id}")
        else:
            return render_template("error.html", message="ketjun luonti epäonnistui")
    else:
        return render_template("error.html", message="otsikon pituus saa olla 1-100 merkkiä ja viestin pituus saa olla 1-20000 merkkiä")

@app.route("/<category_name>/edit_thread", methods=["POST"])
def edit_thread(category_name):
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    category_name = request.form["category_name"]
    thread_id = request.form["thread_id"]
    thread_name = request.form["thread_name"]
    content = request.form["content"]
    if messages.check_thread_title(thread_name) and messages.check_message(content):
        if messages.edit_thread(content, thread_name, thread_id):
            return redirect(f"/{category_name}")
        else:
            return render_template("error.html", message="ketjun muokkaus epäonnistui")
    else:
        return render_template("error.html", message="otsikon pituus saa olla 1-100 merkkiä ja viestin pituus saa olla 1-20000 merkkiä")
    
@app.route("/<category_name>/delete_thread", methods=["POST"])
def delete_thread(category_name):
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    thread_id = request.form["thread_id"]
    if messages.delete_thread(thread_id):
        return redirect(f"/{category_name}")
    else:
        return render_template("error.html", message="ketjun poisto epäonnistui")

@app.route("/<category_name>/<int:thread_id>")
def thread_page(category_name, thread_id):
    category = messages.check_categories(category_name)
    if category is None:
        return redirect("/")
    thread = messages.check_threads(thread_id, category[1])
    list_messages = messages.get_messages(thread_id)
    if thread is None or not users.check_rights(category[1]):
        return redirect("/")
    if category[2] == True and not users.user_id():
        return redirect("/")
    return render_template("thread.html", category=category,
                                        thread=thread,
                                        messages=list_messages,
                                        count_messages=len(list_messages),
                                        current_page="thread")

@app.route("/<category_name>/<int:thread_id>/send_message", methods=["POST"])
def send_message(category_name, thread_id):
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    category_id = request.form["category_id"]
    thread_id = request.form["thread_id"]
    content = request.form["content"]
    if messages.send_message(content, category_id, thread_id):
        return redirect(f"/{category_name}/{thread_id}")
    else:
        return render_template("error.html", message="viestin pituus saa olla 1-20000 merkkiä")
    
@app.route("/<category_name>/<int:thread_id>/edit_message", methods=["POST"])
def edit_message(category_name, thread_id):
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    thread_id = request.form["thread_id"]
    content = request.form["content"]
    message_id = request.form["message_id"]
    if messages.edit_message(content, message_id):
        return redirect(f"/{category_name}/{thread_id}")
    else:
        return render_template("error.html", message="viestin pituus saa olla 1-20000 merkkiä")
    
@app.route("/<category_name>/<int:thread_id>/delete_message", methods=["POST"])
def delete_message(category_name, thread_id):
    if users.csrf_token() != request.form["csrf_token"]:
        abort(403)
    message_id = request.form["message_id"]
    if messages.delete_message(message_id):
        return redirect(f"/{category_name}/{thread_id}")
    else:
        return render_template("error.html", message="viestin poisto epäonnistui")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", current_page="login")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="väärä käyttäjätunnus tai salasana")

@app.route("/logout")
def logout():
    if users.user_id():
        users.logout()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html", current_page="register")
    if request.method == "POST":
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if not re.match(r"^\S{1,32}$", username):
            return render_template("error.html", message="käyttäjätunnuksen pituus saa olla 1-32 merkkiä")
        if users.check_username(username):
            return render_template("error.html", message="käyttäjätunnus on jo olemassa")
        if not re.match(r"^\S{1,64}$", password1):
            return render_template("error.html", message="salasanan pituus saa olla 1-64 merkkiä")
        if password1 != password2:
            return render_template("error.html", message="salasanat ovat erilaiset")
        if users.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="kaikki kentät pitää täyttää oikein")
        
@app.route("/search")
def search():
    return render_template("search.html", current_page="search")

@app.route("/searchresults")
def searchresults():
    query = request.args["query"]
    options = request.args.getlist("search_options")
    categories_result = messages.search_categories(query)
    threads_result = messages.search_threads(query)
    messages_result = messages.search_messages(query)
    if messages.check_message(query) and options != []:
        return render_template("searchresults.html", query=query,
                                                    options=options,
                                                    categories_result=categories_result, 
                                                    threads_result=threads_result,
                                                    messages_result=messages_result, 
                                                    current_page="searchresults")
    return redirect("/search")