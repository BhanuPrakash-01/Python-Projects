import requests

parameters={
    'amount':10,
    'category':18,
    'type':'boolean'
}
responce=requests.get(url='https://opentdb.com/api.php',params=parameters)
responce.raise_for_status()
data=responce.json()
question_data=data['results']