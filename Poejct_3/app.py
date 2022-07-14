from flask import Flask, Response, render_template, request, flash, redirect, url_for, session
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '934a551289bf4b931d327983e7703e879fbd6e2d2251753a'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

import rds_db as db


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search/', methods=['GET'])
def search():
    title_list = []
    if request.method == 'GET':
        search_item = request.args['search']
        if not search_item:
            flash('compound name is required!')
            return render_template('index.html')
        else:
            details = db.get_details(search_item)
            record_num = len(details)

            for _ in range(record_num):
                title_list.append(details[_][1])

            return render_template('index.html', record=f'In Total {record_num} Records', title=title_list)


@app.route('/protocol_details/', methods=['GET'])
def protocol_details():
    content = request.args.get('type')
    one_record = db.get_one_record(content)
    compounds = one_record[0]['ANALYTE']
    compounds = list(set([x.strip() for x in compounds.split(',')]))  #remove duplicates
    compounds = list(filter(None, compounds))  #remove empty string
    url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/" + compounds[0] + "/PNG"
    return render_template('detail.html', one_record=one_record, url=url, compounds=compounds)


if __name__ == "__main__":
    app.run(debug=True)
