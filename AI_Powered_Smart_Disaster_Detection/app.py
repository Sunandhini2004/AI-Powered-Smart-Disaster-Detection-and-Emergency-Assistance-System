from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

HAZARD_RULES = {
    "Flood": ["flood", "flooding", "water rising", "overflow", "heavy rain"],
    "Fire": ["fire", "smoke", "burning", "flames"],
    "Earthquake": ["earthquake", "tremor", "shaking", "quake"],
    "Cyclone": ["cyclone", "hurricane", "storm", "strong winds"],
    "Landslide": ["landslide", "mudslide", "soil slipping"],
}
TIPS = {
    "Flood": ["Move to higher ground if it is safe.", "Stay away from floodwater and submerged roads.", "Follow local authorities' evacuation instructions."],
    "Fire": ["Leave the affected area using a safe exit.", "Do not use lifts in a burning building.", "Call local emergency services once you are safe."],
    "Earthquake": ["Drop, Cover, and Hold On while shaking continues.", "Keep away from windows and objects that may fall.", "When shaking stops, move carefully to a safe area if needed."],
    "Cyclone": ["Stay indoors in a sturdy building, away from windows.", "Keep your phone charged and monitor official alerts.", "Evacuate if local authorities instruct you to do so."],
    "Landslide": ["Move away from moving soil or debris if safe.", "Avoid slopes and river channels during heavy rain.", "Report the location to local emergency authorities."],
    "Unclassified": ["Move away from immediate danger if you can do so safely.", "Contact local emergency services for urgent threats.", "Follow verified instructions from local authorities."],
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/report', methods=['POST'])
def report():
    data = request.get_json(silent=True) or {}
    description = (data.get('description') or '').strip()
    location = (data.get('location') or '').strip()
    if len(description) < 5:
        return jsonify({'error': 'Please describe the situation using at least 5 characters.'}), 400
    lowered = description.lower()
    detected = [name for name, words in HAZARD_RULES.items() if any(word in lowered for word in words)]
    primary = detected[0] if detected else 'Unclassified'
    urgency = 'High' if primary in ('Flood', 'Fire', 'Earthquake', 'Landslide') else ('Moderate' if primary == 'Cyclone' else 'Needs review')
    return jsonify({
        'report_id': 'DEMO-' + datetime.now().strftime('%Y%m%d%H%M%S'),
        'location': location or 'Not provided', 'primary_hazard': primary,
        'detected_hazards': detected or ['No known hazard keyword detected'],
        'urgency': urgency, 'tips': TIPS[primary],
        'notice': 'Demo result only. This system does not contact emergency services or verify real-world conditions.'
    })

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'message': 'Disaster assistance demo backend is running.'})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
