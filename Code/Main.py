from ProcessLogicAddress import processInputCommands
from Functions import extractDataFromArchive

virtualMemory = extractDataFromArchive('C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\BACKING_STORE.bin',
                                       mode='rb')

inputCommands = extractDataFromArchive('C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\address.txt-exemplo_')

for inputCommand in inputCommands:
    print(processInputCommands(inputCommand))

