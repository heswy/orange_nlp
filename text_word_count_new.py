import os
import pdfplumber


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


# 字数统计
def text_word_count(texts):
    word_counts = []
    for text in texts:
        word_counts.append(len(text))
    return word_counts


if __name__ == '__main__':
    folder_path = 'text'
    texts = extract_text_from_pdfs(folder_path)
    word_counts = text_word_count(texts)
    print('字数统计结果：', word_counts)
    # 将结果写入新的 txt 文件
    with open('word_count_result.txt', 'w', encoding='utf-8') as f:
        for count in word_counts:
            f.write(str(count) + '\n')
    folder_path = 'text'
    texts = extract_text_from_pdfs(folder_path)
    word_counts = text_word_count(texts)
    print('字数统计结果：', word_counts)