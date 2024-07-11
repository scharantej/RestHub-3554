
# Import the required modules
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Set up the home route
@app.route('/')
def home():
    return render_template('index.html')

# Set up the reserve route
@app.route('/reserve', methods=['POST'])
def reserve():
    # Get the form data
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    date = request.form.get('date')
    time = request.form.get('time')
    people = request.form.get('people')

    # Validate the form data
    if not all([name, email, phone, date, time, people]):
        return render_template('error.html', message='Please fill in all fields.')
    
    # Check availability
    available = True  # Placeholder for actual availability check

    # If available, store the reservation details
    if available:
        reservation = {
            'name': name,
            'email': email,
            'phone': phone,
            'date': date,
            'time': time,
            'people': people
        }
        # Placeholder for actual reservation storage

        # Redirect to confirmation page
        return render_template('confirmation.html', reservation=reservation)
    
    # If not available, display an error message
    else:
        return render_template('error.html', message='Sorry, that time slot is not available.')

# Set up the error route
@app.route('/error')
def error():
    return render_template('error.html')

# Set up the about route
@app.route('/about')
def about():
    return render_template('about.html')

# Set up the menu route
@app.route('/menu')
def menu():
    return render_template('menu.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
