from flask import Flask, jsonify, render_template_string
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Home route
@app.route("/")
def home():
    app.logger.info("Home page accessed")
    return render_template_string("""
        <h1>🚀 Flask App Running in Docker</h1>
        <p>This app is containerized and ready for AWS ECS deployment.</p>
        <ul>
            <li><a href='/about'>About</a></li>
            <li><a href='/health'>Health Check</a></li>
            <li><a href='/api/data'>API Endpoint</a></li>
        </ul>
    """)

# About page
@app.route("/about")
def about():
    return "<h2>About: This is a sample Flask app running inside Docker for ECS deployment.</h2>"

# Health check route (good for ECS/Load Balancers)
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

# API route
@app.route("/api/data")
def api_data():
    data = {
        "project": "AWS ECS Deployment",
        "language": "Python",
        "framework": "Flask",
        "message": "This is sample JSON response"
    }
    return jsonify(data)

# Custom 404 handler
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Page not found"}), 404


if __name__ == "__main__":
    # Important: Bind to 0.0.0.0 so Docker can expose it
    app.run(host="0.0.0.0", port=5000)
