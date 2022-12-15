import requests
import selenium


token = "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"
url = "https://api.github.com/search/repositories"
query_param = "?q="
query = "create-react-app"

response = requests.get(f"{url}{query_param}{query}", 
    headers = {"Accept": "application/vnd.github+json", 
               "Authorization": f"Bearer {token}", 
               "X-GitHub-Api-Version": "2022-11-28"})

payload = response.json()

print(payload['items'][0]['url'])