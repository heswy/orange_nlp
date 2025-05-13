import json

# 读取词频统计结果
with open('word_frequency_result.txt', 'r', encoding='utf-8') as f:
    word_freq_lines = f.readlines()
word_freq = {line.split(': ')[0]: int(line.split(': ')[1].strip()) for line in word_freq_lines}

# 读取字数统计结果
with open('word_count_result.txt', 'r', encoding='utf-8') as f:
    word_count_lines = f.readlines()
word_count = {line.split(': ')[0]: int(line.split(': ')[1].strip()) for line in word_count_lines}

# 读取情感分析结果
with open('sentiment_analysis_result.txt', 'r', encoding='utf-8') as f:
    sentiment_lines = f.readlines()
sentiment = {line.split(':')[0]: float(line.split(':')[1].strip()) for line in sentiment_lines}

# 统计情感分析结果的正负面和中性比例
positive = sum(1 for score in sentiment.values() if score > 0.65)
negative = sum(1 for score in sentiment.values() if score < 0.65)
neutral = sum(1 for score in sentiment.values() if score == 0.65)
total = len(sentiment)
sentiment_ratio = {
    'positive': positive / total if total > 0 else 0,
    'negative': negative / total if total > 0 else 0,
    'neutral': neutral / total if total > 0 else 0
}

# 整理数据
data = {
    'word_frequency': word_freq,
    'word_count': word_count,
    'sentiment': sentiment,
    'sentiment_ratio': sentiment_ratio
}

# 保存为 JSON 文件
with open('processed_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)