# June, 2021
# This py file is based on CC_NER_from_proxies (Apr, 2021).ipynb
# This finds DEF 14As, reads them, and does NER on the files
#

from __future__ import unicode_literals, print_function
import urllib.request
#from spacy.train_new_entity_type import TRAIN_DATA

#import plac
import random
import warnings
from pathlib import Path
import spacy
from spacy.util import minibatch, compounding
from TRAIN_DATA import TRAIN_DATA  # train examples are in this py file.
from tqdm.auto import tqdm

import os
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

import unicodedata
import jellyfish
from ast import literal_eval
import itertools

# to avoid
set = __builtins__.set

df = pd.DataFrame()

# create a dict of cik and ticker
page = urllib.request.urlopen(
    'https://www.sec.gov/include/ticker.txt').read().decode('utf-8')
pageList = page.split('\n')
idDict = {item.split('\t')[1]: item.split('\t')[0] for item in pageList}


# select the home folder
startFolder = input('which Drive to start with?')
os.chdir(startFolder)  # change to each folder of SP500
for folderName, subfolders, filenames in os.walk(startFolder):
    sp500List = []
    print('The current folder is  ' + folderName)
    print('the # of subfolders is  ' + str(len(subfolders)))
    for subfolder in subfolders:
        sp500List.append(subfolder)
    if folderName == startFolder:
        break  # prevents os.walk from going through all the other subfolders
try:
    sp500List.remove('$RECYCLE.BIN')
    sp500List.remove('System Volume Information')
    sp500List.remove("sec-edgar-filings")  # added on Apr 9, 2021
    sp500List.remove('.System')  # added on Aug 5,2020
    sp500List.remove('_SP500_1995-2016-employmentK')
except:
    pass
# bigDict=defaultdict(list)

# creates a list of folder paths.
# sp500List is the list of sp500 firms
pathList = []
for sp500Firm in sp500List:
    firmName = sp500Firm  # FIRMNAME
    absPath = os.path.join(startFolder, sp500Firm)
    print(absPath)
    pathList.append(absPath)

os.chdir(r'C:\Users\KWan\Documents\NLP & ML\compensation consultant')
nlp = spacy.load(
    r'C:\Users\KWan\Documents\NLP & ML\compensation consultant\CC')
nlp.max_length = 10000000000

# customize the range

startRange = input('start from?')
endRange = input('end to?')
P_pathList = pathList[int(startRange):int(endRange)]


# Integrated functions

# 1.
def find_proxies(dir):
    os.chdir(dir)  # r'F:\ADVANCED MICRO DEVICES INC')
    htmls = os.listdir()
    regex = re.compile('DEF 14')
    proxies = []
    for html in htmls:
        if regex.search(html):
            if html.endswith('html'):
                proxies.append(html)
    print(proxies)
    proxies2007 = []
    regex = re.compile('(\d\d\d\d)-\d\d-\d\d')
    if proxies == None:
        return proxies2007
    else:
        for proxy in proxies:
            try:
                match = int(regex.search(proxy).group(1))
                if match > 2006:
                    proxies2007.append(proxy)
            except AttributeError:
                print(r'no \d\d\d\d-\d\d-\d\d match')

    return proxies2007

# 2.


