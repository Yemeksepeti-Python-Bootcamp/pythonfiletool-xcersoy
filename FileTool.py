import csv, json

class FileToolClass():
    def __init__(self):
        print("\n* Varolan bir dosya üzerinde islem yapmak icin FileOperations() metodunu\n* Basliklarini sizin belirlediginiz yeni bir CSV dosyası yaratmak icin NewFile() metodunu [OR: NewFile(\"Ad,Soyad\")]\n* Basliklarin sutun sayisina gore otomatik yaratildigi yeni bir CSV dosyasi yaratmak icin NewFileAuto() metodunu cagiriniz.\n")
    
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
        fileName = input("Yaratilacak CSV dosyasinin ismini giriniz:\n")
        titleList = fields.split(',')
        titleStr = ""
        for i in titleList:
            titleStr = titleStr + f"\"{i}\","
        titleStr = titleStr[:-1]
        with open(fileName+".csv","w+",encoding="utf-8") as newFile:
            newFile.write(titleStr)

    def NewFileAuto(self):
        fileName = input("Yaratilacak CSV dosyasinin ismini giriniz:\n")
        colCount = input("Yeni dosya kac sutundan olusmalidir?:\n")
        i = 0
        titles = ""
        while i < int(colCount):
            titles = titles + f"\"{i+1}\","
            i+=1
        titles = titles[:-1]
        with open(fileName+".csv","w+",encoding="utf-8") as newFile:
            newFile.write(titles)
        

        