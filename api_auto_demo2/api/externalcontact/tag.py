#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : externalcontact.py
from api_auto_demo.api_auto_demo2.comm import config
from ..wework_api import WeWorkApi

cfg = config.COMMCFG


class Tag(WeWorkApi):
    _get_corp_tag_list_url = cfg.externalcontact + "/get_corp_tag_list"
    _add_corp_tag_url = cfg.externalcontact + "/add_corp_tag"
    _del_corp_tag_url = cfg.externalcontact + "/del_corp_tag"

    def get_corp_tag(self):
        data = {
            "method": "get",
            "url": self._get_corp_tag_list_url,
            "params": {
                "access_token": self.get_token()
            }
        }

        return self.request(data)

    def add_corp_tag(self, tag_list, group_name, **kwargs):
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                'group_name': group_name,
                'tag': tag_list
            }

        data = {
            "method": "post",
            "url": self._add_corp_tag_url,
            "params": {
                "access_token": self.get_token()
            },
            "json": json_data
        }
        return self.request(data)

    def del_corp_tag(self, tag_id_list=None, **kwargs):
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {'tag_id': tag_id_list}
        data = {
            "method": "post",
            "url": self._del_corp_tag_url,
            "params": {
                "access_token": self.get_token()
            },
            "json": json_data
        }
        return self.request(data)

    def clear_all_tags(self):
        r = self.get_corp_tag().json()
        tag_id_list = [j["id"] for i in r["tag_group"] for j in i["tag"]]
        self.del_corp_tag(tag_id_list=tag_id_list)
