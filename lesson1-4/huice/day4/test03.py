import json

json_text = "{'name': 'xiaoming', 'age': '20', 'height': '174.2', 'is_married': 'True', 'sroce': 'None'}"

json_object = json.loads(json_text.replace('\'', '\"'))
print(type(json_object), json_object)



mobile_json = "{'mts':'1380138',\
'province':'北京',\
'catName':'中国移动',\
'telString':'13801380000',\
'areaVid':'29400',\
'ispVid':'3236139',\
'carrier':'北京移动'}"

json_object = json.loads(mobile_json.replace('\'', '\"'), encoding="utf-8")
print(json_object)

for key, value in list(json_object.items()):
    print(key, ' ', value)


stu1 = {'name': 'xiaoming', 'age': 20, 'height': 174.2, 'is_married': True, 'sroce': None}
json_stu1 = json.dumps(stu1)
dic = json.loads(json_stu1)
for key, value in list(json_object.items()):
    print(type(key), ' ', type(value))


# 自定义对象
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return '<MyObj(%s)(%d)>' % (self.name, self.age)

obj = Student('tiantian', 50)

#转换函数
def convert_to_builtin_type(obj):
    print('default(', repr(obj), ')')
    # 把Student对象转换成dict类型的对象
    d = { 'name':obj.name,
          'age':obj.age,
        }
    d.update(obj.__dict__)
    return d

json_str = json.dumps(obj, default=convert_to_builtin_type)
print(type(json.loads(json_str)), json_str)


def dict_to_object(d):
    # 写法一:
    stu = eval('Student(d["name"], d["age"])')

    # 写法二:
    #module = __import__(module_name)
    #class_ = getattr(module, class_name)
    #args = dict((key.encode('ascii'),value) for key,value in d.items())
    #inst = class_(**args)
    return stu

student_instance = json.loads(json_str, object_hook=dict_to_object)
print(type(student_instance), student_instance, student_instance.age)


d1 = json.load(open('mobile.json','r'))
print((d1, type(d1)))

show_json = '''
{"xAxis":["business_autoFans_J","autoAX","autoAX_admin"],"yAxis":[{"2016_08":[14,7,16],"2016_09":[0,13,12],"2016_10":[24,15,7]},{"2016_08":[0,0,5],"2016_09":[32,31,17],"2016_10":[22,22,9]}, {"2016_08":[0,7,10],"2016_09":[0,0,0],"2016_10":[5,13,2]}]}	
'''
show_data = json.loads(show_json)
print(type(show_data))

def search_by_month(data, month):
    show_data = json.loads(data)
    project_name = show_data['xAxis']
    bug_number = []
    for data in show_data['yAxis']:
        sum = 0
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)

        for bug in data['2016_%s' % month]:
            sum += int(bug)
        bug_number.append(sum)

    bug_total = dict(list(zip(project_name, bug_number)))
    return bug_total

print(search_by_month(show_json, 9))