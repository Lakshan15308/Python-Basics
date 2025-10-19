from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask from VS Code!'

@app.route('/about')
def about():
    return 'This is the About page.'

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
