import os
import pdfplumber
import jieba
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from snownlp import SnowNLP


# 提取 PDF 文本
def extract_text_from_pdfs(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with pdfplumber.open(file_path) as pdf:
                text = ''
                for page in pdf.pages:
                    text += page.extract_text()
                texts.append(text)
    return texts


# 情感分析
# 读取停用词文件
with open('/Users/orange/develop/senti/stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = set([line.strip() for line in f.readlines()])


def sentiment_analysis(texts):
    sentiments = []
    for text in texts:
        # 过滤停用词
        words = jieba.lcut(text)
        filtered_words = [word for word in words if word not in stopwords]
        filtered_text = ''.join(filtered_words)
        # 分句分析情感
        sentences = SnowNLP(filtered_text).sentences
        if sentences:
            sentence_sentiments = [SnowNLP(sentence).sentiments for sentence in sentences]
            avg_sentiment = sum(sentence_sentiments) / len(sentence_sentiments)
            sentiments.append(avg_sentiment)
        else:
            s = SnowNLP(filtered_text)
            sentiments.append(s.sentiments)
    print('情感分析结果：', sentiments)
    with open('sentiment_analysis_result.txt', 'w', encoding='utf-8') as f:
        for sentiment in sentiments:
            f.write(f'{sentiment}\n')
    return sentiments


if __name__ == '__main__':
    folder_path = 'text'
    texts = extract_text_from_pdfs(folder_path)
    sentiments = sentiment_analysis(texts)