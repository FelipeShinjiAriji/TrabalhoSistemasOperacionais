from ProcessLogicAddress import processLogicAddress


inputArchive = open(
    'C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\address.txt-exemplo_', 'r', encoding='cp1252')

logicAddresses = tuple(inputArchive.readlines())

inputArchive.close()

for logicAddress in logicAddresses:
    processLogicAddress(int(logicAddress))