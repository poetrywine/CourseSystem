"""
管理员视图层
"""
from interface import admin_interface
from lib import common
from interface import common_interface

# 记录管理员登录状态，因为要在函数体内更改admin_info，
# 所以使用可变类型，这样就可以不使用global了
admin_info = {'user': ''}


# 注册
def register():
    while True:
        # 接受用户输入的username，password
        username = input('输入你的用户名：').strip()
        password = input('输入你的密码：').strip()
        re_password = input('确认你的密码：').strip()

        # 简单的逻辑判断输入的两次密码是否相等
        if password == re_password:
            # username,password传入逻辑接口层
            flag, msg = admin_interface.register_interface(username, password)
            # 接收到逻辑接口层传来的数据，并赋值给flag和msg
            if flag:  # 注册成功
                print(msg)
                break
            else:  # 注册失败
                print(msg)
        else:
            print('两次密码输入不一致！')


# 登录
def login():
    while True:
        username = input('输入你的用户名：').strip()
        password = input('输入你的密码：').strip()
        # 调用逻辑接口层
        flag, msg = admin_interface.login_interface(username, password)
        if flag:
            print(msg)
            # 记录当前用户登录状态
            # 可变类型不需要global
            admin_info['user'] = username
            break
        else:
            print(msg)


# 创建学校
@common.auth('admin')
def creat_school():
    while True:
        school_name = input('输入学校的名称：').strip()
        school_addr = input('输入学校地址：').strip()

        # 调用逻辑接口层
        flag, msg = admin_interface.creat_school_interface(
            # 学校名，学校地址，创建学校的管理员
            school_name, school_addr, admin_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 创建课程
@common.auth('admin')
def creat_course():
    while True:
        # 1.让管理员先选择学校
        # 1.1调用接口，获取所有学校的名称并打印
        flag, school_list_or_msg = common_interface.get_all_school_interface()
        if not flag:
            print(school_list_or_msg)
            break

        for index, school_name in enumerate(school_list_or_msg):
            print(f'编号：{index}\t学校名：{school_name}')
        choice = input('请输入学校编号：').strip()
        if not choice.isdigit():
            print('请输入数字')
            continue
        choice = int(choice)
        if choice not in range(len(school_list_or_msg)):
            print('请输入正确编号')
            continue

        # 获取选择后的学校名字
        school_name = school_list_or_msg[choice]

        # 2.选择学校后，再输入课程名称
        course_name = input('请输入需要创建的课程名称').strip()

        # 3.调用创建课程接口，让管理员去创建课程
        flag, msg = admin_interface.create_course_interface(
            school_name, course_name, admin_info.get('user')
        )
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建讲师
@common.auth('admin')
def creat_teacher():
    while True:
        teacher_name = input('请输入老师名字').strip()
        # 调用接口创建老师
        flag, msg = admin_interface.create_teacher_interface(teacher_name, admin_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)


fun_dic = {
    '1': register,
    '2': login,
    '3': creat_school,
    '4': creat_course,
    '5': creat_teacher,
}


def run():
    while True:
        print("""
        ==========
        1.注册
        2.登录
        3.创建学校
        4.创建课程
        5.创建讲师
        ==========
        """)
        choice = input('选择你要进入的功能:').strip()
        if choice in fun_dic:
            fun_dic.get(choice)()
        else:
            print('请重新输入！')
