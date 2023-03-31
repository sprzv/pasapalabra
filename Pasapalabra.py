import sys
import os
import numpy as np
from PyQt5.QtWidgets import (QWidget, QTextEdit, QVBoxLayout, QSizePolicy, QGroupBox, QGridLayout, QHBoxLayout, QCheckBox, QToolTip, QMessageBox, QApplication, QPushButton, QRadioButton, QLabel)
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

        
class ApplicationWindow(QWidget):
    
    def __init__(self): #constructor, used to initialize the data
        super().__init__()
        self.title = 'Pasapalabra'#window title
        self.left = 100
        self.top = 50
        self.width = 950
        self.height= 940
        self.setWindowIcon(QIcon('bolaAzul.png')) #window icon on corner of window
        
        self.initUI()
         
    def initUI(self):               
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)#sets position and size of window
    
        #fuente letras en bolas
        fuente1=QFont()
        fuente1.setPixelSize(70)
        #bolas azules
        imgAzul=QPixmap('bolaAzul.png')
        imgAzul=imgAzul.scaled(100,100)
        #bolas resaltadas
        imgAzulr=QPixmap('bolaAzulr.png')
        imgAzulr=imgAzulr.scaled(100,100)
        #bolas verdes
        imgVerde=QPixmap('bolaVerde.png')
        imgVerde=imgVerde.scaled(100,100)
        #bolas rojas
        imgRojo=QPixmap('bolaRoja.png')
        imgRojo=imgRojo.scaled(100,100)
        
        #rosco
        #letraA
        self.azulA=QLabel("A",self)
        self.azulA.setPixmap(imgAzul)
        self.azulA.move(430,20)
        self.azulA.hide()
        
        letraA=QLabel("A",self.azulA)
        letraA.setStyleSheet('color: white')
        letraA.setFont(fuente1)
        letraA.move(29,4)
        
        self.azulAr=QLabel("A",self)
        self.azulAr.setPixmap(imgAzulr)
        self.azulAr.move(430,20) #no tiene hide al principio porque queremos que empiece con la letra A resaltada
        
        letraA=QLabel("A",self.azulAr)
        letraA.setStyleSheet('color: white')
        letraA.setFont(fuente1)
        letraA.move(29,4)
        
        self.verdeA=QLabel("A",self)
        self.verdeA.setPixmap(imgVerde)
        self.verdeA.move(430,20)
        self.verdeA.hide()
        
        letraA=QLabel("A",self.verdeA)
        letraA.setStyleSheet('color: white')
        letraA.setFont(fuente1)
        letraA.move(29,4)
        
        self.rojoA=QLabel("A",self)
        self.rojoA.setPixmap(imgRojo)
        self.rojoA.move(430,20)
        self.rojoA.hide()
        
        letraA=QLabel("A",self.rojoA)
        letraA.setStyleSheet('color: white')
        letraA.setFont(fuente1)
        letraA.move(29,4)
        
        #letraB
        self.azulB=QLabel("B",self)
        self.azulB.setPixmap(imgAzul)
        self.azulB.move(530,30)  #no hay hide en el azul al principio porque queremos que aparezca asi
        
        letraB=QLabel("B",self.azulB)
        letraB.setStyleSheet('color: white')
        letraB.setFont(fuente1)
        letraB.move(30,5)
        
        self.azulBr=QLabel("B",self)
        self.azulBr.setPixmap(imgAzulr)
        self.azulBr.move(530,30)
        self.azulBr.hide()
        
        letraB=QLabel("B",self.azulBr)
        letraB.setStyleSheet('color: white')
        letraB.setFont(fuente1)
        letraB.move(30,5)
        
        self.verdeB=QLabel("B",self)
        self.verdeB.setPixmap(imgVerde)
        self.verdeB.move(530,30)
        self.verdeB.hide()
        
        letraB=QLabel("B",self.verdeB)
        letraB.setStyleSheet('color: white')
        letraB.setFont(fuente1)
        letraB.move(30,5)
        
        self.rojoB=QLabel("B",self)
        self.rojoB.setPixmap(imgRojo)
        self.rojoB.move(530,30)
        self.rojoB.hide()
        
        letraB=QLabel("B",self.rojoB)
        letraB.setStyleSheet('color: white')
        letraB.setFont(fuente1)
        letraB.move(30,5)
        
        #letraC
        self.azulC=QLabel("C",self)
        self.azulC.setPixmap(imgAzul)
        self.azulC.move(630,55)
        
        letraC=QLabel("C",self.azulC)
        letraC.setStyleSheet('color: white')
        letraC.setFont(fuente1)
        letraC.move(28,4)
        
        self.azulCr=QLabel("C",self)
        self.azulCr.setPixmap(imgAzulr)
        self.azulCr.move(630,55)
        self.azulCr.hide()
        
        letraC=QLabel("C",self.azulCr)
        letraC.setStyleSheet('color: white')
        letraC.setFont(fuente1)
        letraC.move(28,4)
        
        self.verdeC=QLabel("C",self)
        self.verdeC.setPixmap(imgVerde)
        self.verdeC.move(630,55)
        self.verdeC.hide()
        
        letraC=QLabel("C",self.verdeC)
        letraC.setStyleSheet('color: white')
        letraC.setFont(fuente1)
        letraC.move(28,4)
        
        self.rojoC=QLabel("C",self)
        self.rojoC.setPixmap(imgRojo)
        self.rojoC.move(630,55)
        self.rojoC.hide()
        
        letraC=QLabel("C",self.rojoC)
        letraC.setStyleSheet('color: white')
        letraC.setFont(fuente1)
        letraC.move(28,4)
        
        #letraD
        self.azulD=QLabel("D",self)
        self.azulD.setPixmap(imgAzul)
        self.azulD.move(715,105)
        
        letraD=QLabel("D",self.azulD)
        letraD.setStyleSheet('color: white')
        letraD.setFont(fuente1)
        letraD.move(29,4)
        
        self.azulDr=QLabel("D",self)
        self.azulDr.setPixmap(imgAzulr)
        self.azulDr.move(715,105)
        self.azulDr.hide()
        
        letraD=QLabel("D",self.azulDr)
        letraD.setStyleSheet('color: white')
        letraD.setFont(fuente1)
        letraD.move(29,4)
        
        self.verdeD=QLabel("D",self)
        self.verdeD.setPixmap(imgVerde)
        self.verdeD.move(715,105)
        self.verdeD.hide()
        
        letraD=QLabel("D",self.verdeD)
        letraD.setStyleSheet('color: white')
        letraD.setFont(fuente1)
        letraD.move(29,4)
        
        self.rojoD=QLabel("D",self)
        self.rojoD.setPixmap(imgRojo)
        self.rojoD.move(715,105)
        self.rojoD.hide()
        
        letraD=QLabel("D",self.rojoD)
        letraD.setStyleSheet('color: white')
        letraD.setFont(fuente1)
        letraD.move(29,4)
        
        #letraE
        self.azulE=QLabel("E",self)
        self.azulE.setPixmap(imgAzul)
        self.azulE.move(780,180)
        
        letraE=QLabel("E",self.azulE)
        letraE.setStyleSheet('color: white')
        letraE.setFont(fuente1)
        letraE.move(29,5)
        
        self.azulEr=QLabel("E",self)
        self.azulEr.setPixmap(imgAzulr)
        self.azulEr.move(780,180)
        self.azulEr.hide()
        
        letraE=QLabel("E",self.azulEr)
        letraE.setStyleSheet('color: white')
        letraE.setFont(fuente1)
        letraE.move(29,5)
        
        self.verdeE=QLabel("E",self)
        self.verdeE.setPixmap(imgVerde)
        self.verdeE.move(780,180)
        self.verdeE.hide()
        
        letraE=QLabel("E",self.verdeE)
        letraE.setStyleSheet('color: white')
        letraE.setFont(fuente1)
        letraE.move(29,5)
        
        self.rojoE=QLabel("E",self)
        self.rojoE.setPixmap(imgRojo)
        self.rojoE.move(780,180)
        self.rojoE.hide()
        
        letraE=QLabel("E",self.rojoE)
        letraE.setStyleSheet('color: white')
        letraE.setFont(fuente1)
        letraE.move(29,5)
        
        #letraF
        self.azulF=QLabel("F",self)
        self.azulF.setPixmap(imgAzul)
        self.azulF.move(820,270)
        
        letraF=QLabel("F",self.azulF)
        letraF.setStyleSheet('color: white')
        letraF.setFont(fuente1)
        letraF.move(32,4)
        
        self.azulFr=QLabel("F",self)
        self.azulFr.setPixmap(imgAzulr)
        self.azulFr.move(820,270)
        self.azulFr.hide()
        
        letraF=QLabel("F",self.azulFr)
        letraF.setStyleSheet('color: white')
        letraF.setFont(fuente1)
        letraF.move(32,4)
        
        self.verdeF=QLabel("F",self)
        self.verdeF.setPixmap(imgVerde)
        self.verdeF.move(820,270)
        self.verdeF.hide()
        
        letraF=QLabel("F",self.verdeF)
        letraF.setStyleSheet('color: white')
        letraF.setFont(fuente1)
        letraF.move(32,4)
        
        self.rojoF=QLabel("F",self)
        self.rojoF.setPixmap(imgRojo)
        self.rojoF.move(820,270)
        self.rojoF.hide()
        
        letraF=QLabel("F",self.rojoF)
        letraF.setStyleSheet('color: white')
        letraF.setFont(fuente1)
        letraF.move(32,4)
        
        #letraG
        self.azulG=QLabel("G",self)
        self.azulG.setPixmap(imgAzul)
        self.azulG.move(840,370)
        
        letraG=QLabel("G",self.azulG)
        letraG.setStyleSheet('color: white')
        letraG.setFont(fuente1)
        letraG.move(27,4)
        
        self.azulGr=QLabel("G",self)
        self.azulGr.setPixmap(imgAzulr)
        self.azulGr.move(840,370)
        self.azulGr.hide()
        
        letraG=QLabel("G",self.azulGr)
        letraG.setStyleSheet('color: white')
        letraG.setFont(fuente1)
        letraG.move(27,4)
        
        self.verdeG=QLabel("G",self)
        self.verdeG.setPixmap(imgVerde)
        self.verdeG.move(840,370)
        self.verdeG.hide()
        
        letraG=QLabel("G",self.verdeG)
        letraG.setStyleSheet('color: white')
        letraG.setFont(fuente1)
        letraG.move(27,4)
        
        self.rojoG=QLabel("G",self)
        self.rojoG.setPixmap(imgRojo)
        self.rojoG.move(840,370)
        self.rojoG.hide()
        
        letraG=QLabel("G",self.rojoG)
        letraG.setStyleSheet('color: white')
        letraG.setFont(fuente1)
        letraG.move(27,4)
        
        #letraH
        self.azulH=QLabel("H",self)
        self.azulH.setPixmap(imgAzul)
        self.azulH.move(835,470)
        
        letraH=QLabel("H",self.azulH)
        letraH.setStyleSheet('color: white')
        letraH.setFont(fuente1)
        letraH.move(27,4)
        
        self.azulHr=QLabel("H",self)
        self.azulHr.setPixmap(imgAzulr)
        self.azulHr.move(835,470)
        self.azulHr.hide()
        
        letraH=QLabel("H",self.azulHr)
        letraH.setStyleSheet('color: white')
        letraH.setFont(fuente1)
        letraH.move(27,4)
        
        self.verdeH=QLabel("H",self)
        self.verdeH.setPixmap(imgVerde)
        self.verdeH.move(835,470)
        self.verdeH.hide()
        
        letraH=QLabel("H",self.verdeH)
        letraH.setStyleSheet('color: white')
        letraH.setFont(fuente1)
        letraH.move(27,4)
        
        self.rojoH=QLabel("H",self)
        self.rojoH.setPixmap(imgRojo)
        self.rojoH.move(835,470)
        self.rojoH.hide()
        
        letraH=QLabel("H",self.rojoH)
        letraH.setStyleSheet('color: white')
        letraH.setFont(fuente1)
        letraH.move(27,4)
        
        #letraI
        self.azulI=QLabel("I",self)
        self.azulI.setPixmap(imgAzul)
        self.azulI.move(815,570)
        
        letraI=QLabel("I",self.azulI)
        letraI.setStyleSheet('color: white')
        letraI.setFont(fuente1)
        letraI.move(37,4)
        
        self.azulIr=QLabel("I",self)
        self.azulIr.setPixmap(imgAzulr)
        self.azulIr.move(815,570)
        self.azulIr.hide()
        
        letraI=QLabel("I",self.azulIr)
        letraI.setStyleSheet('color: white')
        letraI.setFont(fuente1)
        letraI.move(37,4)
        
        self.verdeI=QLabel("I",self)
        self.verdeI.setPixmap(imgVerde)
        self.verdeI.move(815,570)
        self.verdeI.hide()
        
        letraI=QLabel("I",self.verdeI)
        letraI.setStyleSheet('color: white')
        letraI.setFont(fuente1)
        letraI.move(37,4)
        
        self.rojoI=QLabel("I",self)
        self.rojoI.setPixmap(imgRojo)
        self.rojoI.move(815,570)
        self.rojoI.hide()
        
        letraI=QLabel("I",self.rojoI)
        letraI.setStyleSheet('color: white')
        letraI.setFont(fuente1)
        letraI.move(37,4)
        
        #letraJ
        self.azulJ=QLabel("J",self)
        self.azulJ.setPixmap(imgAzul)
        self.azulJ.move(760,660)
        
        letraJ=QLabel("J",self.azulJ)
        letraJ.setStyleSheet('color: white')
        letraJ.setFont(fuente1)
        letraJ.move(34,4)
        
        self.azulJr=QLabel("J",self)
        self.azulJr.setPixmap(imgAzulr)
        self.azulJr.move(760,660)
        self.azulJr.hide()
        
        letraJ=QLabel("J",self.azulJr)
        letraJ.setStyleSheet('color: white')
        letraJ.setFont(fuente1)
        letraJ.move(34,4)
        
        self.verdeJ=QLabel("J",self)
        self.verdeJ.setPixmap(imgVerde)
        self.verdeJ.move(760,660)
        self.verdeJ.hide()
        
        letraJ=QLabel("J",self.verdeJ)
        letraJ.setStyleSheet('color: white')
        letraJ.setFont(fuente1)
        letraJ.move(34,4)
        
        self.rojoJ=QLabel("J",self)
        self.rojoJ.setPixmap(imgRojo)
        self.rojoJ.move(760,660)
        self.rojoJ.hide()
        
        letraJ=QLabel("J",self.rojoJ)
        letraJ.setStyleSheet('color: white')
        letraJ.setFont(fuente1)
        letraJ.move(34,4)
        
        #letraL
        self.azulL=QLabel("L",self)
        self.azulL.setPixmap(imgAzul)
        self.azulL.move(685,730)
        
        letraL=QLabel("L",self.azulL)
        letraL.setStyleSheet('color: white')
        letraL.setFont(fuente1)
        letraL.move(33,4)
        
        self.azulLr=QLabel("L",self)
        self.azulLr.setPixmap(imgAzulr)
        self.azulLr.move(685,730)
        self.azulLr.hide()
        
        letraL=QLabel("L",self.azulLr)
        letraL.setStyleSheet('color: white')
        letraL.setFont(fuente1)
        letraL.move(33,4)
        
        self.verdeL=QLabel("L",self)
        self.verdeL.setPixmap(imgVerde)
        self.verdeL.move(685,730)
        self.verdeL.hide()
        
        letraL=QLabel("L",self.verdeL)
        letraL.setStyleSheet('color: white')
        letraL.setFont(fuente1)
        letraL.move(33,4)
        
        self.rojoL=QLabel("L",self)
        self.rojoL.setPixmap(imgRojo)
        self.rojoL.move(685,730)
        self.rojoL.hide()
        
        letraL=QLabel("L",self.rojoL)
        letraL.setStyleSheet('color: white')
        letraL.setFont(fuente1)
        letraL.move(33,4)
        
        #letraM
        self.azulM=QLabel("M",self)
        self.azulM.setPixmap(imgAzul)
        self.azulM.move(590,780)
        
        letraM=QLabel("M",self.azulM)
        letraM.setStyleSheet('color: white')
        letraM.setFont(fuente1)
        letraM.move(24,4)
        
        self.azulMr=QLabel("M",self)
        self.azulMr.setPixmap(imgAzulr)
        self.azulMr.move(590,780)
        self.azulMr.hide()
        
        letraM=QLabel("M",self.azulMr)
        letraM.setStyleSheet('color: white')
        letraM.setFont(fuente1)
        letraM.move(24,4)
        
        self.verdeM=QLabel("M",self)
        self.verdeM.setPixmap(imgVerde)
        self.verdeM.move(590,780)
        self.verdeM.hide()
        
        letraM=QLabel("M",self.verdeM)
        letraM.setStyleSheet('color: white')
        letraM.setFont(fuente1)
        letraM.move(24,4)
        
        self.rojoM=QLabel("M",self)
        self.rojoM.setPixmap(imgRojo)
        self.rojoM.move(590,780)
        self.rojoM.hide()
        
        letraM=QLabel("M",self.rojoM)
        letraM.setStyleSheet('color: white')
        letraM.setFont(fuente1)
        letraM.move(24,4)
        
        #letraN
        self.azulN=QLabel("N",self)
        self.azulN.setPixmap(imgAzul)
        self.azulN.move(485,800)
        
        letraN=QLabel("N",self.azulN)
        letraN.setStyleSheet('color: white')
        letraN.setFont(fuente1)
        letraN.move(27,4)
        
        self.azulNr=QLabel("N",self)
        self.azulNr.setPixmap(imgAzulr)
        self.azulNr.move(485,800)
        self.azulNr.hide()
        
        letraN=QLabel("N",self.azulNr)
        letraN.setStyleSheet('color: white')
        letraN.setFont(fuente1)
        letraN.move(27,4)
        
        self.verdeN=QLabel("N",self)
        self.verdeN.setPixmap(imgVerde)
        self.verdeN.move(485,800)
        self.verdeN.hide()
        
        letraN=QLabel("N",self.verdeN)
        letraN.setStyleSheet('color: white')
        letraN.setFont(fuente1)
        letraN.move(27,4)
        
        self.rojoN=QLabel("N",self)
        self.rojoN.setPixmap(imgRojo)
        self.rojoN.move(485,800)
        self.rojoN.hide()
        
        letraN=QLabel("N",self.rojoN)
        letraN.setStyleSheet('color: white')
        letraN.setFont(fuente1)
        letraN.move(27,4)
        
        #letraÑ
        self.azulÑ=QLabel("Ñ",self)
        self.azulÑ.setPixmap(imgAzul)
        self.azulÑ.move(375,800)
        
        letraÑ=QLabel("Ñ",self.azulÑ)
        letraÑ.setStyleSheet('color: white')
        letraÑ.setFont(fuente1)
        letraÑ.move(27,7)
        
        self.azulÑr=QLabel("Ñ",self)
        self.azulÑr.setPixmap(imgAzulr)
        self.azulÑr.move(375,800)
        self.azulÑr.hide()
        
        letraÑ=QLabel("Ñ",self.azulÑr)
        letraÑ.setStyleSheet('color: white')
        letraÑ.setFont(fuente1)
        letraÑ.move(27,7)
        
        self.verdeÑ=QLabel("Ñ",self)
        self.verdeÑ.setPixmap(imgVerde)
        self.verdeÑ.move(375,800)
        self.verdeÑ.hide()
        
        letraÑ=QLabel("Ñ",self.verdeÑ)
        letraÑ.setStyleSheet('color: white')
        letraÑ.setFont(fuente1)
        letraÑ.move(27,7)
        
        self.rojoÑ=QLabel("Ñ",self)
        self.rojoÑ.setPixmap(imgRojo)
        self.rojoÑ.move(375,800)
        self.rojoÑ.hide()
        
        letraÑ=QLabel("Ñ",self.rojoÑ)
        letraÑ.setStyleSheet('color: white')
        letraÑ.setFont(fuente1)
        letraÑ.move(27,7)
        
        #letraO
        self.azulO=QLabel("O",self)
        self.azulO.setPixmap(imgAzul)
        self.azulO.move(270,780)
        
        letraO=QLabel("O",self.azulO)
        letraO.setStyleSheet('color: white')
        letraO.setFont(fuente1)
        letraO.move(26,5)
        
        self.azulOr=QLabel("O",self)
        self.azulOr.setPixmap(imgAzulr)
        self.azulOr.move(270,780)
        self.azulOr.hide()
        
        letraO=QLabel("O",self.azulOr)
        letraO.setStyleSheet('color: white')
        letraO.setFont(fuente1)
        letraO.move(26,5)
        
        self.verdeO=QLabel("O",self)
        self.verdeO.setPixmap(imgVerde)
        self.verdeO.move(270,780)
        self.verdeO.hide()
        
        letraO=QLabel("O",self.verdeO)
        letraO.setStyleSheet('color: white')
        letraO.setFont(fuente1)
        letraO.move(26,5)
        
        self.rojoO=QLabel("O",self)
        self.rojoO.setPixmap(imgRojo)
        self.rojoO.move(270,780)
        self.rojoO.hide()
        
        letraO=QLabel("O",self.rojoO)
        letraO.setStyleSheet('color: white')
        letraO.setFont(fuente1)
        letraO.move(26,5)
        
        #letraP
        self.azulP=QLabel("P",self)
        self.azulP.setPixmap(imgAzul)
        self.azulP.move(175,730)
        
        letraP=QLabel("P",self.azulP)
        letraP.setStyleSheet('color: white')
        letraP.setFont(fuente1)
        letraP.move(32,5)
        
        self.azulPr=QLabel("P",self)
        self.azulPr.setPixmap(imgAzulr)
        self.azulPr.move(175,730)
        self.azulPr.hide()
        
        letraP=QLabel("P",self.azulPr)
        letraP.setStyleSheet('color: white')
        letraP.setFont(fuente1)
        letraP.move(32,5)
        
        self.verdeP=QLabel("P",self)
        self.verdeP.setPixmap(imgVerde)
        self.verdeP.move(175,730)
        self.verdeP.hide()
        
        letraP=QLabel("P",self.verdeP)
        letraP.setStyleSheet('color: white')
        letraP.setFont(fuente1)
        letraP.move(32,5)
        
        self.rojoP=QLabel("P",self)
        self.rojoP.setPixmap(imgRojo)
        self.rojoP.move(175,730)
        self.rojoP.hide()
        
        letraP=QLabel("P",self.rojoP)
        letraP.setStyleSheet('color: white')
        letraP.setFont(fuente1)
        letraP.move(32,5)
        
        #letraQ
        self.azulQ=QLabel("Q",self)
        self.azulQ.setPixmap(imgAzul)
        self.azulQ.move(95,660)
        
        letraQ=QLabel("Q",self.azulQ)
        letraQ.setStyleSheet('color: white')
        letraQ.setFont(fuente1)
        letraQ.move(25,2)
        
        self.azulQr=QLabel("Q",self)
        self.azulQr.setPixmap(imgAzulr)
        self.azulQr.move(95,660)
        self.azulQr.hide()
        
        letraQ=QLabel("Q",self.azulQr)
        letraQ.setStyleSheet('color: white')
        letraQ.setFont(fuente1)
        letraQ.move(25,2)
        
        self.verdeQ=QLabel("Q",self)
        self.verdeQ.setPixmap(imgVerde)
        self.verdeQ.move(95,660)
        self.verdeQ.hide()
        
        letraQ=QLabel("Q",self.verdeQ)
        letraQ.setStyleSheet('color: white')
        letraQ.setFont(fuente1)
        letraQ.move(25,2)
        
        self.rojoQ=QLabel("Q",self)
        self.rojoQ.setPixmap(imgRojo)
        self.rojoQ.move(95,660)
        self.rojoQ.hide()
        
        letraQ=QLabel("Q",self.rojoQ)
        letraQ.setStyleSheet('color: white')
        letraQ.setFont(fuente1)
        letraQ.move(25,2)
        
        #letraR
        self.azulR=QLabel("R",self)
        self.azulR.setPixmap(imgAzul)
        self.azulR.move(45,570)
        
        letraR=QLabel("R",self.azulR)
        letraR.setStyleSheet('color: white')
        letraR.setFont(fuente1)
        letraR.move(29,4)
        
        self.azulRr=QLabel("R",self)
        self.azulRr.setPixmap(imgAzulr)
        self.azulRr.move(45,570)
        self.azulRr.hide()
        
        letraR=QLabel("R",self.azulRr)
        letraR.setStyleSheet('color: white')
        letraR.setFont(fuente1)
        letraR.move(29,4)
        
        self.verdeR=QLabel("R",self)
        self.verdeR.setPixmap(imgVerde)
        self.verdeR.move(45,570)
        self.verdeR.hide()
        
        letraR=QLabel("R",self.verdeR)
        letraR.setStyleSheet('color: white')
        letraR.setFont(fuente1)
        letraR.move(29,4)
        
        self.rojoR=QLabel("R",self)
        self.rojoR.setPixmap(imgRojo)
        self.rojoR.move(45,570)
        self.rojoR.hide()
        
        letraR=QLabel("R",self.rojoR)
        letraR.setStyleSheet('color: white')
        letraR.setFont(fuente1)
        letraR.move(29,4)
        
        #letraS
        self.azulS=QLabel("S",self)
        self.azulS.setPixmap(imgAzul)
        self.azulS.move(25,470)
        
        letraS=QLabel("S",self.azulS)
        letraS.setStyleSheet('color: white')
        letraS.setFont(fuente1)
        letraS.move(31,4)
        
        self.azulSr=QLabel("S",self)
        self.azulSr.setPixmap(imgAzulr)
        self.azulSr.move(25,470)
        self.azulSr.hide()
        
        letraS=QLabel("S",self.azulSr)
        letraS.setStyleSheet('color: white')
        letraS.setFont(fuente1)
        letraS.move(31,4)
        
        self.verdeS=QLabel("S",self)
        self.verdeS.setPixmap(imgVerde)
        self.verdeS.move(25,470)
        self.verdeS.hide()
        
        letraS=QLabel("S",self.verdeS)
        letraS.setStyleSheet('color: white')
        letraS.setFont(fuente1)
        letraS.move(31,4)
        
        self.rojoS=QLabel("S",self)
        self.rojoS.setPixmap(imgRojo)
        self.rojoS.move(25,470)
        self.rojoS.hide()
        
        letraS=QLabel("S",self.rojoS)
        letraS.setStyleSheet('color: white')
        letraS.setFont(fuente1)
        letraS.move(31,4)
        
        #letraT
        self.azulT=QLabel("T",self)
        self.azulT.setPixmap(imgAzul)
        self.azulT.move(20,370)
        
        letraT=QLabel("T",self.azulT)
        letraT.setStyleSheet('color: white')
        letraT.setFont(fuente1)
        letraT.move(30,6)
        
        self.azulTr=QLabel("T",self)
        self.azulTr.setPixmap(imgAzulr)
        self.azulTr.move(20,370)
        self.azulTr.hide()
        
        letraT=QLabel("T",self.azulTr)
        letraT.setStyleSheet('color: white')
        letraT.setFont(fuente1)
        letraT.move(30,6)
        
        self.verdeT=QLabel("T",self)
        self.verdeT.setPixmap(imgVerde)
        self.verdeT.move(20,370)
        self.verdeT.hide()
        
        letraT=QLabel("T",self.verdeT)
        letraT.setStyleSheet('color: white')
        letraT.setFont(fuente1)
        letraT.move(30,6)
        
        self.rojoT=QLabel("T",self)
        self.rojoT.setPixmap(imgRojo)
        self.rojoT.move(20,370)
        self.rojoT.hide()
        
        letraT=QLabel("T",self.rojoT)
        letraT.setStyleSheet('color: white')
        letraT.setFont(fuente1)
        letraT.move(30,6)
        
        #letraU
        self.azulU=QLabel("U",self)
        self.azulU.setPixmap(imgAzul)
        self.azulU.move(40,270)
        
        letraU=QLabel("U",self.azulU)
        letraU.setStyleSheet('color: white')
        letraU.setFont(fuente1)
        letraU.move(27,5)
        
        self.azulUr=QLabel("U",self)
        self.azulUr.setPixmap(imgAzulr)
        self.azulUr.move(40,270)
        self.azulUr.hide()
        
        letraU=QLabel("U",self.azulUr)
        letraU.setStyleSheet('color: white')
        letraU.setFont(fuente1)
        letraU.move(27,5)
        
        self.verdeU=QLabel("U",self)
        self.verdeU.setPixmap(imgVerde)
        self.verdeU.move(40,270)
        self.verdeU.hide()
        
        letraU=QLabel("U",self.verdeU)
        letraU.setStyleSheet('color: white')
        letraU.setFont(fuente1)
        letraU.move(27,5)
        
        self.rojoU=QLabel("U",self)
        self.rojoU.setPixmap(imgRojo)
        self.rojoU.move(40,270)
        self.rojoU.hide()
        
        letraU=QLabel("U",self.rojoU)
        letraU.setStyleSheet('color: white')
        letraU.setFont(fuente1)
        letraU.move(27,5)
        
        #letraV
        self.azulV=QLabel("V",self)
        self.azulV.setPixmap(imgAzul)
        self.azulV.move(80,180)
        
        letraV=QLabel("V",self.azulV)
        letraV.setStyleSheet('color: white')
        letraV.setFont(fuente1)
        letraV.move(29,4)
        
        self.azulVr=QLabel("V",self)
        self.azulVr.setPixmap(imgAzulr)
        self.azulVr.move(80,180)
        self.azulVr.hide()
        
        letraV=QLabel("V",self.azulVr)
        letraV.setStyleSheet('color: white')
        letraV.setFont(fuente1)
        letraV.move(29,4)
        
        self.verdeV=QLabel("V",self)
        self.verdeV.setPixmap(imgVerde)
        self.verdeV.move(80,180)
        self.verdeV.hide()
        
        letraV=QLabel("V",self.verdeV)
        letraV.setStyleSheet('color: white')
        letraV.setFont(fuente1)
        letraV.move(29,4)
        
        self.rojoV=QLabel("V",self)
        self.rojoV.setPixmap(imgRojo)
        self.rojoV.move(80,180)
        self.rojoV.hide()
        
        letraV=QLabel("V",self.rojoV)
        letraV.setStyleSheet('color: white')
        letraV.setFont(fuente1)
        letraV.move(29,4)
        
        #letraX
        self.azulX=QLabel("X",self)
        self.azulX.setPixmap(imgAzul)
        self.azulX.move(145,105)
        
        letraX=QLabel("X",self.azulX)
        letraX.setStyleSheet('color: white')
        letraX.setFont(fuente1)
        letraX.move(29,4)
        
        self.azulXr=QLabel("X",self)
        self.azulXr.setPixmap(imgAzulr)
        self.azulXr.move(145,105)
        self.azulXr.hide()
        
        letraX=QLabel("X",self.azulXr)
        letraX.setStyleSheet('color: white')
        letraX.setFont(fuente1)
        letraX.move(29,4)
        
        self.verdeX=QLabel("X",self)
        self.verdeX.setPixmap(imgVerde)
        self.verdeX.move(145,105)
        self.verdeX.hide()
        
        letraX=QLabel("X",self.verdeX)
        letraX.setStyleSheet('color: white')
        letraX.setFont(fuente1)
        letraX.move(29,4)
        
        self.rojoX=QLabel("X",self)
        self.rojoX.setPixmap(imgRojo)
        self.rojoX.move(145,105)
        self.rojoX.hide()
        
        letraX=QLabel("X",self.rojoX)
        letraX.setStyleSheet('color: white')
        letraX.setFont(fuente1)
        letraX.move(29,4)
        
        #letraY
        self.azulY=QLabel("Y",self)
        self.azulY.setPixmap(imgAzul)
        self.azulY.move(230,55)
        
        letraY=QLabel("Y",self.azulY)
        letraY.setStyleSheet('color: white')
        letraY.setFont(fuente1)
        letraY.move(31,6)
        
        self.azulYr=QLabel("Y",self)
        self.azulYr.setPixmap(imgAzulr)
        self.azulYr.move(230,55)
        self.azulYr.hide()
        
        letraY=QLabel("Y",self.azulYr)
        letraY.setStyleSheet('color: white')
        letraY.setFont(fuente1)
        letraY.move(31,6)
        
        self.verdeY=QLabel("Y",self)
        self.verdeY.setPixmap(imgVerde)
        self.verdeY.move(230,55)
        self.verdeY.hide()
        
        letraY=QLabel("Y",self.verdeY)
        letraY.setStyleSheet('color: white')
        letraY.setFont(fuente1)
        letraY.move(31,6)
        
        self.rojoY=QLabel("Y",self)
        self.rojoY.setPixmap(imgRojo)
        self.rojoY.move(230,55)
        self.rojoY.hide()
        
        letraY=QLabel("Y",self.rojoY)
        letraY.setStyleSheet('color: white')
        letraY.setFont(fuente1)
        letraY.move(31,6)
        
        #letraZ
        self.azulZ=QLabel("Z",self)
        self.azulZ.setPixmap(imgAzul)
        self.azulZ.move(330,30)
        
        letraZ=QLabel("Z",self.azulZ)
        letraZ.setStyleSheet('color: white')
        letraZ.setFont(fuente1)
        letraZ.move(31,5)
        
        self.azulZr=QLabel("Z",self)
        self.azulZr.setPixmap(imgAzulr)
        self.azulZr.move(330,30)
        self.azulZr.hide()
        
        letraZ=QLabel("Z",self.azulZr)
        letraZ.setStyleSheet('color: white')
        letraZ.setFont(fuente1)
        letraZ.move(31,5)
        
        self.verdeZ=QLabel("Z",self)
        self.verdeZ.setPixmap(imgVerde)
        self.verdeZ.move(330,30)
        self.verdeZ.hide()
        
        letraZ=QLabel("Z",self.verdeZ)
        letraZ.setStyleSheet('color: white')
        letraZ.setFont(fuente1)
        letraZ.move(31,5)
        
        self.rojoZ=QLabel("Z",self)
        self.rojoZ.setPixmap(imgRojo)
        self.rojoZ.move(330,30)
        self.rojoZ.hide()
        
        letraZ=QLabel("Z",self.rojoZ)
        letraZ.setStyleSheet('color: white')
        letraZ.setFont(fuente1)
        letraZ.move(31,5)
        
        #listas bolas
        self.bolasAzules=[self.azulA,self.azulB,self.azulC,self.azulD,self.azulE,self.azulF,self.azulG,self.azulH,self.azulI,self.azulJ,self.azulL,self.azulM,self.azulN,self.azulÑ,self.azulO,self.azulP,self.azulQ,self.azulR,self.azulS,self.azulT,self.azulU,self.azulV,self.azulX,self.azulY,self.azulZ]
        self.bolasAzulesr=[self.azulAr,self.azulBr,self.azulCr,self.azulDr,self.azulEr,self.azulFr,self.azulGr,self.azulHr,self.azulIr,self.azulJr,self.azulLr,self.azulMr,self.azulNr,self.azulÑr,self.azulOr,self.azulPr,self.azulQr,self.azulRr,self.azulSr,self.azulTr,self.azulUr,self.azulVr,self.azulXr,self.azulYr,self.azulZr]
        self.bolasVerdes=[self.verdeA,self.verdeB,self.verdeC,self.verdeD,self.verdeE,self.verdeF,self.verdeG,self.verdeH,self.verdeI,self.verdeJ,self.verdeL,self.verdeM,self.verdeN,self.verdeÑ,self.verdeO,self.verdeP,self.verdeQ,self.verdeR,self.verdeS,self.verdeT,self.verdeU,self.verdeV,self.verdeX,self.verdeY,self.verdeZ]
        self.bolasRojas=[self.rojoA,self.rojoB,self.rojoC,self.rojoD,self.rojoE,self.rojoF,self.rojoG,self.rojoH,self.rojoI,self.rojoJ,self.rojoL,self.rojoM,self.rojoN,self.rojoÑ,self.rojoO,self.rojoP,self.rojoQ,self.rojoR,self.rojoS,self.rojoT,self.rojoU,self.rojoV,self.rojoX,self.rojoY,self.rojoZ]
        
        #**preguntas**
        pregA="Empieza por A:\n\n"+"Cualquier sustancia extraña que,\nintroducida en el cuerpo,\ndesencadena una respuesta defensiva\nespecífica contra ella por parte del\nsistema inmune"
        pregB="Empieza por B:\n\n"+"Producto de desecho elaborado por\nel hígado que es vertido al intestino y\ncolabora en la digestión de las grasas"
        pregC="Empieza por C:\n\n"+"Enfermedad no infecciosa que se\norigina cuando un grupo de células\ndel organismo sufre una alteración en\nsu ritmo habitual de reproducción y\nempiezan a dividirse de manera\ndescontrolada"
        pregD="Empieza por D:\n\n"+"Músculo que separa el tórax del\nabdomen y que participa en la\nventilación pulmonar"
        pregE="Empieza por E:\n\n"+"Parte del sistema nervioso central\ncontenida en el interior del cráneo"
        pregF="Empieza por F:\n\n"+"Unión del óvulo con el\nespermatozoide que tiene lugar\nnormalmente en las Trompas de\nFalopio"
        pregG="Empieza por G:\n\n"+"Órgano especializado en la síntesis y\nsecreción de hormonas"
        pregH="Empieza por H:\n\n"+"Alteración del aparato circulatorio\nconsistente en altos valores de\npresión sanguínea, debida\nprincipalmente a un consumo\nexcesivo de sal en la dieta"
        pregI="Empieza por I:\n\n"+"Capacidad que presenta el organismo\nde reaccionar y defenderse frente a\ncualquier sustancia de procedencia\nexterna reconocida como extraña"
        pregJ="Contiene la J:\n\n"+"Agrupación de células que tienen la\nmisma forma y realizan la misma\nfunción, cuya agrupación da lugar a\nlos órganos"
        pregL="Empieza por L:\n\n"+"Líquido circulatorio encargado de\nrecoger las grasas absorbidas en el\nintestino delgado"
        pregM="Empieza por M:\n\n"+"Compuesto químico obtenido de la\nunión de dos o más átomos mediante\nenlaces químicos"
        pregN="Empieza por N:\n\n"+"Compuesto químico contenido en los\nalimentos que el organismo necesita\npara vivir"
        pregÑ="Contiene la Ñ:\n\n"+"Órgano del aparato excretor que filtra\nla sangre y produce la orina con las\nsustancias inútiles recogidas de\naquella"
        pregO="Empieza por O:\n\n"+"Proceso y momento en que el ovario\nlibera una célula reproductora\nfemenina a la trompa de Falopio"
        pregP="Empieza por P:\n\n"+"Tipo de célula pequeña y sencilla que\ncarece de un núcleo diferenciado"
        pregQ="Contiene la Q:\n\n"+"Células sanguíneas responsables del\ninicio de la coagulación sanguínea"
        pregR="Empieza por R:\n\n"+"Parte basal de los dientes insertada\nen la encía que contiene la cavidad\npulparia"
        pregS="Empieza por S:\n\n"+"Enfermedad infecciosa causada por\nun virus que ataca a los linfocitos del\nsistema inmunitario"
        pregT="Empieza por T:\n\n"+"Alteración del aparato circulatorio\nconsistente en la obstrucción de una\narteria por un coágulo o por\narteriosclerosis"
        pregU="Empieza por U:\n\n"+"Conducto que lleva la orina desde el\nriñón hasta la vejiga urinaria"
        pregV="Empieza por V:\n\n"+"Ser vivo de estructura acelular\ncausante de enfermedades\ninfecciosas"
        pregX="Contiene la X:\n\n"+"Eliminación al exterior del cuerpo de\nlas sustancias de desecho producidas\nen el metabolismo celular"
        pregY="Empieza por Y:\n\n"+"Segunda parte del intestino delgado"
        pregZ="Contiene la Z:\n\n"+"Tipo de proteínas encargadas de\nregular las reacciones metabólicas de\nlas células"
        
        self.preg=[pregA,pregB,pregC,pregD,pregE,pregF,pregG,pregH,pregI,pregJ,pregL,pregM,pregN,pregÑ,pregO,pregP,pregQ,pregR,pregS,pregT,pregU,pregV,pregX,pregY,pregZ]
        
        #**respuestas**
        respA="antígeno"
        respB="bilis"
        respC="cáncer"
        respD="diafragma"
        respE="encéfalo"
        respF="fecundación"
        respG="glándula"
        respH="hipertensión"
        respI="inmunidad"
        respJ="tejido"
        respL="linfa"
        respM="molécula"
        respN="nutriente"
        respÑ="riñón"
        respO="ovulación"
        respP="procariota"
        respQ="plaquetas"
        respR="raíz"
        respS="sida"
        respT="trombosis"
        respU="uréter"
        respV="virus"
        respX="excreción"
        respY="yeyuno"
        respZ="enzimas"
        
        self.respCorr=[respA,respB,respC,respD,respE,respF,respG,respH,respI,respJ,respL,respM,respN,respÑ,respO,respP,respQ,respR,respS,respT,respU,respV,respX,respY,respZ]
        
        #pregunta inicial
        fuente2=QFont()
        fuente2.setPixelSize(25)   
        
        self.pregMuestra=QLabel(self)
        self.pregMuestra.setText(pregA)
        self.pregMuestra.setFont(fuente2)
        self.pregMuestra.resize(420,200)
        self.pregMuestra.move(270,220)
        
        #editor de texto
        fuente3=QFont()
        fuente3.setPixelSize(30)
        self.texto=QTextEdit(self)
        self.texto.setFont(fuente3)
        self.texto.resize(420,50)
        self.texto.move(270,450)
        
        #boton enviar respuesta
        comprobar=QPushButton('Dar respuesta',self)
        comprobar.setFont(fuente2)
        comprobar.resize(205,50)
        comprobar.move(270,550)
        comprobar.clicked.connect(self.respCorrecta)
        
        #boton pasapalabra
        pasa=QPushButton('Pasapalabra',self)
        pasa.setFont(fuente2)
        pasa.resize(205,50)
        pasa.move(485,550)
        pasa.clicked.connect(self.pasapalabra)
        
        self.show()
        
    def respCorrecta(self):
        resp=self.texto.toPlainText()
        self.texto.setText('') #resetea el editor de texto para borrar lo que habia escrito y que este en blanco
        for i in range(len(self.bolasAzulesr)):
            if self.bolasAzulesr[i].isVisible() == True:
                k=i
                self.bolasAzulesr[k].hide()
                nAzulesResto=[]
                for l in range(k+1,len(self.bolasAzules)): #encontrar cual es la siguiente bola azul
                    nAzulesResto.append(l)
                if len(nAzulesResto)>0: #si quedan bolas azules en esta vuelta del rosco
                    for m in range(0,len(nAzulesResto)):
                        if self.bolasAzules[nAzulesResto[m]].isVisible() == True:
                            self.bolasAzules[nAzulesResto[m]].hide()
                            self.bolasAzulesr[nAzulesResto[m]].show()#resaltar la siguiente bola azul
                            self.pregMuestra.setText(self.preg[nAzulesResto[m]]) #cambia la pregunta a la siguiente letra que sea azul
                            break
                else:
                    nAzules=[] #numero de bolas azules que quedan en el rosco
                    for p in range(len(self.bolasAzules)):
                        if self.bolasAzules[p].isVisible() == True:
                            nAzules.append(p) #añade el indice de la bola que esta azul de la lista de bolasAzules a la lista nAzules
                    if len(nAzules)>0: #si quedan bolas azules en el rosco en general
                        self.bolasAzules[nAzules[0]].hide() #usa el primer elemento de la lista nAzules (que tiene el indice de la primera bola azul dentro de la lista bolasAzules) como indice para elegir la siguiente bola en el rosco (en la siguiente vuelta) por la que continuar
                        self.bolasAzulesr[nAzules[0]].show()
                        self.pregMuestra.setText(self.preg[nAzules[0]])
                if resp == self.respCorr[k].lower() or resp ==self.respCorr[k].upper(): #la respuesta es valida toda en minusculas o toda en mayusculas
                    self.bolasVerdes[k].show()
                else:
                    self.bolasRojas[k].show()
                break
        
            
    def pasapalabra(self):
        self.texto.setText('')
        for i in range(len(self.bolasAzulesr)):
            if self.bolasAzulesr[i].isVisible() == True: #encontrar que bola esta resaltada ahora mismo
                k=i
                self.bolasAzulesr[k].hide()
                self.bolasAzules[k].show()
                nAzulesResto=[]
                for l in range(k+1,len(self.bolasAzules)): #encontrar cual es la siguiente bola azul
                    nAzulesResto.append(l)
                if len(nAzulesResto)>0: #si quedan bolas azules en esta vuelta del rosco
                    for m in range(0,len(nAzulesResto)):
                        if self.bolasAzules[nAzulesResto[m]].isVisible() == True:
                            self.bolasAzules[nAzulesResto[m]].hide()
                            self.bolasAzulesr[nAzulesResto[m]].show()#resaltar la siguiente bola azul
                            self.pregMuestra.setText(self.preg[nAzulesResto[m]]) #cambia la pregunta a la siguiente letra que sea azul
                            break
                else:
                    nAzules=[] #numero de bolas azules que quedan en el rosco
                    for p in range(len(self.bolasAzules)):
                        if self.bolasAzules[p].isVisible() == True:
                            nAzules.append(p) #añade el indice de la bola que esta azul de la lista de bolasAzules a la lista nAzules
                    if len(nAzules)>0: #si quedan bolas azules en el rosco en general
                        self.bolasAzules[nAzules[0]].hide() #usa el primer elemento de la lista nAzules (que tiene el indice de la primera bola azul dentro de la lista bolasAzules) como indice para elegir la siguiente bola en el rosco (en la siguiente vuelta) por la que continuar
                        self.bolasAzulesr[nAzules[0]].show()
                        self.pregMuestra.setText(self.preg[nAzules[0]])
                break
                        #break #parar el bucle para que no resalte todas las bolas azules en el rosco

if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv) #creates an application object
    myGUI = ApplicationWindow() #uses class where the main application window is
    myGUI.show()
    sys.exit(app.exec_())