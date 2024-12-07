from flask import*
from pymongo import*
from bson.objectid import ObjectId

# __creating database__
clinet = MongoClient("mongodb://localhost:27017")
database = clinet["Crude"]
collection = database["UserInfo"]
# __________________________
ID=0
app=Flask("__name__")
@app.route("/",methods=["POST","GET"])
def home():
    
    return render_template("home.html")
@app.route("/register",methods=["POST","GET"])
def register():
    global ID
    ID+=1
    if request.method=="POST":
        name=request.form.get("Name")
        lastname=request.form.get("Lastname")
        phonenumber=request.form.get("Phonenumber")
        username=request.form.get("Username")
        password=request.form.get("password")
        a=[{
            "_id":ObjectId() ,
            "name": name,
            "lastname":lastname,
            "phonenumber":phonenumber,
            "username":username,
            "password":password
        }]
        if username=="" or password ==" ":
            flash('You shoud fill all fields!',category='error')

            return render_template("register.html")




        if collection.find_one({"username":username}):
            flash('This information are already exist!',category='error')
            return render_template("register.html")
        if 1<= len(username or password)<=6:
            flash('Your username or password must be more than 6 dicts!',category='error')
            return render_template("register.html")
        


        else:
            
            collection.insert_many(a)
            flash('You Signed up successfully!', 'success')
        return redirect(url_for('register'))
            
    return render_template("register.html")
@app.route("/login",methods=["POST","GET"])
def login():

    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if collection.find_one({"username":username,"password":password}):
            return render_template("main.html")
        if username and password=="admin":
            return redirect(url_for('admin'))
        else:
            flash('Your username or password is incorrect!',category='error')
        return redirect(url_for("login"))
    return render_template("login.html")
@app.route("/admin",methods=["POST","GET"])
def admin():
    if request.method=="POST":
        uspv=request.form.get("uspv")

        


    return render_template("admin.html")
    
    




if __name__=="__main__":
    app.secret_key = 'super secret key'
    app.run( debug=False,host='0.0.0.0')