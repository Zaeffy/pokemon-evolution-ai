from __future__ import print_function
import os
import time
from re import search
from json import dump
from requests import get


class Retriever(object):

    def __init__(self, t):
        self._type = t
        self._list = []

    @staticmethod
    def _retrieve(url):
        try:
            ret = get(url).json()
        except:  # This should never happen except if the API is down - don't try to manage it, just ignore
            print("Error retrieving url " + url)
            return None
        time.sleep(1)  # Sleeping here to avoid spamming the API - we don't need to get everything that fast
        return ret

    @staticmethod
    def extract_id(url, t):
        result = search("/" + t + "/([0-9]+)/", url)
        return int(result.group(1))

    def retrieve_full_list(self):
        objects = Retriever._retrieve('https://pokeapi.co/api/v2/' + self._type + '/?limit=100')
        i = 0
        while "There is a next page":
            print("Retrieving " + self._type + " page " + str(i + 1) + "/" + str(int(objects['count'] / 100) + 1))
            i = i + 1
            for obj in objects['results']:
                formatted = self._retrieve_single(obj['url'])
                if formatted is not None:
                    self._list.append(formatted)
            if objects['next']:
                objects = self._retrieve(objects['next'])
            else:
                break

    def write(self):
        filename = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "data", self._type + ".json"))
        with open(filename, "w+") as fp:
            dump(self._list, fp)

    def retrieve(self):
        self.retrieve_full_list()
        self.write()

    def _format_object(self, json):
        raise NotImplementedError

    def _retrieve_single(self, url):
        obj = Retriever._retrieve(url)
        if obj is None:
            return None
        return self._format_object(obj)
