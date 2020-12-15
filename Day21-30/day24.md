# 关系数据库入门


## 关系数据库概述
1. 数据持久化 - 将数据保存到能够长久保存数据的存储介质中，在掉电的情况下数据也不会丢失。
2. 数据库发展史 - 网状数据库、层次数据库、关系数据库、NoSQL数据库。
3. 关系数据库特点。
  理论基础：集合论和关系代数。
  具体表象：用二维表（有行和列）组织数据。
  编程语言：结构化查询语言（SQL）。
4. ER模型（实体关系模型）和概念模型图。


## MySQL简介
1. 常用命令
  查看服务器版本: select version();
  查看所有数据库: show databases;
  切换到指定数据库: use mysql;
  查看数据库下所有表: show tables;


## SQL详解
### 基本操作
我们通常可以将SQL分为三类：DDL（数据定义语言）、DML（数据操作语言）和DCL（数据控制语言）。DDL主要用于创建（create）、删除（drop）、修改（alter）数据库中的对象，比如创建、删除和修改二维表；DML主要负责插入数据（insert）、删除数据（delete）、更新数据（update）和查询（select）；DCL通常用于授予权限（grant）和召回权限（revoke）。

> 说明：SQL是不区分大小写的语言，为了书写方便，下面的SQL都使用了小写字母来书写。

1. DDL（数据定义语言）
```
-- 如果存在名为school的数据库就删除它
drop database if exists school;

-- 创建名为school的数据库并设置默认的字符集和排序方式
create database school default charset utf8;

-- 切换到school数据库上下文环境
use school;

-- 创建学院表
create table tb_college
(
collid 		int auto_increment comment '编号',
collname 	varchar(50) not null comment '名称',
collintro 	varchar(500) default '' comment '介绍',
primary key (collid)
);

-- 创建学生表
create table tb_student
(
stuid 		int not null comment '学号',
stuname 	varchar(20) not null comment '姓名',
stusex 		boolean default 1 comment '性别',
stubirth 	date not null comment '出生日期',
stuaddr 	varchar(255) default '' comment '籍贯',
collid 		int not null comment '所属学院',
primary key (stuid),
foreign key (collid) references tb_college (collid)
);

-- 创建教师表
create table tb_teacher
(
teaid 		int not null comment '工号',
teaname 	varchar(20) not null comment '姓名',
teatitle 	varchar(10) default '助教' comment '职称',
collid 		int not null comment '所属学院',
primary key (teaid),
foreign key (collid) references tb_college (collid)
);

-- 创建课程表
create table tb_course
(
couid 		int not null comment '编号',
couname 	varchar(50) not null comment '名称',
coucredit 	int not null comment '学分',
teaid 		int not null comment '授课老师',
primary key (couid),
foreign key (teaid) references tb_teacher (teaid)
);

-- 创建选课记录表
create table tb_record
(
recid 		int auto_increment comment '选课记录编号',
sid 		int not null comment '选课学生',
cid 		int not null comment '所选课程',
seldate 	datetime default now() comment '选课时间日期',
score 		decimal(4,1) comment '考试成绩',
primary key (recid),
foreign key (sid) references tb_student (stuid),
foreign key (cid) references tb_course (couid),
unique (sid, cid)
);
```

