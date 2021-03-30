#!/user/bin/env python
# encoding: utf-8
"""
@author: zwnong
@project: HogwartsSDE17
@file: wework_address.py
@time: 2021/3/28 20:34
"""
# 不使用session
import requests


class WeworkAddress:
    """
    # 接口提速改良方案1：并发 多进程（资源消耗大） 辅组插件 pytest-dve/pytest-xdist 推荐使用 - n auto 原理：利用cpu逻辑处理器
    # 问题 进程之间资源不互通 使用文件锁（待研究）
    # 使用1：命令行 pytesy -n auto
    # pycharm设置 Edit configurations--》Additional Arguments 添加 -n auto
    # 接口提速改良2： 问题 不使用session 发送一次请求 就会获取一次token 相当于重复 每发送一次请求 握手ssl-->挥手ssl 100次就有100次握手ssl-->挥手ssl
    #               解决  使用requests的session 发送一次请求握手ssl 100次请求（用例）后 在进行挥手，只有一次 握手ssl-->挥手ssl
    # 使用：声明一个session session类里面有很多方法 他是重新封装了一套完整的requests请求
    # Session()和get()是一个并行关系 即 Session().get() = requests.get()
    # requests底层的方法也开启了session管理
    # 案例：在wework_address2.py
    """

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 企业id: corpid
        # 应用的凭证密钥：corpsecret 权限说明 接口使用范围，比如，同步通讯录的接口必须要用通讯录同步助手的access_token
        params = {"corpid": "wwb636abb767a13836",
                  "corpsecret": "dKM7tQH5rCf_PgLMZlMEoz3Zv-v2I4RNeDpWB71XM3c"
                  }

        r = requests.get(url, params=params)
        return r.json()['access_token']

    def parameterization_add_member(self, *args):
        """
        参数化时改进 添加成员
        :param args: args[0]为 user_id
        :param :args[0]为 user_id
        :param :args[0]为 user_id手机必须是11位
        :param :args[0]为 user_id
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        params = {
            "access_token": self.token
        }
        data = {
            "userid": args[0],
            "name": args[1],
            "mobile": f"+86 {args[2]}",
            "department": args[3]
        }
        r = requests.post(url, json=data, params=params)
        return r.json()

    def add_member(self, userid: str, name: str, phone: str, department: list):
        """
        添加成员
        :param userid:
        :param name:
        :param phone: 手机必须是11位
        :param department:
        :return:
        """
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        params = {
            "access_token": self.token
        }
        data = {
            "userid": userid,
            "name": name,
            "mobile": f"+86 {phone}",
            "department": department
        }
        r = requests.post(url, json=data, params=params)
        return r.json()

    def delete_member(self, userid):
        """
        删除成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={userid}"
        r = requests.get(url)
        return r.json()

    def update_member(self, userid: str, name: str = None, mobile: str = None):
        """
        修改成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
        }
        r = requests.post(url, json=data)
        return r.json()

    def get_info(self, userid):
        """
        查看成员
        :return:
        """
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={userid}"
        r = requests.get(url)
        return r.json()
