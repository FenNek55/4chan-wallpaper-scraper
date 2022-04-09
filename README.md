# 4chan-wallpaper-scraper
Python web scraper for automatically downloading wallpapers from boards.4chan.org/wg/

## Dependencies
Project uses selenium for getting page source and BeautifulSoup for working with website data

## Goal of the project
The goal of this project is to create a scraper that gets number of responses in each thread. Then it should download given number of most popular images in a thread (based on number of replies) from given number of most popular threads (also based on number of replies). This could be used to download most popular wallpapers of the day and set them as your current wallpaper.

Since different boards have simmilar structure, it should also be possible to do the same scraping procedure on other boards

**Warning** 4chan boards might contain NSFW images
