# AI YouTube Bot Script

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Set API Service Name and Version
API_SERVICE_NAME = 'youtube'  
API_VERSION = 'v3'  
CLIENT_SECRETS_FILE = 'client_secret.json'

# Get credentials and create an API client
scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']

def main():
    # Create a flow object. This object holds the authorization information.
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes)
    credentials = flow.run_console()

    youtube = googleapiclient.discovery.build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    # Example: Retrieve your channel's videos
    request = youtube.channels().list(
        part="contentDetails",
        mine=True
    )
    response = request.execute()

    print(response)

if __name__ == '__main__':
    main()