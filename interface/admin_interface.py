from db import models


# 管理员注册接口
def register_interface(username, password):
    """
    接收到管理员视图层传来的username和password
    1、先判断用户是否存在
    2、存在则返回数据False和‘用户已存在’给管理员视图层
    3、不存在则保存数据，并返回数据True和'注册成功！'给管理员视图层
    :param username:
    :param password:
    :return:
    """

    # 调用Admin类中的select方法，由该方法去调用db_handler中的select_data功能获取对象
    admin_obj = models.Admin.select(username)

    # 检查用户是否存在，存在则返回False
    if admin_obj:
        return False, '用户已存在'
    # 不存在则保存数据
    else:
        admin_obj = models.Admin(username, password)
        admin_obj.save()
        return True, '注册成功！'


# 登入接口
def login_interface(username, password):
    admin_obj = models.Admin.select(username)

    if not admin_obj:
        return False, '用户名不存在！'

    if password == admin_obj.password:
        return True, '登入成功！'
    else:
        return False, '密码错误！'

    # user_obj = models.Admin(username, password)
    # obj = user_obj.login()
    # if obj:
    #     if obj.password == password:
    #         return True, '登入成功'
    #     else:
    #         return False, '用户名或密码错误！'
    # else:
    #     return False, '用户名或密码错误！'


# 管理员创建学校接口
def creat_school_interface(school_name, school_addr, admin_name):
    # 查看当前学校是否已存在
    # school_obj ----> 对象 or None
    school_obj = models.School.select(school_name)
    # 若学校存在，则返回False告诉用户学校已存在
    if school_obj:
        return False, '学校已存在！'
    # 若不存在，则创建学校， （注意：由管理员对象来创建）
    # 获取当前管理员对象
    admin_obj = models.Admin.select(admin_name)
    # 由管理员来调用创建学校的方法，并传入学校的名字与地址
    admin_obj.creat_school(school_name, school_addr)
    return True, f'{school_name}创建成功'


# 管理员创建课程接口
def create_course_interface(school_name, course_name, admin_name):
    # 1.查看课程是否存在
    # 1.1 先获取学校对象中的课程列表
    school_name = school_name.rstrip('.pk')
    school_obj = models.School.select(school_name)

    # 1.2 判断当前课程是否存在课程列表中
    if course_name in school_obj.course_list:
        return False, '当前课程已存在！'
    # 1.3 若课程不存在，则创建课程，由管理员来创建
    admin_obj = models.Admin.select(admin_name)
    admin_obj.creat_course(school_obj, course_name)
    return True, f'{course_name}课程创建成功！绑定给{school_name}校区！'


# 管理员创建老师接口
def create_teacher_interface(teacher_name, admin_name, teacher_password='123'):
    # 1.判断老师是否存在
    teacher_obj = models.Teacher.select(teacher_name)
    # 2.若存在，则返回不能创建
    if teacher_obj:
        return False, '老师已存在'
    # 3.若不存在，则创建老师，让管理员来创建
    else:
        admin_obj = models.Admin.select(admin_name)
        admin_obj.creat_teacher(teacher_name, teacher_password)
        return True, f'{teacher_name}创建成功！'

