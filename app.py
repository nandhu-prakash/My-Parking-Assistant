from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# store location (temporary)
parking_location = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_location():
    global parking_location
    data = request.json
    parking_location = {
        "lat": data['lat'],
        "lng": data['lng']
    }
    return jsonify({"message": "Location saved!"})

@app.route('/get', methods=['GET'])
def get_location():
    if parking_location:
        lat = parking_location['lat']
        lng = parking_location['lng']
        map_link = f"https://www.google.com/maps?q={lat},{lng}"
        return jsonify({"map": map_link})
    else:
        return jsonify({"error": "No location saved"})

if __name__ == '__main__':
    app.run(debug=True)