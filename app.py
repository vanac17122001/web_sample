from flask import Flask, render_template

# call the Flask constructor
#application object

app= Flask(__name__)

#view function

@app.route('/')
@app.route('/index')

def index() :
	return render_template('index.html')

@app.route('/add')
def add():
	return render_template('add.html')

if __name__ == '__main__':
	
	app.run(debug=True)
