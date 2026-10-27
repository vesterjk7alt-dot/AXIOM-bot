
# AXIOM Smart Hunter - Reddit API example
# Read-only example. Requires approved API access.

import os
import requests


def get_reddit_posts():
    client_id = os.environ["REDDIT_CLIENT_ID"]
    client_secret = os.environ["REDDIT_CLIENT_SECRET"]
    user_agent = os.environ["REDDIT_USER_AGENT"]

    token_response = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=(client_id, client_secret),
        data={"grant_type": "client_credentials"},
        headers={"User-Agent": user_agent},
        timeout=15,
    )
    token_response.raise_for_status()
    token = token_response.json()["access_token"]

    response = requests.get(
        "https://oauth.reddit.com/r/CryptoCurrency/new",
        headers={
            "Authorization": f"bearer {token}",
            "User-Agent": user_agent,
        },
        params={"limit": 10},
        timeout=15,
    )
    response.raise_for_status()

    for post in response.json()["data"]["children"]:
        print(post["data"]["title"])


if __name__ == "__main__":
    get_reddit_posts()
