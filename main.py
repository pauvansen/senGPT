from flask import Flask, request, jsonify, render_template
from datetime import datetime
from SenGPT import SenGPTCache

app = Flask(__name__)
# ref: https://flask.palletsprojects.com/en/3.0.x/quickstart/

predictor = SenGPTCache()
predictor.setup_model()
predictor.setup_in_memory_cache()
predictor.setup_sqlite_cache()
predictor.setup_prompt_template("Your name ist SenGPT and you are a helpful assistant. Answer the following question only in German: {question}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    question = data.get('question')
    
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    result = predictor.predict(question)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({"answer": result, "timestamp": timestamp})

if __name__ == '__main__':
    app.run(debug=True)
