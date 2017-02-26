
from discovery_face_verify import verify_match


import time

git_url = "https://raw.githubusercontent.com/phurtad2/To_Be_Discovered/master/twitter_thumbnails/" #+ MP_66.jpg"
face_b  = "https://raw.githubusercontent.com/phurtad2/To_Be_Discovered/master/twitter_thumbnails/dylan_ou.jpg"

for i in range(100):
    print(i)
    face_a = git_url + "TW_" + str(i) 
    print(verify_match(face_a, face_b))
