from requests import get

websites = (
    "naver.com",
    "https://google.com",
    "twitter.com",
)
results = {}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    if (get(website).status_code == 200):
        results[website] = 'OK'
    else:
        results[website] = 'FAiled'

print(results)
