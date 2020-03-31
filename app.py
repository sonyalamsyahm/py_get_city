from configparser import ConfigParser
from pymongo import MongoClient
from pprint import pprint
from provinces_and_cities import cities, provinces
from time import sleep

config = ConfigParser()
config_path = 'config.ini'
config.read(config_path)

client = config['MongoClient']
db_server = MongoClient(client['client'])
db_col = db_server[client['dbs']]
ori_data = db_col[client['ori_data']]


news = ori_data.find({'source': {'$nin': ['telegram', 'instagram','facebook', 'twitter']}})

for data in news:
    words = []
    for x in cities:
        if x in data['text'].title():
            words.append(x)
    for x in provinces:
        if x in data['text'].title():
            words.append(x)
    new_words = list(dict.fromkeys(words))
    print(new_words)
    print(data['text'])
