# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:47:55 2020

@author: Administrator
"""



file=['original/test.txt','result/0.pre/text1.txt','result/0.pre/text2.txt','result/1.javadoc/text@.txt','result/2.html/text_html.txt','result/3.nonASC/text_nonASC.txt','result/4.nonEng/text_nonEng.txt','result/5.internet_address/text_address.txt','result/6.short_words/text_short.txt','result/7.meaningless_words/text_meaningless.txt']

def inter_address(s):  #判断是否包含网址链接
    if('https://' in s):
        return True
    else:
        return False

def elimenate_javadoc(s):  #是否包含javadoc标志 
    import re
    if(re.search('@[a-z]+',s)):
        return True
    else:
        return False
    
def get_first_sentence(docstring):   #获取注释第一句
    import re
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
    import re
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
    import re
    global_black_list = ['return','Return','this','that','This','That','Them','them']
    first_black_list = ['set','get','Get','Set','Add','add','Sets','sets','gets','Gets']
    splitted1 = s.split()[0]
    
    if(re.search('|'.join(global_black_list), s)):
        return True

    if re.search('|'.join(first_black_list), splitted1):
        return True
    else:
        return False
    

def auto_filter():
    count=0
    count1=0 
    count2=0 
    count3=0 
    count4=0 
    count5=0 
    count6=0 
    count7=0 
    total_num=0
    i=0
    while (i<=9):
        if(i==0):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                count=count+1
                print(count)
                f.write(get_first_sentence(line))
                f.write('\r\n')
            fp.close()
            f.close()
        if(i==1):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:           
                if(line=='\n'):
                    line = line.strip("\n")
                f.write(line)                
            fp.close()
            f.close()
        if(i==2):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                if(elimenate_javadoc(line)):
                    count1=count1+1
                    print(count1,'yes1')      
                    continue
                f.write(line)
            fp.close()
            f.close()
        if(i==3):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                if(eliminate_tags_of_html(line)):
                    count2=count2+1
                    print(count2,'yes2')      
                    continue
                f.write(line)
            fp.close()
            f.close()
        if(i==4):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                if(is_ASC(line)):
                    count3=count3+1
                    print(count3,'yes3')      
                    continue
                f.write(line)
            fp.close()
            f.close()     
        if(i==5):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                if(none_English(line)):
                    count4=count4+1
                    print(count4,'yes4')      
                    continue
                f.write(line)
            fp.close()
            f.close()  
        if(i==6):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                if(inter_address(line)):
                    count5=count5+1
                    print(count5,'yes5')      
                    continue
                f.write(line)
            fp.close()
            f.close()
        if(i==7):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                if(short_words(line)):
                    count6=count6+1
                    print(count6,'yes6')      
                    continue
                f.write(line)
            fp.close()
            f.close()
        if(i==8):
            fp = open(file[i],'r',encoding='UTF-8')
            f = open(file[i+1],'w',encoding='UTF-8')
            for line in fp:
                if(meaningless_words(line)):
                    count7=count7+1
                    print(count7,'yes7')      
                    continue
                f.write(line)
            fp.close()
            f.close()
        if(i==9):
            fp = open(file[i],'r',encoding='UTF-8')
            for line in fp:
                total_num=total_num+1
            fp.close()
        i=i+1  
    num_dict={"count1":count1,"count2":count2,"count3":count3,"count4":count4,"count5":count5,"count6":count6,"count7":count7,"total_num":total_num}
    print(num_dict)
    num_list=[count1,count2,count3,count4,count5,count6,count7,total_num]
    return num_list


import openpyxl

num_dict=auto_filter()

workbook=openpyxl.load_workbook("result/统计结果.xlsx")
worksheet=workbook.worksheets[0]
for i in range(2,10):  
    worksheet.cell(i,4,num_dict[i-2])
workbook.save(filename="result/统计结果.xlsx")

        
    

