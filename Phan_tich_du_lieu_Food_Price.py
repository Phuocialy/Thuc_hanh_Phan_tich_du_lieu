import pandas as pd

df = pd.read_csv('FoodPrice_in_Turkey.csv')

# Sử dụng hàm info() để kiểm tra thông tin bộ dữ liệu
print(df.info())


# Sử dụng groupby và mean để tính giá trung bình của từng loại thực phẩm

df1 = df.groupby(['ProductName'])['Price'].mean()

print(df1)

# Bạn đề xuất tất cả các yêu cầu phân tích, hiện tại bạn chưa làm được, nhưng hãy chúng ta sẽ giải quyết ở các bài học sau
# Cần xử lý dữ liệu nhiễu do lỗ từ người nhập dữ liệu, hay vì một lý do nào đó mà dữ liệu đó bị mất
