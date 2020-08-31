from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from pymongo import MongoClient


app = Flask(__name__)


con=MongoClient("mongodb://localhost:27017/myDB")
db=con['myDB']
c_details=db['contactDetails']

@app.route('/delete')
def Delete():
	key=request.values.get("_id")
	c_details.delete({"_id":(key)})

@app.route('/showdata')
def Data():
	datas= c_details.find({}, {'_id': False})
	return render_template('data.html',datas=datas)


@app.route('/submit' , methods=["post"])
def Submit():
	if request.method == 'POST':
		message=request.form['message']
		name=request.form['name']
		email=request.form['email']
		subject=request.form['subject']

		c_details.insert_one({'message': message, 'name': name,'email':email,'subject':subject})
		msg="Data has been submitted!!"
	return render_template('contact.html',mes=msg)

	"""return render_template("contact.html")"""
@app.route('/')
def Home():
	return render_template('index.html')

@app.route('/tutorials')
def Tutorials():
	return render_template('tutorials.html')

@app.route('/coursedetails')
def courseDetails():
	return render_template('course_details.html')

@app.route('/elements')
def Elements():
	return render_template('elements.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/blog')
def Blog():
	return render_template('blog.html')

@app.route('/singleblog')
def single_blog():
	return render_template('single-blog.html')

@app.route('/contacts')
def contacts():
	return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
