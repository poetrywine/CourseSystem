"""
用于保存对象与获取对象
"""
import pickle
from conf import settings
import os


# 保存用户数据
def save_data(obj):
    # 获取对象的保存文件夹路径
    # obj.__class__ 表示获取对象obj的类
    # obj.__class__.name__ 表示对象obj的类的类名,
    class_name = obj.__class__.__name__
    user_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_path):
        os.mkdir(user_path)

    # 拼接当前用户的pickle文件路径，以用户名作为文件名
    # obj.username是对象的username属性，
    # 由于本函数还要给其他用户使用，比如student、teacher使用，所以在Student和Teacher类的定义时都要有username属性，且名称必须是username
    user_data_path = os.path.join(
        user_path, f'{obj.username}.pk'
    )

    # 打开文件保存对象，通过pickle
    with open(user_data_path, mode='wb') as f:
        pickle.dump(obj, f)


# 查看数据, 有则返回查询到的对象，没有则返回None
def check_data(cla, username):
    # 获取对象的保存文件夹路径
    # obj.__class__ 表示获取对象obj的类
    # obj.__class__.name__ 表示对象obj的类的类名,
    class_name = cla.__name__
    user_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_path):
        return None

    # 拼接当前用户的pickle文件路径，以用户名作为文件名
    # obj.username是对象的username属性，
    # 由于本函数还要给其他用户使用，比如student、teacher使用，所以在Student和Teacher类的定义时都要有username属性，且名称必须是username
    user_data_path = os.path.join(
        user_path, f'{username}.pk'
    )
    if os.path.exists(user_data_path):
        # 打开文件保存对象，通过pickle
        with open(user_data_path, mode='rb') as f:
            obj = pickle.load(f)
        return obj
    return None
