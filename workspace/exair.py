import requests
#serviceKey='UYarzU%2BxHwMRSYof%2BGdaYx9aTb7QMVJxstOWwwxdxD%2Buy1lTlnAkwk8vBgOV%2FZ%2B5Fe552PXRMK7ftvaRqJrxWg%3D%3D'
serviceKey='UYarzU+xHwMRSYof+GdaYx9aTb7QMVJxstOWwwxdxD+uy1lTlnAkwk8vBgOV/Z+5Fe552PXRMK7ftvaRqJrxWg=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : 'serviceKey', 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '서울', 'ver' : '1.0' }

response = requests.get(url, params=params)
print(response.text)