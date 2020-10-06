
"""
可以注册， 交学费， 选择班级，

"""
from db import models


def register_interface(username, password):
    user_obj = models.Student.select(username)

    if user_obj:
        return False, '用户已存在'
    else:
        stu_obj = models.Student(username, password)
        stu_obj.save()
        return True, '注册成功'


# 登录接口
def login_interface(username, password):
    user_obj = models.Student.select(username)
    if user_obj:
        if user_obj.password == password:
            return True, '登录成功！'
        else:
            return False, '密码错误！'
    else:
        return False, '用户不存在！'


# 选择学校接口
def choice_school_interface(school_name, username):
    stu_obj = models.Student.select(username)
    stu_obj.add_school(school_name)
    return True, '选择学校成功！'


# 获取学生所在学校所有课程接口
def get_course_list_interface(username):
    # 1.获取当前学生对象
    student_obj = models.Student.select(username)
    school_name = student_obj.school
    school_name = school_name.rstrip('.pk')
    print(school_name)
    # 2.判断当前学生是否由学校，若没有则返回False
    if not school_name:
        return False, '没有学校，请先选择学校'
    # 3.开始获取学校对象中的课程列表
    school_obj = models.School.select(school_name)

    # 3.1 判断当前学校中是否有课程，若没有，则联系管理员创建
    course_list = school_obj.course_list
    if not course_list:
        return False, '没有课程，请先联系管理员创建'

    # 3.2 若有则返回课程列表
    return True, course_list


# 选择课程接口
def choice_course_interface(course_name, username):
    user_obj = models.Student.select(username)
    user_obj.add_course(course_name)
    return True, f'选择{course_name}成功！'


# 查看分数接口
def check_score_interface(username):
    user_obj = models.Student.select(username)
    if not user_obj.score:
        return False, '没有课程分数'
    else:
        score_dic = user_obj.score
        return True, score_dic
