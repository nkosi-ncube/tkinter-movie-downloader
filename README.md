# Tkinter Movie Downloader

This project is a web scraper and downloader for movies from the Goojara website. It uses Selenium to automate browser actions, interact with the web page, and download the movie file using curl.

## Features

- Automates searching for movies on Goojara.
- Interacts with web page elements to navigate and find movie links.
- Downloads movies directly to a specified directory.

## Prerequisites

- Python 3.x
- Selenium
- ChromeDriver
- Google Chrome browser
- termcolor

## Installation

1. **Install Python packages**:
    ```bash
    pip install selenium termcolor
    ```

2. **Download ChromeDriver**:
    - Download the ChromeDriver that matches your Chrome browser version from [here](https://sites.google.com/a/chromium.org/chromedriver/).
    - Place the `chromedriver` executable in a directory accessible by your system's PATH.

3. **Download Google Chrome** if not already installed from [here](https://www.google.com/chrome/).

## Usage

1. **Set up the download directory**:
    Modify the `download_directory` variable in the script to the desired location on your system.
    ```python
    download_directory="/path/to/your/download_directory"
    ```

2. **Run the script**:
    ```bash
    python scapper.py
    ```
    Follow the on-screen prompts to enter the name of the movie you want to download.

