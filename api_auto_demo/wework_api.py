#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : wework_api.py
import json
import logging
import requests

logging.basicConfig(level=logging.INFO)


class WeWorkApi:
    _BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin"
    _GETTOKEN_URL = _BASE_URL + "/gettoken"
    _GET_CORP_TAG_LIST_URL = _BASE_URL + "/externalcontact/get_corp_tag_list"
    _ADD_CORP_TAG_URL = _BASE_URL + "/externalcontact/add_corp_tag"
    _DEL_CORP_TAG_URL = _BASE_URL + "/externalcontact/del_corp_tag"
    _CORPID = "XXXXXXXXXXX"
    _CORPSECRET = "XXXXXXXXXXX"

    def __init__(self, token=None):
        self.token = token
        if self.token == None:
            params = {
                "corpid": self._CORPID,
                "corpsecret": self._CORPSECRET
            }
            res = requests.get(url=self._GETTOKEN_URL, params=params)
            logging.info("url:%s ,params:%s response:%s" % (self._GETTOKEN_URL, params, json.dumps(res.json())))
            self.token = res.json()["access_token"]

    def get_corp_tag(self):
        params = {
            "access_token": self.token
        }
        res = requests.post(url=self._GET_CORP_TAG_LIST_URL, params=params)
        logging.info("url:%s ,params:%s response:%s" % (self._GET_CORP_TAG_LIST_URL, params, json.dumps(res.json())))

        return res

    def add_corp_tag(self, json_datas):
        params = {"access_token": self.token}
        res = requests.post(url=self._ADD_CORP_TAG_URL, params=params, json=json_datas)
        logging.info("url:%s ,params:%s ,json_datas %s ，response:%s" % (
            self._ADD_CORP_TAG_URL, params, json_datas, json.dumps(res.json())))
        return res

    def del_corp_tag(self, json_datas):
        params = {"access_token": self.token}
        res = requests.post(url=self._DEL_CORP_TAG_URL, params=params, json=json_datas)
        logging.info("url:%s ,params:%s ,json_datas %s ，response:%s" % (
            self._DEL_CORP_TAG_URL, params, json_datas, json.dumps(res.json())))
        return res