2. DML
```
-- 插入学院数据
insert into tb_college (collname, collintro) values 
('计算机学院', '计算机学院1958年设立计算机专业，1981年建立计算机科学系，1998年设立计算机学院，2005年5月，为了进一步整合教学和科研资源，学校决定，计算机学院和软件学院行政班子合并统一运作、实行教学和学生管理独立运行的模式。 学院下设三个系：计算机科学与技术系、物联网工程系、计算金融系；两个研究所：图象图形研究所、网络空间安全研究院（2015年成立）；三个教学实验中心：计算机基础教学实验中心、IBM技术中心和计算机专业实验中心。'),
('外国语学院', '四川大学外国语学院设有7个教学单位，6个文理兼收的本科专业；拥有1个一级学科博士授予点，3个二级学科博士授予点，5个一级学科硕士学位授权点，5个二级学科硕士学位授权点，5个硕士专业授权领域，同时还有2个硕士专业学位（MTI）专业；有教职员工210余人，其中教授、副教授80余人，教师中获得中国国内外名校博士学位和正在职攻读博士学位的教师比例占专任教师的60%以上。'),
('经济管理学院', '四川大学经济学院前身是创办于1905年的四川大学经济科；已故经济学家彭迪先、张与九、蒋学模、胡寄窗、陶大镛、胡代光，以及当代学者刘诗白等曾先后在此任教或学习；1905年，四川大学设经济科；1924年，四川大学经济系成立；1998年，四川大学经济管理学院变更为四川大学经济学院。');

-- 插入学生数据
insert into tb_student (stuid, stuname, stusex, stubirth, stuaddr, collid) values
(1001, '杨逍', 1, '1990-3-4', '四川成都', 1),
(1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
(1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
(1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
(1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
(2035, '东方不败', 1, '1988-6-30', null, 2),
(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
(3755, '项少龙', 1, '1993-1-25', null, 3),
(3923, '杨不悔', 0, '1985-4-17', '四川成都', 3),
(4040, '隔壁老王', 1, '1989-1-1', '四川成都', 2);

-- 删除学生数据
delete from tb_student where stuid=4040;

-- 更新学生数据
update tb_student set stuname='杨过', stuaddr='湖南长沙' where stuid=1001;

-- 插入老师数据
insert into tb_teacher (teaid, teaname, teatitle, collid) values 
(1122, '张三丰', '教授', 1),
(1133, '宋远桥', '副教授', 1),
(1144, '杨逍', '副教授', 1),
(2255, '范遥', '副教授', 2),
(3366, '韦一笑', '讲师', 3);

-- 插入课程数据
insert into tb_course (couid, couname, coucredit, teaid) values 
(1111, 'Python程序设计', 3, 1122),
(2222, 'Web前端开发', 2, 1122),
(3333, '操作系统', 4, 1122),
(4444, '计算机网络', 2, 1133),
(5555, '编译原理', 4, 1144),
(6666, '算法和数据结构', 3, 1144),
(7777, '经贸法语', 3, 2255),
(8888, '成本会计', 2, 3366),
(9999, '审计学', 3, 3366);

-- 插入选课数据
insert into tb_record (sid, cid, seldate, score) values 
(1001, 1111, '2017-09-01', 95),
(1001, 2222, '2017-09-01', 87.5),
(1001, 3333, '2017-09-01', 100),
(1001, 4444, '2018-09-03', null),
(1001, 6666, '2017-09-02', 100),
(1002, 1111, '2017-09-03', 65),
(1002, 5555, '2017-09-01', 42),
(1033, 1111, '2017-09-03', 92.5),
(1033, 4444, '2017-09-01', 78),
(1033, 5555, '2017-09-01', 82.5),
(1572, 1111, '2017-09-02', 78),
(1378, 1111, '2017-09-05', 82),
(1378, 7777, '2017-09-02', 65.5),
(2035, 7777, '2018-09-03', 88),
(2035, 9999, default, null),
(3755, 1111, default, null),
(3755, 8888, default, null),
(3755, 9999, '2017-09-01', 92);
```

