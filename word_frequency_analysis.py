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


# 词频统计
# 读取停用词文件
with open('/Users/orange/develop/senti/stopwords.txt', 'r', encoding='utf-8') as f:
    stopwords = set([line.strip() for line in f.readlines()])


def word_frequency(texts):
    all_words = []
    for text in texts:
        words = jieba.lcut(text)
        # 打印部分分词结果用于调试
        print("部分分词结果:", words[:10])
        # 过滤停用词
        filtered_words = [word for word in words if word not in stopwords]
        # 打印部分停用词用于调试
        print("部分停用词:", list(stopwords)[:10])
        all_words.extend(filtered_words)
    counter = Counter(all_words)
    sorted_words = counter.most_common()
    return sorted_words


if __name__ == '__main__':
    folder_path = 'text'
    texts = extract_text_from_pdfs(folder_path)
    word_freq = word_frequency(texts)
    with open('word_frequency_result.txt', 'w', encoding='utf-8') as f:
        for word, freq in word_freq:
            f.write(f'{word}: {freq}\n')
    print('词频统计结果：', word_freq)