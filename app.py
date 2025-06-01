from flask import Flask, render_template, jsonify
from model import cluster_customers

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clusters')
def get_clusters():
    data = cluster_customers()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
