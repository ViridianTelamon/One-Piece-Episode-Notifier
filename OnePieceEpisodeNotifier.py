from win10toast_click import ToastNotifier
from bs4 import BeautifulSoup
import webbrowser
import requests
import os

print("One Piece Episode Notifier")

print("\nBy:  ViridianTelamon.")

print("\n--------------------")

print('\nUse The Command "pythonw" In Your Terminal To Run This Program In The Background, So The Command Would Be "pythonw OnePieceEpisodeNotifier.py", This Is For The Best Use Of This Program.')

print("\n--------------------")

def open_url():
    webbrowser.open_new_tab(link)

url = requests.get("https://www.crunchyroll.com/one-piece.rss")
web = BeautifulSoup(url.content, "xml")
link = web.find_all("link")[2].get_text()
episode = link[45:49]

with open("episode.txt", "w") as f:
    pass

with open("episode.txt", "r+") as f:
    current = f.read()
    if episode > current:
        title = "A New Episode Of One Piece Is Here."
        message = f"Episode {episode} | A New Episode Of One Piece Has Released Right Now, Click Here To Watch It."
        icon = os.getcwd() + "/" + "OnePiece.ico"
        toast = ToastNotifier()
        toast.show_toast(
            f"{title}",
            f"{message}",
            icon_path=icon,
            duration=5,
            threaded=True,
            callback_on_click=open_url
        )

        f.seek(0)
        f.write(episode)
        f.truncate()