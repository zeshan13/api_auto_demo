#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zeshan
# @File    : miitmproxy_map_local.py

# https://docs.mitmproxy.org/
import json
# pip install mitmproxy==5.2
import mitmproxy.http

class Events:

    def recursion(self,base_data):
        #
        if isinstance(base_data, dict):
            #
            for k, v in base_data.items():
                # 如果key值为name，修改value值
                if k == "name":
                    base_data[k] = "周耳朵测试"
                else:
                    base_data[k] = self.recursion(v)
        elif isinstance(base_data, list):
            #list继续遍历
            base_data = [self.recursion(i) for i in base_data]
        elif isinstance(base_data, float):
            # 浮点数类型修改测试
            base_data = 9999999999999999.00
            # pass
        else:
            base_data = base_data

        return base_data

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        # 实现rewrite，重写响应数据信息
        # if 条件代表匹配规则
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            # 修改响应数据：读取json文件数据，赋值给data
            with open("./quote.json",encoding="utf-8") as f:
                data = f.read() #str类型
            # data重新赋值给flow.response.text
            flow.response.text = data

# 将event事件加到插件中
addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump
    #使用debug模式启动mitmdump
    mitmdump(['-p', '8006', '-s', __file__])

