import requests


find_url = "https://www.findthemissing.org/en/photos/thumb/"


k = 0
for i in range(4000):
    response = requests.get(find_url + str(i))
    if response.status_code == 200:
        data = "An image! i =" + str(i)
        print(data);
        jpeg = 'mp_' + str(k) + ".jpeg"
        k += 1
        with open("missing_photos/" + jpeg, 'wb') as handle:
            response = requests.get(find_url + str(i), stream=True)

            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)


    if response.status_code == 404:
        print("not an image")
