import csv, json, os
from typing import NewType

class FileToolClass():
    def __init__(self,path="",fields=[]):
        self.path = path
        self.fields = fields
        if not self.path and not self.fields:
            NewFileAutoCol()
        if not self.path and self.fields:
            NewFile(self.fields)
        if self.path and self.fields:
            PathAndFields(self.path,self.fields)

    def Menu(self):
        with open(self.path,"r+",encoding="utf-8") as file:
            content = file.readlines()
        input_ = input("Search function: 1\nDelete function: 2\nAppend function: 3\nUpdate function: 4\nJSON function: 5\nMerge Function: 6\n")
        if input_ == "1":
            funcSearch(content)
        if input_ == "2":
            funcDelete(file,content) 
        if input_ == "3":
            funcAppend(file)
        if input_ == "4":
            funcUpdate(file,content)
        if input_ == "5":
            funcJson(self)
        if input_ == "6":
            funcMerge(self.path)

def PathAndFields(path,fields):
    with open(path,"r+",encoding="utf-8") as file:
        fileHeader = file.readline(0)
        if fields != fileHeader:
            dummyFile = file.name + ".bak"
            with open(dummyFile,"w") as write_obj:
                str_ = ""
                for i in fields:
                    if isinstance(i,str):
                        str_ = str_ + f"\"{i}\","
                    else:
                        str_ = str_ + f"{i},"
                str_ = str_[:-1]
                write_obj.write(str_+"\n")
                for line in file:
                    write_obj.write(line)
            os.remove(path)
            os.rename(dummyFile,path)

def NewFileAutoCol():
    fileName = input("Enter file name to be created:\n")
    colCount = input("Enter number of columns:\n")
    i = 0
    titles = ""
    while i < int(colCount):
        titles = titles + f"\"{i+1}\","
        i+=1
    titles = titles[:-1]
    with open(fileName+".csv","w+",encoding="utf-8") as newFile:
        newFile.write(titles)

def NewFile(fields):
    fileName = input("Enter file name to be created:\n")
    titleList = fields.split(',')
    titleStr = ""
    for i in titleList:
        if isinstance(i,str):
            titleStr = titleStr + f"\"{i}\","
        else:
            titleStr = titleStr + f"{i},"
    titleStr = titleStr[:-1]
    with open(fileName+".csv","w+",encoding="utf-8") as newFile:
        newFile.write(titleStr)

def funcSearch(content):
    counter = 0
    searchStrLines = []
    searchStr = input("Text to search:\n")
    for line in content:
        if searchStr in line:
            counter += 1
            searchStrLines.append(line)
    print(f"{searchStr} can be found {counter} times in the following lines:")
    print(*searchStrLines,end="\n")

def funcDelete(file,content):
    file.seek(0)
    file.truncate()
    deleteOption = input("Delete by row number: 1\nDelete by text: 2\n")
    
    if deleteOption == "1":
        lineNoToDelete = [int(x) for x in input("Enter row number(s) [Ex: 1 OR 1,2,3]:\n").split(',')]
        for number, line in enumerate(content):
            if number+1 not in lineNoToDelete:
                file.write(line)

    if deleteOption == "2":
        strToDelete = [x for x in input("Enter text(s) [Ex: text OR text1,text2,text3]:\n").split(',')]
        for str_ in strToDelete:
            for number, line in enumerate(content):
                if str_ not in line:
                    file.write(line)

def funcAppend(file):
    lineToAppend = input("Line to be appended:\n")
    while True:
        file_eof = file.read()
        if file_eof == '':
            file.write("\n"+lineToAppend)
            break

def funcUpdate(file,content):
    file.seek(0)
    file.truncate()
    oldStr = input("Old text:\n")
    newStr = input("New text:\n")
    for number, line in enumerate(content):
        file.write(line.replace(oldStr,newStr))

def funcJson(self):
    lineNo = input("This operation will convert the line you choose into JSON and return it; allowing you to assign it to a variable.\nRow number:\n")
    jsonData = []
    jsonDict = {}
    for d in csv.DictReader(open(self.path)):
        for k,v in d.items():
            jsonDict[k.strip()] = v.strip()
        jsonData.append(json.dumps(jsonDict))
    jsonDataLineStr = jsonData[int(lineNo)-2].replace("\\\"","")
    print(jsonDataLineStr)
    return jsonDataLineStr

def funcMerge(path):
    file3Name = input("Enter file name to be created:\n")
    f2 = input("Enter path of second file:\n")
    with open(f2,"r+",encoding="utf-8") as file2:
        with open (path,"r+") as file:
            file2Header = file2.readline(0)
            fileHeader = file.readline(0)
            content = file2.readlines()
            file2.seek(0)
            file2.truncate()
            for number, line in enumerate(content):
                if number != 0:
                    file2.write(line)  
    if fileHeader == file2Header:
        with open(f2,"r+",encoding="utf-8") as file2:
            with open (path,"r+") as file:
                fileData = file.read()
                file2Data = file2.read()
                fileData += "\n"
                fileData += file2Data
    with open (file3Name+".csv","w") as f3:
        f3.write(fileData)