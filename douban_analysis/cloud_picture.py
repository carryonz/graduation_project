import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import csv
import random

stopword_path = './data/stopwords.txt'
file_path = './data/review.csv'
del_path = './data/del.txt'

def load_corpus(corpus_path):
    with open(corpus_path, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    review_data = np.array(rows).tolist()

    review_good = []
    review_bad = []
    for words in review_data:
        if words[0] == '1':
            review_good.append(words[1])
        else:
            review_bad.append(words[1])

    return review_good, review_bad


# jieba分词
def review_to_text(review):
    stop_words = load_stopwords(stopword_path)
    jieba.del_word(del_path)
    review = jieba.cut(review)
    all_stop_words = set(stop_words)
    # 去掉停用词
    review_words = [w for w in review if w not in all_stop_words]
    return review_words

def load_stopwords(file_path):
    stop_words = []
    with open(file_path, encoding='UTF-8') as words:
       stop_words.extend([i.strip() for i in words.readlines()])
    return stop_words


def create_word_cloud(text, picture_name):
    wl = " ".join(text)
    # 设置词云
    wc = WordCloud(
        # 设置背景颜色
        background_color="white",
        # 设置最大显示的词云数
        max_words=50,
        # 这种字体都在电脑字体中，一般路径
        font_path='C:/Windows/Fonts/simfang.ttf',
        height=1200,
        width=1600,
        # 设置字体最大值
        max_font_size=300,
        # 设置有多少种随机生成状态，即有多少种配色方案
        random_state=100,
    )

    myword = wc.generate(wl)  # 生成词云
    # 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file(picture_name)  # 把词云保存下

if __name__ == "__main__":
    jieba.load_userdict("./data/userdict.txt")
    train_review_good, train_review_bad = load_corpus(file_path)
    review_train_good = [' '.join(review_to_text(review)) for review in train_review_good]
    create_word_cloud(review_train_good, "good.png")
    review_train_bad = [' '.join(review_to_text(review)) for review in train_review_bad]
    create_word_cloud(review_train_bad, "bad.png")