from db_test import test
from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/test',methods=[ 'GET'])
def location_api():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    timestamp = datetime.datetime.now()
    
    test(kecepatan=kecepatan,latitude=latitude,longitude=longitude,timestamp=timestamp)
    
    return{
        "kecepatan": kecepatan,
        "latitude": latitude,
        "longitude": longitude
    }

if __name__ == '__main__':
    app.run(debug=True)