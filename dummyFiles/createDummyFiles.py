from random import randint
def createDummyFile(pendencias,notas,nome):
    content = "{\"pendências\":"+"\""+str(pendencias)+"\""+','+"\""+"notas\":"+"\""+str(notas)+"\""+'}'
    file = open(nome+'.json',"w")
    file.write(content)
    file.close()

def createDummyFiles(nome,quantidade):
    for i in range(0,quantidade):
        createDummyFile(randint(0,20),randint(0,20),nome+str(i))

if __name__ == "__main__":
    createDummyFiles('teste',20)