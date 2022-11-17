def processLogicAddress(logicAddress: int):
    match logicAddress:
        case -1:
            print('Escrever o conteúdo da TLB')
        case -2:
            print('Escrever entradas da tabela de páginas(somente páginas com bit de presença ZERO -> páginas não carregadas na memória principal)')
        case -3:
            print('Escrever entradas da tabela de páginas (somente páginas com bit de presença UM -> páginas carregas na memória principal).')
        case _:
            if logicAddress < 0:
                print('Error')
            else:
                print(logicAddress)
