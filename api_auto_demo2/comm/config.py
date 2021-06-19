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
COMMCFG.BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin"
COMMCFG.EXTERNALCONTACT = COMMCFG.BASE_URL + "/externalcontact"
COMMCFG.USER = COMMCFG.BASE_URL + "/user"
COMMCFG.DEPARTMENT = COMMCFG.BASE_URL + "/department"
COMMCFG.GETTOKEN = COMMCFG.BASE_URL + "/gettoken"
COMMCFG.CORPID = "wwf995b72179c58238"
COMMCFG.EXTERNALCONTACT_CORPSECRET = "NY-jWNzfPVJ_bFubS90JFLc8J6pr8XFITL0nyM_esMA"
COMMCFG.CONTACT_CORPSECRET = "FQZw5GqJUV9HKq5EAy9lK1Dvrgs7-LaUszFH1Hfqb4c"
