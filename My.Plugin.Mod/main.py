# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import socket
import pyperclip

# 主逻辑方法
def main_function(query):
    nums = query.split("%")
    answer = int(nums[0]) % int(nums[1])
    return answer

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