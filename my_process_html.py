from bs4 import BeautifulSoup as bs
import os, sys, logging, string, glob
import cssutils as cu
import json

ferr = open("errors_in_scraping.log","w")

if __name__ == "__main__":
   main(sys.argv)
