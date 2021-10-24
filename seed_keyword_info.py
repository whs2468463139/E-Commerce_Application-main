from search_info import SearchInfo


class SeedKeywordInfo:
    keyword = None
    count = 0
    age = None
    gender = None
    education = None
    search_id = None

    def __repr__(self):
        return "SeedKeywordInfo<{0}>: {1}".format(self.keyword, {
            'count': self.count,
            'age': self.age,
            'gender': self.gender,
            'education': self.education,
            'search_id': self.search_id,
        })

    def __init__(self, keyword, count, search_info: SearchInfo):
        self.keyword = keyword
        self.count = count
        self.age = search_info.age
        self.gender = search_info.gender
        self.education = search_info.education
        self.search_id = search_info.id

    def to_csv_data(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}\n".format(
            self.keyword, self.count, self.age, self.gender, self.education, self.search_id
        )

    def save_to_file(self):
        with open('processed_data.csv', 'a', encoding='utf-8') as file:
            file.write(self.to_csv_data())
