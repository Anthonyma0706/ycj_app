from flask import Flask, request, render_template, session, redirect, url_for
import pandas as pd
from os import listdir
from os.path import isfile, join
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def choose_file():
    if request.method == 'POST':
        session['filename'] = request.form.get('file')
        return redirect(url_for('choose_sheet'))
    files = os.listdir('uploads')
    return render_template('choose_file.html', files=files)


@app.route('/choose_sheet', methods=['GET', 'POST'])
def choose_sheet():
    if request.method == 'POST':
        session['sheet_name'] = request.form.get('sheet_name')
        return redirect(url_for('actions'))
    df = pd.read_excel(os.path.join("uploads", session['filename']), sheet_name=None)
    sheets = df.keys()
    return render_template('choose_sheet.html', sheets=sheets)

@app.route('/actions', methods=['GET'])
def actions():
    return render_template('actions.html')


def calc_remain(df, factory, product):
    df_product = df[(df['厂家名称'] == factory) & (df['商品名称'] == product)]
    remain = df_product['入库'].sum() - df_product['出库'].sum()

    return remain

@app.route('/query_remain', methods=['GET', 'POST'])
def query_remain():
    if request.method == 'POST':
        factory = request.form.get('factory')
        product = request.form.get('product')
        df = pd.read_excel(os.path.join("uploads", session['filename']), sheet_name=session['sheet_name'])
        remain = calc_remain(df, factory, product)
        return render_template('query_remain.html', remain=remain)
    else:
        return render_template('query_remain.html')


@app.route('/input_data', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        data = dict(request.form)
        data['日期'] = pd.to_datetime(data['日期']).strftime('%Y%m%d')
        filename = session['filename']
        df = pd.read_excel(os.path.join("uploads", filename), sheet_name="库存")
        df = df.append(data, ignore_index=True)
        df.to_excel(os.path.join("uploads", filename), sheet_name="库存", index=False)

        session['factory'] = data['厂家名称']
        session['product'] = data['商品名称']

        return redirect(url_for('update_stock'))

    return render_template('input_data.html')

@app.route('/update_stock', methods=['GET'])
def update_stock():
    df = pd.read_excel(os.path.join("uploads", session['filename']), sheet_name="库存")
    factory = session['factory']
    product = session['product']
    remain = calc_remain(df, factory, product)
    return render_template('update_stock.html', remain=remain)


if __name__ == '__main__':
    app.run(debug=True)
