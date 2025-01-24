from flask import Flask, request, redirect, url_for, render_template, session
import mysql.connector
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for session management

# Database configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'mysql',
    'database': 'mydatabase'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get data from the form
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        city = request.form['city']
        data = request.form['data']

        # Insert data into MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, age, email, city, data)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, age, email, city, data))
        conn.commit()
        cursor.close()
        conn.close()

        # After submitting data, redirect to the game page
        return redirect(url_for('game'))

    # Fetch data from MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT name, age, email, city, data FROM users")
    data_list = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('index.html', data_list=data_list)

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'correct_number' not in session:
        # Generate a new random number if not already set
        session['correct_number'] = random.randint(1, 100)
    correct_number = session['correct_number']

    if request.method == 'POST':
        # Simple number guessing game
        user_guess = int(request.form['guess'])

        if user_guess == correct_number:
            message = "You won! The correct number was " + str(correct_number)
            session['correct_number'] = random.randint(1, 100)  # Reset the correct number
            return render_template('game.html', message=message, reload=False)
        elif abs(user_guess - correct_number) <= 5:
            message = "Too close!"
        elif user_guess < correct_number:
            message = "Too low!"
        else:
            message = "Too high!"

        return render_template('game.html', message=message, reload=False)

    return render_template('game.html', message="Guess a number between 1 and 100!", reload=False)

@app.route('/reveal', methods=['GET'])
def reveal():
    correct_number = session.get('correct_number', 'Not set')
    return render_template('reveal.html', correct_number=correct_number)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

