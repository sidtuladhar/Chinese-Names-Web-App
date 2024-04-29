import pandas as pd
from flask import Flask, request, jsonify, render_template
from functions import compute_name

app = Flask(__name__, template_folder='templates', static_folder='../static')

given_name_df = pd.read_csv('../data/givenname.csv')
family_name_df = pd.read_csv('../data/familyname.csv')


def family_name(name):
    family_names = family_name_df['surname'].tolist()
    if name[:2] in family_names:
        return name[:2]
    elif name[0] in family_names:
        return name[0]


def NFT(name):
    length = len(name)
    if length <= 1:
        return 0, 0

    nFemale = 581570041  # from population.csv
    totalNFT = 0
    totalNFC = 0

    surname = family_name(name)

    for character in list(name)[len(surname):]:
        try:
            NFC = given_name_df[given_name_df['character'] == character]['n.female'].iloc[0]
        except IndexError:
            continue

        totalNFC += NFC
        totalNFT += NFC / nFemale
    return [float(format(totalNFT / (length - 1) * 1000, '.5f')), totalNFC / (length - 1)]


def NMT(name):
    length = len(name)
    if length <= 1:
        return 0, 0

    nMale = 600353517  # from population.csv
    totalNMT = 0
    totalNMC = 0
    missing_char = 0

    surname = family_name(name)

    for character in list(name)[len(surname):]:
        print(character)
        try:
            NMC = given_name_df[given_name_df['character'] == character]['n.male'].iloc[0]
        except IndexError:
            missing_char += 1
            continue
        totalNMC += NMC
        totalNMT += NMC / nMale
    return [float(format(totalNMT / (length - 1) * 1000, '.5f')), totalNMC / (length - 1), missing_char]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search_names():
    name = request.args.get('name', '')
    year = request.args.get('year', '')
    print(name, year)

    result = compute_name(name, int(year))
    additional_variables = NFT(name) + NMT(name)
    print(additional_variables)

    result_array = [result[6][0], result[7][0], result[8][0], result[9][0], result[10][0], result[11][0], result[12][0],
                    result[13][0], result[14][0], additional_variables[1],
                    additional_variables[3], additional_variables[0], additional_variables[2], additional_variables[4]]

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
    app.run(debug=True)
