FROM python:3.10
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo "Asia/Shanghai" > /etc/timezone
COPY . /code
WORKDIR /code
RUN export $(cat .env | xargs)
RUN pip install --upgrade pip  -i https://pypi.mirrors.ustc.edu.cn/simple/
RUN pip install -r requirements/production.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list
RUN  apt-get clean

RUN apt-get update -qqy && apt-get install -y netcat

EXPOSE 5000

CMD ["/bin/bash", "bin/startup.sh"]
