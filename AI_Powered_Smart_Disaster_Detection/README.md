# AI-Powered Smart Disaster Detection and Emergency Assistance System

A student-friendly full-stack prototype using HTML, CSS, JavaScript, and Python Flask.

## Features
- Responsive dashboard and disaster report form
- Demo keyword matching for flood, fire, earthquake, cyclone, and landslide
- General safety tips, report ID, and priority label
- Backend health endpoint at `/api/health`

## Important
This is an academic demonstration, not a validated AI model or a real emergency service. It does not contact emergency responders, access live sensors, or verify actual conditions. Keyword matching can be wrong. In India, call 112 for emergency assistance when appropriate and follow official local alerts.

## Run in VS Code on Windows
1. Extract the ZIP.
2. Open VS Code → **File → Open Folder** → choose `AI_Powered_Smart_Disaster_Detection`.
3. Open **Terminal → New Terminal** and run one command at a time:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py app.py
```

If PowerShell blocks activation, skip the activation command and run:

```powershell
py -m pip install -r requirements.txt
py app.py
```

4. Keep the terminal open and visit `http://127.0.0.1:5000` in your browser.
5. To test the backend, visit `http://127.0.0.1:5000/api/health`.

## macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 app.py
```
Then open `http://127.0.0.1:5000`.

## Example test reports
- Heavy rain has caused flooding and water is rising near houses.
- There is smoke and fire in a building.
- People felt earthquake shaking in the area.
- A cyclone with strong winds is approaching.

## Structure
```text
AI_Powered_Smart_Disaster_Detection/
├── app.py
├── requirements.txt
├── README.md
├── templates/index.html
└── static/
    ├── css/style.css
    └── js/script.js
```
