from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='../static')

top100name_df = pd.read_csv('../data/top100name.year.csv')
top50char_df = pd.read_csv('../data/top50char.year.csv')
top1000name_df = pd.read_csv('../data/top1000name.prov.csv')
familyname_df = pd.read_csv('../data/familyname.csv')
givenname_df = pd.read_csv('../data/givenname.csv')
population_df = pd.read_csv('../data/population.csv')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search_names():
    search_term = request.args.get('q', '').lower()
    results = []

    # Search through the name columns for matches
    name_columns = [col for col in top100name_df.columns if col.startswith('name')]
    for col in name_columns:
        matches = top100name_df[top100name_df[col].str.lower().str.contains(search_term, na=False)]
        if not matches.empty:
            for _, row in matches.iterrows():
                result = {
                    'Name': row[col],
                    'Year': col.split('.')[-1]
                }
                results.append(result)

    return jsonify(results)


@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(port=1234, debug=True)
