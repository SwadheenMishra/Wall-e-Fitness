from instagrapi import Client

def upload(path: str, caption: str = "get gud? lol") -> None:
    cl = Client()
    cl.login("YOUR ID", "YOUR PASSWORD")

    cl.photo_upload(path, caption)


if __name__ == '__main__':
    upload("img1.jpg", "Hackerman!!")
