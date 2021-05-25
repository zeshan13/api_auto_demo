#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : base_api.py
# 多协议支持、协议变更、切换不同的http库
import json
import logging
import requests

logging.basicConfig(level=logging.INFO)


class BaseApi:
    def request(self, request: dict):
        if "url" in request:
            return self.http_requsests(request)
        if "rpc" == request.get("protocol"):
            self.rpc_requests(request)

    def http_requsests(self, request):
        # request = {
        #     "protocol":"http",
        #     "url":"",
        #     "params":{},
        #     "method":"",
        #     "json":{}
        #
        # }
        r = requests.request(**request)
        logging.info("request:%s response:%s" % (request, json.dumps(r.json())))
        return r

    def rpc_requests(self, request):
        pass

    def socket_requests(self):
        pass
