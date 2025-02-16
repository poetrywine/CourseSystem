"""
公共接口
"""
import os
from conf import settings


# 获取所有学校名称接口
def get_all_school_interface():
    # 1.获取学校文件夹路径
    school_dir = os.path.join(
        settings.DB_PATH, 'School'
    )

    # 2.判断文件夹是否存在
    if not os.path.exists(school_dir):
        return False, '没有学校，请先联系管理员'

    # 3.文件夹若存在，则获取文件夹中所有文件的名字
    school_list = os.listdir(school_dir)
    return True, school_list


# 获取所有课程名称接口
def get_all_course_interface():
    # 获取Course文件夹路径
    course_path = os.path.join(
        settings.DB_PATH, 'Course'
    )
    if not os.path.exists(course_path):
        return False, '没有课程，请先联系管理员创建！'

    # 获取Course文件夹下所有文件的名称
    course_name_list = os.listdir(course_path)
    return True, course_name_list
