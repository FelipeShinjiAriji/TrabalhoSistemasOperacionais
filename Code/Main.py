from ProcessLogicAddress import processInputCommands, extractDataFromTxt

#inputArchiveData = open('C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\BACKING_STORE.bin', mode='rb')
#print(inputArchiveData)
#physicalAddresses = tuple(inputArchiveData.read())
#inputArchiveData.close()
#print(physicalAddresses)

physicalAddresses = extractDataFromTxt('C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\addresses.txt')

inputCommands = extractDataFromTxt('C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\address.txt-exemplo_')

for inputCommand in inputCommands:
    processInputCommands(inputCommand)
