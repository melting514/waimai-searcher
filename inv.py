#!/usr/bin/ python
# -*- coding:utf-8 -*-
INDEX_DIR = "IndexFiles.index"
 
import web
from web import form
import urllib2
import re
import urlparse
import sys, os, lucene
from bs4 import BeautifulSoup
from java.io import File
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version

vm_env=lucene.initVM()