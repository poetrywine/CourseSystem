"""
学校类、学员类、课程类、讲师类、管理员类
"""
from db import db_handler


# 父类，让所有子类都继承select与save方法
class Base:
    # 查看数据
    @classmethod
    def select(cls, username):
        # obj:对象 or None
        obj = db_handler.check_data(cls, username)
        return obj

    # 保存数据
    def save(self):
        # 调用db_handler中的save_data帮我保存对象
        db_handler.save_data(self)


# 管理员类
class Admin(Base):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # 创建学校
    @staticmethod
    def creat_school(school_name, school_addr):
        """该方法内部调用了学校类来实例化，从而得到学校的对象，然后通过该学校对象的save方法保存此次创建的学校的数据"""
        school_obj = School(school_name, school_addr)
        school_obj.save()

    # 创建课程
    def creat_course(self, school_obj, course_name):
        # 1.调用课程类，实例化创建课程
        course_obj = Course(course_name)
        course_obj.save()
        # 2.获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)
        # 3.更新学校数据
        school_obj.save()

    # 创建讲师
    def creat_teacher(self, teacher_name, teacher_password):
        # 调用老师类，实例化得到老师对象，并保存
        teacher_obj = Teacher(teacher_name, teacher_password)
        teacher_obj.save()


# 学校类
class School(Base):
    def __init__(self, name, addr):
        # 注：必须写self.username,因为db_handler里面的select_data由对象的username属性
        self.username = name
        self.addr = addr

        # 课程列表：每所学校都应该由相应的课程
        self.course_list = []


# 学生类
class Student(Base):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.course_list = []
        self.score = {}  # {'course_name': 0}
        self.school = ''

    def add_school(self, school_name):
        self.school = school_name
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()
        course_obj = Course.select(course_name)
        # print(course_obj.username)
        # print(self.username)
        course_obj.student_list.append(self.username)
        course_obj.save()


# 课程类
class Course(Base):
    def __init__(self, course_name):
        self.username = course_name
        self.student_list = []


# 老师类
class Teacher(Base):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.course_list_from_tea = []

    # 选择教授课程
    def choice_teach_course(self, course_name):
        self.course_list_from_tea.append(course_name)
        self.save()

    # 查看课程下的学生
    def check_course_student(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list

    # 修改学生分数
    def correct_student_score(self, student_name, course_name, score):
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()



