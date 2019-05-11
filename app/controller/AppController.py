from flask import request, render_template, jsonify
from app import app
from app.module import AppModule
import pandas as pd
pd.set_option('display.max_colwidth', -1)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            message = """
                <div class="alert alert-danger alert-dismissible fade show mb-0" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                  <span aria-hidden="true">×</span>
                </button>
                <i class="fa fa-info mx-2"></i>
                <strong>Failed!</strong> Should upload file first.</div>
            """
        else:
            message = """
                <div class="alert alert-success alert-dismissible fade show mb-0" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                  <span aria-hidden="true">×</span>
                </button>
                <i class="fa fa-info mx-2"></i>
                <strong>Success</strong> Datasets is updated.</div>
            """
            AppModule.saveDataset(request.files['file'])
        return render_template('upload.html', message=message)
    else:
        return render_template("upload.html")


@app.route('/search', methods=['GET'])
def getResult():
    if 'q' in request.args:
        if request.args['q'] != "":
            q = request.args['q']
            dataset = AppModule.loadDataset()
            datapreprocess = AppModule.loadDataPreprocessing()
            scores = AppModule.search(q, datapreprocess)
            df = pd.DataFrame()
            df['Nama Resep'] = dataset['Nama']
            df['Bahan'] = dataset['Bahan']
            df['Resep'] = dataset['Resep']
            df['Usia'] = dataset['Usia']
            df['Score'] = scores

            result = df.sort_values(by=['Score'], ascending=[False]).head(10)
            print()
            if result.iloc[0,4] == 0.0:
                message = """
                <div class="alert alert-danger alert-dismissible fade show mb-0" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                  <span aria-hidden="true">×</span>
                </button>
                <i class="fa fa-info mx-2"></i>
                <strong>Failed!</strong> Text not found.</div>
                """
                return render_template('search.html', message=message)
            else:

                return render_template('result.html', tables=[
                result.to_html(classes="table mb-0 border-0 table-responsive", justify='unset', index=False).replace(
                    'border="1"', "")])
        else:
            message = """
                <div class="alert alert-danger alert-dismissible fade show mb-0" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                  <span aria-hidden="true">×</span>
                </button>
                <i class="fa fa-info mx-2"></i>
                <strong>Failed!</strong> Should contain text.</div>
            """
            return render_template('search.html', message=message)
    else:
        return render_template('search.html')
