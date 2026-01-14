from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the "route" (the URL path)
@app.route('/')
def hello_world():
    # This looks inside the 'templates' folder for index.html
    return render_template('index.html')

if __name__ == '__main__':
    # Start the server in debug mode
    app.run(debug=True)