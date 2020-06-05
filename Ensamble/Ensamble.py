# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:42:07 2020

@author: Majo
"""
import sys
import pkg_resources.py2_warn
import sklearn.utils._cython_blas
import sklearn.neighbors.typedefs
import sklearn.neighbors._quad_tree
import sklearn.tree
import sklearn.tree._utils
sys.setrecursionlimit(1000000)
from ventana_ui import *
from ventanaPCA_ui import *
from ventanaKNN import *
from ventanaBayes import *
from ventanaClasif import *
from ventanaArbol import *
from ventanaEnsamble import *
from ventanaPrediccion import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from numpy import arange,sin,pi
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from matplotlib.colors import ListedColormap
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import funciones as f 
import matplotlib.patches as mpatches
import seaborn as sb
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest
from PyQt5.QtCore import  QSize
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.preprocessing import scale 
from sklearn.cluster import KMeans  
from sklearn.preprocessing import scale  
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import KFold, cross_val_score

col=[]
a=0
e=0
c=0
import warnings
np.seterr(divide='ignore', invalid='ignore')
warnings.filterwarnings('ignore')
class Ensamble(QtWidgets.QWidget, Ui_Ensamble):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png')) 
        self.setFixedSize(self.size())
        self.Button_predecir.clicked.connect(self.clasificar)
    def clasificar(self):
        archivo=self.label_6.text()
        nuevo=self.lineEdit.text()
        self.close()
        self.nv=Prediccion()    #Crear nueva ventana para mostrar resultados
        self.nv.archivo.setText(archivo)
        df=f.leerArchivo(archivo)
        nuevo=nuevo.split(",")
        nuevo= [float(x) for x in nuevo]
        (clases,precision,clase)=f.construirEnsamble2(df,nuevo)
        self.nv.cknn.setText(str(clases[0]))
        self.nv.pknn.setText(str(precision[0]))
        self.nv.cb.setText(str(clases[1]))
        self.nv.pb.setText(str(precision[1]))
        self.nv.ca.setText(str(clases[2]))
        self.nv.pa.setText(str(precision[2]))
       
       
        self.nv.show()
        
class Prediccion(QtWidgets.QWidget, Ui_Prediccion):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QIcon('icon.png')) 
        self.setFixedSize(self.size())
        self.Button_grafica.clicked.connect(self.mostrarGrafica)
    def mostrarGrafica(self):
        archivo=self.archivo.text()
        df=f.leerArchivo(archivo)
        f.graficaDispercion(df)
class Clasificador(QtWidgets.QWidget, Ui_Clasificador):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.clasif_KNN.clicked.connect(self.clasificador_knn)
        self.clasif_Bayes.clicked.connect(self.clasificador_bayes)
        self.clasif_Arbol.clicked.connect(self.clasificador_arbol)
        self.setWindowIcon(QIcon('icon.png')) 
        self.setFixedSize(self.size())
    def clasificador_knn(self):
        x=self.label.text()
        self.w=KNN()
        self.w.label_3.setText(x);
        self.w.show()
    def clasificador_bayes(self):
        x=self.label.text()
        self.w=Bayes()
        self.w.label_3.setText(x);
        self.w.show()
    def clasificador_arbol(self):
        x=self.label.text()
        self.w=Arbol()
        self.w.archivo.setText(x);
        self.w.show()
        
        
class Bayes(QtWidgets.QWidget, Ui_Bayes):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)   
        self.Button_presicion.clicked.connect(self.calcularBayes)
        self.Button_predecir.clicked.connect(self.predecir)
        self.setWindowIcon(QIcon('icon.png')) 
        self.setFixedSize(self.size())
    def calcularBayes(self):
        archivo=self.label_3.text()
        dataframe=f.leerArchivo(archivo)    
        dataframe.drop(['clase'], axis=1)
        
        n_columns=f.num_atributos(archivo)
        
        
        X=dataframe.drop(['clase'], axis=1)
        y=dataframe['clase']
         
        # Division de datos para entrenamientoy prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                            test_size = 0.25, 
                                                            random_state = 0)
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)    
        # Creacion del modelo Naive Bayes
        # y entrenamiento del mismo
        
        classifier = GaussianNB()
        classifier.fit(X_train, y_train)
        # Prediccion del conjunto de prueba
        y_pred = classifier.predict(X_test)
                
        matriz_c = confusion_matrix(y_test, y_pred)
        #VALIDACIÓN CRUZADA
        scores = cross_val_score(classifier,X,y, cv=3)
        #print ("Accuracy: ", (scores.mean(), scores.std() / 2))
        self.label_matriz.setText(str(matriz_c))
        self.label_presicion1.setText(format(classifier.score(X_train, y_train)))
        self.label_presicion2.setText(str(scores.mean()))
    def predecir(self):
        nuevo=self.lineEdit.text();
        fileName=self.label_3.text();
        df=f.leerArchivo(fileName)
        nuevo=nuevo.split(sep=',')
        nuevo= [float(x) for x in nuevo]
        clase=f.bayes(df, nuevo)
        self.label_clase.setText(str(clase[0]))
       
class KNN(QtWidgets.QWidget, Ui_KNN):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.Button_presicion.clicked.connect(self.calcularKnn)
        self.Button_predecir.clicked.connect(self.predecir)
        self.setWindowIcon(QIcon('icon.png')) 
        self.setFixedSize(self.size())
    def calcularKnn(self):
        archivo=self.label_3.text()
        kn = self.spinBox.value()
        df=f.leerArchivo(archivo)
        
        X=df.drop(['clase'], axis=1)
        y = df['clase'].values
        Xentrenamiento, Xprueba, Yentrenamiento, Yprueba = train_test_split(X, y,test_size = 0.25,random_state = 0)
        
        sc = StandardScaler()
        Xentrenamiento = sc.fit_transform(Xentrenamiento)
        Xprueba = sc.transform(Xprueba)
        
        n_neighbors = kn
        clasificador = KNeighborsClassifier(n_neighbors =kn, metric = 'minkowski', p = 2)
        clasificador.fit(Xentrenamiento, Yentrenamiento)
        y_pred = clasificador.predict(Xprueba)
        matriz = confusion_matrix(Yprueba, y_pred)
        
        knn = KNeighborsClassifier(n_neighbors)
        knn.fit(Xentrenamiento, Yentrenamiento)
        scores = cross_val_score(knn,Xprueba, Yprueba, cv=3)
        #mprint ("Accuracy: ", (scores.mean(), scores.std() / 2))
        pred = knn.predict(Xprueba)
        
        self.label_matriz.setText(str(matriz))
        self.label_presicion1.setText(format(knn.score(Xentrenamiento, Yentrenamiento)))
        self.label_presicion2.setText(str(scores.mean()))

    def predecir(self):
        nuevo=self.lineEdit.text();
        archivo=self.label_3.text();
        kn = self.spinBox.value()
        df=f.leerArchivo(archivo)
        nuevo=nuevo.split(",")
        nuevo= [float(x) for x in nuevo]
        clase=f.knn(df, nuevo, kn)
        self.label_clase.setText(str(clase[0])) 
    
class Arbol(QtWidgets.QWidget, Ui_Arbol):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)    
        self.setWindowIcon(QIcon('icon.png')) 
        self.setFixedSize(self.size())
        self.Button_presicion.clicked.connect(self.construirArbol)
        self.Button_predecir.clicked.connect(self.predecir)
    def construirArbol(self):
        archivo=self.archivo.text()
        leaf=self.leaf.value()
        depth=self.depth.value()
        data=f.leerArchivo(archivo)
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
        self.label_matriz.setText(str(matriz))
        #Calculo la precisión del modelo
        precision = precision_score(y_test, y_pred, average='micro')
        #VALIDACIÓN CRUZADA
        scores = cross_val_score(algoritmo,X,y, cv=3)
        #print ("Accuracy: ", (scores.mean(), scores.std() / 2))
        self.label_precision.setText(str(scores.mean()))
        
    def predecir(self):
        nuevo=self.lineEdit.text();
        archivo=self.archivo.text();
        df=f.leerArchivo(archivo)
        leaf=self.leaf.value()
        depth=self.depth.value()
        nuevo=nuevo.split(",")
        nuevo= [float(x) for x in nuevo]
        clase=f.arbol(df,nuevo,leaf,depth)
        self.label_clase.setText(str(clase[0]))
class Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.calcular_pca.clicked.connect(self.calcularPca)
        self.setWindowIcon(QIcon('icon.png')) 
        self.setFixedSize(self.size())
    def calcularPca(self):
        comp = self.spinBox.value()
        fileName=self.label_2.text()
        if fileName:
            data=f.leerArchivo(fileName)
            df=pd.DataFrame(data) 
            scaler = StandardScaler()
            scaler.fit(df)
            scaled_data = scaler.transform(df)     
            pca = PCA(n_components=comp)
            
            pca.fit(scaled_data)
            pca1 = pca.transform(scaled_data)
            scaled_data.shape
            pca1.shape
            plt.figure(figsize=(8,6))
            plt.scatter(pca1[:,0],pca1[:,1],c=df['clase'],cmap='rainbow')
            plt.xlabel('Primer componente principal')
            plt.ylabel('Segundo componente principal')
            #print(pca.components_)
            plt.show()
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.Button_abrir.clicked.connect(self.abrir)
        self.Button_pca.clicked.connect(self.pca)
        self.Button_clasif.clicked.connect(self.clasificadores)
        self.Button_ensamble.clicked.connect(self.ensamble)
        self.setWindowIcon(QIcon('icono.ico')) 
        self.setFixedSize(self.size())
    def abrir(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            f= open(fileName,"r")
            elementos = f.readline()
            atributos = f.readline()
            
            f.close()
            self.elementos.setText("numero de elementos: " + elementos)
            self.atributos.setText("numero de atributos: " + atributos)
            self.label.setText(fileName)
    def pca(self):
        x=self.label.text()
        print("file: " +x)
        self.w = Form()
        self.w.label_2.setText(x)
        self.w.show()
    
    def clasificadores(self):
        x=self.label.text()
        self.w=Clasificador()
        self.w.label.setText(x);
        self.w.show()
    def ensamble(self):
        x=self.label.text()
        self.w=Ensamble()
        self.w.label_6.setText(x);
        self.w.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    

