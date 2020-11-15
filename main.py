
from tkinter import Tk
from tkinter import Button
from tkinter import Canvas
from tkinter import Label
from tkinter import Frame
from PIL import Image, ImageTk
import pandas as pd
import joblib
import numpy as np
import modelworks
import matplotlib.pyplot as plt

def analyze():
    model=joblib.load('mymodel.pkl')
    df,now,names,Y_s=modelworks.getDf()
    mX=pd.DataFrame(columns=['Период'])
    mX.loc[0]=now.year+1
    mXA=pd.DataFrame(columns=['Период'])
    mXA.loc[0]=now.year
    pred=model.predict(mX)
    pred1=model.predict(mXA)
    k=pred[0]
    kA=pred1[0]
    C=[]
  
    print(Y_s)
    print(k)
    names=list(df.columns.values)
    new_names=names[1:]
    print(new_names)
    for i in range(0,len(Y_s)):
        C.append(str(k[i]*100/kA[i]-100)+'%\n\n')
  
    R=[]
    for i in range(0,len(kA)):
        R.append(new_names[i]+' '+C[i])
    fig=plt.figure(figsize=(20,20))
    plt.barh(new_names, k)
    plt.title('Возможная популярность специальностей в следующем году')
    plt.savefig('saved_fig.png')
    otchet = Tk()  
    otchet.title("Отчёт")
    
    label = Label(otchet, text="Прирост/убыль популярности").grid(row=1,column=1)
    for i in range(0,len(R)):
        label=Label(otchet, text=R[i]).grid(row=i+2,column=1)
    label=Label(otchet, text='График находится в папке со скриптом').grid(row=20,column=1)
    
    otchet.mainloop()
    
    

if __name__ == "__main__":
    window = Tk()  
    window.title("Explorer")  
    window.geometry('270x140') 
    window.resizable(width=False, height=False) 

    window["bg"]="SpringGreen2"
    btn1 = Button(window, text="Предикт популярных вакансий", command=analyze)  
    btn1.grid(column=2, row=1, ipadx=10, ipady=6, padx=10, pady=10 )
    btn1["bg"]="white"
    window.mainloop()

