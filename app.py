from flask import Flask, render_template, redirect, request, session, url_for
from db import add_pj, add_user, get_all_logins, get_all_passwords, get_all_users, get_pj_by_id, get_all_title, get_all_pjs, delete_pj_by_id

app = Flask(__name__, template_folder='', static_folder='')

#Page_managed
@app.route('/')
def main():
    session['id'] = 1
    session['id'] += 1
    session['title_a'] = 'Login'
    titles = get_all_title()
    try:
        if session['title_antificate'] == True:
            session['title_a'] = 'Login'
        else:
            session['title_a'] = 'Profile'
    except:
        session['title_a'] = 'Login'
    return render_template('/html/main.html', titles=titles, title_a=session['title_a'])

@app.route("/login", methods={"GET", "POST"})
def sing_in():

    if request.method == 'POST':

        login = request.form.get('login')
        password = request.form.get('password')

        data = get_all_users()

        for i in data:
            if login == i[0] and password == i[1]:
                user_name = login
                session['logged_in'] = True
                session['login_out'] = False
                session['title_antificate'] = False
                return redirect(url_for('profile', name=user_name))

            else:
                mgs = "Login or password is incorrect"
                return redirect(url_for('sing_in', mg=mgs))
    else:
        return render_template('/html/login.html')

@app.route("/reg", methods={"GET", "POST"})
def sing_up():
    if request.method == "POST":
        login = request.form.get('login')
        password = request.form.get('password')        
        data1 = get_all_logins()
        for i in data1:
            if login != i[0]:
                add_user(login, password)
                return redirect(url_for("sing_in"))

            else: 
                mg = "This login is used"
                return render_template("/html/reg.html", mg)
        
    elif session['id'] != 0 and request.method == "GET":

        return render_template('html/reg.html')

@app.route("/profile", methods={"GET", "POST"})
def profile():
    pj = get_all_pjs()

    if session['logged_in'] == True and request.method == "POST":
        title = request.form.get("title")
        about = request.form.get("about")
        img = request.form.get("img")
        user_id = request.form.get("user_id")
        add_pj(title=title, about=about, image= img, user_id= user_id)
        return redirect(url_for("profile"))

    elif session['logged_in'] == True and request.method == "GET":
        return render_template('/html/profile.html', pjs=pj)
    
    elif session['log_out'] == True:
        return redirect('home')

@app.route('/<id>')
def pj(id):
    pj = get_pj_by_id(id)
    if pj:
        return render_template('/html/pj.html', showed_pj=pj, images=pj[0][2].split(','))
    
    return redirect('/')

@app.route('/dell', methods=["POST"])
def dell():
    id = request.form.get('id')
    delete_pj_by_id(id)
    return redirect(url_for('profile'))

@app.route('/log_out', methods=["POST"])
def log_out():
    session['logged_in'] = False
    session['log_out'] = True
    session['title_antificate'] == True
    return redirect(url_for('main'))

#run sity
app.secret_key = "I never lose"

app.run(debug=True)