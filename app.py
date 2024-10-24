import os

from flask import Flask
app = Flask(__name__)

@app.route('/')

def main():
    # Fetch the password from environment variables
    password = os.getenv('MY_PASSWORD')

    if password:
        print(f"Hello, World! The fetched password is: {password}")
    else:
        print("Hello, World! No password found.")

if __name__ == "__main__":
    main()
