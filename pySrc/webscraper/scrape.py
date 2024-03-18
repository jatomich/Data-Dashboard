'''
                      GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 Full license text can be found at <https://www.gnu.org/licenses/gpl-3.0.html#license-text>.
###########################################################################################
Title: scrape.py

Description: This file contains the main function within which the user is prompted for a scraper method
and a url to scrape.

Author: Andrew Tomich
'''
from scrapers import StarScraper

def scrape():
    # Prompt the user for a url
    # filepath: str = input("Enter a datasource filepath: ")
    filepath = '../data/FULLY_COMBINED_DATASET.xlsx'

    # instantiate a Scraper object
    star_scraper: StarScraper = StarScraper(filename=filepath)


    # Call the get_html method
    star_scraper.scrape_star_data()
    # Quit the webdriver
    star_scraper.webdriver.quit()


# Call the scrape function
if __name__ == '__main__':
    scrape()