from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Smart Quiz Questions - AI Generated
QUIZ_DATA = [
    {"q": "What does AI stand for?", "options": ["Artificial Intelligence", "Auto Input", "Actual Interface", "Active Internet"], "ans": 0},
    {"q": "Which Python library is used for ML?", "options": ["NumPy", "Flask", "React", "Node"], "ans": 0},
    {"q": "What is Blockchain used for in certificates?", "options": ["Secure Verification", "Styling", "Database only", "No use"], "ans": 0},
    {"q": "Voice Quiz uses which API?", "options": ["Web Speech API", "Google Maps", "Payment API", "Camera API"], "ans": 0},
    {"q": "AI Proctoring detects?", "options": ["Face & Eye movement", "Only typing", "Only mouse", "Nothing"], "ans": 0}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-quiz')
def get_quiz():
    return jsonify(QUIZ_DATA)

@app.route('/submit-quiz', methods=['POST'])
def submit_quiz():
    data = request.json
    score = 0
    total = len(QUIZ_DATA)
    for i, q in enumerate(QUIZ_DATA):
        if str(data.get(str(i))) == str(q['ans']):
            score += 1

    percentage = (score/total)*100
    certificate_id = f"SMART-{random.randint(1000,9999)}-BLOCK-{random.randint(10000,99999)}"

    return jsonify({
        "score": score,
        "total": total,
        "percentage": percentage,
        "certificate_id": certificate_id,
        "message": "Blockchain Verified!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)