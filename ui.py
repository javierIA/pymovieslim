from PySide6.QtWidgets import QApplication,QHBoxLayout,QWidget, QPushButton, QLabel,QFileDialog,QDialog,QComboBox,QMessageBox,QCheckBox,QSlider
from PySide6.QtGui import  QFont
from PySide6.QtCore import Qt

def initui(self):
         
        self.title = "Video Mixer"
        self.setGeometry(100, 100, 300, 500)
        self.setWindowTitle(self.title)

        lbl1=QLabel(self)
        lbl1.setText("Open Video:")
        lbl1.setGeometry(50,50,100,30)    
        lbl1.setFont(QFont("Arial",12))
        lbl1.setAlignment(Qt.AlignLeft)

        btn1=QPushButton(self)
        btn1.setText("Open")
        btn1.setGeometry(150,50,100,30)
        btn1.setFont(QFont("Arial",12))
        btn1.clicked.connect(self.openvideo)

        lbl2=QLabel(self)
        lbl2.setText("Open Audio:")
        lbl2.setGeometry(50,100,100,30)
        lbl2.setFont(QFont("Arial",12))
        lbl2.setAlignment(Qt.AlignLeft)

        btn2=QPushButton(self)
        btn2.setText("Open")
        btn2.setGeometry(150,100,100,30)
        btn2.setFont(QFont("Arial",12))
        btn2.clicked.connect(self.openaudio)


        lbl3=QLabel(self)
        lbl3.setText("Music:")
        lbl3.setGeometry(50,200,100,30)
        lbl3.setFont(QFont("Arial",12))
        lbl3.setAlignment(Qt.AlignLeft)
       
        comb1=QComboBox(self)
        comb1.setGeometry(150,200,100,30)
        comb1.setFont(QFont("Arial",12))
        comb1.addItems(["1","2","3","4","5","6"]) 
        comb1.setCurrentIndex(3)
        comb1.currentTextChanged.connect(self.change) 

        lblrun=QLabel(self)
        lblrun.setText("Run")
        lblrun.setGeometry(50,150,100,30)
        lblrun.setFont(QFont("Arial",12))
        lblrun.setAlignment(Qt.AlignLeft)
        #enviar el btnrun al final
        
        btnrun=QPushButton(self)
        btnrun.setText("Run")
        btnrun.setGeometry(150,150,100,30)
        btnrun.setFont(QFont("Arial",12))
        btnrun.setFlat(True)
        btnrun.clicked.connect(self.run)

        lbl4=QLabel(self)
        lbl4.setText("Is noise:")
        lbl4.setGeometry(50,250,100,30)
        lbl4.setFont(QFont("Arial",12))
        lbl4.setAlignment(Qt.AlignLeft)

        checkbox=QCheckBox(self)
        checkbox.setGeometry(150,250,100,30)
        checkbox.setFont(QFont("Arial",12))
        checkbox.setChecked(False)
        checkbox.stateChanged.connect(self.changeNoise)
        checkbox.setText("NoiseREMOVE")
       
        self.voicevolumen=QSlider(self)
        self.voicevolumen.setGeometry(150,300,100,100)
        self.voicevolumen.setFont(QFont("Arial",12))
        self.voicevolumen.setOrientation(Qt.Vertical)
        self.voicevolumen.setRange(1,10)
        self.voicevolumen.setValue(1)
        self.voicevolumen.setTickPosition(QSlider.TicksBothSides)
        self.voicevolumen.setTickInterval(0.5)
        self.voicevolumen.valueChanged.connect(self.changevolumenvoice)
        
   
    
        self.lbl5=QLabel(self)
        self.lbl5.setText(f"Voice :")
        self.lbl5.setGeometry(10,300,150,50)
        self.lbl5.setFont(QFont("Arial",12))
        self.lbl5.setAlignment(Qt.AlignBottom)
        

        self.lbl6=QLabel(self)
        self.lbl6.setText(f"Music") 
        self.lbl6.setGeometry(10,350,150,50)
        self.lbl6.setFont(QFont("Arial",12))
        self.lbl6.setAlignment(Qt.AlignBottom)
        

        self.slider2=QSlider(self)
        self.slider2.setGeometry(220,300,100,100)
        self.slider2.setFont(QFont("Arial",12))
        self.slider2.setOrientation(Qt.Vertical)
        self.slider2.setRange(0,50)
        self.slider2.setValue(20)
        self.slider2.setTickPosition(QSlider.TicksBothSides)
        self.slider2.setTickInterval(5)
        self.slider2.valueChanged.connect(self.changevolumenmusic)

        self.show()
     