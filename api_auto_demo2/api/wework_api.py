#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : wework_api.py
# 封装企业微信通用方法

import logging
from api_auto_demo.api_auto_demo2.api.base_api import BaseApi

logging.basicConfig(level=logging.INFO)
from ..comm import config

CFG = config.COMMCFG


class WeWorkApi(BaseApi):
    def __init__(self, corpid=CFG.CORPID, corpsecret=CFG.EXTERNALCONTACT_CORPSECRET):
        self.corpid = corpid
        self.corpsecret = corpsecret

    def get_token(self, ):
        data = {
            "method": "get",
            "url": CFG.GETTOKEN,
            "params": {
                "corpid": self.corpid,
                "corpsecret": self.corpsecret
            }
        }
        res = self.request(data)

        return res.json()["access_token"]
