def extractDataFromArchive(url: str, mode: str = 'r'): # Extrai uma tupla de int do arquivo url
    inputArchive = open(url, mode=mode)
    match mode:
        case 'r':
            data = tuple([eval(line) for line in inputArchive.readlines()])
        case _:
            data = tuple(inputArchive.read())
    inputArchive.close()
    return data

def decomposeAddress(address: int):
    intPageNumber = address//256
    intOffset = address%256
    return (intPageNumber, intOffset)