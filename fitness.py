import time
import requests
from subprocess import Popen, PIPE

server_process = None


def is_server_running():
    """Check if the server is running by sending a request to /messages/count."""
    url = "http://127.0.0.1:5000/messages/count"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Server is successfully running!")
            return True
    except requests.exceptions.ConnectionError:
        print("Failed to connect to the server.")
    return False


def start_server():
    global server_process
    print("Starting the server...")
    server_process = Popen(['python', 'server.py'], stdout=PIPE, stderr=PIPE)

    # Wait for the server to start
    time.sleep(2)  # Wait for a couple of seconds to allow the server to start

    if not is_server_running():
        print("Error: Server did not start.")
        stop_server()
        exit(1)


def stop_server():
    global server_process
    if server_process:
        print("Stopping the server...")
        server_process.terminate()
        server_process.wait()


def test_time_behavior():
    """Test the response time for posting a message."""
    print("\nTesting Time Behavior:")
    url = "http://127.0.0.1:5000/messages"
    data = {"message": "Test message"}

    start_time = time.time()
    response = requests.post(url, json=data)
    end_time = time.time()

    response_time = end_time - start_time
    if response.status_code == 200 and response_time < 0.1:
        print(f"Response time: {response_time:.5f} seconds (Pass)")
    else:
        print(f"Response time: {response_time:.5f} seconds (Fail)")


def test_recoverability():
    """Test the system's recoverability after a simulated disconnection."""
    print("\nTesting Recoverability:")
    url = "http://127.0.0.1:5000/messages"

    print("Simulating database disconnection...")
    stop_server()
    start_time = time.time()
    time.sleep(5)  # Simulate 5 seconds of connection loss

    try:
        print("Attempting to send a message during failure...")
        response = requests.post(url, json={"message": "Message during failure"})
        print("Failed to simulate failure correctly.")
    except requests.exceptions.ConnectionError:
        print("Connection failed as expected during disconnection.")

    start_server()
    time.sleep(5)
    end_time = time.time()

    recovery_time = end_time - start_time
    if recovery_time < 300:
        print(f"Recovery time: {recovery_time:.2f} seconds (Pass)")
    else:
        print(f"Recovery time: {recovery_time:.2f} seconds (Fail)")

    print("Sending message after recovery...")
    response = requests.post(url, json={"message": "Message after recovery"})
    if response.status_code == 200:
        print("Message sent successfully after recovery (Pass)")
    else:
        print("Message sending after recovery failed (Fail)")


def test_maintainability():
    """Test the maintainability of the system by checking feature addition."""
    print("\nTesting Maintainability:")
    url = "http://127.0.0.1:5000/messages/latest"

    # Simulate feature addition by testing the latest message endpoint
    start_time = time.time()

    response = requests.get(url)
    end_time = time.time()

    if response.status_code == 200:
        print(f"Successfully retrieved latest message: {response.json()} (Pass)")
    else:
        print(f"Failed to retrieve latest message. Status code: {response.status_code} (Fail)")

    # Output the time taken for the feature test
    recovery_time = end_time - start_time
    if recovery_time < 60000:
        print(f"Time taken for maintainability test: {recovery_time:.2f} seconds (Pass)")
    else:
        print(f"Time taken for maintainability test: {recovery_time:.2f} seconds (Fail)")


if __name__ == "__main__":
    start_server()
    test_time_behavior()
    test_recoverability()
    test_maintainability()
    stop_server()
