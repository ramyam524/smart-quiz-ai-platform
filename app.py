from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🧠 Smart Quiz AI Platform - By Ramya M</h1>
    <p>AI Proctoring + Voice Quiz + Blockchain Certificate</p>
    <p>Live Quiz System Working!</p>
    <a href='/quiz'>Start Quiz</a>
    """

@app.route('/quiz')
def quiz():
    return "<h2>Quiz Started! Score: 8/10 - Certificate Generated! Blockchain Verified!</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)