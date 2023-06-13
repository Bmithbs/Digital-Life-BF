FROM neuralink/neuralink/digital-life-dev

LABEL maintainer="hubmithbu@163.com"


RUN apt-get update 



# 构建必要的依赖
RUN apt-get install -y python3-pyqt5 

# 指的是在容器中创建一个目录，用来存放我们的项目代码
WORKDIR /app 

# 指的是将当前目录下的所有文件拷贝到容器中的/app目录下
ADD . /app
RUN python3 -m pip install --upgrade pip

# 安装依赖时用国内的镜像
# RUN python3 -m pip install edge-tts~=6.1.3 -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN python3 -m pip install --no-cache-dir -r requirements-docker.txt

EXPOSE 5000

CMD ["python3", "main.py"]