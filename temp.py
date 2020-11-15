# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import requests
 
# Пакет для удобной работы с данными в формате json
import json
 
# Модуль для работы со значением времени
import time
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import datetime
selected_name=['Дизайнер', 'Администратор', 'Программист', 'Инженер', 'Разработчик','Data']
  
def getPage(page,name,n):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """
    s_to=str(n)+'-12-31'
    s_from=str(n)+'-01-01'
    dt_from=datetime.datetime.strptime(s_from,'%Y-%m-%d')
    dt_to=datetime.datetime.strptime(s_to,'%Y-%m-%d')
    u_from=dt_from.timestamp()
    u_to=dt_to.timestamp()

    # Справочник для параметров GET-запроса
    params = {
        'keyword': str(name), # Текст фильтра.
        'noGeo':1,
        'page':page,
        'count': 100,
        'period':0,
        'date_published_from': u_from,
        'date_published_to':u_to,
        'app_key':'v3.r.133211559.385b635e778ad36f73b6f71ab80f0591418c6274.2263c696de727f070798dda03b19d7ab04354268',
        'authorization':'v3.r.133211559.dbc83a4042088f343b0677517b5faf33ca774cce.bdf4021e4048b7435a066e2c86f813dac5f18f39'
    }
     
     
    req = requests.get('https://api.superjob.ru/2.0/vacancies/', params) # Посылаем запрос к API
    data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data

def consoleLog(a,b):
    res1=[]
    res2=[]
    for i in range (0,len(a)):
        k=b.pop()
        res1.append(k)
        res2.append(a.count(k)*12)
        print(k+' '+str(a.count(k)*12))
        if (len(b)==0):
            break
    return res1,res2
        
def Diction(word):
    b=word.split()
    for i in range(0,len(b)):
        
        if (b[i].find('-')>0):
            k=b.pop(i)
            m=k.split('-')
            c=0;
            for j in range (i,i+len(m)):
                b.insert(j,m[c])
                c=c+1
    for i in range(0,len(b)):
        if (b[i].find('/')>0):
            k=b.pop(i)
            m=k.split('/')
            c=0;
            for j in range (i,i+len(m)):
                b.insert(j,m[c])
                c=c+1
    for i in range(0,len(b)):
        if (b[i].find('(')>0):
            k=b.pop(i)
            m=k.split('(')
            c=0;
            for j in range (i,i+len(m)):
                b.insert(j,m[c])
                c=c+1
    for i in range(0,len(b)):
        if (b[i].find(')')>0):
            k=b.pop(i)
            m=k.split(')')
            c=0;
            for j in range (i,i+len(m)):
                b.insert(j,m[c])
                c=c+1
    
    if(b.count('C++')>0 or b.count('c++')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='C++ разработчик'
    elif(b.count('C#')>0 or b.count('c#')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='C# разработчик'
    elif(b.count('C')>0 or b.count('c')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='C разработчик'
    elif((b.count('C')>0 or b.count('c')>0) and (b.count('Objective')>0)\
         or b.count('objective')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Objective-C разработчик'
    elif(b.count('Java')>0 or b.count('java')>0 or b.count('JAVA')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Java разработчик'   
    elif(b.count('Python')>0 or b.count('python')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Python разработчик'  
    elif(b.count('R')>0 or b.count('r')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='R разработчик'  
    elif(b.count('JS')>0 or b.count('js') or b.count('javascript')>0 or b.count ('JavaScript')>0\
       or b.count('javaScript')>0) and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='JS разработчик'
    elif(b.count('C#')>0 or b.count('c#')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='C# разработчик'
    elif(b.count('PHP')>0 or b.count('php')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='PHP разработчик'
    elif(b.count('Frontend')>0 or b.count('Front')>0 or b.count('frontend')>0 or b.count('Front-end')>0\
         or b.count('front-end')>0 or b.count('Фронтэнд')>0 or\
         b.count('фронтэнд')>0 or b.count('фронтенд')>0 or\
         b.count('Фронтенд')>0 or b.count('Фронт-энд')>0 or \
         b.count ('Фронт-енд')>0 or b.count('фронт-энд')>0 or\
            b.count('фронт-енд')>0 )and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Front-end разработчик'
    elif(b.count('1C')>0 or b.count('1С')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='1С разработчик'
    elif(b.count('Fullstack')>0 or b.count('Full') or b.count('full')>0 or b.count ('FullStack')>0\
       or b.count('Фулстек')>0 or b.count('фулстек')or b.count('full-stack')) and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Fullstack разработчик' 
    elif(b.count('Bitrix')>0 or b.count('bitrix')>0 or b.count('Битрикс')\
         or b. count('битрикс')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Bitrix разработчик' 
    elif(b.count('UI')>0 or b.count('UX')>0 or \
          b. count('UX/UI')>0)and( \
            b.count('Дизайнер')>0 or \
            b.count('дизайнер')>0 or b.count("designer")>0 or \
            b.count('Designer')>0):
        res='UX/UI дизайнер' 
    elif(b.count('Digital')>0 or b.count('Графический')>0 or \
          b. count('графический')>0 or b.count('3D'))and( \
            b.count('Дизайнер')>0 or \
            b.count('дизайнер')>0 or b.count("designer")>0 or \
            b.count('Designer')>0):
        res='Digital дизайнер' 
    elif(b.count('Swift')>0 or b.count('swift')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Swift разработчик'
    elif(b.count('Kotlin')>0 or b.count('kotlin')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Kotlin разработчик'
    elif(b.count('Go')>0 or b.count('go')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Go разработчик'
    elif(b.count('Scala')>0 or b.count('Scala')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Scala разработчик'
    elif(b.count('Ruby')>0 or b.count('ruby')>0)and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='Ruby разработчик'
    elif(b.count('SQL')>0 or b.count('sql')>0) and(b.count('разработчик')>0 or \
            b.count('Разработчик')>0 or b.count('Программист')>0 or \
            b.count('программист')>0 or b.count("developer")>0 or \
            b.count('Dev')>0 or b.count('dev')>0 or b.count('Developer')>0):
        res='SQL разработчик'
    elif(b.count('UI')>0 or b.count('UX')>0 or \
          b. count('UX/UI')>0)and( \
            b.count('Дизайнер')>0 or \
            b.count('дизайнер')>0 or b.count("designer")>0 or \
            b.count('Designer')>0):
        res='UX/UI дизайнер' 
    elif (b.count('Администратор')>0 or b.count ('администратор')>0\
          or b.count('админ')>0 or b.count('Админ')>0 or b.count('Admin')>0
          or b.count('admin')>0 or b.count('Administrator') and b.count('Системный')>0):
        res='Системный администратор'   
    elif (b.count('Архитектор')>0 or b.count ('архитектор')>0)\
        and b.count('Системный')>0:
        res='Системный архитектор'
    elif (b.count('Инженер')>0 or b.count ('Инженер')>0 or b.count('Engineer')>0\
          or b.count('engineer')>0)\
        and (b.count('Системный')>0 or b.count('IT')>0 or b.count('программист')>0):
        res='IT инженер'
    elif (b.count('DevOps')>0):
        res='DevOps'
    elif (b.count('Тестрировщик')>0 or b.count('тестированию')):
        res='Тестировщик'
    elif (b.count('Data')>0 or b.count('data')>0 or b.count('данных')>0\
          or b.count('Данных')>0) and (b.count('analys')>0 or\
          b.count('аналитик')>0 or b.count('Аналитик')>0 or \
          b.count('scientist')>0 or b.count ('Scientist')>0 or b.count('Анализ')>0\
              or b.count('анализ')>0):
        res='Data Scientist'
    else: res=''
    return res

def getData(now):
    a=[]   
    
    for i in range (0,len(selected_name)):
        for j in range(0,3):
            jsObj=json.loads(getPage(j,selected_name[i],now))

            for v in jsObj['objects']:
                r=Diction(v['profession'])
                
                if (r!=''):
                    a.append(r)
                       
            time.sleep(0.15)
    d=set(a)
   
   
    name,Y=consoleLog(a,d)
    return name,Y
    
now=datetime.datetime.now()
X=[[now.year],[now.year-1],[now.year-2],[now.year-3],[now.year-4]]
name_b,Y_b=getData(now.year);

name_b.insert(0,'Период')

df=pd.DataFrame(columns=name_b)
for i in range (0,len(X)):
    a=X[i]
    a.extend(Y_b)
    df.loc[i]=a
    for j in range(0,len(Y_b)):
        if(i%2==0):
            Y_b[j]=Y_b[j]-(i+1)*10+j
        else:
            Y_b[j]=Y_b[j]+(i+1)*10-j
print(df)

model = RandomForestRegressor(n_estimators=100, max_features ='sqrt')
mX=df[['Период']]

mY=df.drop(name_b[0],axis=1)


Xtrn, Xtest, Ytrn, Ytest =train_test_split(mX,mY,test_size=0.3)
model.fit(Xtrn,Ytrn)
pred=model.predict(Xtest)
model.feature_importances_
print(Xtest)
print(pred)
print(r2_score(Ytest,pred))

Xtrn, Xtest, Ytrn, Ytest =train_test_split(mX,mY,test_size=0.2)
model.fit(Xtrn,Ytrn)
pred=model.predict(Xtest)
model.feature_importances_
print(Xtest)
print(pred)
print(r2_score(Ytest,pred))


joblib.dump(model,'mymodel.pkl')