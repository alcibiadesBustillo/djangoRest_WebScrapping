"""Web scrapper

This script allows the user scraping and  print to the console all 
the links of a website. It is assumed that the possible website are in
the config.yaml file.

This tool accepts comma separated value websites.

This script requires that `beautifoulsoup4, yaml` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * _news_scrapper - returns the links of the website
    * main - the main function of the script
"""

import argparse
import logging
logging.basicConfig(level=logging.INFO)
from common import config

import news_page_objects as news


logger = logging.getLogger(__name__)

def _news_scrapper(news_site_uid):
    """Scrape the news website

    Parameters
    ----------
    news_site_uid : str
        The name key of the website in the config.yaml file    

    Returns
    -------
    list
        lorep
    """
    host = config()['news_sites'][news_site_uid]['url']
    logger.info('\tBeggining scraper for {}'.format(host))
    #print('{} is the site to scrape'.format(news_site_uid))
    homepage = news.HomePage(news_site_uid, host)

    articles = []
    for link in homepage.article_links:
        print(link)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    news_sites_choices = list(config()['news_sites'].keys())
    parser.add_argument(
        'news_site',
        type=str,
        help='The news site that you want to scrape',
        choices=news_sites_choices        
    )
    args = parser.parse_args()
    _news_scrapper(args.news_site)

if __name__ == "__main__":
    main()