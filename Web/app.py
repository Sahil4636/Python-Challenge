# pyrefly: ignore [missing-import]
from flask import Flask
import os

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)