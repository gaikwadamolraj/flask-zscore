from flask import Flask, request, jsonify

app = Flask(__name__)


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

    return jsonify({"scores": zscores})

@app.route('/api/v1/company/<string:isoCode>/<int:id>/<int:reportId>', methods=['GET'])
def getLastReportById(isoCode, id, reportId):
    return jsonify({"message": "Not connected with db, so no prev report"})
