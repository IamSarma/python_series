import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.status_code = requests.codes.ok

print(type(res))
print(res.status_code)
print(len(res.text))
print(res.text[:252])
