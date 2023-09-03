from googleapiclient.discovery import build
import os, json

DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")

class YoutubeApi:

    def __init__(self, api_key):

        self.youtube_api = build("youtube", "v3", developerKey=api_key)

    def youtube_search(self, query: object) -> object:
        search_response = self.youtube_api.search().list(
            q=query,
            part="id,snippet",
            maxResult=10
        ).execute()

        video_ids = []
        for item in search_response.get("items", []):
            if item["id"]["kind"] == "youtube#video":
                video_ids.append()
        return ",".join(video_ids)

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
            r.append({"video_id":item['id'], "title":item["snippet"]["title"],
                      "channelTitle":item["snippet"]["channelTitle"],
                      "commentCount":item["statistics"]["commentCount"]})
        return r

    def comment(self, video_id, max_cnt):
        comment_list_response = self.youtube_api.videos().list(
            videoId=video_id,
            part='snippet,statistics',
            maxResults=max_cnt
        ).execute()

        for comment in comment_list_response.get("items",):
            snippet = comment['snippet']['topLevelComment']['snippet']
            map = {"videoId":snippet["videoId"], "textOriginal":snippet['textOriginal'], "authorDisplayName":snippet["authorDisplayName"]}
            print(map)
            # print(snippet['textOriginal'], snippet['authorDisplayName'])
            # print(json.dumps(comment))

if __name__ == "__main__":
    DEVELOPER_KEY = os.getenv("YOUTUBE_API_KEY")
    api = YoutubeApi(DEVELOPER_KEY)
    #api.youtube_search("업무 자동화")
    # video_ids = api.youtube_search("슈카월드")
    # r_video = api.video(video_ids)
    #video_id = ""
    # print(r_video)
    # for item in r_video:
    #     print(item)

    api.comment("", 61)