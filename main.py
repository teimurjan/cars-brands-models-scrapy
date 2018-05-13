import sys
import time
import json
import codecs
from optparse import OptionParser
from selenium import webdriver
from settings import CHROME_DRIVER_LOCATION, BASE_URL
from scrapy import Scrapy

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-o', '--output', dest="filename", help="Write output to a file")

    options, args = parser.parse_args()
    if options.filename is None:
        print('usage: python main.py -o <outputfile>')
        sys.exit(2)

    scrapy = Scrapy()
    scrapy.run()

    with codecs.open(options.filename , 'w', encoding='utf-8') as f:
        json.dump(scrapy.result, f, ensure_ascii=False)
