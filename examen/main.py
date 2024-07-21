from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/exercise1', methods=['GET', 'POST'])
def exercise1():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        cans = int(request.form['cans'])
        price_per_can = 9000
        total = price_per_can * cans
        discount = 0

        if 18 <= age <= 30:
            discount = 0.15
        elif age > 30:
            discount = 0.25

        total_with_discount = total * (1 - discount)
        return render_template('exercise1.html', name=name, total=total, total_with_discount=total_with_discount)

    return render_template('exercise1.html')

@app.route('/exercise2', methods=['GET', 'POST'])
def exercise2():
    users = {'juan': 'admin', 'pepe': 'user'}
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            if username == 'juan':
                message = 'Bienvenido administrador juan'
            else:
                message = 'Bienvenido usuario pepe'
        else:
            message = 'Usuario o contraseña incorrectos'
    return render_template('exercise2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
