from instagrapi import Client
from instagrapi.exceptions import TwoFactorRequired


def login_to_instagram(username, password, verification_code=None):
    # Create a client instance
    client = Client()

    try:
        # Try to login
        if verification_code:
            logged_in = client.login(username, password, verification_code=verification_code)
        else:
            logged_in = client.login(username, password)

        # If login was successful
        if logged_in:
            print("Login was successful")
            return client
    except TwoFactorRequired:
        # If 2FA is required, prompt for verification code
        verification_code = input("Enter 2FA verification code: ")
        return login_to_instagram(username, password, verification_code)
    except Exception as e:
        # If login was not successful
        print("Login was not successful:", e)


def unfollow_all_users(client):
    # Fetch users you are following
    following = client.user_following(client.user_id)
    for user_id, user_info in following.items():
        username = user_info.username
        print(f"Unfollowing {username}")
        client.user_unfollow(user_id)


if __name__ == "__main__":
    # Provide your Instagram username and password here
    username = "<your_username>"
    password = "<your_password>"

    # Attempt to login
    client = login_to_instagram(username, password)

    if client:
        # Unfollow every person
        unfollow_all_users(client)