from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Fetch the password from environment variables
    password = os.environ.get("MY_PASSWORD")

    if password:
        return f"Hello, World! The fetched password is: {password}"
    else:
        return f"Hello, World! No password found."

if __name__ == '__main__':
    app.run()
