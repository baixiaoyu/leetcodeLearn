import configparser

# 初始化
conf = configparser.ConfigParser()
# 读取配置文件
conf.read('test.cnf', encoding='utf-8')

# 获得配置文件中的所有sections
print(conf.sections())
# section是区分大小写的，写成小写会被认为不存在
print(conf.has_section('mysql'))

# 获取section = Mysql 下的所有options，即keys
print(conf.options('Mysql'))
# option 不区分大小写，判断结果为True
print(conf.has_option('Mysql', 'DATABASE'))

# 获取section = Mysql 下的所有键值对
print(conf.items('Mysql'))

# 获取section=Mysql下host键对应的value值
# get方法通过不同类型，存在getint、getfloat、getboolean 不同的类型
# 其中getboolean 可以识别 true/false、 1/0、yes/no、 on/off
print(conf.get('Mysql', 'host'))
print(conf.getboolean('Mysql', 'status'))


