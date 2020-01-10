import requests


if __name__ == "__main__":
    download_list = []
    with open("files.txt", "r") as f:
        lines = f.read().split("\n")
        for line in lines:
            download_list.append(line)





