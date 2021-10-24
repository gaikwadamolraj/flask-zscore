from flask import Flask, request, jsonify



from . import config


app = Flask(__name__)
app.app_context().push()
db.init_app(app)

is_db=False

# calculate zscore for particular years data
def calculateZscore(data):
    ebit = data['ebit']
    equity = data['equity']
    retained_earnings = data['retained_earnings']
    sales = data['sales']
    total_assets = data['total_assets']
    total_liabilities = data['total_liabilities']
    year = data['year']

    # working capital calculated 
    working_capital = total_assets / total_liabilities
    X1 = working_capital / total_assets
    X2 = retained_earnings / total_assets
    X3 = ebit / total_assets
    X4 = equity / total_liabilities
    X5 = sales / total_assets

    return { "year": year, "zscore": (1.2*X1 + 1.4*X2 + 3.3*X3 + 0.6*X4 + 1.0*X5)}  

# save score to db
def saveZscore(isoCode, companyId, score):
    return database.add_instance(Score, isoCode=isoCode, companyId=companyId, score=score)

@app.route('/',  methods=['GET'])
def hello():
    return jsonify({"message": "hello"}), 200

@app.route('/api/v1/company/<string:isoCode>/<int:id>', methods=['PUT'])
def zScore(isoCode, id):
    data = request.get_json(force=True)
    zscores = []
    for d in data['financials'] :
        zscore = calculateZscore(d)
        zscores.append(zscore)

    if is_db == "True":
        print('i am inside')
        # save score to db and return the report id
        reportId = saveZscore(isoCode, id, zscores)
        return jsonify({"scores": zscores, "reportId" : reportId})
    else:
        print('i am inside else', config.is_db)
        return jsonify({"scores": zscores})

@app.route('/api/v1/company/<string:isoCode>/<int:id>/<int:reportId>', methods=['GET'])
def getLastReportById(isoCode, id, reportId):
    if is_db == "True":
        reports = database.get_by_args(Score, id=reportId)
        zScoreReport = []
        for report in reports:
            if(id == report.companyId and isoCode == report.isoCode):
                zReport =  {
                        "id": report.id,
                        "isoCode": report.isoCode,
                        "companyId": report.companyId,
                        "score": report.score
                    }
                zScoreReport.append(zReport)
        return jsonify(zScoreReport), 200
    else:
        return jsonify({"message": "Not connected with db, so no prev report"})
