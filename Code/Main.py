import sys
from Functions import extractDataFromArchive, relocate

address = 'C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\ArquivoLivro2\\addresses.txt' # sys.argv[1]
quadro = 128  # sys.argv[2]
algoritimo = 'LRU'  # sys.argv[3]


tlb = []
pageTable = []
physicalMemory = []


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
    value = virtualMemory[logicAddress]

    return 'Virtual address: {VirtualAddress} Physical address: {PhysicalAddress} Value: {Value}'.format(
        VirtualAddress=logicAddress,
        PhysicalAddress=physicalAddress,
        Value=value)


def processLogicAddress(logicAddress: int):
    pageNumber = logicAddress//256
    for pageFramePair in tlb:
        if pageNumber == pageFramePair[0]:  # TLB hit
            if algoritimo == 'LRU': # LRU in TLB and in physical memory
                physicalMemory.remove(pageFramePair[1])
                physicalMemory.append(pageFramePair[1])
                tlb.remove(pageFramePair)
                tlb.append(pageFramePair)
            return pageFramePair[1]  # return frame
    else:  # TLB miss
        if not (pageNumber in pageTable):
            pageTable.append(pageNumber)
        frameNumber = pageTable.index(pageNumber)

        if algoritimo == 'LRU': #LRU in physical memory
            for physicalFrame in physicalMemory:
                if physicalFrame == frameNumber:
                    physicalMemory.remove(physicalFrame)
                    physicalMemory.append(physicalFrame)

        relocate(frameNumber ,physicalMemory, quadro)
        relocate([pageNumber, frameNumber], tlb, 16)
        return frameNumber


virtualMemory = extractDataFromArchive(
    'C:\\Users\\Usuario\\Documents\\SistemasOperacionais\\Prova\\Prova2\\ArquivoLivro2\\BACKING_STORE.bin', mode='rb')
inputCommands = extractDataFromArchive(address)


for inputCommand in inputCommands:
    print(processInputCommands(inputCommand))

