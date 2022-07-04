# -*- coding: UTF-8 -*-
'''
@Time: 2021/11/3 20:05
@author: nicole1010
'''

import yaml
import os
import os.path
import configparser
import json
from urllib.parse import urlencode
import urllib

class FileTool():

    def path(self, filepath):
        """
        :param filepath:
        :return:返回绝对路径
        """
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )
        fpath = PATH(filepath)
        return fpath

    def load_yaml(self, filepath):
        """
        读取 yaml 文件
        :param logpath:
        :return:
        """
        try:
            yamldata = yaml.safe_load(open(filepath, "rb"))
            return yamldata
        except Exception as e:
            print(e)

    def yaml_to_list(self, filepath):
        """
        :param filepath:
        :return: 返回列表
        """
        alertList = []
        data = self.load_yaml(filepath)
        for v in data.values():
            alertList.append(list(filter(None, v)))
        return alertList


    def get_yaml_value(self, filepath, k, k1):
        """
        获取以 k:{k1: v1, k2: v2, ...}格式存储的值
        :param self:
        :param filepath:
        :param k:
        :param k1:
        :return:
        """
        yamldata = self.load_yaml(filepath)
        v = yamldata.get(k)
        for item in v:
            v1 = item.get(k1)
            return v1

    def get_yaml_value_path(self, filepath, k, k1):
        """
        获取以 k:{k1: v1, k2: v2, ...}格式存储的值
        :param self:
        :param filepath:
        :param k:
        :param k1:
        :return:
        """
        yamldata = self.load_yaml(filepath)
        v = yamldata.get(k)
        for item in v:
            v1 = item.get(k1)
            v1 = self.path(v1)
            return v1

    def set_yaml_value( self, filepath, k,  keyname, setvalue):
        """
        修改以 k:{k1: v1, k2: v2, ...}格式存储的值
        :param filepath:
        :param k:
        :param keyname:
        :param setvalue:
        :return:
        """
        yamldata = self.load_yaml(filepath)
        v = yamldata[k]
        for item in v:
            if keyname in item.keys():
                item['keyname'] = setvalue
                return item['keyname']


    def get_yaml_node_value(self, filepath, k):
        """
        获取以 k:{k1: v1, k2: v2, ...}格式存储的整个节点的值
        :param filepath:
        :return:
        """
        yamldata = self.load_yaml(filepath)
        value = yamldata.get(k)
        return value

    def open_ini(self, logpath):
        """
        读取 ini 文件
        :param logpath:
        :return:
        """
        config = configparser.ConfigParser()
        config.read(logpath)
        return config

    def get_log_args(self, logpath):
        """
        获取 ini 里 args 的值
        :param logpath:
        :return:
        """
        config = self.open_ini(logpath)
        args = config.get('handler_file', 'args')
        return args

    def get_common_path(self):
        """
        仅testcase中的脚本需要使用
        """
        pathList = [
            "../data/yaml/common.yaml",
            "../../../../data/yaml/common.yaml"
        ]
        for path in pathList:
            if self.whether_path_exists(path):
                return self.path(path)

    def whether_path_exists(self, path) -> object:
        """
        判断 path 是否存在，返回true or false
        """
        return os.path.exists(self.path(path))

    def load_json(self, jsonpath):
        """
        读json文件
        """
        with open(jsonpath, "r") as f:
            jsondata = json.load(f)
        return jsondata

    def get_json_value(self, jsonpath, url):
        """
        获取json中，特定key的值
        """
        jsondata = self.load_json(jsonpath)
        value = jsondata.get(url)
        return value

    def del_dict_keys(self, dict, key):
        """
        删除字典元素，返回删除后的新字典
        """
        if key in dict:
            del dict[key]
        return dict

    def get_dict_value(self, list, key):
        """
        在列表中获取字典特定key的值
        """
        for data in list:
            val = data.get(key)
            return val

    def get_url_host(self, url):
        """
        获取url中"?"之前的链接
        """
        url = url.split("?")[0]
        return url

    def get_url_params(self, url):
        """
        获取url中"?"之后的参数，返回字典格式
        """
        params = url.split("?")[1]
        plist = params.split("&")
        dict_temp = {}
        for id in plist:
            k = id.split("=")[0]
            v = id.split("=")[1]
            if v.isdigit():
                v = int(v)
            dict_temp[k] = v
        return dict_temp

    def clear_file(self, filepath):
        """
        清空文本内容
        """
        with open(filepath, 'r+') as f:
            f.truncate()

    def delete_file(self, filepath):
        """
        删除文件
        :param filepath:
        :return:
        """
        file = self.whether_path_exists(filepath)
        if file:
            os.remove(self.path(filepath))

    def sys_cmd(self, cmd):
        """
        执行cmd命令
        :param cmd:
        :return:
        """
        os.system(cmd)

    def checkout(self, filepath):
        """
        已提交到远端的调试用文件，提交前checkout
        :param filepath:
        :return:
        """
        fpath = self.path(filepath)
        self.sys_cmd(f"git checkout {fpath}")

    def urlencoded_to_json(self, str):
        """
        application/x-www-form-urlencoded 转换成 application/json
        :param str:  flow.requests.get_text
        :return:
        """
        parsed_result = {}
        for name, value in urllib.parse.parse_qsl(str):
            parsed_result[name] = value
        return parsed_result

    def create_file(self, relative_path):
        """
        如果文件不存在，自动创建文件
        :param relative_path:
        :return:
        """
        filepath = self.path(relative_path)
        if not self.whether_path_exists(filepath):
            file = open(filepath, 'a+')
            file.close()