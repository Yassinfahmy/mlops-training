import  requests


ride={
    "do_location_id": 20 ,
    "DOLocationID": 10,
    "trip_distance": 40
}


url = 'http://localhost:9696/predict'

response = requests.post(url, json=ride)
print(response.json())