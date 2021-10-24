from common import Common
from search_info import SearchInfo
from seed_keyword_info import SeedKeywordInfo


def data_preprocessing(max_line_num=100000):
    print("数据预处理")
    with open('processed_data.csv', 'w', encoding='utf-8') as file:
        print("清空processed_data文件内容")
        file.write("keyword, count, age, gender, education, search_id\n")
    with open('data.txt', 'r', encoding='utf-8') as file:
        line_num = 1
        for line in file:
            if line_num > max_line_num:
                break
            line_num += 1
            search_info = SearchInfo(line)
            for keyword in Common.seed_keywords:
                count = search_info.have_content(keyword)
                if count:
                    seed_keyword_info = SeedKeywordInfo(keyword, count, search_info)
                    seed_keyword_info.save_to_file()
                    print(line_num, seed_keyword_info)
