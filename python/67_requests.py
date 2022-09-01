import requests

# res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# res.status_code = requests.codes.ok

# print(type(res))
# print(res.status_code)
# print(len(res.text))
# print(res.text[:252])


# Checking for errors
res = requests.get(
    "https://automatetheboringstuff.com/page_that_does_not_exist")

try:
    res.raise_for_status()
except Exception as exc:
    print(f"There was a problem: {exc}")
