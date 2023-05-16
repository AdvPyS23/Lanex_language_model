import pandas as pd

# Create an empty DataFrame with the desired columns
vocabulary_list_cn = pd.DataFrame(columns=["word", "translation", "pronunciation", "usage", "category", "difficulty"])

# Add some data to the DataFrame (example data)
data = [
    {"word": "苹果", "translation": "apple", "pronunciation": "píng guǒ", "usage": "我今天吃了一个苹果。", "category": "fruit", "difficulty": "1"},
    {"word": "房子", "translation": "house", "pronunciation": "fáng zi", "usage": "这是我的房子。", "category": "infrastructure", "difficulty": "1"},
    {"word": "车", "translation": "car", "pronunciation": "chē", "usage": "我有一辆红色的车。", "category": "transportation", "difficulty": "1"},
    {"word": "丹顶鹤", "translation": "red-crowned crane", "pronunciation": "Dān dǐng hè", "usage": "是丹顶鹤不是鹤顶红。", "category": "animal", "difficulty": "1"},
    {"word": "电脑", "translation": "computer", "pronunciation": "diàn nǎo", "usage": "我用电脑写作业。", "category": "technology", "difficulty": "2"},
    {"word": "工程师", "translation": "engineer", "pronunciation": "gōng chéng shī", "usage": "我梦想成为一名工程师。", "category": "career", "difficulty": "2"},
    {"word": "复杂", "translation": "complex", "pronunciation": "fù zá", "usage": "这个问题很复杂。", "category": "description", "difficulty": "3"},
    {"word": "麻烦", "translation": "trouble", "pronunciation": "má fan", "usage": "这件事情很麻烦。", "category": "description", "difficulty": "3"},
    {"word": "生物信息", "translation": "bioinformatics", "pronunciation": "Shēngwù xìnxī", "usage": "我在上生物信息学。", "category": "technology", "difficulty": "3"},
    {"word": "左", "translation": "left", "pronunciation": "Zuǒ", "usage": "请在下个路口左转。", "category": "direction", "difficulty": "1"}
    ]

# Convert the data to a DataFrame
data_df = pd.DataFrame(data)

# Concatenate the data with the existing DataFrame
vocabulary_list_cn = pd.concat([vocabulary_list_cn, data_df], ignore_index=True)

# Save the DataFrame to a CSV file
vocabulary_list_cn.to_csv("vocabulary_chinese_simp.csv", index=False)

