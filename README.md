# zscore

## Project setup
```
 Using python 3.7.12 version
```

```
pip install -r requirements.txt
```

### Compiles and hot-reloads for development
```
 FLASK_APP=app.py flask run
```


### Run python app and then run below command to unit tests
```
python -m pytest
```

# NOTE
## WORKING CAPITAL calculated using below formula
```
 working_capital = total_assets / total_liabilities
```
# Deployment
### 
```
 Travis support added
```
```
 Deployed app on Heroku(without db)
  - DB support added on local and its working fine
  - Used hooks of Heroku to auto deploy.
```
```
 Deployed on kubenetes(minikube)

 o/p:
    NAME                         READY   STATUS    RESTARTS   AGE
    pod/flask-55b446ddbc-dm2pk   1/1     Running   0          160m

    NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
    service/flask        NodePort    10.101.151.70   <none>        5000:31108/TCP   160m
    service/kubernetes   ClusterIP   10.96.0.1       <none>        443/TCP          166m

    NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
    deployment.apps/flask   1/1     1            1           160m

    NAME                               DESIRED   CURRENT   READY   AGE
    replicaset.apps/flask-55b446ddbc   1         1         1       160m
    app % kl pod/flask-55b446ddbc-dm2pk
    * Serving Flask app "app.py"
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
    127.0.0.1 - - [24/Oct/2021 01:48:45] "GET /api/v1/company/gb/1234/12 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:49:07] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:55:58] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:55:59] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:55:59] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:55:59] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:55:59] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:56:00] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:56:00] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:56:00] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:56:00] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
    127.0.0.1 - - [24/Oct/2021 01:56:01] "PUT /api/v1/company/gb/1234 HTTP/1.1" 200 -
```

# Test
### Test this with curl command
```
    curl -X PUT \
    https://flask-zscore.herokuapp.com//api/v1/company/gb/1234 \
    -H 'cache-control: no-cache' \
    -H 'content-type: application/json' \
    -H 'postman-token: 5dfc7c39-2a46-cede-949e-4f703302e4a7' \
    -d '{"financials": [ 
    {"year": 2020, "ebit": 123.45, "equity": 234.56, "retained_earnings": 345.67, "sales":  1234.56, "total_assets": 345.67, "total_liabilities": 456.78}, 
    {"year": 2019, "ebit": 122.63, "equity": 224.56, "retained_earnings": 325.33, "sales":  1214.99, "total_assets": 325.04, "total_liabilities": 426.78}, 
    {"year": 2018, "ebit": 120.17, "equity": 214.06, "retained_earnings": 225.00, "sales":  1204.01, "total_assets": 305.11, "total_liabilities": 426.78}, 
    {"year": 2017, "ebit": 118.23, "equity": 204.96, "retained_earnings": 125.97, "sales":  1200.00, "total_assets": 290.75, "total_liabilities": 426.78}, 
    {"year": 2016, "ebit": 116.05, "equity": 234.56, "retained_earnings": 105.11, "sales":  1010.82, "total_assets": 250.13, "total_liabilities": 426.78}]}'

    Response:
        {
            "scores": [
                {
                    "year": 2020,
                    "zscore": 6.460767804898895
                },
                {
                    "year": 2019,
                    "zscore": 6.702748104168705
                },
                {
                    "year": 2018,
                    "zscore": 6.582050042561276
                },
                {
                    "year": 2017,
                    "zscore": 6.366685063220324
                },
                {
                    "year": 2016,
                    "zscore": 6.493126672682154
                }
            ]
        }
```
```
 GET call:
 https://flask-zscore.herokuapp.com/api/v1/company/gb/1234/12

 Response:
    {
    "message": "Not connected with db, so no prev report"
   }
```
