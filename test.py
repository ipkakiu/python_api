import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 67, "name": "Kelvin", "views": 948},
        {"likes": 8473, "name": "Gerorge", "views": 163984},
        {"likes": 943, "name": "Petre", "views": 29084}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

# response = requests.delete(BASE + "video/0")
# #response = requests.put(BASE + "video/1", {"likes": 10, "name": "Marco", "views": 3768})
# print(response)
input()
# response = requests.get(BASE + "video/0")
response = requests.patch(BASE + "video/0", {"views": 99999, "likes": 88888})
print(response.json())