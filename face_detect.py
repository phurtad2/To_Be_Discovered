from cs_key import key
import http.client, urllib.request, urllib.parse, urllib.error, base64
import requests
import json

def face_id(url):
    headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',

    })
    body = {
    "url": url #"http://pixel.nymag.com/imgs/fashion/daily/2014/12/04/04-channing-tatum.w529.h529.jpg"
    }


    front_url ='https://westus.api.cognitive.microsoft.com/face/v1.0/detect?{}'.format(params) #'westus.api.cognitive.microsoft.com/face/v1.0/detect?'
    conn = requests.post(front_url, headers=headers, json=body)

    if(conn.text== '[]'):
        return None
    try :
        return json.loads(conn.text)[0]['faceId']
    except KeyError:
        return 0.0
