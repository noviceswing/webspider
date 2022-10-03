## Beautiful Soup 4
### 用途：
+ 从HTML或XML提取数据（解析器）
### 操作文档树
+ soup.name获得tag的name
  这是个获取tag的小窍门,可以在文档树的tag中多次调用这个方法.下面的代码可以获取<body>标签中的第一个<b>标签:
+ soup.contents将tag以列表形式输出
+ 
### 关注点
+ 得到的是BeautifulSoup对象，按照标准格式输出
+ HTML主要标签
  + <head> <title> <a>
+ 浏览结构化数据的方法
    1. soup.find_all()
    2. soup.find(id = '') #可以直接定位到id
+ 获取文字内容
  + soup.get_text()
+ 支持第三方解析器
  + 推荐使用lxml
+ beautifulsoup将html转换成树形结构
  + Tag对象
    1. tag.name(tag的name)
    2. tag.attrs(tag中的属性, 操作方法与字典相同)
  + NavigableString对象(包装tag中的字符串)
    1. tag.string
  + BeautifulSoup对象
    + 表示的是一个文档的全部内容.大部分时候,可以把它当作 Tag 对象
  + comment对象
    + 是一种特殊类型的NavigableString对象
