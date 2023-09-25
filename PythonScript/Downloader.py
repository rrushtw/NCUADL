import re
import requests


class Downloader:
    def __init__(self) -> None:
        self.__googleDriveDomain = 'https://drive.google.com/'
    # end def

    def Download(self, url: str, filename: str) -> None:
        if url.startswith(self.__googleDriveDomain):
            file_id_match = re.search(r"([A-Za-z0-9_\-]{28,})", url)

            if not file_id_match:
                print("Invalid Google Drive link")
                return

            # if file_id_match:
            file_id = file_id_match.group(1)
            download_url = f"{self.__googleDriveDomain}uc?id={file_id}"
            r = requests.get(download_url, stream=True)
            with open(filename, 'wb') as file:
                for chunk in r.iter_content(1024):
                    file.write(chunk)

            return
        # else:

        response = requests.get(url)
        with open(filename, 'wb') as file:
            file.write(response.content)
    # end def
# end class


if __name__ == '__main__':
    downloader = Downloader()

    url = input("Enter URL of the file to download: ")
    filename = input("Enter filename to save as: ")

    downloader.Download(url, filename)
