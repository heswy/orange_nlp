# 项目介绍 📋

本项目主要用于对实习周报进行数据分析和可视化展示，通过对周报内容的情感分析、词频统计等操作，以直观的数据大屏形式呈现结果。

## 文件作用 📄

| 文件名 | 作用 |
| ---- | ---- |
| index.html | 数据大屏可视化页面，使用 ECharts 展示词频统计、情感分析等结果。 |
| process_data.py | 数据处理脚本，用于处理原始数据。 |
| processed_data.json | 处理后的 JSON 格式数据，供 `index.html` 页面使用。 |
| sentiment_analysis.py | 情感分析脚本，对周报文本进行情感分析并输出结果。 |
| sentiment_analysis_result.txt | 情感分析结果文件，记录每周的情感得分。 |
| stopwords.txt | 停用词文件，用于过滤文本中的停用词。 |
| text_word_count_new.py | 文本字数统计脚本。 |
| word_count_result.txt | 文本字数统计结果文件。 |
| word_frequency_analysis.py | 词频分析脚本，统计文本中的词频。 |
| word_frequency_result.txt | 词频分析结果文件。 |
| 开发要求.md | 项目开发要求文档。 |

## 数据大屏访问方式 🌐

1. 确保项目所需的依赖已经安装，可在项目根目录下创建并激活虚拟环境：
```bash
python3 -m venv venv
source venv/bin/activate
```
2. 运行数据处理和分析脚本，生成 `processed_data.json` 文件。
3. 直接在浏览器中打开 `index.html` 文件，即可访问数据大屏。

