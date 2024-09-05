import http.client
import json
import os
import time
from urllib.parse import urlencode
from dotenv import load_dotenv


load_dotenv()

GITHUB_API = 'api.github.com'
ISSUE_ENDPOINT = '/repos/lobehub/lobe-chat/issues'
TOKEN = "" ##Put here your token GitHub
JSON_OUT_DIR = "...." ##Put here the folder where you want to save the results.
RATE_LIMIT_HR = 5000


def download(page: int) -> bool:
    connection = http.client.HTTPSConnection(GITHUB_API)
    headers = {'Accept': 'application/vnd.github+json',
               'User-Agent': 'wm-2024-ai4se',
               'Authorization': 'Bearer ' + TOKEN,
               'X-GitHub-Api-Version': '2022-11-28'}
    query = {'state': 'closed', 'page': str(page), 'per_page': str(100)}
    connection.request('GET', ISSUE_ENDPOINT + '?' + urlencode(query),
                       headers=headers)

    res_text = connection.getresponse().read().decode()
    res_json = json.loads(res_text)

    for issue in res_json:
        issue_id = issue['id']

        with open(os.path.join(JSON_OUT_DIR, str(issue_id) + '.json'), 'w') as f:
            json.dump(issue, f)

        print("Downloaded issue " + str(issue_id))

    return len(res_json) > 0


def main():
    page = 1
    more = True
    while more:
        more = download(page)
        page += 1
        time.sleep(3600 / RATE_LIMIT_HR)


if __name__ == '__main__':
    main()
