import requests
import json

def send_request(url):
    try:
        response = requests.get(url)
        return response.json(), response.status_code
    except Exception as e:
        print(f"Błąd: {e}")
        return None, None

def check_response(response, status_code, expected_status, keys):
    if status_code != expected_status:
        return False
    try:
        for key in keys:
            if key not in response:
                return False
        return True
    except json.JSONDecodeError:
        return False

def main():
    tests = [
        {
            "url": "https://jsonplaceholder.typicode.com/posts/1",
            "expected_status": 200,
            "keys": ["userId", "id", "title", "body"]
        },
        {
            "url": "https://jsonplaceholder.typicode.com/users/1",
            "expected_status": 200,
            "keys": ["id", "name", "username", "email"]
        },
        {
            "url": "https://jsonplaceholder.typicode.com/todos/1",
            "expected_status": 200,
            "keys": ["userId", "id", "title", "completed"]
        }
    ]

    for i, test in enumerate(tests, 1):
        response, status_code = send_request(test["url"])
        if response is not None:
            if check_response(response, status_code, test["expected_status"], test["keys"]):
                print(f"Test {i}: PASSED")
            else:
                print(f"Test {i}: FAILED")
        else:
            print(f"Test {i}: FAILED to fetch response")

if __name__ == "__main__":
    main()
