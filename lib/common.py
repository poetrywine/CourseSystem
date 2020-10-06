"""
常用的公共方法
"""


# 多用户登录认证装饰器
def auth(role):
    from core import admin, teacher, student

    # 登录认证装饰器
    def login_auth(func):
        def inner(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()
            elif role == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.login()
            elif role == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print('当前视图没有权限')
        return inner
    return login_auth
