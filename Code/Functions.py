def extractDataFromArchive(url: str, mode: str = 'r'): # Extrai uma tupla de int do arquivo url
    inputArchive = open(url, mode=mode)
    match mode:
        case 'r':
            data = tuple([eval(line) for line in inputArchive.readlines()])
        case _:
            data = tuple(inputArchive.read())
    inputArchive.close()
    return data


def fifo(item, table: list, tableLength: int):
    if tableLength <= len(table):
        table.pop(0)
    table.append(item)