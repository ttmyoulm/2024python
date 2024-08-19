import requests
serviceKey='m1Oi1NUJV+wZSAoPooIMCSufOAVvpKzdwUsgfcl8HZ4vDxYYz2rGCErr/Ynd3bLPR4yiKdOSAg/ASohJhNLtHg=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : 'serviceKey', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '울산', 'ver' : '1.0' }

response = requests.get(url, params=params)
data=response.json()
print(type(data))
print(data['response']['body']['items'][1]['pmValue'])