#!/usr/bin/python
# -*- coding: UTF-8 -*-
# zip -q -r -e -m -o [yourName].zip someThing
import os
import subprocess
import time
from os.path import dirname, abspath
from jinja2 import PackageLoader, Environment

ROOT = abspath(dirname(__file__))
env = Environment(loader=PackageLoader(os.path.split(ROOT)[-1], 'templates'))

demoPath = ROOT + "/templates/"
demoPro = "{module}"
cuModuleName = "jingxuan"
cuProjectName = "log"


def firstUpper(name):
    return name[0].capitalize() + name[1:]


config = {
    "module": cuModuleName,
    "Module": firstUpper(cuModuleName),
    "project": cuProjectName,
    "module_project": cuModuleName+"-"+cuProjectName,
    "ModuleProject": firstUpper(cuModuleName)+firstUpper(cuProjectName),

}


def copyPro(moduleName="module"):
    return "cd {0} && rm -rf {2}* && cp -R  {1} {2}".format(demoPath, demoPro, moduleName)


def zipFIle(moduleName="module"):
    return "zip -q -r {0}.zip {0}".format(moduleName)


def rename(path):
    for moduleDir in os.listdir(path):
        os.chdir(path)
        pathName = moduleDir.replace("{module}", cuModuleName).replace("{project}", cuProjectName) \
            .replace("{ModuleProject}", config.get("ModuleProject"))
        if "{module}" in moduleDir or "{project}" in moduleDir:
            os.rename(moduleDir, pathName)
        if os.path.isdir(os.path.join(path, pathName)):
            rename(path + "/" + pathName)
        else:
            if moduleDir.endswith("tpl"):
                tplPath = os.path.join(path, moduleDir).replace(demoPath, "")
                template = env.get_template(tplPath)
                html = template.render(config)
                save_dir = os.path.join(path, moduleDir). \
                    replace(".tpl", "").replace("{Module}", config.get("Module"))\
                    .replace("{ModuleProject}", config.get("ModuleProject"))
                with open(save_dir, "wb+") as fp:
                    fp.write(html.encode("utf-8"))
                os.remove(os.path.join(path, moduleDir))


def gen_tpl(modulename, projectName):
    global cuModuleName
    cuModuleName = modulename
    global cuProjectName
    cuProjectName = projectName
    result = subprocess.Popen(copyPro(cuModuleName+"-"+cuProjectName), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    print(result)
    time.sleep(0.5)

    rename(demoPath + cuModuleName+"-"+cuProjectName)
    os.chdir(demoPath)
    subprocess.Popen(zipFIle(cuModuleName+"-"+cuProjectName), stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
