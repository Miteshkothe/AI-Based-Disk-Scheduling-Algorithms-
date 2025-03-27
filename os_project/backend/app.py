from flask import Flask, request, jsonify, render_template
from algorithms import fcfs, sstf, scan
# from ai_scheduler import ai_predict

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    data = request.get_json()
    requests = data['requests']
    head = data['head']
    algorithm = data['algorithm']

    if algorithm == "FCFS":
        result = fcfs(requests, head)
    elif algorithm == "SSTF":
        result = sstf(requests, head)
    elif algorithm == "SCAN":
        result = scan(requests, head)
    # elif algorithm == "AI":
    #     result = ai_predict(requests, head)
    else:
        return jsonify({"error": "Invalid algorithm"}), 400

    return jsonify({"schedule": result})

if __name__ == '__main__':
    app.run(debug=True)
