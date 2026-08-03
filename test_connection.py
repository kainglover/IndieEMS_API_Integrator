import requests

API_KEY = "YTYcW4tJl9E6xkea8M6cSt6mpQugKHcNv2HmVidYb"

headers = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

endpoints = [
    "devices",
    "devicestatus",
    "history",x
    "viewarchives",
    "exportarchive",
    "archive"
]

for endpoint in endpoints:

    url = f"https://restapi01.indieems.com/v1/cobbemc/"

    print("\n" + "=" * 80)
    print("Testing:", url)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=50
        )

        print("Status:", response.status_code)
        print("Response:", response.text[:300])

    except Exception as e:
        print("ERROR:", e)