```
-- 查询所有学生信息
select * from tb_student;

-- 查询所有课程名称及学分(投影和别名)
select couname, coucredit from tb_course;
select couname as 课程名称, coucredit as 学分 from tb_course;

-- 查询所有学生的姓名和性别(条件运算)
select stuname as 姓名, case stusex when 1 then '男' else '女' end as 性别 from tb_student;
select stuname as 姓名, if(stusex, '男', '女') as 性别 from tb_student;

-- 查询所有女学生的姓名和出生日期(筛选)
select stuname, stubirth from tb_student where stusex=0;

-- 查询所有80后学生的姓名、性别和出生日期(筛选)
select stuname, stusex, stubirth from tb_student where stubirth>='1980-1-1' and stubirth<='1989-12-31';
select stuname, stusex, stubirth from tb_student where stubirth between '1980-1-1' and '1989-12-31';

-- 查询姓"杨"的学生姓名和性别(模糊)
select stuname, stusex from tb_student where stuname like '杨%';

-- 查询姓"杨"名字两个字的学生姓名和性别(模糊)
select stuname, stusex from tb_student where stuname like '杨_';

-- 查询姓"杨"名字三个字的学生姓名和性别(模糊)
select stuname, stusex from tb_student where stuname like '杨__';

-- 查询名字中有"不"字或"嫣"字的学生的姓名(模糊)
select stuname, stusex from tb_student where stuname like '%不%' or stuname like '%嫣%';

-- 查询没有录入家庭住址的学生姓名(空值)
select stuname from tb_student where stuaddr is null;

-- 查询录入了家庭住址的学生姓名(空值)
select stuname from tb_student where stuaddr is not null;

-- 查询学生选课的所有日期(去重)
select distinct seldate from tb_record;

-- 查询学生的家庭住址(去重)
select distinct stuaddr from tb_student where stuaddr is not null;

-- 查询男学生的姓名和生日按年龄从大到小排列(排序)
select stuname as 姓名, datediff(curdate(), stubirth) div 365 as 年龄 from tb_student where stusex=1 order by 年龄 desc;

-- 查询年龄最大的学生的出生日期(聚合函数)
select min(stubirth) from tb_student;

-- 查询年龄最小的学生的出生日期(聚合函数)
select max(stubirth) from tb_student;

-- 查询男女学生的人数(分组和聚合函数)
select stusex, count(*) from tb_student group by stusex;

-- 查询课程编号为1111的课程的平均成绩(筛选和聚合函数)
select avg(score) from tb_record where cid=1111;

-- 查询学号为1001的学生所有课程的平均分(筛选和聚合函数)
select avg(score) from tb_record where sid=1001;

-- 查询每个学生的学号和平均成绩(分组和聚合函数)
select sid as 学号, avg(score) as 平均分 from tb_record group by sid;

-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- 分组以前的筛选使用where子句 / 分组以后的筛选使用having子句
select sid as 学号, avg(score) as 平均分 from tb_record group by sid having 平均分>=90;

-- 查询年龄最大的学生的姓名(子查询/嵌套的查询)
select stuname from tb_student where stubirth=( select min(stubirth) from tb_student );

-- 查询年龄最大的学生姓名和年龄(子查询+运算)
select stuname as 姓名, datediff(curdate(), stubirth) div 365 as 年龄 from tb_student where stubirth=( select min(stubirth) from tb_student );

-- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
select stuname from tb_student where stuid in ( select stuid from tb_record group by stuid having count(stuid)>2 );

-- 查询学生姓名、课程名称以及成绩(连接查询)
select stuname, couname, score from tb_student t1, tb_course t2, tb_record t3 where stuid=sid and couid=cid and score is not null;

-- 查询学生姓名、课程名称以及成绩按成绩从高到低查询第11-15条记录(内连接+分页)
select stuname, couname, score from tb_student inner join tb_record on stuid=sid inner join tb_course on couid=cid where score is not null order by score desc limit 5 offset 10;

select stuname, couname, score from tb_student inner join tb_record on stuid=sid inner join tb_course on couid=cid where score is not null order by score desc limit 10, 5;

-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
select stuname, avgmark from tb_student, ( select sid, avg(score) as avgmark from tb_record group by sid ) temp where stuid=sid;

select stuname, avgmark from tb_student inner join ( select sid, avg(score) as avgmark from tb_record group by sid ) temp on stuid=sid;

-- 查询每个学生的姓名和选课数量(左外连接和子查询)
select stuname, ifnull(total, 0) from tb_student left outer join ( select sid, count(sid) as total from tb_record group by sid ) temp on stuid=sid;
```

3. DCL

```
-- 创建可以远程登录的root账号并为其指定口令
create user 'root'@'%' identified by '123456';

-- 为远程登录的root账号授权操作所有数据库所有对象的所有权限并允许其将权限再次赋予其他用户
grant all privileges on *.* to 'root'@'%' with grant option;

-- 创建名为hellokitty的用户并为其指定口令
create user 'hellokitty'@'%' identified by '123123';

-- 将对school数据库所有对象的所有操作权限授予hellokitty
grant all privileges on school.* to 'hellokitty'@'%';

-- 召回hellokitty对school数据库所有对象的insert/delete/update权限
revoke insert, delete, update on school.* from 'hellokitty'@'%';
```

### 索引
索引是关系型数据库中用来提升查询性能最为重要的手段。关系型数据库中的索引就像一本书的目录，我们可以想象一下，如果要从一本书中找出某个知识点，但是这本书没有目录，这将是意见多么可怕的事情（我们估计得一篇一篇的翻下去，才能确定这个知识点到底在什么位置）。创建索引虽然会带来存储空间上的开销，就像一本书的目录会占用一部分的篇幅一样，但是在牺牲空间后换来的查询时间的减少也是非常显著的。

