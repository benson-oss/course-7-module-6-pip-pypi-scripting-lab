from datetime import datetime
import requests


log_data = [
    "User logged in",
    "User updated profile",
    "Report exported"
]

filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"


def fetch_data():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    if response.status_code == 200:
        return response.json()

    return {}


def generate_log(post):
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

        file.write("\nAPI Data\n")
        file.write(f"Title: {post.get('title', 'No title found')}\n")
        file.write(f"Body: {post.get('body', 'No body found')}\n")


if __name__ == "__main__":
    post = fetch_data()

    generate_log(post)

    print(f"Log written to {filename}")
    print("Fetched Post Title:", post.get("title", "No title found"))