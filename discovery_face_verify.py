import requests
from cs_key import key

import http.client, urllib.request, urllib.parse, urllib.error, base64

from face_detect import face_id

def verify_match(f_one, f_two):

    body = {
        "faceId":"c5c24a82-6845-4031-9d5d-978df9175426",
        "peronId":"815df99c-598f-4926-930a-a734b3fd651c",
        "personGroupId":"sample_group"
    }
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }

    params = urllib.parse.urlencode({
    })

    # url1 = face_id('http://pixel.nymag.com/imgs/fashion/daily/2014/12/04/04-channing-tatum.w529.h529.jpg')
    url2 = face_id(f_one)
    url1 = face_id(f_two)
    body = {
        'faceId1':url1,
        'faceId2':url2
    }


    front_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/verify?{}'.format(params) #'westus.api.cognitive.microsoft.com/face/v1.0/detect?'
    conn = requests.post(front_url, headers=headers, json=body)
    return conn.text
