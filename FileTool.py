class FileTool():
    def __init__(self):
        print("Konsol islemleri icin Menu() metodunu, dosya islemleri icin FileOperations() metodunu cagiriniz.")
    def Menu(self,path):
        with open(path) as file:
            content = file.readlines()
        input_ = input("Dosyada arama yapmak icin 's', silme yapmak icin 'd', ekleme yapmak icin 'a', guncelleme yapmak icin 'u' karakterini yaziniz: \n")

fileTool = FileTool()
fileTool.Menu("letter_frequency.csv")
