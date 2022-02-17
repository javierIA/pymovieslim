from calendar import c
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QFileDialog,QDialog,QComboBox,QMessageBox,QCheckBox
from PySide6.QtGui import QIcon, QPixmap, QFont, QPalette
from PySide6.QtCore import Qt,Slot,QTextStream,QFile
import qdarkstyle
import subprocess
import sys
import os
from helpers import tools 
from pathlib import Path
class Window(QWidget):
    pathvideo=None
    pathaudio=None
    musicnumber=1
    removeNoise=False
    def __init__(self):
        super().__init__()
              
        self.title = "Video Mixer"
        self.setGeometry(100, 100, 300, 300)
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

    

    def changeNoise(self,CheckState):
       Window.removeNoise=CheckState
    def change(self,text):
        Window.musicnumber=text
        print(Window.musicnumber)
    def openvideo(self):

        fileName = QFileDialog.getOpenFileName(self,
        "Open video", "..", "Video Files (*.mp4)")
        Window.pathvideo=fileName[0]
    def openaudio(self):

        fileName = QFileDialog.getOpenFileName(self,
        "Open audio", "..", "Audio Files (*.mp3)")
        Window.pathaudio=fileName[0]
    def run(self):
        video_path=Window.pathvideo
        audio_path=Window.pathaudio
     
        if  video_path != None or audio_path != None :
            output_path =  QFileDialog.getExistingDirectory(self,"SaveFIle", "..")
            try:
                if Window.removeNoise:
                    print("removendo ruido")
                    tools.removeNoise(video_path,output_path)
                
                tools.normalizeAudio(audio_path,numbermusic=int(Window.musicnumber))
                filename = Path(video_path).name
                os.system("ffmpeg -i  "+video_path+" -i "+audio_path+" -map 0:v -map 1:a -c:v copy -shortest  "+output_path+"/"+str(filename))

             
               # subprocess.call(f"ffmpeg -i  {video_path} -i  {audio_path} -map 0:v -map 1:a -c:v copy -shortest  "+output_path+"/"+str(filename))
                dlg = QDialog(self)
                dlg.setWindowTitle("Success")
                dlg.setGeometry(100, 100, 300, 300)
                
            
            except IndexError as e:
            
               dialogo=QMessageBox.critical(self, "Diálogo de error", e)
               dialogo.setWindowTitle("Error")
               dialogo.show()
               
        else:
                dialogo=QMessageBox.critical(self, "Diálogo de error", "No se ha seleccionado ningún archivo")
                dialogo.setWindowTitle("Error")
                dialogo.show()
           
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Window()
    window.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
    