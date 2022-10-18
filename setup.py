#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  setup.py
@Time    :  2022/08/31 15:53:21
@Author  :  LiuKeCode
@Desc    :  None
====================================
"""
# here put the import lib

import os
from setuptools import setup, find_packages

with open(
        os.path.join(os.path.dirname(__file__), "requirements.txt"), "r"
) as fh:
    requirements = fh.readlines()

NAME = "qywechat"
DESCRIPTION = (
    "This is a msg-robot for qywechat."
)
AUTHOR = "LiuKe"
URL = "https://github.com/liukecode/qywechat"
VERSION = None

about = {}

with open("README.md", "r", encoding="UTF-8") as fh:
    about["long_description"] = fh.read()

root = os.path.abspath(os.path.dirname(__file__))

if not VERSION:
    with open(os.path.join(root, "qywechat", "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    license="MIT",
    description=DESCRIPTION,
    long_description=about["long_description"],
    long_description_content_type="text/markdown",
    author=AUTHOR,
    maintainer="Liuke",
    url=URL,
    keywords=["wechat", "qywechat", "weixin", "qyweixin", "wecom", "api", "bot", "robot"],
    install_requires=[req for req in requirements],
    packages=find_packages(exclude=("tests",)),
    package_data={'': ['*.yaml'], },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Communications",
        "Topic :: Office/Business",
    ],
    python_requires=">=3.7",
)
