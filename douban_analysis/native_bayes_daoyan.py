# -*- coding: utf-8 -*-
from native_bayes_sentiment_analyzer import SentimentAnalyzer
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sql import Mysql_Control


model_path = './data/bayes.pkl'
userdict_path = './data/userdict.txt'
stopword_path = './data/stopwords.txt'
corpus_path = './data/review.csv'

Data = [
    ['zhangyimou_text', '张艺谋'],
    ['fengxiaogang_text', '冯小刚'],
    ['zhouxingchi_text', '周星驰'],
    ['xuke_text', '徐克'],
    ['chenkaige_text', '陈凯歌']
]

def get_test(analyzer):
    # text = '倍感失望的一部诺兰的电影，感觉更像是盗梦帮的一场大杂烩。虽然看之前就知道肯定是一部无法超越前传2的蝙蝠狭，但真心没想到能差到这个地步。节奏的把控的失误和角色的定位模糊绝对是整部影片的硬伤。'
    mysqls = Mysql_Control()
    xx = []
    yy = []
    for data in Data:
        print("{} start.....".format(data[1]))
        ret = mysqls.select_db(data[0])
        xx.append(data[1])
        texts = []
        for id in ret:
            texts.append(id[0])
        pos = 0.0
        all = 0.0
        for text in texts:
            b = analyzer.analyze(text=text)
            if b >= 0.5:
                pos = pos + 1
            all = all + 1
        yy.append(pos/all)
        print("{} finish.....result = {}".format(data[1], pos/all))
    return xx, yy


def zhuxing(name_list, num_list):
    # name_list = ['喜剧', '悬疑', '历史' ,'科幻', '武侠']
    # num_list = [0.87, 0.57, 0.31, 0.90, 0.55]

    plt.bar(range(len(num_list)), num_list,tick_label=name_list)

    font1 = FontProperties(fname=r"C:/Windows/Fonts/simfang.ttf",size=20) 
    #设置图表标题，并给坐标轴加上标签
    plt.title("影评导演作品好评率统计", fontproperties=font1)
    plt.xlabel("导演", fontproperties=font1)
    plt.ylabel("好评率", fontproperties=font1)
    plt.xticks(fontproperties=font1)
    plt.axhline(0.8,linewidth=0)
    for a,b in zip(range(len(num_list)),num_list):
        plt.text(a, b+0.05, '%.4f' % b, ha='center', va= 'bottom',fontsize=10)
    plt.savefig("./data/daoyan1.png")
    plt.show()



if __name__ == "__main__":
    analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)
    name_list, num_list = get_test(analyzer)
    zhuxing(name_list, num_list)