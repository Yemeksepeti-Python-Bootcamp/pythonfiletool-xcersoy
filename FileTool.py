class FileTool():
    def __init__(self):
        print("Konsol islemleri icin Menu() metodunu, dosya islemleri icin FileOperations() metodunu cagiriniz.")
    def Menu(self,path):
        with open(path) as file:
            content = file.readlines()
        input_ = input("Dosyada arama yapmak icin 's', silme yapmak icin 'd', ekleme yapmak icin 'a', guncelleme yapmak icin 'u' karakterini yaziniz: \n")
        if input_ == "s":
            counter = 0
            searchStrLines = []
            searchStr = input("Dosyada aranacak metni yaziniz: \n")
            for line in content:
                if searchStr in line:
                    counter += 1
                    searchStrLines.append(line)
            print(f"{searchStr} kelimesi {path} dosyasında {counter} kere asagidaki satirlarda gecmektedir:")
            print(*searchStrLines,end="\n")

fileTool = FileTool()
fileTool.Menu("letter_frequency.csv")
