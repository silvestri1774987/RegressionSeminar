import pandas as pd  
import numpy as np  
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from tkinter import *
  




root = Tk() 
root.geometry("600x600") 
root.title(" Regression ") 


def Take_input(): 
    INPUT = inputtxt.get("1.0", "end-1c") 
    out = Regre_Sol(INPUT)
    Output.insert(END, out)
    #print(INPUT) 
      
l = Label(text = "Insert the 90th answer of the SCL90 survey(copy and paste)") 
inputtxt = Text(root, height = 10*2, 
                width = 25*2, 
                bg = "light yellow") 
  
Output = Text(root, height = 5*2,  
              width = 25*2,  
              bg = "light cyan") 
  
Display = Button(root, height = 2*2, 
                 width = 20*2,  
                 text ="Show", 
                 command = lambda:Take_input()) 

#k = INPUT.get(1.0, END)

l.pack() 

inputtxt.pack() 
Display.pack() 

Output.pack() 

def Regre_Sol(inp):
    
    dataset = pd.read_csv("TERESA_Training.csv")
    dataset = dataset.fillna(method='ffill')
    #print(dataset["Total Score"].values)
    y = []
    df = dataset.copy()


    #df = dataset.drop(dataset.index[[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]])
    df.drop(df.index[[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]], inplace=True)

    for index,label in dataset["Total Score"].iteritems():
        if( index%2 != 0):
            y.append(label)  

    #print("Prima Intervista:")

    for index,label in df["Total Score"].iteritems():#in df abbiamo solo le rows prima intervista
        print(label)

    #print("Total Scores ultima intervista")
    for i in y:#in y total scores ultima intervista
        print("y:"+str(i))
    for index,label in df["Total Score"].iteritems():
        print(index,label)
    #print("Dataset per Training")


    df["Total Score"] = y

    for index,label in df["Total Score"].iteritems():
        print(index,label)

    X = df[["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90"]].values

    Y =df["Total Score"].values

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1, random_state=0)

    regressor = LinearRegression()  
    regressor.fit(X_train, Y_train)

    #print(regressor.intercept_)
    #print(regressor.coef_)
    print(inp.split())
    X_ins = np.array(list(inp.split()), dtype=int)
    print(X_ins.reshape(1, -1))
    print(X_test)
    Y_pred = regressor.predict(X_ins.reshape(1, -1))
    #Y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Predicted': Y_pred.flatten()})
    print(df)
    return df
    #coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])  
    #print(coeff_df)

mainloop() 







