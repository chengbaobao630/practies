#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from os.path import dirname, abspath
import subprocess
import time
from jinja2 import PackageLoader, Environment


ROOT = abspath(dirname(__file__))
env = Environment(loader=PackageLoader(ROOT, 'templates'))

demoPath = "/Users/chengcheng/develop/java/pro/"
demoPro = "{module}"
cuModuleName = "hehda"


def copyPro(moduleName="module"):
    return "cd {0} && rm -rf {2} && cp -R  {1} {2}".format(demoPath, demoPro, moduleName)


result = subprocess.Popen(copyPro(cuModuleName), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

time.sleep(0.5)


def rename(path):
    for moduleDir in os.listdir(path):
        os.chdir(path)
        if "{module}" in moduleDir:
            os.rename(moduleDir, moduleDir.replace("{module}", cuModuleName))
        if os.path.isdir(os.path.join(path, moduleDir.replace("{module}", cuModuleName))):
            rename(path+"/"+moduleDir.replace("{module}", cuModuleName))
        else:
            if "{Module}" in moduleDir and moduleDir.endswith("tpl"):
                template = env.get_template("./test.html")
                html = template.render({"config": config})
                print("hehda")


rename(demoPath+cuModuleName)
