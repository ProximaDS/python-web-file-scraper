# Importing necessary libraries
import os
import time
import subprocess
import requests
import ssl
import logging 
import datetime 

# This line allows us to bypass SSL certificate verification, which can help if we are downloading from a site with a certificate that isn't trusted.
ssl._create_default_https_context = ssl._create_unverified_context

# Importing additional modules that will be used for parsing and decoding URLs
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from unidecode import unidecode

# Asking user to input URL from where files will be downloaded
url = input("Enter the read link: ")

# Asking user to specify the directory where the files will be stored
folder_location = input("Enter write path: ")

# If the specified directory does not exist, create it
if not os.path.exists(folder_location):
    os.mkdir(folder_location)

# Creating a log file in the directory to keep track of any files that were skipped
log_file = os.path.join(folder_location, "skipped_files.log")

# Send a GET request to the provided URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# Initialize the file counter
index = 1

# Open the log file in write mode
with open(log_file, "w") as f:
    # For every link in the HTML that ends with specified file types
    for link in soup.select("a[href$='.pdf'], a[href$='.docx'], a[href$='.doc'], a[href$='.xls'], a[href$='.xlsx']"):
        # Define the filename using the counter and the original filename, decoded to ASCII
        filename = os.path.join(folder_location, f"{index:04d}_{unidecode(link['href'].split('/')[-1])}")
        # Create a command to be run in the system's shell: download the file using wget
        cmd = ["wget", "-O", filename, "--no-check-certificate", urljoin(url, link['href'])]
        try:
            # Try to execute the command
            subprocess.run(cmd, check=True)
            print(f"File '{filename}' downloaded successfully.")
        except subprocess.CalledProcessError as e:
            # If the command fails, log the filename and the current timestamp to both the console and the log file
            logging.info(f"Skipped file: {unidecode(link['href'].split('/')[-1])} - {time.strftime('%Y-%m-%d %H:%M:%S')}")
            f.write(f"{unidecode(link['href'].split('/')[-1])} - {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            # Delete the incomplete file
            os.remove(filename)
        # Pause for 0.2 seconds to avoid overloading the server with requests
        time.sleep(0.2)
        # Increment the file counter
        index += 1
