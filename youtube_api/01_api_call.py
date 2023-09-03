from googleapiclient.discovery import build
import os

DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")

class YoutubeApi:

    def __init__(self, api_key):

        self.youtube_api = build("youtube", "v3", developerKey=api_key)

    def youtube_search(self, query):
        search_response = youtube_api.search().list(
            q=query,
            part="id,snippet",
            maxResult=10
        ).execute()

        for item in search_response.get("items", []):
            print(item)

    def video(self, video_ids):
        print(video_ids)
        youtube_api = build("youtube", "v3", developerKey=DEVELOPER_KEY)
        videos_list_response = self.youtube_api.videos().list(
            id=video_ids,
            part='snippet,statistics'
        ).execute()

        r = []
        for item in videos_list_response.get("items", []):
            print(item)
            r.append({"video_id":item['id'], "title":item["snippet"]["title"], "commentCount":item["statistics"]["commentCount"]})
        return r

if __name__ == "__main__":
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
    api = YoutubeApi(DEVELOPER_KEY)
    api.youtube_search("업무 자동화")
    # api.youtube_search("슈카월드")
    video_id = ""
    r_video = api.video("")
    print(r_video)