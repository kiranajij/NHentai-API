import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from nhentai import NHentai

def test_case01():
    search = NHentai().search('320165')
    assert search is not None

def test_case02():
    search = NHentai().search('658468468')
    assert len(search.get('doujins')) == 0

def test_case03():
    search = NHentai().search('naruto')
    assert len(search.get('doujins')) > 0

def test_case04():
    search = NHentai().search('320253')
    assert search is not None

def test_case05():
    search = NHentai().search('320066')
    assert search is not None

def test_case06():
    search = NHentai().search('auhdasudhudasd')
    assert len(search.get('doujins')) == 0

def test_case07():
    search = NHentai().search('full color')
    assert len(search.get('doujins')) > 0
