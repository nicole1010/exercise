# -*- coding: UTF-8 -*-
"""
@Time: 2022/11/5 15:28
@author: nicole1010
"""
import requests
rank = "https://topic.kkmh.com/gamecard/v2/rank/get_rank_by_id?id=33&rankDisplayType=1&size=200"
res = requests.get(rank)
resjson = res.json()
ranklist = resjson.get("data").get("rankListData")
for item in ranklist:
    userName = item['userName']
    rank = item['rank']
    value = item['value']
    # if rank in [10, 30]:
    #     print(f"{userName} —— {rank} —— {value}\n")

    if userName in ["6枯蝶_残香_零叶", "是地主家的傻鹅子"]:
        print(f"{userName} —— {rank} —— {value}\n")




