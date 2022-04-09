# 4chan-wallpaper-scraper
Python web scraper for automatically downloading wallpapers from boards.4chan.org/wg/

## Goal of the project
The goal of this project is to create a scraper that gets number of responses in each thread. Then it should download given number of most popular images in a thread (based on number of replies) from given number of most popular threads (also based on number of replies). This could be used to download most popular wallpapers of the day and set them as your current wallpaper.

## Dependencies
**TODO**: add requirements.txt
⚠️ Before running the script makes sure you installed all the required dependencies with the command below (you need python and pip first)
`pip install beautifulsoup4 selenium webdriver_manager`

## Using the scraper
To run the scraper, simply clon this repository and run chanScrape.py. All images and data will be stored in the output folder. Remember to install dependencies first ⬆️

Running the scraper:
(in root folder)

`python .\src\chanScrape.py <number_of_threads> <number_of_images_in_each_thread>`

so running

`python .\src\chanScrape.py 3 10`

will download first ten images from top 3 threads sorted by number of responses

Since different boards have simmilar structure, it is possible to do the same scraping procedure on other boards by changing the url in chanScrape.py file

**Warning** 4chan boards might contain NSFW images
