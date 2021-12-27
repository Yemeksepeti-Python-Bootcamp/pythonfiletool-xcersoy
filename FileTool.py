class FileTool():
    def __init__(self):
        print("Konsol islemleri icin Menu() metodunu, dosya islemleri icin FileOperations() metodunu cagiriniz.")
    def Menu(self,path):
        with open(path,"r+") as file:
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
                print(f"{searchStr} metni {path} dosyasında {counter} kere asagidaki satirlarda gecmektedir:")
                print(*searchStrLines,end="\n")
            if input_ == "d":
                file.seek(0)
                file.truncate()
                deleteOption = input("Satir numarasina gore silmek icin 'n', girilecek metne gore silmek icin 't' karakterini yaziniz:\n")
                if deleteOption == "n":
                    linesToDelete = [int(x) for x in input("Silinecek satir numarasini veya numaralarini arada virgul olacak sekilde giriniz: ").split(',')]
                    for number, line in enumerate(content):
                        if number+1 not in linesToDelete:
                            file.write(line)
                if deleteOption == "t":
                    linesToDelete = [x for x in input("Girilecek metni veya metinleri iceren satirlarin silinecegi metni veya metinleri arada virgul olacak sekilde giriniz:\n").split(',')]
                    for searchWord in linesToDelete:
                        for number, line in enumerate(content):
                            if searchWord not in line:
                                file.write(line)

fileTool = FileTool()
fileTool.Menu("letter_frequency.csv")
