#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : config.py
class ConstError(Exception): pass


class _const(object):
    def __setattr__(self, k, v):
        if k in self.__dict__:
            raise ConstError
        else:
            self.__dict__[k] = v


COMMCFG = _const()
COMMCFG.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
COMMCFG.externalcontact = COMMCFG.base_url + "/externalcontact"
COMMCFG.user = COMMCFG.base_url + "/user"
COMMCFG.department = COMMCFG.base_url + "/department"
COMMCFG.gettoken = COMMCFG.base_url + "/gettoken"
COMMCFG.corpid = "XXXXXXXX"
COMMCFG.corpsecret = "XXXXXXXX"
