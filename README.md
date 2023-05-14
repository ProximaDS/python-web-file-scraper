# Repository Description

## General Information

This repository contains a Python script designed to automate the process of downloading specific file types from a given webpage. The script is capable of handling PDF, DOC, DOCX, XLS, and XLSX file formats. The user will be prompted to input the URL from which the files will be downloaded, and the directory where they will be stored.

## Functionality

The script works by sending a GET request to the provided URL, then using the BeautifulSoup library to parse the HTML content of the page. It looks for links ending with the specified file types (.pdf, .docx, .doc, .xls, .xlsx), and then attempts to download each file using the wget command.

If the specified directory for storing the files does not exist, the script automatically creates it. The script also keeps a log of any files that were skipped during the download process in a file named "skipped_files.log". This helps the user understand if any files were not downloaded and why.

In case a file download fails, the script logs the filename and the current timestamp to both the console and the log file. Then, it deletes the incomplete file.

To avoid overloading the server with rapid successive requests, the script incorporates a brief pause (0.2 seconds) between file downloads.

## Prerequisites

To run the script, you'll need Python installed on your machine along with the following Python packages:

- os, time, subprocess, requests, ssl, logging, datetime for core functionalities
- urllib for parsing and decoding URLs
- BeautifulSoup for parsing the HTML content of a webpage
- unidecode for converting non-ASCII characters into their closest ASCII equivalents

Please note that this script uses wget for downloading files, so you need to have it installed on your machine.

## Disclaimer

This script bypasses SSL certificate verification. This can help if you're downloading from a site with a certificate that isn't trusted, but should be used with caution as it does not validate the identity of the server.

## How to Use

Simply run the script, and when prompted, provide the URL from where the files are to be downloaded and the directory where you want the files to be stored.

This script is intended to be a utility for downloading specific file types from a URL. It can be particularly useful for batch downloading files from a webpage.\

## Additional Instructions for Installing and Using wget

### Linux

Wget is a free utility available for Unix-like operating systems. Most Linux distributions have wget installed by default. If not, you can install it using your distribution's package manager. For example, on Ubuntu, you can install wget by opening a terminal and typing:

```
sudo apt-get install wget
```

### Windows

Windows users can download wget from the GNU Win32 project page (http://gnuwin32.sourceforge.net/packages/wget.htm) or install it via a package manager like Chocolatey.

To install wget using Chocolatey, first, install Chocolatey by following the instructions at https://chocolatey.org/install. Once Chocolatey is installed, you can install wget by opening a command prompt (cmd.exe) as an administrator and typing:

```
choco install wget
```

### macOS

On macOS, you can install wget using Homebrew. If you don't have Homebrew installed, you can install it by pasting the following command in a macOS Terminal prompt:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Once Homebrew is installed, you can install wget by typing:

```
brew install wget
```

### Using wget in the script

Once wget is installed, it can be used directly in the command line or through subprocess calls in a script, as seen in this repository. The script constructs a wget command and uses subprocess.run() to download the target file. If the download fails, an exception is raised, logged, and the incomplete file is removed.
