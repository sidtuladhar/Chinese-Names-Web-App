from flask import Flask, request, jsonify, render_template
from functions import compute_name

app = Flask(__name__, template_folder='templates', static_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search_names():
    name = request.args.get('q', '').lower()

    result = compute_name(name, 1995)
    SNU = result[7][0]
    SNI = result[8][0]
    NU = result[9][0]
    CCU = result[10][0]
    NG = result[11][0]
    NV = result[12][0]
    NW = result[13][0]
    NC = result[14][0]

    return jsonify(f"SNU: {SNU}\nSNI: {SNI}\nNU: {NU}\nCCU: {CCU}\nNG: {NG}\nNV: {NV}\nNW: {NW}\nNC: {NC}")


@app.route('/results', methods=['GET'])
def result():
    name = request.args.get('results', '')
    return render_template('results.html', results=name)


@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(port=1234, debug=True)
