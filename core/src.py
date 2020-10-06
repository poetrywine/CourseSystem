"""
主视图
"""
from core import admin
from core import student
from core import teacher


fun_dic = {
    '1': admin.run,
    '2': student.run,
    '3': teacher.run,
}


def run():
    while True:
        print("""
        ==========
        1.管理员视图
        2.学生视图
        3.讲师视图
        ==========
        """)
        choice = input('选择你要进入的视图:').strip()
        if choice in fun_dic:
            fun_dic.get(choice)()
            break
        else:
            print('请重新输入！')
