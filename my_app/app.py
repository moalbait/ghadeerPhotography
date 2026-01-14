from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the "route" (the URL path)
@app.route('/')
def hello_world():
    # This looks inside the 'templates' folder for index.html
    return render_template('index.html')

# 'About Me ' Page
@app.route('/About Me')
def about_me():
    return "<h1>About Me Page</h1> Information about me will go here.</h1>"
# 'Gallery' Page
@app.route('/Gallery')
def gallery():
    return "<h1>Gallery Page</h1> A collection of my photographs will go here.</h1>"
@app.route('/Inquire')
def Inquire():
    return "<h1>Contact Page</h1> Information on how to reach me will go here.</h1>"
if __name__ == '__main__':
    # Start the server in debug mode
    app.run(debug=True)