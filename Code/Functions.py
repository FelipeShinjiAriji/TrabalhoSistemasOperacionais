def extractDataFromArchive(url: str, mode: str = 'r'): # Extrai uma tupla de int do arquivo url
    inputArchive = open(url, mode=mode)
    match mode:
        case 'r':
            data = tuple([eval(line) for line in inputArchive.readlines()])
        case _:
            data = list(inputArchive.read())
            for index in range(len(data)):
                if data[index] > 127:
                    data[index] = data[index] - 256
            data = tuple(data)

    inputArchive.close()
    return data


def relocate(item, table: list, tableLength: int):
    if tableLength <= len(table):
        table.pop(0)
    table.append(item)