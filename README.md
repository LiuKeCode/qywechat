# QyWechat
[![GitHub issues](https://img.shields.io/github/issues/liukecode/qywechat)](https://github.com/liukecode/qywechat/issues)
[![GitHub forks](https://img.shields.io/github/forks/liukecode/qywechat)](https://github.com/liukecode/qywechat/network)
[![GitHub stars](https://img.shields.io/github/stars/liukecode/qywechat)](https://github.com/liukecode/qywechat/stargazers)
[![GitHub license](https://img.shields.io/github/license/liukecode/qywechat)](https://github.com/liukecode/qywechat/blob/main/LICENSE)
[![contributors](https://img.shields.io/github/contributors/liukecode/qywechat)](https://github.com/liukecode/qywechat/graphs/contributors)
[![PyPI](https://img.shields.io/pypi/v/qywechat)](https://pypi.org/project/qywechat/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/qywechat)](https://pypi.org/project/qywechat/)
[![Downloads](https://pepy.tech/badge/qywechat/month)](https://pepy.tech/project/qywechat)

This is a msg-robot for [qywechat](https://developer.work.weixin.qq.com/document/path/91770)

## Install
```
python -m pip install qywechat
```
## Getting Started
send text msg
```
import qywechat
key = "b8cxxx"
bot = qywechat.Bot(key)
data = {
    	"msgtype": "text",
    	"text": {
        	"content": "hello world"
    	}
   }
# @ user, all user
# data = {
#    "msgtype": "text",
#    "text": {
#        "content": "LiuKeTest Msg",
#		"mentioned_list":["liuke","@all"],
#		"mentioned_mobile_list":["13800001111","@all"]
#    }
#}
bot.send_msg(data)
```

send markdown msg
```
data = {
    "msgtype": "markdown",
    "markdown": {
        "content": "实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。\n
         >类型:<font color=\"comment\">用户反馈</font>
         >普通用户反馈:<font color=\"comment\">117例</font>
         >VIP用户反馈:<font color=\"comment\">15例</font>"
    }
}
```

send image
```
bot.img_msg("path/test.jpg")
```
send file
```
media_id = bot.upload_file("path/liuke.zip")
data = {
    "msgtype": "file",
    "file": {
 		"media_id": media_id
    }
}
bot.send_msg(data)
```

send image & text msg
```
data = {
    "msgtype": "news",
    "news": {
       "articles" : [
           {
               "title" : "LiuKeTest",
               "description" : "qywechat",
               "url" : "https://xxx",
               "picurl" : "http://xxx.png"
           }
        ]
    }
}
bot.send_msg(data)
```

## Features
- Support all types message
- Support send image
- Support upload file


## Contributing

Contributions are welcome.<br/>
If you've found a bug within this project, please open an issue to discuss what you would like to change.<br/>
If it's an issue with the API, please report any new issues at [qywechat issues](https://github.com/liukecode/qywechat)