def open_proxy1(proxies2007):
    """loop 2007 and after proxies and yield those with 'consultant' hits """
    from bs4 import BeautifulSoup, UnicodeDammit
    import html
    if proxies2007 == []:
        fileList, hitList = None, None
    else:
        #regex=re.compile('committee', re.I)
        fileList = []
        hitList = []
        TypeErrorList = []
        for proxy in proxies2007:
            hit = []
            try:
                with open(proxy, 'r', encoding='utf8') as f:
                    contents = f.read()
                    bs = BeautifulSoup(contents, 'lxml')
            except TypeError:  # when bs4 does not work
                typeErrorList.append(proxy)  # record the filename
                # hitList.append(hit) # and return a blank list
                continue

            for item in bs.find_all(string=re.compile('consultant', re.I)):

                if re.search(r'audit', str(item), re.I | re.VERBOSE):
                    continue

                text = unicodedata.normalize("NFKC", item)
                text = html.unescape(text)
                #text=UnicodeDammit(text, ["windows-1252"], smart_quotes_to="html").unicode_markup
                text = re.sub(r'\n', ' ', text)
                text = re.sub(r'\x92', "'", text)  # \x92
                text = re.sub(r'\x93', '"', text)
                text = re.sub(r'\x94', '"', text)
                text = re.sub(r'\x97', ' ', text)
                hit.append(text)

            for item in bs.find_all(string=re.compile('committee', re.I)):

                if re.search(r'audit', str(item), re.I | re.VERBOSE):
                    continue
                if re.search(r'GOVERNANCE', str(item), re.I | re.VERBOSE):
                    continue
                if re.search(r'nominating', str(item), re.I | re.VERBOSE):
                    continue
                if re.search(r'(legal)|(counsel)', str(item), re.I | re.VERBOSE):
                    continue
                if not re.search(r'compensation', str(item), re.I | re.VERBOSE):
                    continue
                if re.search(r'peer', str(item), re.I | re.VERBOSE):
                    continue
                if re.search(r'(member)|(consist)', str(item), re.I | re.VERBOSE):
                    continue
                if re.search(r'comparator', str(item), re.I | re.VERBOSE):
                    continue

                # find=item.parent.get_text()
                text = unicodedata.normalize("NFKD", item)
                text = html.unescape(text)
                #text=UnicodeDammit(text, ["windows-1252"], smart_quotes_to="html").unicode_markup
                text = re.sub(r'\n', ' ', text)
                text = re.sub(r'\x92', "'", text)  # \x92
                text = re.sub(r'\x93', '"', text)
                text = re.sub(r'\x94', '"', text)
                text = re.sub(r'\x97', ' ', text)
                hit.append(text)

            for item in bs.find_all(string=re.compile('compensation', re.I)):
                text = unicodedata.normalize("NFKD", item)
                text = html.unescape(text)
                #text=UnicodeDammit(text, ["windows-1252"], smart_quotes_to="html").unicode_markup
                text = re.sub(r'\n', ' ', text)
                text = re.sub(r'\x92', "'", text)  # \x92
                text = re.sub(r'\x93', '"', text)
                text = re.sub(r'\x94', '"', text)
                hit.append(text)

            if hit != []:
                fileList.append(proxy)
                hitList.append(hit)
        #result={'file': proxy, 'text': hit}
        # resultDict.update(result)
        # hitList=list(set(hitList))
    return fileList, hitList

# 3.


def NER2(iterable):
    """NER() processes texts within a list of texts, compared with ner() that processes merged texts.
    NER2() combines NER() and choose_CC_sentence()"""

    CC_set = set()
    sent_set = set()
    #sent_list = []
    for item in iterable:
        doc = nlp(item)
        for sent in doc.sents:
            if 'consultant' in [token.text.lower() for token in sent]:
                for ent in sent.ents:
                    if ent.label_ == "CC":
                        print(ent.text)
                        CC_set.add(ent.text.upper())
                        sent_set.add(str(sent.text).strip())
                        # sent_list.append(str(sent.text).strip())
            elif 'committee' in [token.text.lower() for token in sent]:
                for ent in sent.ents:
                    if ent.label_ == "CC":
                        print(ent.text)
                        CC_set.add(ent.text.upper())
                        sent_set.add(str(sent.text).strip())
                        # sent_list.append(str(sent.text).strip())
    return CC_set, sent_set  # , sent_list

# 4.


def extract_firm_info(file_name):
    import re
    regex = re.compile(
        r"f:\\(.*)\\(\d+).*(\d\d\d\d)-\d\d-\d\d(-\d\d)?\.html", re.IGNORECASE)
    firm = regex.search(r'{}'.format(file_name)).group(1)
    cik = regex.search(r'{}'.format(file_name)).group(2)
    year = regex.search(r'{}'.format(file_name)).group(3)
    try:
        tic = str(idDict[cik]).upper()
    # myterious error NEWS CORP 2014 1564708 NWS
    except:
        tic = None
    if tic == "NWS":
        tic = None
    return firm, year, cik, tic

# 5.


