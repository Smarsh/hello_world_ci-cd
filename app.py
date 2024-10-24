from flask import Flask
import hvac  # HashiCorp Vault API client

app = Flask(__name__)

# Initialize Vault client
client = hvac.Client(url='https://hashicorp-vault.hashicorp-vault.svc.cluster.local:8200', token='your-root-token')

@app.route('/')
def hello_world():
    # Fetch secrets from Vault
    secret = client.secrets.kv.v2.read_secret_version(path='secret/hello-world-shail')
    
    # Extract password from the secret
    password = secret['data']['data']['password']

    # Display hello message with username
    return f"Hello! Your password is {password}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

