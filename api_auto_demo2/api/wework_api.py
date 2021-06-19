#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : wework_api.py
# 封装企业微信通用方法

import logging
from api_auto_demo.api_auto_demo2.api.base_api import BaseApi

logging.basicConfig(level=logging.INFO)
from ..comm import config

cfg = config.COMMCFG


class WeWorkApi(BaseApi):

    def get_token(self, ):
        data = {
            "method": "get",
            "url": cfg.GETTOKEN,
            "params": {
                "corpid": cfg.CORPID,
                "corpsecret": cfg.CORPSECRET
            }
        }
        res = self.request(data)

        return res.json()["access_token"]
