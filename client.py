import requests

SERVER_URL = 'http://127.0.0.1:5000'


def send_message(message):
    """Send a message to the server."""
    url = f"{SERVER_URL}/messages"
    data = {'message': message}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")


def get_messages():
    """Retrieve all messages from the server."""
    url = f"{SERVER_URL}/messages"
    response = requests.get(url)
    if response.status_code == 200:
        messages = response.json().get('messages', [])
        print("Messages:")
        for msg in messages:
            print(f"{msg['timestamp']}: {msg['message']}")
    else:
        print("Failed to retrieve messages.")


def get_message_count():
    """Get the total number of messages."""
    url = f"{SERVER_URL}/messages/count"
    response = requests.get(url)
    if response.status_code == 200:
        count = response.json().get('count', 0)
        print(f"Total messages: {count}")
    else:
        print("Failed to retrieve message count.")


if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Send Message")
        print("2. View Messages")
        print("3. Get Message Count")
        print("4. Exit")

        choice = input("Choose an option: ")

        match choice:
            case '1':
                msg = input("Enter your message: ")
                send_message(msg)
            case '2':
                get_messages()
            case '3':
                get_message_count()
            case '4':
                break
            case _:
                print("Invalid choice, please try again.")
