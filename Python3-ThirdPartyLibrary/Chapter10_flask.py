# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)  # 实例化Flask类


@app.route("/")  # 告知函数的URL（http://127.0.0.1:5000/）给app
def hello():
    return "Hello World!"


@app.route("/powers")  # 告知函数的URL（http://127.0.0.1:5000/powers）给app
def powers(n=10):
    """计算幂"""
    return ', '.join(str(2**i) for i in range(n))


@app.route("/square/<int:n>")  # 告知函数的URL给app
def square(n):
    """计算平方"""
    return str(n*n)


if __name__ == "__main__":
    app.run()


# ### 脚本说明
# 使用Flask创建极简的Web应用；
#
# ### 执行脚本
# 1-在命令行下执行“py -3 Chapter10_flask.py”，显示结果如下：
#   * Serving Flask app "TempTest" (lazy loading)
#   * Environment: production
#     WARNING: Do not use the development server in a production environment.
#     Use a production WSGI server instead.
#   * Debug mode: off
#   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
# 2-在浏览器打开“http://127.0.0.1:5000/”页面，将看到函数hello的返回结果；
# 3-在浏览器打开“http://127.0.0.1:5000/powers”页面，将看到函数powers的返回结果；
# 4-在浏览器打开“http://127.0.0.1:5000/square/9”页面，将看到square(9)的返回结果；
#
# ### @app.route()
# 可以通过@app.route()来设置多个函数，每个函数的URL各不相同；
# 可以使用尖括号指定参数，也能执行参数类型转换，例如：@app.route("/square/<int:n>")；
#
# ### Flask
# 简单又实用的Flask，适用于较复杂的服务端Web应用开发；
# A simple framework for building complex web applications.
# Home-page: https://www.palletsprojects.com/p/flask/
# Documentation：http://flask.pocoo.org/docs/
