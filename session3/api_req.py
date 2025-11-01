import requests

def getApiData(url):
    try:
        response = requests.get(url)
        return response.json()
    except Exception as err:    
        return err

def postApiData(url, data, headers):
    response = requests.post(url, json = data, headers=headers)
    print(response.json())