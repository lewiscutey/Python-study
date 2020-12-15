from pymysql.cursors import DictCursor
import pymysql

"""
添加一个部门。
"""


def main():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    # 1. 创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='lewis')
    try:
        # 2. 通过连接对象获取游标
        with con.cursor() as cursor:
            # 3. 通过游标执行SQL并获得执行结果
            result = cursor.execute(
                'insert into tb_dept values (%s, %s, %s)',
                (no, name, loc)
            )
        if result == 1:
            print('添加成功!')
        # 4. 操作成功提交事务
        con.commit()
    finally:
        # 5. 关闭连接释放资源
        con.close()


# if __name__ == '__main__':
#     main()

"""
删除一个部门。
"""


def main():
    no = int(input('编号: '))
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='lewis',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'delete from tb_dept where dno=%s',
                (no, )
            )
        if result == 1:
            print('删除成功!')
        else:
            print('删除失败！')
    finally:
        con.close()


# if __name__ == '__main__':
#     main()

"""
更新一个部门
"""


def main():
    no = int(input('编号: '))
    name = input('名字: ')
    loc = input('所在地: ')
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='lewis',
                          autocommit=True)
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'update tb_dept set dname=%s, dloc=%s where dno=%s',
                (name, loc, no)
            )
        if result == 1:
            print('更新成功!')
    finally:
        con.close()


# if __name__ == '__main__':
#     main()

"""
查询所有部门
"""


def main():
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='lewis')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute(
                'select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])
    finally:
        con.close()


# if __name__ == '__main__':
#     main()


"""
分页查询员工信息
"""


class Emp(object):

    def __init__(self, no, name, job, sal):
        self.no = no
        self.name = name
        self.job = job
        self.sal = sal

    def __str__(self):
        return f'\n编号：{self.no}\n姓名：{self.name}\n职位：{self.job}\n月薪：{self.sal}\n'


def main():
    page = int(input('页码: '))
    size = int(input('大小: '))
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='lewis')
    try:
        with con.cursor() as cursor:
            cursor.execute(
                'select eno as no, ename as name, job, sal from tb_emp limit %s,%s',
                ((page - 1) * size, size)
            )
            for emp_tuple in cursor.fetchall():
                emp = Emp(*emp_tuple)
                print(emp)
    finally:
        con.close()


if __name__ == '__main__':
    main()
