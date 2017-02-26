
from discovery_face_verify import verify_match


import time

git_url = "https://raw.githubusercontent.com/phurtad2/To_Be_Discovered/master/missing_persons/" #+ MP_66.jpg"
face_b  = "https://raw.githubusercontent.com/phurtad2/To_Be_Discovered/master/missing_persons/MP_10.jpg"
for i in range(1, 100):
    face_a = git_url + "MP_" + str(i) + ".jpg"
    print(i)
    print(verify_match(face_a, face_b))
    time.sleep(.5)
