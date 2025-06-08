from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_data = None
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        user_data = {'name': name, 'message': message}
    return render_template('index.html', user_data=user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
