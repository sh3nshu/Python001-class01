相关链接
《提问的智慧》： https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/master/README-zh_CN.md
Python 3.7.7 官方文档： https://docs.python.org/zh-cn/3.7/
GitHub 搜索帮助： https://help.github.com/cn/github/searching-for-information-on-github
PEP8： https://www.python.org/dev/peps/pep-0008/
Google Python Style Guides： http://google.github.io/styleguide/pyguide.html

------------
常用 pip 源地址
豆瓣： https://pypi.doubanio.com/simple/
清华： https://mirrors.tuna.tsinghua.edu.cn/help/pypi/
中科大： https://pypi.mirrors.ustc.edu.cn/simple/
阿里云： https://mirrors.aliyun.com/pypi/simple/
修改方式
临时替换
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
永久替换（先升级 pip：pip install pip -U ）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

-----------
虚拟环境和包
https://docs.python.org/zh-cn/3.7/tutorial/venv.html

---------
如果之前没有 Python 编程经验，请在预习周尽快熟悉下 Python 基础语法。
Python 标准语法： https://docs.python.org/zh-cn/3.7/tutorial/index.html
Python 内置函数： https://docs.python.org/zh-cn/3.7/library/functions.html
Python 内置类型： https://docs.python.org/zh-cn/3.7/library/stdtypes.html
Python 数据类型： https://docs.python.org/zh-cn/3.7/library/datatypes.html
Python 标准库： https://docs.python.org/zh-cn/3.7/library/index.html
Python 计算器使用： https://docs.python.org/zh-cn/3.7/tutorial/introduction.html
Python 数据结构： https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html
Python 其他流程控制工具 : https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html
Python 中的类： https://docs.python.org/zh-cn/3.7/tutorial/classes.html
Python 定义函数： https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions
再此之外，如果想快速了解并掌握爬虫的知识，还需要有 HTML（超文本标记语言）的基础哦
HTML 标准语法： https://developer.mozilla.org/zh-CN/docs/Web/HTML
HTML 元素参考： https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element
HTML 属性参考： https://developer.mozilla.org/zh-CN/docs/Web/HTML/Attributes
HTML 全局属性： https://developer.mozilla.org/zh-CN/docs/Web/HTML/Global_attributes
HTML 链接类型： https://developer.mozilla.org/zh-CN/docs/Web/HTML/Link_types
-------
requests 官方文档链接： https://requests.readthedocs.io/zh_CN/latest/
Beautiful Soup 官方文档链接： https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
W3C 标准官方文档：
https://www.w3.org/standards/


---------
Python 简介： https://docs.python.org/zh-cn/3.7/tutorial/introduction.html
Python 数据结构： https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html
Python 其他流程控制工具 : https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html
Python 中的类： https://docs.python.org/zh-cn/3.7/tutorial/classes.html
Python 定义函数： https://docs.python.org/zh-cn/3.7/tutorial/controlflow.html#defining-functions

-----------
Scrapy 架构官方文档介绍： https://docs.scrapy.org/en/latest/topics/architecture.html
1. 获取课程源码操作方法
切换分支：git checkout 2c
2. Scrapy Xpath 官方学习文档： https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths
3. Xpath 中文文档：https://www.w3school.com.cn/xpath/index.asp
4. Xpath 英文文档：https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf
5. 补充说明：
12 分 32 秒处“打印的选择器信息用 元祖 括起来”，此处有一点小的问题，相信细心的同学已经察觉到了，注意我们需把 元祖 改成 列表。
18 分 18 秒处视频中讲述 “ dont_filter 设置为 True 后，不会受到 allowed_domains 的限制”。更正为 dont_filter 设置为 True，是用来解除去重功能。Scrapy 自带 url 去重功能，第二次请求之前会将已发送的请求自动进行过滤处理。所以将 dont_filter 设置为 True 起到的作用是解除去重功能，一旦设置成重 True，将不会去重，直接发送请求。
相信细心的同学们已经发现了这些小问题，稍后我们会对课程及视频进行相应的修订，望周知哦！
----------
1. 获取课程源码操作方法
切换分支：git checkout 2d
2. yield 表达式官方文档：https://docs.python.org/zh-cn/3.7/reference/expressions.html#yieldexpr
3. yield 语句官方文档：https://docs.python.org/zh-cn/3.7/reference/simple_stmts.html#yield
4. Python 推导式官方文档：https://docs.python.org/zh-cn/3.7/tutorial/datastructures.html#list-comprehensions
5. 补充说明：
视频中老师所讲 yield 返回的是单独的一个值，更准确的说返回的值必须是对象，在此章节我们暂定只把它理解返回一个值。在后面的章节多线程部分，我们会结合课程再对 yield 进行详解。

-----------
http://toscrape.com  这个网站专门用于爬虫爬取数据的练习网站
