#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : user.py
from api_auto_demo.api_auto_demo2.comm import config
from .department import Department
from ..wework_api import WeWorkApi

CFG = config.COMMCFG


class User(WeWorkApi):
    _create_member_url = CFG.USER + "/create"
    _get_member_url = CFG.USER + "/get"
    _update_member_url = CFG.USER + "/update"
    _delete_member_url = CFG.USER + "/delete"
    _batchdelete_member_url = CFG.USER + "/batchdelete"
    _simplelist_url = CFG.USER + "/simplelist"

    def __init__(self, corpid=CFG.CORPID, corpsecret=CFG.CONTACT_CORPSECRET):
        WeWorkApi.__init__(self, corpid, corpsecret)
        self.corpid = corpid
        self.corpsecret = corpsecret

    def get_member(self, userid):
        data = {
            "method": "get",
            "url": self._get_member_url,
            "params": {
                "access_token": self.get_token(),
                "userid": userid
            }
        }

        return self.request(data)

    def simplelist(self, department_id, fetch_child=None):
        data = {
            "method": "get",
            "url": self._simplelist_url,
            "params": {
                "access_token": self.get_token(),
                "department_id": department_id
            }
        }
        if fetch_child:
            data["params"]["fetch_child"] = fetch_child

        return self.request(data)

    def create_member(self, userid, name, mobile, department_list, **kwargs):
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                'userid': userid,
                'name': name,
                'mobile': mobile,
                'department': department_list,
            }

        data = {
            "method": "post",
            "url": self._create_member_url,
            "params": {
                "access_token": self.get_token()
            },
            "json": json_data
        }
        return self.request(data)

    def update_member(self, userid, name, **kwargs):
        if 'json' in kwargs:
            json_data = kwargs['json']
        else:
            json_data = {
                'userid': userid,
                'name': name
            }

        data = {
            "method": "post",
            "url": self._update_member_url,
            "params": {
                "access_token": self.get_token()
            },
            "json": json_data
        }
        return self.request(data)

    def delete_member(self, userid):

        data = {
            "method": "get",
            "url": self._delete_member_url,
            "params": {
                "access_token": self.get_token(),
                "userid": userid
            }
        }
        return self.request(data)

    def batchdelete_member(self, useridlist):
        data = {
            "method": "get",
            "url": self._batchdelete_member_url,
            "params": {
                "access_token": self.get_token(),
                "useridlist": useridlist
            }
        }
        return self.request(data)

    def clear_members(self):
        r = self.simplelist(department_id=1, fetch_child=1)
        ureid_list = [userlist["userid"] for userlist in r.json()["userlist"]]
        for userid in ureid_list:
            if userid == "HuangZeShan":
                pass
            else:
                self.delete_member(userid)
