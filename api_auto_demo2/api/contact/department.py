#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : department.py
from api_auto_demo.api_auto_demo2.comm import config
from ..wework_api import WeWorkApi

CFG = config.COMMCFG


class Department(WeWorkApi):
    _create_department_url = CFG.DEPARTMENT + "/create"
    _get_department_list_url = CFG.DEPARTMENT + "/list"
    _update_department_url = CFG.DEPARTMENT + "/update"
    _delete_department_url = CFG.DEPARTMENT + "/delete"

    def __init__(self, corpid=CFG.CORPID, corpsecret=CFG.CONTACT_CORPSECRET):
        WeWorkApi.__init__(self, corpid, corpsecret)
        self.corpid = corpid
        self.corpsecret = corpsecret

    def get_department_list(self, id=None):
        data = {
            "method": "get",
            "url": self._get_department_list_url,
            "params": {
                "access_token": self.get_token()
            }
        }
        if id:
            data["params"]["id"] = id

        return self.request(data)

    def create_department(self, name, parentid, **kwargs):
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                'name': name,
                'parentid': parentid
            }

        data = {
            "method": "post",
            "url": self._create_department_url,
            "params": {
                "access_token": self.get_token()
            },
            "json": json_data
        }
        return self.request(data)

    def update_department(self, id, name, **kwargs):
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                'id': id,
                "name": name
            }

        data = {
            "method": "post",
            "url": self._update_department_url,
            "params": {
                "access_token": self.get_token()
            },
            "json": json_data
        }
        return self.request(data)

    def delete_department(self, id):
        data = {
            "method": "get",
            "url": self._delete_department_url,
            "params": {
                "access_token": self.get_token(),
                "id": id
            },
        }
        return self.request(data)

    def clear(self):
        r = self.get_department_list()
        id_list = [department["id"] for department in r.json()["department"]]
        for id in id_list:
            self.delete_department(id)
