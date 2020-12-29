# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:47:55 2020

@author: Administrator
"""

def inter_address(s):  #判断是否包含网址链接
    if('https://' in s):
        return True
    else:
        return False

def elimenate_javadoc(s):  #是否包含javadoc标志
    if(re.search('@[a-z]+',line)):
        return True
    else:
        return False
    
def get_first_sentence(docstring):   #获取注释第一句
    docstring = re.split(r'[.\n\r]',docstring.strip('\n'))[0]
    return docstring

def is_ASC(s):  #是否包含非英文字符
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return True
    else:
        return False

def none_English(s):     #是否不包含任何英文字符
    import re
    if(re.search('[a-zA-Z]', s)):
        return False
    else:
        return True
    
def eliminate_tags_of_html(s):     #是否包含html标签
    if (re.search('</?[^>]+>', s)):
        return True
    else:
        return False
    
def short_words(s):    #是否少于3个单词
    a = s.split()
    if (len(a)<=2):
        return True
    else:
        return False
    
def meaningless_words(s):   #以get,set,return开头或注释中包含this,that等指代词
    global_black_list = ['return','Return','this','that','This','That','Them','them']
    first_black_list = ['set','get','Get','Set','Add','add','Sets','sets','gets','Gets']
    splitted1 = s.split()[0]
    
    if(re.search('|'.join(global_black_list), s)):
        return True

    if re.search('|'.join(first_black_list), splitted1):
        return True
    else:
        return False
    

import re


count=0 


fp = open('text_short.txt','r',encoding='UTF-8')
f = open('text_meaningless.txt','w',encoding='UTF-8')


for line in fp:
    if(meaningless_words(line)):
        count=count+1
        print(count,'yes')      
        continue
    f.write(line)
        
    
print('the number of count',count)

fp.close()
f.close()