import requests
import json


# sp=requests.get("http://api.k780.com/?app=weather.today&weaid=1&appkey=APPKEY&sign=SIGN&format=json")
# print(sp.text)

headers={
    "Content-Type":"application/json"
}
datas={
    "msgtype":"news",
    "news":{
        "articles":[
        {"title":"大鸟转转转酒吧0",
        "description":"酒吧前台消息",
        "url":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4232317840,3112508633&fm=11&gp=0.jpg",
        "picurl":"https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2853553659,1775735885&fm=26&gp=0.jpg"
        },
        {"title":"大鸟转转转酒吧1",
        "description":"酒吧前台消息",
        "url":"https://www.baidu.com",
        "picurl":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4232317840,3112508633&fm=11&gp=0.jpg"
        },
        {"title":"大鸟转转转酒吧2",
        "description":"酒吧前台消息",
        "url":"https://www.baidu.com",
        "picurl":"https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=4232317840,3112508633&fm=11&gp=0.jpg"
        }
        
        ]
    }
}

# datas={
#     "msgtype":"text",
#     "text":{
#        "content":"群消息测试",
#        "mentioned_list":["@all"]
       
#         }
        
#     }

s=requests.post("https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=",headers=headers,data=json.dumps(datas))    
#key位置填入你的key
print(s.text)