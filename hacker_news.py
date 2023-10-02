import requests
import time


def get_hacker_news():
    # Hacker NewsのAPIエンドポイント
    api_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

    # トップニュースのIDリストを取得
    response = requests.get(api_url)
    if response.status_code != 200:
        print("APIからデータを取得できませんでした。")
        return

    top_story_ids = response.json()

    # ニュースの詳細データを取得し表示（間隔を空けて）
    for i, story_id in enumerate(top_story_ids, start=1):
        if i > 30:
            break  # 30回のAPIリクエストを超えた場合、終了

        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story_response = requests.get(story_url)
        if story_response.status_code != 200:
            print(f"ニュース {story_id} のデータを取得できませんでした。")
            continue

        story_data = story_response.json()
        title = story_data.get('title')
        link = story_data.get('url')

        if link:
            print({'title': title, 'link': link})
        else:
            print({'title': title, 'link': None})

        # 1秒の間隔を空ける
        time.sleep(1)


if __name__ == "__main__":
    get_hacker_news()
