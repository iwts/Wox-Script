# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import socket
import pyperclip

# 主逻辑方法
def main_function():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip

class Main(Wox):
    def query(self, query):
        ip = main_function()
        
        results = list()
        results.append({
            "Title": ip,
            "SubTitle": "click can copy",
            "IcoPath": "Images/ico.ico",
            "JsonRPCAction": {
                "method": "copy",
                "parameters": [ip],
                "dontHideAfterAction": False
            }
        })
        return results

    # 允许copy
    def copy(self, keyword):
        pyperclip.copy(keyword)


if __name__ == "__main__":
    Main()