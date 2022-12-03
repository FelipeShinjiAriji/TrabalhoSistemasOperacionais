from Functions import fifo
from Functions import extractDataFromArchive


tlb = []
pageTable = []


def processInputCommands(inputCommand: int):
    match inputCommand:
        case -1:
            #print('Escrever o conteúdo da TLB')
            return tlb
        case -2:
            #print('Escrever entradas da tabela de páginas(somente páginas com bit de presença ZERO -> páginas não carregadas na memória principal)')
            return pageTable
        case -3:
            #print('Escrever entradas da tabela de páginas (somente páginas com bit de presença UM -> páginas carregas na memória principal).')
            return pageTable
        case _:
            if inputCommand < 0:
                print('Error')
            else:
                return formatOutput(inputCommand)


def formatOutput(logicAddress: int):
    frameNumber = processLogicAddress(logicAddress)
    offset = logicAddress % 256
    physicalAddress = 256*frameNumber + offset

    return 'Virtual address: {VirtualAddress} Physical address: {PhysicalAddress} Value: {Value}'.format(
        VirtualAddress=logicAddress,
        PhysicalAddress=physicalAddress,
        Value=0)


def processLogicAddress(logicAddress: int):
    pageNumber = logicAddress//256
    for pageFramePair in tlb:
        if pageNumber == pageFramePair[0]:  # TLB hit
            return pageFramePair[1]  # return frame
    else:  # TLB miss
        if not (pageNumber in pageTable):
            pageTable.append(pageNumber)
        frameNumber = pageTable.index(pageNumber)
        fifo([pageNumber, frameNumber], tlb, 16)
        return frameNumber


virtualMemory = extractDataFromArchive(
    'C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\ArquivoLivro2\\BACKING_STORE.bin', mode='rb')
inputCommands = extractDataFromArchive(
    'C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\ArquivoLivro2\\addresses.txt')


for inputCommand in inputCommands:
    print(processInputCommands(inputCommand))

