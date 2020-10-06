from lib import common
from interface import student_interface
from interface import common_interface

student_info = {
    'user': ''
}


# 注册
def register():
    while True:
        username = input('输入你的用户名：').strip()
        password = input('输入你的密码：').strip()
        re_password = input('确认你的密码：').strip()
        if password == re_password:
            flag, msg = student_interface.register_interface(username, password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码输入不一致，重新输入！')


# 登录
def login():
    while True:
        username = input('输入你的用户名').strip()
        password = input('输入你的密码').strip()

        flag, msg = student_interface.login_interface(username, password)
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)


# 选择学校
@common.auth('student')
def choice_school():
    while True:
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break

        for index, school_name in enumerate(school_list):
            print(f'学校编号：{index}, 学校名称{school_name}')
        choice = input('请选择对应编号').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice in range(len(school_list)):
                school_name = school_list[choice]
                flag, msg = student_interface.choice_school_interface(school_name, student_info.get('user'))
                if flag:
                    print(msg)
                    break
            else:
                print('请输入正确编号！')

        else:
            print('请输入正确编号！')


# 选择课程
@common.auth('student')
def choice_course():
    while True:
        # 1.先获取‘当前学生’所在学校的课程列表
        flag, course_list = student_interface.get_course_list_interface(
            student_info.get('user')
        )
        if not flag:
            print(course_list)
            break
        # 2.打印课程列表，并让用户选择课程
        for index, course_name in enumerate(course_list):
            print(f'编号：{index},\t课程：{course_name}')
        choice = input('请选择对应编号：')
        if choice.isdigit():
            choice = int(choice)
            if choice in range(len(course_list)):
                flag, msg = student_interface.choice_course_interface(
                    course_list[choice], student_info.get('user')
                )
                if flag:
                    print(msg)
                    break
            else:
                print('请输入正确编号！')
        else:
            print('请输入正确编号！')


# 查看分数
@common.auth('student')
def check_score():
    print('查看分数')
    flag, score_dic_or_msg = student_interface.check_score_interface(student_info.get('user'))
    if flag:
        for course_name, score in score_dic_or_msg.items():
            print(f'课程：{course_name},\t分数：{score}')
    else:
        print(score_dic_or_msg)


fun_dic = {
    '1': register,
    '2': login,
    '3': choice_school,
    '4': choice_course,
    '5': check_score,
}


def run():
    while True:
        print("""
        ==========
        1.注册
        2.登录
        3.选择学校
        4.选择课程
        5.查看分数
        ==========
        """)
        choice = input('选择你要进入的功能:').strip()
        if choice in fun_dic:
            fun_dic.get(choice)()
        else:
            print('请重新输入！')

