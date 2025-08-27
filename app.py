# app.py

import asyncio
import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
from pymongo import MongoClient
from bson.objectid import ObjectId

# Assuming bugfiner_runner.py is in the same directory
# We'll need to modify bugfiner_runner.py to accept the db client and return the report_id
from bugfiner_runner import parse_args, main as bugfiner_main, REPORT_DIR, OUTPUT_DIR

app = Flask(__name__)

# --- MongoDB Configuration ---
# You can change 'mongodb://localhost:27017/' to your MongoDB connection string
# For production, use environment variables for security (e.g., os.environ.get("MONGO_URI"))
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.bugfiner_db # Your database name

# Ensure report directory exists (for local files like videos/screenshots)
os.makedirs(REPORT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def run_bugfiner_task(args_list, mongo_db) -> str:
    """
    Parses arguments, runs the bugfiner_runner's main function,
    and returns the MongoDB ObjectId of the saved report.
    This function will be called by the Flask app.
    """
    parser = parse_args()
    args = parser.parse_args(args_list)
    
    # We will modify bugfiner_main to accept the mongo_db object and return the report_id
    report_id = await bugfiner_main(args, mongo_db) 
    return str(report_id) # Convert ObjectId to string for URL

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles the main form for submitting bug reports.
    After submission, it triggers the bug analysis and redirects to the report view.
    """
    if request.method == "POST":
        bug_desc = request.form.get("bug_desc")
        test_url = request.form.get("test_url")
        test_name = request.form.get("test_name")
        gemini_key = request.form.get("gemini_key") # Still passed via form for now, but env is better
        headful = request.form.get("headful") == "on"
        record_video = request.form.get("record_video") != "off"
        
        args = [
            "--url", test_url,
            "--test-name", test_name,
            "--bug", bug_desc,
        ]
        if headful:
            args.append("--headful")
        if not record_video:
            args.append("--no-video")
        if gemini_key:
            args += ["--gemini-key", gemini_key]
        
        # Run the bugfiner script as a task and get the MongoDB report ID
        # Note: In a real production app, this would be offloaded to a background task queue (e.g., Celery)
        report_mongo_id = asyncio.run(run_bugfiner_task(args, db))

        # Redirect to the detailed report page
        return redirect(url_for("view_report", report_id=report_mongo_id))

    # For GET requests, render the initial bug submission form
    return render_template("index.html")

@app.route("/report/<report_id>")
def view_report(report_id):
    """
    Displays a detailed bug report fetched from MongoDB.
    """
    try:
        # Fetch the report from MongoDB using the provided ID
        report_data = db.reports.find_one({"_id": ObjectId(report_id)})
        
        if not report_data:
            abort(404, description="Report not found")

        # Convert ObjectId to string for JSON serialization in template
        report_data['_id'] = str(report_data['_id'])
        
        # Determine if a bug was found for conditional rendering
        bug_found = report_data.get("llm_bug_check", "").lower().startswith("bug found")

        return render_template("report.html", report=report_data, bug_found=bug_found)
    except Exception as e:
        print(f"Error fetching report: {e}")
        abort(500, description="Internal server error fetching report")

@app.route("/media/<path:filename>")
def serve_media(filename):
    """
    Serves static media files (screenshots, videos) from the OUTPUT_DIR.
    """
    return send_from_directory(OUTPUT_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)