import requests

# res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# res.status_code = requests.codes.ok

# print(type(res))
# print(res.status_code)
# print(len(res.text))
# print(res.text[:252])


# Checking for errors
# res = requests.get(
#     "https://automatetheboringstuff.com/page_that_does_not_exist")

# try:
#     res.raise_for_status()
# except Exception as exc:
#     print(f"There was a problem: {exc}")


# Saving downloaded files to the hard drive
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
play_file = open("Romeo_And_Juliet.txt", "wb")

for chunk in res.iter_content(100000):
    play_file.write(chunk)

play_file.close()
