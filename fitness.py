import time
import requests


def test_time_behavior():
    """Test the response time for posting a message."""
    url = "http://127.0.0.1:5000/messages"
    data = {"message": "Test message"}

    start_time = time.time()
    response = requests.post(url, json=data)
    end_time = time.time()

    response_time = end_time - start_time
    assert response.status_code == 200
    print(f"Response time: {response_time:.5f} seconds")
    assert response_time < 0.1  # Response should be less than 100ms


if __name__ == "__main__":
    test_time_behavior()
