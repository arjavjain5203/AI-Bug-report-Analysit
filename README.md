</head>
<body>
<div class="container">
    <h1>🛠 BugFiner AI</h1>
    <section>
        <h2>🚀 Features</h2>
        <ul>
            <li>Automated Bug Reproduction: Converts vague bug reports into actionable test steps.</li>
            <li>Headless or Headful Execution: Run browser tests with or without UI.</li>
            <li>Live Logs Streaming: View test execution in real-time.</li>
            <li>Video Recording: Optional recording of the browser session for debugging.</li>
            <li>Markdown Reports: Generates structured, human-readable bug reports.</li>
            <li>Dashboard: Manage and view all tests, logs, and reports in a modern, dark-themed interface.</li>
            <li>AI-Powered Analysis: Uses GPT-style AI to interpret vague bug descriptions into reproducible steps.</li>
        </ul>
    </section>
    <section>
        <h2>🎯 Workflow</h2>
        <ul>
            <li>User Submits Bug Report → BugFiner AI Analyzes Description</li>
            <li>Bug Repro Steps Identified?
                <ul>
                    <li>Yes → Automated Browser Test</li>
                    <li>No → Request More Info</li>
                </ul>
            </li>
            <li>Capture Logs & Screenshots → Generate Markdown Report → Dashboard Displays Report → Developer Reviews & Fixes Bug</li>
        </ul>
    </section>
    <section>
        <h2>⚙️ Installation</h2>
        <pre>
git clone https://github.com/AbheyTiwari/BugFiner.git
cd BugFiner

python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

pip install -r requirements.txt

python app.py
        </pre>
    </section>
    <section>
        <h2>🧩 Usage</h2>
        <ul>
            <li>Enter bug description, test URL, and test name.</li>
            <li>Optionally add Gemini API key for AI analysis.</li>
            <li>Choose whether to run with UI and/or record video.</li>
            <li>Click <strong>Run Test</strong> and watch live logs.</li>
            <li>Access detailed Markdown reports in the dashboard.</li>
        </ul>
    </section>
    <section>
        <h2>📂 File Structure</h2>
        <pre>
BugFiner/
│
├─ app.py
├─ bugfiner_runner.py
├─ static/
│   ├─ style.css
│   └─ script.js
├─ templates/
│   ├─ index.html
│   └─ report.html
├─ bug_reports/
└─ requirements.txt
        </pre>
    </section>
    <section>
        <h2>💡 Future Enhancements</h2>
        <ul>
            <li>Multi-tab/browser testing for complex workflows</li>
            <li>CI/CD integration for automated regression testing</li>
            <li>Plugin system to add custom AI models</li>
            <li>Dashboard analytics for bug trends</li>
        </ul>
    </section>
    <section>
        <h2>📈 Tech Stack</h2>
        <ul>
            <li>Backend: Python, Flask, asyncio</li>
            <li>AI: GPT-style models (Gemini, OpenAI API)</li>
            <li>Frontend: HTML5, CSS3, JS, modern dark UI</li>
            <li>Browser Automation: Playwright / Selenium</li>
            <li>Reporting: Markdown + live logs</li>
        </ul>
    </section>
    <section>
        <h2>🔗 Links</h2>
        <a href="https://github.com/AbheyTiwari/BugFiner" class="btn" target="_blank">GitHub Repository</a>
        <a href="https://github.com/AbheyTiwari/BugFiner/issues" class="btn" target="_blank">Issue Tracker</a>
    </section>
    <section>
        <h2>⚖️ License</h2>
        <p>MIT License © 2025 <a href="https://github.com/AbheyTiwari" target="_blank">Abhey Tiwari</a></p>
    </section>
</div>
</body>
</html>
