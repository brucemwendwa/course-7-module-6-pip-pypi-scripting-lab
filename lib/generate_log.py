from datetime import datetime


API_URL = "https://jsonplaceholder.typicode.com/posts/1"
DEFAULT_LOG_DATA = ["User logged in", "User updated profile", "Report exported"]


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("Log data must be provided as a list.")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    import requests

    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        return {}

    return {}


def main():
    post = fetch_data()
    log_data = DEFAULT_LOG_DATA.copy()

    title = post.get("title")
    if title:
        log_data.append(f"Fetched Post Title: {title}")

    generate_log(log_data)


if __name__ == "__main__":
    main()
