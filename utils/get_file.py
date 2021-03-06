# coding = utf-8
"""
@File     :  get_file.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/30  3:07
"""

import yaml
import sys

sys.path.append('..')


class GetFile:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = r'/ui_framework/xueqiu_app/datas\caps.yaml'
        else:
            self.file_path = file_path
        self.data = self.get_yaml()

    def get_yaml(self):
        data = yaml.safe_load(open(str(self.file_path), 'r', encoding='utf-8'))
        return data

    # 传入key获取value
    def get_value(self, *args):

        try:
            value = self.data.get(*args)
        except EOFError:
            value = None
        return value


if __name__ == '__main__':
    run = GetFile()
    print(run.get_yaml())
    # print(run.get_value('add')['datas'])
