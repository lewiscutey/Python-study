"""
软件安装和配置
"""

"""
使用包管理工具
"""
1. yum - Yellowdog Updater Modified。
2. rpm - Redhat Package Manager。


"""
下载解压配置环境变量
"""
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-3.6.5.tgz
gunzip mongodb-linux-x86_64-rhel70-3.6.5.tgz
tar -xvf mongodb-linux-x86_64-rhel70-3.6.5.tar
export PATH=$PATH:$HOME/bin:$HOME/mongodb-linux-x86_64-rhel70-3.6.5/bin
mongod --version

"""
源代码构建安装
"""
1. 安装Python 3.6。

[root ~]# yum install gcc
[root ~]# wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
[root ~]# gunzip Python-3.6.5.tgz
[root ~]# tar -xvf Python-3.6.5.tar
[root ~]# cd Python-3.6.5
[root ~]# ./configure --prefix=/usr/local/python36 --enable-optimizations
[root ~]# yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
[root ~]# make && make install
...
[root ~]# ln -s /usr/local/python36/bin/python3.6 /usr/bin/python3
[root ~]# python3 --version
Python 3.6.5
[root ~]# python3 -m pip install -U pip
[root ~]# pip3 --version

2. 安装Redis-3.2.12。
[root ~]# wget http://download.redis.io/releases/redis-3.2.12.tar.gz
[root ~]# gunzip redis-3.2.12.tar.gz
[root ~]# tar -xvf redis-3.2.12.tar
[root ~]# cd redis-3.2.12
[root ~]# make && make install
[root ~]# redis-server --version
Redis server v=3.2.12 sha=00000000:0 malloc=jemalloc-4.0.3 bits=64 build=5bc5cd3c03d6ceb6
[root ~]# redis-cli --version
redis-cli 3.2.12

3. 配置服务
 1. 启动防火墙服务：systemctl start firewalld
 2. 终止防火墙服务：systemctl stop firewalld
 3. 重启防火墙服务：systemctl restart firewalld
 4. 查看防火墙服务状态：systemctl status firewalld
 5. 设置/禁用防火墙服务开机自启: systemctl enable firewalld | systemctl disable firewalld

4. 计划任务
 1. 在指定的时间执行命令。
    at - 将任务排队，在指定的时间执行。
    atq - 查看待执行的任务队列。
    atrm - 从队列中删除待执行的任务。

 2. 计划任务表 - crontab。

5. 网络访问和管理
 1. 安全远程连接 - ssh。
 2. 通过网络获取资源 - wget。
 3. 发送和接收邮件 - mail。
 4. 网络配置工具（旧） - ifconfig。
 5. 网络配置工具（新） - ip。
 6. 网络可达性检查 - ping。
 7. 显示或管理路由表 - route。
 8. 查看网络服务和端口 - netstat / ss。
 9. 网络监听抓包 - tcpdump。
 10. 安全文件拷贝 - scp。
 11. 文件同步工具 - rsync。
 12. 安全文件传输 - sftp。


 """
 进程管理
 """
 1. 查看进程 - ps。
 2. 显示进程状态树 - pstree。
 3. 查找与指定条件匹配的进程 - pgrep。
 4. 通过进程号终止进程 - kill。
 5. 通过进程名终止进程 - killall / pkill。
 6. 将进程置于后台运行。
 7. 查询后台进程 - jobs。
 8. 让进程在后台继续运行 - bg。
 9. 将后台进程置于前台 - fg。
 10. 调整程序/进程运行时优先级 - nice / renice。
 11. 用户登出后进程继续工作 - nohup。
 12. 跟踪进程系统调用情况 - strace。
 13. 查看当前运行级别 - runlevel。
 14. 实时监控进程占用资源状况 - top。


