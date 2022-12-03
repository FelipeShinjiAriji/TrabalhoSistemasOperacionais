from ProcessLogicAddress import processInputCommands
from Functions import extractDataFromArchive

virtualMemory = extractDataFromArchive('C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\ArquivoLivro2\\BACKING_STORE.bin',
                                       mode='rb')

inputCommands = extractDataFromArchive(
    'C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\ArquivoLivro2\\addresses.txt')

for inputCommand in inputCommands:
    print(processInputCommands(inputCommand))

