# -*- coding: utf-8 -*-
from native_bayes_sentiment_analyzer import SentimentAnalyzer


model_path = './data/bayes.pkl'
userdict_path = './data/userdict.txt'
stopword_path = './data/stopwords.txt'
corpus_path = './data/review.csv'


analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)
text = '无感'
pos = analyzer.analyze(text=text)
print('好评率：{}'.format(pos))