import requests
#print(requests.__version__)
#r = requests.get('https://www.google.com/')
#print(r.status_code)

r = requests.get('https://raw.githubusercontent.com/zisen01/CMPUT404_lab1/master/lab1.py')
print(r.text)
