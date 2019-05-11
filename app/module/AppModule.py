from app.constant.StringConstant import ReplacerText, Information
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory  # Rumus Library
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import os
import pandas as pd
import re

stemmer = StemmerFactory().create_stemmer()  # Object stemmer
remover = StopWordRemoverFactory().create_stop_word_remover()  # objek stopword


def saveDataset(file):
    file.save(os.path.join('app/db', 'datasets.xlsx'))
    data = pd.read_excel('app/db/datasets.xlsx')
    document = data.Bahan.tolist()
    document = [temp.replace(u"\xa0", u"") for temp in document]
    document = [temp.replace(u"\n", u", ") for temp in document]
    document = [str(temp) for temp in document]
    document = preprocess(document)
    document = filtering(document)
    dfDocument = pd.DataFrame({'Bahan':document})
    return dfDocument.to_excel('app/db/dataset-pre.xlsx', index=False)


def loadDataset():
    return pd.read_excel('app/db/datasets.xlsx')


def loadDataPreprocessing():
    data = pd.read_excel('app/db/dataset-pre.xlsx')
    return data.Bahan.tolist()


def preprocess(doc):  # fungsi untuk preprocesing dokumen
    listStem = []  # variabel untuk menampung data preprocesing
    for i in doc:
        lowerku = i.lower()  # membuat huruf kecil
        s = re.sub(r'[^\w\s]', '', lowerku)  # normalisasi text dari code
        textStemmed = stemmer.stem(s)  # steming kata
        textClean = remover.remove(textStemmed)  # membuang kata tdak penting
        if textClean != "-":
            listStem.append(textClean)  # menambah data kata yang sudah di steming di dalam variabel liststem
    return listStem  # mengembalikan nilai listStem


def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces:
        # Check if string is in the main string
        if elem in mainString:
            # Replace the string
            mainString = mainString.replace(elem, newString)
    return mainString


def filtering(ingredients):
    filteredText = []
    for text in ingredients:
        result = ''.join([i for i in text if not i.isdigit()])
        otherStr = replaceMultiple(result, ReplacerText.LIST_REPLACE_TEXT, "")
        a = re.sub(' +', ' ', otherStr)  # untuk menghilangkan double spasi dikalimat
        b = a.lstrip()  # untuk hilangkan spasi di depan kalimat
        filteredText.append(b)
    return filteredText


def dice_distance(a, b):
    c = a.intersection(b)
    return float(2 * len(c)) / (len(a) + len(b))


def search(query, datanya):
    lol = preprocess([query])
    alldata = []
    alldata.append(set(lol[0].split(" ")))
    for i in datanya:
        lol2 = preprocess([i])
        alldata.append(lol2[0].split(" "))

    score = []
    #     print alldata
    for tf in range(1, len(alldata)):
        score.append(dice_distance(alldata[0], alldata[tf]))
    #     print len(alldata)
    #         print score
    return score

