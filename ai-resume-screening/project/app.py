from flask import Flask
from routes import initialize_routes

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'

# Initialize routes
initialize_routes(app)

if __name__ == '__main__':
    import os
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
