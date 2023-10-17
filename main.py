from flask import Flask, jsonify
import subprocess
from waitress import serve

app = Flask(__name__)


# Định nghĩa hàm getUser
def getUser():
    file_path = "firebase/firebase-storage.py"
    subprocess.Popen(["python", file_path], shell=True)


# Định nghĩa hàm trainingImg
def trainingImg():
    file_path = "trainingImg.py"
    subprocess.Popen(["python", file_path], shell=True)


# Enpoint to training
@app.route('/getdata', methods=['GET'])
def excute_getdata():
    try:
        getUser()
        return jsonify({"user_output": "get user ok"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Enpoint to training
@app.route('/training', methods=['GET'])
def excute_training():
    try:
        trainingImg()
        return jsonify({"message": "Training initiated."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
#1 nguoi 5s


# Enpoint to Face Recognition
@app.route('/recognition', methods=['GET'])
def execute_recognition():
    try:
        return jsonify({"user_output": "get user ok", "message": "Training initiated."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
