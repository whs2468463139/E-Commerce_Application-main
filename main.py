from data_preprocessing import data_preprocessing
from compkey import compkey
from common import Common

if __name__ == '__main__':
    # data_preprocessing()

    for keyword in Common.seed_keywords:
      compkey(keyword)
