import os

# 获取项目根目录路径
BASE_PATH = os.path.dirname(
    os.path.dirname(__file__)
)


# 获取db文件夹路径
DB_PATH = os.path.join(
    BASE_PATH, 'db'
)
