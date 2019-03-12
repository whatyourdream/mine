from flask import request, render_template
from app import app
from app.module import AppModule
import pandas as pd


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        AppModule.saveDataset(request.files['file'])
        doneMessage = '<div class="alert alert-success"><strong>Success!</strong> Datasets is updated.</div>'
        return render_template('index.html', done=doneMessage)
    else:
        return render_template("index.html")

@app.route('/api/get-result', methods=['POST'])
def getResult():
    q = None if request.json['query'] is "" else request.json['query']
    dataset = AppModule.loadDataset()
    datapreprocess = AppModule.loadDataPreprocessing()
    scores = AppModule.search(q, datapreprocess)
    df = pd.DataFrame(dataset['Bahan'])
    df['Score'] = scores
    df['Information'] = AppModule.RelevantChecker(df['Score'])
    result = df.sort_values(by=['Score'], ascending=[False])
    return result.to_json(orient='split', index=False)