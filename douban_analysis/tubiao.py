import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def zhexian(input_values, squares):
    input_values = [2016, 2017, 2018, 2019, 2020]
    squares = [0.87, 0.57, 0.31, 0.90, 0.55]
    plt.plot(input_values, squares, 'o-',label=u"线条")

    font1 = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=20) 
    #设置图表标题，并给坐标轴加上标签
    plt.title("影评各年份好评率统计", fontproperties=font1)
    plt.xlabel("年份", fontproperties=font1)
    plt.ylabel("好评率", fontproperties=font1)
    plt.axhline(0.8)
    for a,b in zip(range(len(squares)),squares):
        plt.text(a, b+0.05, '%.4f' % b, ha='center', va= 'bottom',fontsize=10)
    #设置刻度标记的大小
    plt.tick_params(axis='both', labelsize=14)
    plt.savefig("./data/nianfen2.png")
    plt.show()


def zhuxing(name_list, num_list):
    name_list = ['喜剧', '悬疑', '历史' ,'科幻', '武侠']
    num_list = [0.6466, 0.5528, 0.6422, 0.6337, 0.5991]

    plt.bar(range(len(num_list)), num_list,tick_label=name_list)

    font1 = FontProperties(fname=r"C:/Windows/Fonts/simfang.ttf",size=20) 
    #设置图表标题，并给坐标轴加上标签
    plt.title("影评各分类好评率统计", fontproperties=font1)
    plt.xlabel("分类", fontproperties=font1)
    plt.ylabel("好评率", fontproperties=font1)
    plt.xticks(fontproperties=font1)
    plt.axhline(0.8,linewidth=0)
    for a,b in zip(range(len(num_list)),num_list):
        plt.text(a, b+0.05, '%.4f' % b, ha='center', va= 'bottom',fontsize=10)
    plt.savefig("./data/fenlei2.png")
    plt.show()

if __name__ == "__main__":
    zhuxing('','')
    # zhexian('','')