"""
系统诊断
"""
1. 系统启动异常诊断 - dmesg。
2. 查看系统活动信息 - sar。
3. 查看内存使用情况 - free。
4. 虚拟内存统计 - vmstat。
5. CPU信息统计 - mpstat。
6. 查看进程使用内存状况 - pmap。
7. 报告设备CPU和I/O统计信息 - iostat。
8. 显示所有PCI设备 - lspci。
9. 显示进程间通信设施的状态 - ipcs。


"""
Shell编程
"""
例子1：输入两个整数m和n，计算从m到n的整数求和的结果。

#!/usr/bin/bash
printf 'm = '
read m
printf 'n = '
read n
a=$m
sum=0
while [ $a -le $n ]
do
    sum=$[ sum + a ]
    a=$[ a + 1 ]
done
echo '结果: '$sum


例子2：自动创建文件夹和指定数量的文件。

#!/usr/bin/bash
printf '输入文件夹名: '
read dir
printf '输入文件名: '
read file
printf '输入文件数量(<1000): '
read num
if [ $num -ge 1000 ]
then
    echo '文件数量不能超过1000'
else
    if [ -e $dir -a -d $dir ]
    then
        rm -rf $dir
    else
        if [ -e $dir -a -f $dir ]
        then
            rm -f $dir
        fi
    fi
    mkdir -p $dir
    index=1
    while [ $index -le $num ]
    do
        if [ $index -lt 10 ]
        then
            pre='00'
        elif [ $index -lt 100 ]
        then
            pre='0'
        else
            pre=''
        fi
        touch $dir'/'$file'_'$pre$index
        index=$[ index + 1 ]
    done
fi


例子3：自动安装指定版本的Redis。

#!/usr/bin/bash
install_redis() {
    if ! which redis-server > /dev/null
    then
        cd /root
        wget $1$2'.tar.gz' >> install.log
        gunzip /root/$2'.tar.gz'
        tar -xf /root/$2'.tar'
        cd /root/$2
        make >> install.log
        make install >> install.log
        echo '安装完成'
    else
        echo '已经安装过Redis'
    fi
}

install_redis 'http://download.redis.io/releases/' $1


"""
相关资源
"""
1. Linux命令行常用快捷键

快捷键	功能说明
tab	自动补全命令或路径
Ctrl+a	将光标移动到命令行行首
Ctrl+e	将光标移动到命令行行尾
Ctrl+f	将光标向右移动一个字符
Ctrl+b	将光标向左移动一个字符
Ctrl+k	剪切从光标到行尾的字符
Ctrl+u	剪切从光标到行首的字符
Ctrl+w	剪切光标前面的一个单词
Ctrl+y	复制剪切命名剪切的内容
Ctrl+c	中断正在执行的任务
Ctrl+h	删除光标前面的一个字符
Ctrl+d	退出当前命令行
Ctrl+r	搜索历史命令
Ctrl+g	退出历史命令搜索
Ctrl+l	清除屏幕上所有内容在屏幕的最上方开启一个新行
Ctrl+s	锁定终端使之暂时无法输入内容
Ctrl+q	退出终端锁定
Ctrl+z	将正在终端执行的任务停下来放到后台
!!	执行上一条命令
!数字	执行数字对应的历史命令
!字母	执行最近的以字母打头的命令
!$ / Esc+.	获得上一条命令最后一个参数
Esc+b	移动到当前单词的开头
Esc+f	移动到当前单词的结尾

2. man查阅命令手册的内容说明

手册中的标题	功能说明
NAME	命令的说明和介绍
SYNOPSIS	使用该命令的基本语法
DESCRIPTION	使用该命令的详细描述，各个参数的作用，有时候这些信息会出现在OPTIONS中
OPTIONS	命令相关参数选项的说明
EXAMPLES	使用该命令的参考例子
EXIT STATUS	命令结束的退出状态码，通常0表示成功执行
SEE ALSO	和命令相关的其他命令或信息
BUGS	和命令相关的缺陷的描述
AUTHOR	该命令的作者介绍