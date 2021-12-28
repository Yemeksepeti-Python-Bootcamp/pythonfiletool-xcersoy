import csv, json

class FileToolClass():
    def __init__(self):
        print("Varolan bir dosya üzerinde islem yapmak icin FileOperations() metodunu, basliklari ile birlikte yeni bir CSV dosyası yaratmak icin NewFile() metodunu cagiriniz.")
    
    def FileOperations(self,path):
        with open(path,"r+",encoding="utf-8") as file:
            content = file.readlines()
            input_ = input("Dosyada arama yapmak icin 's', silme yapmak icin 'd', ekleme yapmak icin 'a', guncelleme yapmak icin 'u', belli bir satırı JSON'a cevirmek icin 'j' karakterini yaziniz:\n")
            if input_ == "s":
                counter = 0
                searchStrLines = []
                searchStr = input("Dosyada aranacak metni yaziniz:\n")
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
                    lineNoToDelete = [int(x) for x in input("Silinecek satir numarasini veya numaralarini arada virgul olacak sekilde giriniz:\n").split(',')]
                    for number, line in enumerate(content):
                        if number+1 not in lineNoToDelete:
                            file.write(line)
                if deleteOption == "t":
                    strToDelete = [x for x in input("Girilecek metni veya metinleri iceren satirlarin silinecegi metni veya metinleri arada virgul olacak sekilde giriniz:\n").split(',')]
                    for str_ in strToDelete:
                        for number, line in enumerate(content):
                            if str_ not in line:
                                file.write(line)
            if input_ == "a":
                lineToAppend = input("Dosyaya eklenecek satiri giriniz:\n")
                while True:
                    file_eof = file.read()
                    if file_eof == '':
                        file.write("\n"+lineToAppend)
                        break
            if input_ == "u":
                file.seek(0)
                file.truncate()
                oldStr = input("Degistirilecek metni giriniz:\n")
                newStr = input("Yeni metni giriniz:\n")
                for number, line in enumerate(content):
                    file.write(line.replace(oldStr,newStr))
            if input_ == "j":
                lineNo = input("Bu islem secmis oldugunuz satiri JSON formatina cevirerek konsola yazdiracak ve return ederek bir degiskene atamaniza olanak saglayacaktir.\nBir satir numarasi giriniz:\n")
                jsonData = [json.dumps(d) for d in csv.DictReader(open(path))]
                jsonDataLineStr = jsonData[int(lineNo)-2].replace("\\\"","")
                print(jsonDataLineStr)
                return jsonDataLineStr

    def NewFile(self,fields):
        newFileDecision = input("Yaratilacak CSV dosyasinin basliklarini belirlemek isterseniz 'y', sutun numarası bazinda otomatik belirlenmesini isterseniz 'n' karakterini giriniz:\n")
        if newFileDecision == "y":
            pass
        if newFileDecision =="n":
            pass

