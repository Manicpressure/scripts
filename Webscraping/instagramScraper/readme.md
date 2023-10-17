# Instagram Hashtag Image Downloader

This script allows users to search for a specific hashtag on Instagram and download all the images related to that hashtag.

## Dependencies

Selenium: A tool for automating browsers.
`pip install selenium`

WebDriver Manager for Python: A helper to manage web driver related dependencies.
`pip install webdriver_manager`

Wget for Python: Pure Python download utility.
`pip install wget`

Chrome: Ensure that Google Chrome is installed on your machine as this script uses Chrome's WebDriver.

## Configuration

Before running the script, please make sure to configure the following:
Replace the USERNAME and PASSWORD values in the script with your Instagram username and password.

## Usage
Execute the Script:
`python <script_name>.py <hashtag>`

Replace <script_name>.py with the name of your script, and <hashtag> with the desired hashtag you want to search for.

## How it Works
The script logs in to Instagram using the provided credentials.
It navigates to the hashtag search page.
It identifies all the image elements and collects the source URLs of these images.
Creates a new directory (or uses an existing one) named after the hashtag in the current working directory.
Downloads and saves all the images in this directory.

## Notes
This script uses Chrome's WebDriver. Make sure to have Google Chrome installed on your system.
Instagram's website design and elements can change. If elements are updated, the script might need modifications to work correctly.
Use this script responsibly. Excessive or aggressive use might result in your IP address or account being temporarily blocked by Instagram.
