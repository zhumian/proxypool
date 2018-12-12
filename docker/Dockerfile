FROM python:3.7
LABEL proxypool=1.0
MAINTAINER zhumian liuchikit@foxmail.com

# 指定时区，使docker容器与宿主机时间同步
ENV TZ Asia/Shanghai

WORKDIR /usr/workspace/proxypool

# 将上层目录下的文件拷贝到[WORKDIR]目录下
COPY . .

WORKDIR /usr/workspace/proxypool

# 安装python模块
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口
EXPOSE 9000

# 运行要执行的命令
CMD [ "python", "main.py" ]



