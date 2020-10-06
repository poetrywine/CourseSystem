from db import models


# 登录接口
def login_interface(username, password):
    user_obj = models.Teacher.select(username)
    if user_obj:
        if user_obj.password == password:
            return True, '登录成功'
        else:
            return False, '密码错误'
    else:
        return False, '用户已存在'


# 查看教授课程接口
def check_teach_course_interface(username):
    user_obj = models.Teacher.select(username)
    teach_course_list = user_obj.course_list_from_tea
    if teach_course_list:
        return True, teach_course_list
    else:
        return False, '暂时没有教授的课程！'


# 选择教授课程接口
def choice_teach_course_interface(username, course_name):
    user_obj = models.Teacher.select(username)
    user_obj.choice_teach_course(course_name)
    return True, f'选择{course_name}成功！'


# 查看课程下学生接口
def check_course_student_interface(username, course_name):
    teacher_obj = models.Teacher.select(username)
    student_list = teacher_obj.check_course_student(course_name)
    return student_list


# 修改学生分数接口
def correct_student_course_interface(student_name, course_name, teacher_name, score):
    teacher_obj = models.Teacher.select(teacher_name)
    teacher_obj.correct_student_score(student_name, course_name, score)
    return True, '修改成功'

