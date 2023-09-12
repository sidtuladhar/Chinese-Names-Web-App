from flask import Flask, request, jsonify, render_template
from functions import compute_name

app = Flask(__name__, template_folder='templates', static_folder='../static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search_names():
    name = request.args.get('name', '')
    year = request.args.get('year', '')
    print(name, year)

    result = compute_name(name, int(year))
    result_array = [result[6][0], result[7][0], result[8][0], result[9][0], result[10][0], result[11][0], result[12][0],
                    result[13][0], result[14][0]]

    return jsonify(result_array)


@app.route('/results', methods=['GET'])
def result():
    name = request.args.get('name', '')
    year = request.args.get('year', '')
    return render_template('results.html', name=name, year=year)


@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(port=1234, debug=True)
