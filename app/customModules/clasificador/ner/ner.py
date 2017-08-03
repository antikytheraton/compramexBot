from sklearn.externals import joblib
import unicodedata

def elimina_tildes(s):
   return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

def frase2lista(frase):
    frase = elimina_tildes(frase.replace('?', '').replace('¿', '').replace('-', '').replace('.', ''))
    return ['-','-','-']+frase.split(" ")+['-','-','-']

def prepara_frase(words):
    features=[]
    feature={}
    for ind,word in enumerate(words):
        if word!='-' and  word!='':
            feature['0']=words[ind-3]
            feature['1']=words[ind-2]
            feature['2']=words[ind-1]
            feature['3']=words[ind]
            feature['4']=words[ind+1]
            feature['5']=words[ind+2]
            feature['6']=words[ind+3]
            features.append(feature)
            feature={}
    return features

def getNer(frase):
    hash_path = "vectorizer_entity.pkl"
    clf_path = "clasifier_entity.pkl"
    clf = joblib.load(clf_path)
    print(clf)
    vectorizer=joblib.load(hash_path)
    print(vectorizer)
    lista=frase2lista(frase)
    print(lista)
    features=prepara_frase(lista)
    print(features)
    features=vectorizer.transform(features)
    print(features)
    clases=clf.predict(features)
    return lista,clases

entities=getNer("donde puedo comprar una laptop")
print(entities)
