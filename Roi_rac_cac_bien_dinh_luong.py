import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# định nghĩa khoảng giá trị các nhóm
bins = [18, 25, 35, 60, 100]
# thực hiện rời rạc hóa
cats = pd.cut(ages, bins)
# print(cats)
# lấy ra index của nhóm tương ứng với các phần tử
cats.codes

# lấy ra các nhóm
cats.categories
# thống kê số lượng phần tử ở mỗi nhóm
print(pd.value_counts(cats))

# sinh dữ liệu ngẫu nhiên gồm 20 phần tử
data = np.random.rand(20)
cut_data = pd.cut(data, 4, precision=2)
# print(cut_data)
print(pd.value_counts(cut_data))