import os
import re
from telethon.sync import TelegramClient

# API credentials
api_id = 1234567  # Replace with your API ID
api_hash = 'your_api_hash_here'  # Replace with your API Hash
channel_username = 'your_channel_username'  # Replace with your Telegram channel username

# Function to clean file names
def clean_file_name(file_name):
    # Remove everything inside parentheses (including the parentheses)
    file_name = re.sub(r'.*?', '', file_name)
    
    # Remove "_signed" and "_mod" unless it is part of "gen_signed"
    if "gen_signed" not in file_name:
        file_name = file_name.replace('_signed', '').replace('_mod', '')
    
    # Remove patterns starting with "(com."
    file_name = re.sub(r'com\..*?', '', file_name)
    
    # Remove the '@' symbol from Telegram links
    return file_name

# Connect to Telegram Client
with TelegramClient('session_name', api_id, api_hash) as client:
    # Get all messages from the specified channel
    messages = client.get_messages(channel_username, limit=100)  # You can adjust the limit as needed
    
    # Create a list to store the file names and their links
    file_links = []
    
    # Loop through all the messages
    for message in messages:
        # Check if the message contains a file
        if message.file and message.file.mime_type == 'application/vnd.android.package-archive':  # Filter for .apk files
            file_name = message.file.name
            file_link = f'https://t.me/{channel_username}/{message.id}'
            
            # Clean the file name
            cleaned_file_name = clean_file_name(file_name)
            
            # Add the cleaned file name and link to the list
            file_links.append(f"{cleaned_file_name}, {file_link}")
    
    # Sort the list alphabetically by file name (case insensitive)
    file_links.sort(key=lambda x: x.split(',')[0].lower())
    
    # Write the cleaned file names and links to a text file
    with open('file_links.txt', 'w', encoding='utf-8') as file:
        for entry in file_links:
            file.write(entry + '\n')

print("Process completed. File links saved to 'file_links.txt'.")
