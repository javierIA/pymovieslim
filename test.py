from pathlib import Path
from PySide6.QtWidgets import QApplication,QHBoxLayout,QWidget, QPushButton, QLabel,QFileDialog,QDialog,QComboBox,QMessageBox,QCheckBox,QSlider
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtCore import Qt
import qdarkstyle
import sys
import os
from helpers import tools 
from pathlib import Path , PureWindowsPath
from ui import initui
import shutil
class Window(QWidget):
    pathvideo=None
    pathaudio=None
    musicnumber=1
    removeNoise=False
  
    def __init__(self):
        super().__init__()
        initui(self)
        
    
    def changevolumenvoice(self,value):
        self.lbl5.setText(f"Voice : {value} DB")
        print(value)
    
    def changevolumenmusic(self,value):
        self.lbl6.setText(f"Music : {value} DB")
        print(value)
   
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
        
        if Window.pathvideo!=None or Window.pathaudio!=None:
            os.makedirs("tmp", exist_ok=True)
            shutil.copy(Window.pathaudio, "tmp/audio.mp3")
            video_path=Window.pathvideo
            audio_path=str(PureWindowsPath(str(os.getcwd())+"/tmp/audio.mp3"))
     
            output_path =  QFileDialog.getExistingDirectory(self,"SaveFIle", "..")
            try:
                if Window.removeNoise:
                    print("removendo ruido")
                    tools.removeNoise(audio_path)
                
                tools.normalizeAudio(audio_path,numbermusic=int(Window.musicnumber),volumenvoice=float(self.voicevolumen.value()),volumenmusic=int(self.slider2.value()))  
                filename = Path(video_path).name
                os.system("ffmpeg -i  "+video_path+" -i "+audio_path+" -map 0:v -map 1:a -c:v copy -shortest  "+output_path+"/"+str(filename))

             
               # subprocess.call(f"ffmpeg -i  {video_path} -i  {audio_path} -map 0:v -map 1:a -c:v copy -shortest  "+output_path+"/"+str(filename))
                msgBox = QMessageBox(self)
                msgBox.setText("Se guardo en ."+output_path+"/"+str(filename)) 
                msgBox.setWindowTitle("Error")
                msgBox.exec()

            
            except IndexError as e:
                msgBox=QMessageBox()
                msgBox=QMessageBox.critical(self, "Diálogo de error", str(e))
                msgBox.exec()
               
        else:   
                msgBox=QMessageBox()
                msgBox=QMessageBox.critical(self, "Diálogo de error", "No se ha seleccionado ningún archivo")
                msgBox.show()
        os.remove("tmp/audio.mp3")
        shutil.rmtree('tmp')

           
          
def main():

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())
    ex = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    