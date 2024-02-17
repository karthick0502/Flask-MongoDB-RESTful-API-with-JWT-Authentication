# main.py - Entry point for the Flask application

# Importing the Flask application instance from the spiceblue package
from spiceblue import app

# Entry point of the application
if __name__ == '__main__':
    # Running the Flask application in debug mode
    app.run(debug=True)
