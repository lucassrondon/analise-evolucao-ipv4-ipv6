from os import listdir


class Parser:
    def __init__(self, rib_data_path: str, stats_data_path: str) -> None:
        self.rib_data_path = rib_data_path
        self.stats_data_path = stats_data_path

    def run(self) -> dict:
        # variável para guardar os dados extraídos de todos os arquivos
        dados_por_data = dict()
        ribs = listdir(self.rib_data_path)
        if '.gitkeep' in ribs:
            ribs.remove('.gitkeep')

        # for para extrair dados de todos os arquivos na pasta de arquivos
        for rib_file_name in ribs:
            rib_file_path = self.rib_data_path + rib_file_name
            print(f'Processing file: {rib_file_name}')

            # setando/resetando variáveis de interesse
            total_anunciando_ipv4 = int()
            total_anunciando_ipv6 = int()
            total_sa = int()
            anunciando_ambos = int()
            anunciando_somente_ipv4 = int()
            anunciando_somente_ipv6 = int()
            quantidade_ipv4 = int()
            quantidade_ipv6 = int()
            afrinic = {'quantidade_ipv4': 0, 'quantidade_ipv6': 0, 'total_sa': 0, 'anunciando_somente_ipv4': 0,
                       'anunciando_somente_ipv6': 0, 'anunciando_ambos': 0}
            apnic = {'quantidade_ipv4': 0, 'quantidade_ipv6': 0, 'total_sa': 0, 'anunciando_somente_ipv4': 0,
                     'anunciando_somente_ipv6': 0, 'anunciando_ambos': 0}
            arin = {'quantidade_ipv4': 0, 'quantidade_ipv6': 0, 'total_sa': 0, 'anunciando_somente_ipv4': 0,
                    'anunciando_somente_ipv6': 0, 'anunciando_ambos': 0}
            lacnic = {'quantidade_ipv4': 0, 'quantidade_ipv6': 0, 'total_sa': 0, 'anunciando_somente_ipv4': 0,
                      'anunciando_somente_ipv6': 0, 'anunciando_ambos': 0}
            ripencc = {'quantidade_ipv4': 0, 'quantidade_ipv6': 0, 'total_sa': 0, 'anunciando_somente_ipv4': 0,
                       'anunciando_somente_ipv6': 0, 'anunciando_ambos': 0}

            # listas de sistemas autônomos
            sistemas_autonomos = dict()
            sistemas_ipv4 = set()
            sistemas_ipv6 = set()

            # listas de ips
            lista_de_ipv4 = set()
            lista_de_ipv6 = set()

            with open(rib_file_path, "r") as rib_file:
                for linha in rib_file:
                    partes = linha.strip().split('|')

                    if len(partes) >= 8:
                        # interpretando dados de uma linha """

                        ipv = partes[1].strip()
                        rota = partes[2].strip()

                        # pega o ultimo elemento da rota
                        elementos_rota = rota.split()
                        if not elementos_rota:
                            continue
                        if '{' not in elementos_rota[-1].strip():
                            sistema_autonomo = elementos_rota[-1].strip()
                        else:
                            sistema_autonomo = elementos_rota[-2].strip()

                        # ifs para pegar as variáveis de interesse dos dados extraídos da linha """

                        # verifica se o sistema autônomo ainda não está na lista de sistemas autônomos
                        if sistema_autonomo not in sistemas_autonomos:
                            sistemas_autonomos[sistema_autonomo] = {'ipv4': 0, 'ipv6': 0}
                            total_sa += 1

                        # pegando o total de elementos ipv4 e ipv6
                        if "." in ipv and ipv not in lista_de_ipv4:
                            lista_de_ipv4.add(ipv)
                            sistemas_autonomos[sistema_autonomo]['ipv4'] += 1
                            quantidade_ipv4 += 1
                        elif ":" in ipv and ipv not in lista_de_ipv6:
                            lista_de_ipv6.add(ipv)
                            sistemas_autonomos[sistema_autonomo]['ipv6'] += 1
                            quantidade_ipv6 += 1

                        # verifica se o IP é IPv4 ou IPv6 e se o AS que está
                        # anunciando ainda nao está na lista
                        # importante para pegar a quantidade de elementos unicos
                        if "." in ipv and sistema_autonomo not in sistemas_ipv4:
                            sistemas_ipv4.add(sistema_autonomo)
                            total_anunciando_ipv4 += 1
                        elif ":" in ipv and sistema_autonomo not in sistemas_ipv6:
                            sistemas_ipv6.add(sistema_autonomo)
                            total_anunciando_ipv6 += 1

            # pegando quantidade de sistemas autônomos com ambos (ipv4 e ipv6) e com somente ipv4
            for sistema_autonomo in sistemas_ipv4:
                if sistema_autonomo in sistemas_ipv6:
                    anunciando_ambos += 1
                else:
                    anunciando_somente_ipv4 += 1

            # pegando quantidade de sistemas autônomos com somente ipv6
            for sistema_autonomo in sistemas_ipv6:
                if sistema_autonomo not in sistemas_ipv4:
                    anunciando_somente_ipv6 += 1

            dados_continente_por_data = dict()
            for continente in ['afrinic', 'apnic', 'arin', 'lacnic', 'ripencc']:
                dados_continente_por_data[continente] = self.pegar_ases_continente(continente, rib_file_name)

            # checando em qual região está cada sistema autônomo
            # as informações de um sistema autônomo de uma região são
            # adicionadas às informações daquela região
            for sistema in sistemas_autonomos:
                if sistema in dados_continente_por_data['afrinic']:
                    afrinic['quantidade_ipv4'] += sistemas_autonomos[sistema]['ipv4']
                    afrinic['quantidade_ipv6'] += sistemas_autonomos[sistema]['ipv6']
                    afrinic['total_sa'] += 1

                    if sistemas_autonomos[sistema]['ipv4'] > 0 and sistemas_autonomos[sistema]['ipv6'] > 0:
                        afrinic['anunciando_ambos'] += 1
                    elif sistemas_autonomos[sistema]['ipv4'] > 0:
                        afrinic['anunciando_somente_ipv4'] += 1
                    elif sistemas_autonomos[sistema]['ipv6'] > 0:
                        afrinic['anunciando_somente_ipv6'] += 1

                elif sistema in dados_continente_por_data['apnic']:
                    apnic['quantidade_ipv4'] += sistemas_autonomos[sistema]['ipv4']
                    apnic['quantidade_ipv6'] += sistemas_autonomos[sistema]['ipv6']
                    apnic['total_sa'] += 1

                    if sistemas_autonomos[sistema]['ipv4'] > 0 and sistemas_autonomos[sistema]['ipv6'] > 0:
                        apnic['anunciando_ambos'] += 1
                    elif sistemas_autonomos[sistema]['ipv4'] > 0:
                        apnic['anunciando_somente_ipv4'] += 1
                    elif sistemas_autonomos[sistema]['ipv6'] > 0:
                        apnic['anunciando_somente_ipv6'] += 1

                elif sistema in dados_continente_por_data['arin']:
                    arin['quantidade_ipv4'] += sistemas_autonomos[sistema]['ipv4']
                    arin['quantidade_ipv6'] += sistemas_autonomos[sistema]['ipv6']
                    arin['total_sa'] += 1

                    if sistemas_autonomos[sistema]['ipv4'] > 0 and sistemas_autonomos[sistema]['ipv6'] > 0:
                        arin['anunciando_ambos'] += 1
                    elif sistemas_autonomos[sistema]['ipv4'] > 0:
                        arin['anunciando_somente_ipv4'] += 1
                    elif sistemas_autonomos[sistema]['ipv6'] > 0:
                        arin['anunciando_somente_ipv6'] += 1

                elif sistema in dados_continente_por_data['lacnic']:
                    lacnic['quantidade_ipv4'] += sistemas_autonomos[sistema]['ipv4']
                    lacnic['quantidade_ipv6'] += sistemas_autonomos[sistema]['ipv6']
                    lacnic['total_sa'] += 1

                    if sistemas_autonomos[sistema]['ipv4'] > 0 and sistemas_autonomos[sistema]['ipv6'] > 0:
                        lacnic['anunciando_ambos'] += 1
                    elif sistemas_autonomos[sistema]['ipv4'] > 0:
                        lacnic['anunciando_somente_ipv4'] += 1
                    elif sistemas_autonomos[sistema]['ipv6'] > 0:
                        lacnic['anunciando_somente_ipv6'] += 1

                elif sistema in dados_continente_por_data['ripencc']:
                    ripencc['quantidade_ipv4'] += sistemas_autonomos[sistema]['ipv4']
                    ripencc['quantidade_ipv6'] += sistemas_autonomos[sistema]['ipv6']
                    ripencc['total_sa'] += 1

                    if sistemas_autonomos[sistema]['ipv4'] > 0 and sistemas_autonomos[sistema]['ipv6'] > 0:
                        ripencc['anunciando_ambos'] += 1
                    elif sistemas_autonomos[sistema]['ipv4'] > 0:
                        ripencc['anunciando_somente_ipv4'] += 1
                    elif sistemas_autonomos[sistema]['ipv6'] > 0:
                        ripencc['anunciando_somente_ipv6'] += 1

            dados_por_data[rib_file_name] = {
                'quantidade_ipv4': quantidade_ipv4,
                'quantidade_ipv6': quantidade_ipv6,
                'total_sa': total_sa,
                'anunciando_somente_ipv4': anunciando_somente_ipv4,
                'anunciando_somente_ipv6': anunciando_somente_ipv6,
                'anunciando_ambos': anunciando_ambos,
                'dados_sistemas_autonomos': sistemas_autonomos,
                'afrinic': afrinic,
                'apnic': apnic,
                'arin': arin,
                'lacnic': lacnic,
                'ripencc': ripencc,
            }

        self.print_dados(dados_por_data)

        return dados_por_data

    def pegar_ases_continente(self, continente: str, rib_file_name: str) -> list:
        file_path = f'{self.stats_data_path}{continente}/{rib_file_name}'

        with open(file_path, "r") as rib_file:
            ases = []
            for linha in rib_file:
                partes = linha.strip().split('|')

                if continente == 'apnic' and len(partes) >= 5 and partes[0] == 'apnic':
                    ases.append(partes[4])
                elif continente != 'apnic' and len(partes) >= 4 and 'asn' in partes:
                    ases.append(partes[3])

            return ases

    @staticmethod
    def print_dados(dados_por_data: dict) -> None:
        # imprime as contagens de cada arquivo
        for chave in dados_por_data:
            print('-' * 50)
            print(f"Arquivo: {chave}")
            print()
            print(f"Total de ASs: {dados_por_data[chave]['total_sa']}")
            print(f"Total de IPv4: {dados_por_data[chave]['quantidade_ipv4']}")
            print(f"Total de IPv6: {dados_por_data[chave]['quantidade_ipv6']}")
            print(f"ASs anunciando somente IPv4: {dados_por_data[chave]['anunciando_somente_ipv4']}")
            print(f"ASs anunciando somente IPv6: {dados_por_data[chave]['anunciando_somente_ipv6']}")
            print(f"ASs anunciando IPv4 e IPv6: {dados_por_data[chave]['anunciando_ambos']}")
            print(
                f"Afrinic | "
                f"Total de IPV4: {dados_por_data[chave]['afrinic']['quantidade_ipv4']} | "
                f"Total de IPV6: {dados_por_data[chave]['afrinic']['quantidade_ipv6']} | "
                f"Total ASs: {dados_por_data[chave]['afrinic']['total_sa']} | "
                f"ASs Somente IPV4: {dados_por_data[chave]['afrinic']['anunciando_somente_ipv4']} | "
                f"ASs Somente IPV6: {dados_por_data[chave]['afrinic']['anunciando_somente_ipv6']} | "
                f"ASs Ambos: {dados_por_data[chave]['afrinic']['anunciando_ambos']}"
            )
            print(
                f"Apnic | "
                f"Total de IPV4: {dados_por_data[chave]['apnic']['quantidade_ipv4']} | "
                f"Total de IPV6: {dados_por_data[chave]['apnic']['quantidade_ipv6']} | "
                f"Total ASs: {dados_por_data[chave]['apnic']['total_sa']} | "
                f"ASs Somente IPV4: {dados_por_data[chave]['apnic']['anunciando_somente_ipv4']} | "
                f"ASs Somente IPV6: {dados_por_data[chave]['apnic']['anunciando_somente_ipv6']} | "
                f"ASs Ambos: {dados_por_data[chave]['apnic']['anunciando_ambos']}"
            )
            print(
                f"Arin | "
                f"Total de IPV4: {dados_por_data[chave]['arin']['quantidade_ipv4']} | "
                f"Total de IPV6: {dados_por_data[chave]['arin']['quantidade_ipv6']} | "
                f"Total ASs: {dados_por_data[chave]['arin']['total_sa']} | "
                f"ASs Somente IPV4: {dados_por_data[chave]['arin']['anunciando_somente_ipv4']} | "
                f"ASs Somente IPV6: {dados_por_data[chave]['arin']['anunciando_somente_ipv6']} | "
                f"ASs Ambos: {dados_por_data[chave]['arin']['anunciando_ambos']}"
            )
            print(
                f"Lacnic | "
                f"Total de IPV4: {dados_por_data[chave]['lacnic']['quantidade_ipv4']} | "
                f"Total de IPV6: {dados_por_data[chave]['lacnic']['quantidade_ipv6']} | "
                f"Total ASs: {dados_por_data[chave]['lacnic']['total_sa']} | "
                f"ASs Somente IPV4: {dados_por_data[chave]['lacnic']['anunciando_somente_ipv4']} | "
                f"ASs Somente IPV6: {dados_por_data[chave]['lacnic']['anunciando_somente_ipv6']} | "
                f"ASs Ambos: {dados_por_data[chave]['lacnic']['anunciando_ambos']}"
            )
            print(
                f"Ripencc | "
                f"Total de IPV4: {dados_por_data[chave]['ripencc']['quantidade_ipv4']} | "
                f"Total de IPV6: {dados_por_data[chave]['ripencc']['quantidade_ipv6']} | "
                f"Total ASs: {dados_por_data[chave]['ripencc']['total_sa']} | "
                f"ASs Somente IPV4: {dados_por_data[chave]['ripencc']['anunciando_somente_ipv4']} | "
                f"ASs Somente IPV6: {dados_por_data[chave]['ripencc']['anunciando_somente_ipv6']} | "
                f"ASs Ambos: {dados_por_data[chave]['ripencc']['anunciando_ambos']}"
            )
            print('-' * 50)
