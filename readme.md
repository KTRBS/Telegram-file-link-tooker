## this is ktr devock tool

# **Telegram Channel File Extractor**  

This Python script extracts `.apk` file names and links from a Telegram channel and saves them in a text file (`file_links.txt`).  

## **Features**  
✅ Extracts `.apk` file names and their respective Telegram links  
✅ Saves results in `file_links.txt` (creates the file if it doesn't exist)  
✅ Sorts file names alphabetically (case-insensitive)  
✅ Removes unnecessary parts from file names:  
  - Deletes **everything inside parentheses** `()`  
  - Removes `"_signed"` and `"_mod"` **except** when the name contains `"gen_signed"`  
  - Removes `"(com.xxx)"` patterns (e.g., `(com.example.app)`)  
✅ Cleans Telegram links by removing `@` from the channel username  

## **Installation**  
### **Prerequisites**  
- Python 3.x  
- Install dependencies:  
  ```sh
  pip install telethon

## **Usage**  
1. **Get your Telegram API credentials:**  
   - Go to [my.telegram.org](https://my.telegram.org/)  
   - Sign in and navigate to "API Development Tools"  
   - Create a new app and get your `api_id` and `api_hash`  

2. **Configure the script:**  
   Open the script and set the following variables:  
   ```python
   api_id = 1234567  # Replace with your API ID
   api_hash = 'your_api_hash_here'  # Replace with your API Hash
   channel_username = 'your_channel_username'  # Replace with the Telegram channel username  
3. **Run the script:**  
   ```sh
   python zare.py
