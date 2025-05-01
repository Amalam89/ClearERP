from flask import Flask, render_template, request, redirect, send_from_directory
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Send to Formspree (replace the URL with your own below)
    requests.post('https://formspree.io/f/mpwdzrqg', data={
        'name': name,
        'email': email,
        'message': message
    })

    return redirect('/')  # Send them back to homepage (or a thank-you page)

@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/terms', methods=['GET'])
def terms():
    return render_template('terms.html')

@app.route('/favicon.png')
def favicon():
    return send_from_directory('static', 'favicon.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)

