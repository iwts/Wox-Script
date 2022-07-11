# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import time
import pyperclip

# 主逻辑方法
def main_function(query):
    if query.isdigit():
        time_local = time.localtime(int(query))
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return timestamp
    else:
        timeArray = time.strptime(query, "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(timeArray)
        return int(timestamp)

class Main(Wox):
    def query(self, query):
        answer = main_function(query)
        
        results = list()
        results.append({
            "Title": answer,
            "SubTitle": "click can copy",
            "IcoPath": "Images/ico.ico",
            "JsonRPCAction": {
                "method": "copy",
                "parameters": [answer],
                "dontHideAfterAction": False
            }
        })
        return results

    # 允许copy
    def copy(self, content):
        pyperclip.copy(content)


if __name__ == "__main__":
    Main()