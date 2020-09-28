import sys
from PyQt5.QtWidgets import QFileDialog, QWidget, QApplication, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,QGridLayout, QTextEdit
    """
    Meu primeiro bloco de notas em python :)
    @Autor: Meguinha - Matheus Felipe Vieira Santiago
    TSKDASKDAKSDKASKDAKSDKASKDASKDAKSDAISHWEFHQWIEUFHWIEH
    
    """

def setColor(obj, cor):
    obj.setStyleSheet(f"background-color: {cor}")

class Bloquito(QWidget):
    

    def __init__(self):
        super().__init__()
        self.savepath = None
        self.setWindowTitle("Bloquito")
        self.setStyleSheet("background-color: 	#2fb7c2; ")
        self.resize(800,600)
        self.initUI()
        
    def initUI(self):
        
        
        #----------------------------------------
        #   Buttons
        #----------------------------------------
        btn_new = QPushButton("NEW")
        btn_save = QPushButton("SAVE")
        btn_open = QPushButton("OPEN")
        
        btn_open.clicked.connect(self.event_open)
        btn_new.clicked.connect(self.event_new)
        btn_save.clicked.connect(self.event_save)   
        
        setColor(btn_new, "#f8f8ff")
        setColor(btn_save, "#f8f8ff")
        setColor(btn_open, "#f8f8ff")

        self.textbox = QTextEdit()
        setColor(self.textbox, "#f8f8ff")
        #----------------------------------------
        #   horizontal layout box ♡╰(*´︶`*)╯♡
        #----------------------------------------
        self.hbox = QHBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(btn_open)
        self.hbox.addWidget(btn_new)
        self.hbox.addWidget(btn_save)
        
        #----------------------------------------
        #   vertical layoutbox (⌒▽⌒)♡
        #----------------------------------------
        self.vbox = QVBoxLayout()
        self.hbox.addStretch(1)
        self.setLayout(self.vbox)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.textbox)

    def event_open(self):
        print("open event")
        #le um arquivo
        #similar ao event_save
        #so que apenas faz leitura limpa o qtextedit e cola o que tem no arquivo por cima
        
        file_path = QFileDialog.getOpenFileName(self)
        self.savepath = file_path[0]
        self.setWindowTitle(f"Bloquito - {self.savepath}")
        print(self.textbox.toPlainText())
        with open(f'{self.savepath}', 'r') as textfile:
            data = textfile.read() # armazena os dados do arquivo lido
            self.textbox.clear()
            self.textbox.setPlainText(data)
                

       
        
    def event_new(self):
        #abre uma nova janela
        try:
            self.nw = Bloquito()
            self.nw.show()
        except:
            print("Erro event_new")


    def event_save(self):
        """
        event_save 
        gerencia o evendo o btn_save
        praticamente serve para definir o caminho e nome do arquivo que vai ser salvo
        cria um QFILEDIALOG que vai ser responsavel por definir o caminho e salvar em uma tupla
        file_path é a tula e sua pos [0] tem o path onde queremos salvar ja com o nome do arquivo salvo

        """
        try:
            if self.savepath == None:
                file_path = QFileDialog.getSaveFileName(self, "Save File Window Title", "defualt.txt", "All Files(*)")
                self.savepath = file_path[0]
            self.setWindowTitle(f"Bloquito - {self.savepath}")
            with open(f'{self.savepath}', 'w') as file:
                file.write(self.textbox.toPlainText())

        except:
            pass
        # print(self.textbox.toPlainText())
        #file_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        #with open("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Bloquito()
    win.show()
    sys.exit(app.exec_())
    
