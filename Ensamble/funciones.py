# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 15:33:20 2020

@author: Majo
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import seaborn as sb
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
import warnings
np.seterr(divide='ignore', invalid='ignore')
#warnings.filterwarnings('ignore')
def leerArchivo(fileName):
    if fileName:
            col=[]
            f= open(fileName,"r")
            elementos = f.readline()
            atributos = f.readline()
            clases = f.readline()
            a=int(atributos)
            e=int(elementos)
            c=int(clases)
            f.close()
            
            at=int(atributos)
            for x in range(at+1):
                y=str(x)
                if x==at:
                    col.append("clase")
                else:
                    col.append("col_" + y)
                    
            data = pd.read_csv(fileName, skiprows=3, names=col)
            return data
def num_atributos(fileName):
     f= open(fileName,"r")
     elementos = f.readline()
     atributos = f.readline()
     f.close()
     atributos=int(atributos)
     return atributos;
def bayes(df,nuevo):
    data=df
    X=data.drop(['clase'], axis=1)
    y=data['clase']
    k=int(len(data.columns))-1
    best=SelectKBest(k="all")
    # Ajuste de escalas
    X_new = best.fit_transform(X, y)
    X_new.shape
    selected = best.get_support(indices=True)
 
    used_features =X.columns[selected]

    X_train, X_test = train_test_split(data, test_size=0.2, random_state=6) 
    y_train =X_train["clase"]
    y_test = X_test["clase"]
    
    
    # Creacion del modelo Naive Bayes y entrenamiento del mismo
    gnb = GaussianNB()
    gnb.fit(
        X_train[used_features].values,
        y_train
    )
    # Prediccion del conjunto de prueba
    y_pred = gnb.predict(X_test[used_features])

    clase=gnb.predict([nuevo])
    probabilidad=gnb.predict_proba([nuevo])
    #print("Bayes: ", probabilidad)
    probabilidad=probabilidad[0,clase]
    
    
    x = np.array(clase)
    x=np.append (x,probabilidad)

    return x

def knn(df,nuevo, n_neighbors):
    data=df
    X = data.drop(['clase'], axis=1)
    y = data['clase'].values
     
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    n_neighbors = n_neighbors
    # we create an instance of Neighbours Classifier and fit the data.
    clf = KNeighborsClassifier(n_neighbors, weights='distance')
    clf.fit(X, y)
     
    
    clase=clf.predict([nuevo])
    probabilidad=clf.predict_proba([nuevo])
    probabilidad=probabilidad[0,clase]
    
    x = np.array(clase)
    x=np.append (x,probabilidad)

    return x
    

def arbol(df,nuevo,leaf=5,depth=100):
    data=df
    X = np.array(data.drop(['clase'], 1))
    y = np.array(data['clase'])
        
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        
    algoritmo = DecisionTreeClassifier(criterion='entropy', 
                                          min_samples_split=20,
                                          min_samples_leaf=leaf,
                                          max_depth = depth)
    #Entreno el modelo
    algoritmo.fit(X_train, y_train)
    #Realizo una predicción
    y_pred = algoritmo.predict(X_test)
    #matriz de Confusión
    matriz = confusion_matrix(y_test, y_pred)
    #Calculo la precisión del nuevo elemento
    clase= algoritmo.predict([nuevo])
    probabilidad=algoritmo.predict_proba([nuevo])
    probabilidad=probabilidad[0,clase]
    
    x = np.array(clase)
    x=np.append (x,probabilidad)
    return x

# def construirEnsamble(df,nuevo):
#     c1=df.sample(frac=.8, replace=True)
#     c2=df.sample(frac=.8, replace=True)
#     c3=df.sample(frac=.8, replace=True)
#     #obtener las predicciones
#     prediccion1=knn(c1,nuevo,8)
#     prediccion2=bayes(c2,nuevo)
#     prediccion3=arbol(c3,nuevo)
#     #Obtener a partir del arreglo las clases que predijo cada clasificador
#     clases=[prediccion1[0],prediccion2[0],prediccion3[0]]
#     #obtener las probabilidades
#     porcentajes=[prediccion1[1],prediccion2[1],prediccion3[1]]
#     mejor_precision=max(porcentajes) #Mejor precision
#     mejor_clasificador=porcentajes.index(mejor_precision)
#     if(mejor_clasificador==0):
#          clase= (int(clases[0]))
#     else:
#         if(mejor_clasificador==1):
#              clase=  (int(clases[1]))
#         else:
#             clase= (int(clases[2]))
#     return (clases,porcentajes,clase)
def construirEnsamble2(df,nuevo):
    c1=df.sample(frac=.8, replace=True)
    c2=df.sample(frac=.8, replace=True)
    c3=df.sample(frac=.8, replace=True)
    #obtener las predicciones
    prediccion1=knn(c1,nuevo,8)
    prediccion2=bayes(c2,nuevo)
    prediccion3=arbol(c3,nuevo)
    #Obtener a partir del arreglo las clases que predijo cada clasificador
    clases=[prediccion1[0],prediccion2[0],prediccion3[0]]
    #obtener las probabilidades
    porcentajes=[prediccion1[1],prediccion2[1],prediccion3[1]]
    mejor_precision=max(porcentajes) #Mejor precision
    mejor_clasificador=porcentajes.index(mejor_precision)
    clase=clases[mejor_clasificador]
    return (clases,porcentajes,clase)

def determinarClase(clases,porcentajes):
    mejor_precision=max(porcentajes) #Mejor precision
    mejor_clasificador=porcentajes.index(mejor_precision)
    if(mejor_clasificador==0):
          return(int(clases[0]))
    else:
        if(mejor_clasificador==1):
              return  (int(clases[1]))
        else:
            return (int(clases[2]))

def graficaDispercion(df):
    conjunto=df['clase'].values
    conjuntoE=[]
    conjunto2=df.drop(['clase'], axis=1).values
    for x in range(len(conjunto2)):
        (cs,p,c)=construirEnsamble2(df,conjunto2[x, :])
        #conjuntoE.append(determinarClase(df,conjunto2[x, :])) 
        conjuntoE.append(c)
    plt.figure(figsize=(8,6))
    plt.scatter(conjuntoE,conjunto, facecolors='none', edgecolors='r')
    plt.xlabel('Clases predecidas por el ensamble')
    plt.ylabel('Clases reales')
    plt.show()