def make_uppercase(df_cell):

    l = list(df_cell)
    for item in l:
        item = re.sub(r'george.*paulin', 'COOK', item, flags=re.I)
        item = re.sub(r'john.*england', 'TOWERS PERRIN', item, flags=re.I)
        # print(str(df['year'])) # df implicitly looks at the column of the same row.
        if jellyfish.jaro_similarity(item, str(firm_df['firm'])) > .7:
            l.remove(item)
            print(item, "removed for its similarity with firmName")
        elif jellyfish.jaro_similarity(item, str(firm_df['tic'])) > .8:
            l.remove(item)
            print(item, "removed for its similarity with ticker")
        elif item in str(firm_df['firm']):
            l.remove(item)
            print(item, "removed because it contains the firmname")
        elif item.isnumeric():
            l.remove(item)
            print(item, "removed because it is only a number")
        elif item == "RSU":
            l.remove(item)
        elif item.endswith('PLAN'):
            l.remove(item)
        elif item == 'INDEPENDENT COMPENSATION CONSULTANT':
            l.remove(item)
        elif item == "INDEPENDENT COMPENSATION":
            l.remove(item)
        elif item == 'THE COMPENSATION CONSULTANT':
            l.remove(item)
        elif item == 'PSU':
            l.remove(item)
        elif item == 'PSUs':
            l.remove(item)
        elif item == 'RSU':
            l.remove(item)
        elif item == 'RSUs':
            l.remove(item)

    return set(l)

    # 6.


def remove_duplicates(iterable):
    """1. checks string similarity
       2. creates combinations
       3. replaces strings"""

    import re
    import jellyfish
    import itertools
    l = list(iterable)
    # if len(l)>5:
    # return set(l)
    # elif len(l)==1:
    # return l

    combo = itertools.combinations(l, 2)  # create combinations of 2
    for item in combo:
        print(item)
        if jellyfish.jaro_similarity(item[0], item[1]) > .7:
            if len(item[0]) < len(item[1]):
                try:
                    l.remove(item[1])
                except:
                    pass
            else:
                try:
                    l.remove(item[0])
                except:
                    pass

    set2 = {re.sub(r'(Frederic)?\.?\s*W?\.?\s*Cook\s*&\s*Co\.?,?\s*(Inc)?\.?',
                   "COOK", i, flags=re.I) for i in l}
    set3 = {re.sub(r'F\.?\s*W\.?\s*Cook', "COOK", i, flags=re.I) for i in set2}
    return set3


def process(dir):
    os.chdir(dir)
    # os.getcwd()
    proxies = find_proxies(dir)
    data = {}
    pathList = []
    for i in proxies:
        filePath = os.path.join(dir, i)
        print(filePath)
        pathList.append(filePath)  # create a list of file paths.
    if pathList == []:
        print('No DEF 14A in the folder')
        return 0
    else:
        filename, text = open_proxy1(pathList)
        data.update({'file_name': filename, 'text': text})
        firm_df = pd.DataFrame.from_dict(data)
        # create columns with firm info
        from tqdm.auto import tqdm
        # df.iterrows() will iterate each row
        for i, row in tqdm(firm_df.iterrows(), total=len(firm_df)):
            # row['column name'] to select certain column within a row
            filename = str(row["file_name"])
            #print('filename is', filename)
            firm, year, cik, tic = extract_firm_info(filename)
            # then, create a new column that contains the result of the operation.
            firm_df.at[i, "firm"] = firm
            firm_df.at[i, 'year'] = year
            firm_df.at[i, 'cik'] = cik
            firm_df.at[i, 'tic'] = tic

        firm_df['result'] = firm_df['text'].apply(NER2)
        firm_df['CC'] = firm_df['result'].apply(lambda x: x[0])
        firm_df['CC_sentence'] = firm_df['result'].apply(lambda x: x[1])

        return firm_df


def process2(firm_df):

    firm_df['CC1'] = firm_df['CC'].apply(make_uppercase)
    firm_df['CC2'] = firm_df['CC1'].apply(remove_duplicates)
    firm_df.drop(columns=['result'])

    return firm_df


############
# execution
############
for i, dir in enumerate(P_pathList):
    print('\n\n\nThe index # is', i+int(startRange))
    print(dir)
    firm_df = process(dir)
    try:
        if firm_df == 0:
            continue
    except:
        if firm_df.empty:
            continue
    firm_df = process2(firm_df)
    df = pd.concat([df, firm_df])

# reodrdering
column_order = ["firm", "year", 'cik', 'tic', 'text',
                'CC2', 'CC_sentence', 'CC', 'CC1', "file_name"]
df = df.reindex(columns=column_order)

# set index
df.set_index(['cik', 'year'], inplace=True)

# serializing
os.chdir(r'C:\Users\KWan\Documents\NLP & ML\compensation consultant')

df.to_pickle(f"CC_df_{startRange}-{endRange}.pkl")
print(f'NER for {startRange}-{endRange} completed.')