MySQL中，所有数据类型的列都可以被索引，常用的存储引擎InnoDB和MyISAM能支持每个表创建16个索引。InnoDB和MyISAM使用的索引其底层算法是B-tree（B树），B-tree是一种自平衡的树，类似于平衡二叉排序树，能够保持数据有序。这种数据结构能够让查找数据、顺序访问、插入数据及删除的操作都在对数时间内完成。

接下来我们通过一个简单的例子来说明索引的意义，比如我们要根据学生的姓名来查找学生，这个场景在实际开发中应该经常遇到，就跟通过商品名称查找商品道理是一样的。我们可以使用MySQL的explain关键字来查看SQL的执行计划。

##### 我们简单的为大家总结一下索引的设计原则：

- 最适合索引的列是出现在WHERE子句和连接子句中的列。
- 索引列的基数越大（取值多重复值少），索引的效果就越好。
- 使用前缀索引可以减少索引占用的空间，内存中可以缓存更多的索引。
- 索引不是越多越好，虽然索引加速了读操作（查询），但是写操作（增、删、改）都会变得更慢，因为数据的变化会导致索引的更新，就如同书籍章节的增删需要更新目录一样。
- 使用InnoDB存储引擎时，表的普通索引都会保存主键的值，所以主键要尽可能选择较短的数据类型，这样可以有效的减少索引占用的空间，利用提升索引的缓存效果。

最后，还有一点需要说明，InnoDB使用的B-tree索引，数值类型的列除了等值判断时索引会生效之外，使用>、<、>=、<=、BETWEEN...AND... 、<>时，索引仍然生效；对于字符串类型的列，如果使用不以通配符开头的模糊查询，索引也是起作用的，但是其他的情况会导致索引失效，这就意味着很有可能会做全表查询。

### 视图

视图是关系型数据库中将一组查询指令构成的结果集组合成可查询的数据表的对象。简单的说，视图就是虚拟的表，但与数据表不同的是，数据表是一种实体结构，而视图是一种虚拟结构，你也可以将视图理解为保存在数据库中被赋予名字的SQL语句。

使用视图可以获得以下好处：

1. 可以将实体数据表隐藏起来，让外部程序无法得知实际的数据结构，让访问者可以使用表的组成部分而不是整个表，降低数据库被攻击的风险。
2. 在大多数的情况下视图是只读的（更新视图的操作通常都有诸多的限制），外部程序无法直接透过视图修改数据。
3. 重用SQL语句，将高度复杂的查询包装在视图表中，直接访问该视图即可取出需要的数据；也可以将视图视为数据表进行连接查询。
4. 视图可以返回与实体数据表不同格式的数据，

## 几个重要的概念
### 范式理论 - 设计二维表的指导思想
第一范式：数据表的每个列的值域都是由原子值组成的，不能够再分割。
第二范式：数据表里的所有数据都要和该数据表的键（主键与候选键）有完全依赖关系。
第三范式：所有非键属性都只和候选键有相关性，也就是说非键属性之间应该是独立无关的。

### 数据完整性
1. 实体完整性 - 每个实体都是独一无二的
  主键（primary key） / 唯一约束 / 唯一索引（unique）
2. 引用完整性（参照完整性）- 关系中不允许引用不存在的实体
  外键（foreign key）
3. 域完整性 - 数据是有效的
- 数据类型及长度
- 非空约束（not null）
- 默认值约束（default）
- 检查约束（check）

### 数据一致性
1. 事务：一系列对数据库进行读/写的操作，这些操作要么全都成功，要么全都失败。
2. 事务的ACID特性
- 原子性：事务作为一个整体被执行，包含在其中的对数据库的操作要么全部被执行，要么都不执行
- 一致性：事务应确保数据库的状态从一个一致状态转变为另一个一致状态
- 隔离性：多个事务并发执行时，一个事务的执行不应影响其他事务的执行
- 持久性：已被提交的事务对数据库的修改应该永久保存在数据库中
3. MySQL中的事务操作
开启事务环境
```
start transaction
或
begin
```
提交事务
```
commit
```
回滚事务
```
rollback
```