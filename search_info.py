from common import Common


class SearchInfo:
    id = None
    age = None
    gender = None
    education = None
    query_list = []

    def __repr__(self):
        return "SearchInfo<{0}>: {1}".format(self.id, {
            'age': self.age,
            'gender': self.gender,
            'education': self.education,
            'query_list': "共%s条记录" % len(self.query_list),
        })

    def __init__(self, info):
        info = info.split('	')
        self.id = info[0]
        self.age = Common.age_map[int(info[1])]
        self.gender = Common.gender_map[int(info[2])]
        self.education = Common.education_map[int(info[3])]
        self.query_list = info[4:]

    def have_content(self, content):
        cnt = 0
        for query in self.query_list:
            if content in query:
                cnt += 1
        return cnt
