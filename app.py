# app.py
import os

def main():
    # Read template from ConfigMap
    with open("/config/template", "r") as file:
        template = file.read()

    # Read password from externalsecret
    with open("/secret/password", "r") as file:
        password = file.read().strip()

    # Replace .password in the template
    message = template.replace(".password", password)
    print(message)

if __name__ == "__main__":
    main()