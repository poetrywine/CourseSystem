from lib import common
from interface import teacher_interface
from interface import common_interface


teacher_info = {
    'user': ''
}


# 登录
def login():
    while True:
        username = input('输入用户名：').strip()
        password = input('输入密码：').strip()

        flag, msg = teacher_interface.login_interface(username, password)
        if flag:
            print(msg)
            teacher_info['user'] = username
            break
        else:
            print(msg)


# 查看教授课程
@common.auth('teacher')
def check_teach_course():
    flag, course_list_or_msg = teacher_interface.check_teach_course_interface(teacher_info.get('user'))
    if flag:
        print('教授的课程有：')
        for course_name in course_list_or_msg:
            print(f'{course_name}\t', end='')
    else:
        print(course_list_or_msg)


# 选择教授课程
@common.auth('teacher')
def choice_teach_course():
    # 获取所有已存在的课程并打印给老师选择
    while True:
        flag, course_list_or_msg = common_interface.get_all_course_interface()
        if not flag:
            print(course_list_or_msg)
        else:
            for index, course_name in enumerate(course_list_or_msg):
                course_name = course_name.rstrip('.pk')
                print(f'课程编号：{index}\t课程名称：{course_name}')
        # 老师选择后保存
        choice = input('请输入选择的编号：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice in range(len(course_list_or_msg)):
                flag, msg = teacher_interface.choice_teach_course_interface(
                    teacher_info.get('user'), course_list_or_msg[choice].rstrip('.pk')
                )
                if flag:
                    print(msg)
                    break
                else:
                    print('选择失败！')
        else:
            print('请输入正确编号')


# 查看课程下的学生
@common.auth('teacher')
def check_course_student():
    while True:
        # 打印老师教授的课程，并让老师选择
        flag, course_list = teacher_interface.check_teach_course_interface(
            teacher_info.get('user')
        )
        if not flag:
            print(course_list)
        else:
            print('教授课程有')
            for index, course_name in enumerate(course_list):
                print(f'课程编号：{index}\t课程名称：{course_name.rstrip(".pk")}')
            choice = input('输入你选择的编号：').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice in range(len(course_list)):
                    student_list = teacher_interface.check_course_student_interface(
                        teacher_info.get('user'), course_list[choice].rstrip('.pk')
                    )
                    if student_list:
                        print(f'{course_list[choice]}课程下的学生有：')
                        for student_name in student_list:
                            print(f'{student_name}\t', end='')
                        break
                    else:
                        print('该课程下没有学生！')
                        break
            else:
                print('输入正确的课程编号！')


# 修改学生分数
@common.auth('teacher')
def correct_student_course():
    correct_stu_score_course_name = ''
    while True:
        # 获取老师教的所有课程并打印，让老师选择一门课程
        flag, course_list_or_msg = teacher_interface.check_teach_course_interface(
            teacher_info.get('user')
        )
        if flag:
            for index, course_name in enumerate(course_list_or_msg):
                print(f'课程编号{index}\t课程名称{course_name}')
            choice = input('选择你的课程编号：').strip()
            if choice.isdigit():
                choice = int(choice)
                correct_stu_score_course_name = course_list_or_msg[choice]
            else:
                print('请重新输入！')
                continue
        else:
            print(course_list_or_msg)
            continue
        # 从老师选择的课程中打印出所有学生，让老师选择一位更改
        student_list = teacher_interface.check_course_student_interface(
            teacher_info.get('user'), correct_stu_score_course_name
        )
        print(f'{correct_stu_score_course_name}课程中学生姓名：')
        for index, student_name in enumerate(student_list):
            print(f'编号：{index}\t姓名{student_name}')
        choice = input('输入你要修改的学生编号：').strip()
        if choice.isdigit():
            score = input('输入你要修改的分数：').strip()
            if score.isdigit():
                score = int(score)
                if score in range(0, 101):
                    choice = int(choice)
                    if choice in range(len(student_list)):
                        flag, msg = teacher_interface.correct_student_course_interface(
                            # 学生姓名              # 课程名字                      老师姓名
                            student_list[choice], correct_stu_score_course_name, teacher_info.get('user'), score
                        )
                        if flag:
                            print(msg)
                            break
                        else:
                            print('修改失败')
                    else:
                        print('请输入正确编号')
                else:
                    print('输入0~100的数字')
            else:
                print('输入数字')


fun_dic = {
    '1': login,
    '2': check_teach_course,
    '3': choice_teach_course,
    '4': check_course_student,
    '5': correct_student_course,
}


def run():
    while True:
        print("""
        ==========
        1.登录
        2.查看教授课程
        3.选择教授课程
        4.查看课程下的学生
        5.修改学生分数
        ==========
        """)
        choice = input('选择你要进入的功能:').strip()
        if choice in fun_dic:
            fun_dic.get(choice)()
        else:
            print('请重新输入！')
