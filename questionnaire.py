#coding=utf-8
#functional:从csv文件统计调查数据
#data from web:http://www.zuopiezi.org/answer/answers.Asp
#author：Linpan From www.zuopiezi.org
#time:2015-7-18
#email:yidiyu0507s@163.com
#DATA_TIME:From 2015-07-17

import  csv
import re

'''
单独测试选项值数据：
#dict={'c1':u'是','c2':u'不是','c3':u'不知道','c4':u'其他'}
#dict={'c1':u'会','c2':u'会点 ','c3':u'一点不会','c4':u'两手都会'}
#dict={'c1':u'有','c2':u'没有 ','c3':u'不知道 ','c4':u'没有关心过'}
#dict={'c1':u'支持','c2':u'纠正','c3':u'无所谓','c4':u'不好说,看情况'}
#dict={'c1':u'左手','c2':u'右手','c3':u'两手都可以','c4':u'不知道'}
#dict={'c1':u'会点，但不熟练','c2':u'一直都是','c3':u'只会用右手','c4':u'被纠正过来了'}
#dict={'c1':u'我是幸福的','c2':u'喜忧参半','c3':u'我是自豪的','c4':u'有时比较痛苦'}
#dict={'c1':u'没感觉到','c2':u'有点创新','c3':u'想法经常和别人不同','c4':u'不管聪明否，至少在人生激励着我'}
#dict={'c1':u'好奇','c2':u'兴趣','c3':u'不会','c4':u'保留，我已经习惯原来的'}
#dict={'c1':u'家里有左撇子','c2':u'家人是，我不是','c3':u'我亲戚有的是','c4':u'朋友是'}
#dict={'c1':u'立即纠正因为自古都是右手写字','c2':u'和家长沟通看他们的态度','c3':u'和家长沟通看他们的态度观察一段时间后让孩子自己来决定','c4':u'支持孩子因为世界存在差异性'}
'''
dict={'question1':{'c1':u'是','c2':u'不是','c3':u'不知道','c4':u'其他'},'question2': {'c1':u'会','c2':u'会点 ','c3':u'一点不会','c4':u'两手都会'},\
    'question3':{'c1':u'有','c2':u'没有','c3':u'不知道','c4':u'没有关心过'},'question4':{'c1':u'支持','c2':u'纠正','c3':u'无所谓','c4':u'不好说，看情况'},\
    'question5':{'c1':u'左手','c2':u'右手','c3':u'两手都可以','c4':u'不知道'},'question6':{'c1':u'会点,但不熟练','c2':u'一直都是','c3':u'只会用右手','c4':u'被纠正过来了'},\
    'question7':{'c1':u'我是幸福的','c2':u'喜忧参半','c3':u'我是自豪的','c4':u'有时比较痛苦'},'question8':{'c1':u'没感觉到','c2':u'有点创新','c3':u'想法经常和别人不同','c4':u'不管聪明否,至少在人生激励着我'},\
    'question9':{'c1':u'好奇','c2':u'兴趣','c3':u'不会','c4':u'保留,我已经习惯原来的'},'question10':{'c1':u'家里有左撇子','c2':u'家人是,我不是','c3':u'我亲戚有的是','c4':u'朋友是'},\
    'question11':{'c1':u'立纠正因为自古都是右手写字','c2':u'和家长沟通看他们的态度','c3':u'和家长沟通看他们的态度观察一段时间后让孩子自己来决定','c4':u'支持孩子因为世界存在差异性'}}
def get_rows_values(i):
    p=u"[\u4e00-\u9fa5]+" #匹配中文部分，过滤其他字符。
    cA,cB,cC,cD=0,0,0,0

    with open('c:\qr.csv','rb')as f:
        reader=csv.reader(f)
        c=[title[i].decode('gb2312') for title in reader]

    match = [re.findall(u"[\u4e00-\u9fa5]+",x) for x in c]
    baseno='question'+str(i)
    for x in match:
        dstr = ('').join(x)
        if dstr==dict[baseno]['c1']:
            cA+=1
        elif dstr==dict[baseno]['c2']:
            cB+=1
        elif dstr==dict[baseno]['c3']:
            cC+=1
        elif dstr==dict[baseno]['c4']:
            cD+=1

    print dict[baseno]['c1']+":",cA
    print dict[baseno]['c2']+":",cB
    print dict[baseno]['c3']+":",cC
    print dict[baseno]['c4']+":",cD


if __name__=="__main__":
    for i in range(1,11):
        print "第%s道问卷结果为:"%i
        get_rows_values(i)
        print '\n'



























