#!/usr/bin/python3
from bin import http_ssl_verf
from urllib.parse import urlparse
from bin import web_crawler
import sys

#This function is made trim the url to get the specific domain for the next function to work upon
def url_splitter(url,flag):
    x = urlparse(url)
    if (x.scheme != 'https') and (x.scheme != 'http'):
        print("\n\nThe website link has no scheme. Did you mean https://"+str(url)+"?")
        sys.exit(0)        
    split_url = str(x.netloc)
    if x.port is not None:
       rem_port = ':'+str(x.port)
       split_url = split_url.replace(str(rem_port),'')
    if split_url.startswith('www'):
       split_url = split_url.split("www.")[1]
    print("\n\n")
    http_ssl_verf.check_ssl(split_url)
    print("\n\n")
    web_crawler.crawl(url, flag)
    web_crawler.load_animation()
    print("\n\n")
    web_crawler.print_target_links()
    print("\n\n")
    web_crawler.call_sql_vul_check()
