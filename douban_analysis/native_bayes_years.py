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
    ['2016_text', '2016'],
    ['2017_text', '2017'],
    ['2018_text', '2018'],
    ['2019_text', '2019'],
    ['2020_text', '2020']
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


def zhexian(input_values, squares):
    # input_values = [2016, 2017, 2018, 2019, 2020]
    # squares = [0.87, 0.57, 0.31, 0.90, 0.55]
    print('start generate picture.....')
    plt.plot(input_values, squares, 'o-',label=u"线条")

    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=20) 
    #设置图表标题，并给坐标轴加上标签
    plt.title("影评各年份好评率统计", fontproperties=font1)
    plt.xlabel("年份", fontproperties=font1)
    plt.ylabel("好评率", fontproperties=font1)

    #设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)
    plt.axhline(0.7,linewidth=0)
    for a,b in zip(range(len(squares)),squares):
        plt.text(a, b+0.05, '%.4f' % b, ha='center', va= 'bottom',fontsize=10)
    plt.savefig("./data/nianfen1.png")
    plt.show()



if __name__ == "__main__":
    analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)
    input_values, squares = get_test(analyzer)
    zhexian(input_values, squares)