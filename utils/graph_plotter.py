import matplotlib.pyplot as plt
from datetime import datetime


class GraphPlotter:
    def __init__(self, dados) -> None:
        self.dados = dados
        self.datas_em_ordem = self.pegar_datas_em_ordem(dados)
        self.tempos = self.numerar_datas(dados)

    def plot_grafico_total_sa(self) -> None:
        total_sa = []
        afrinic_total_sa = []
        apnic_total_sa = []
        arin_total_sa = []
        lacnic_total_sa = []
        ripencc_total_sa = []

        for data in self.datas_em_ordem:
            total_sa.append(self.dados[data]['total_sa'])
            afrinic_total_sa.append(self.dados[data]['afrinic']['total_sa'])
            apnic_total_sa.append(self.dados[data]['apnic']['total_sa'])
            arin_total_sa.append(self.dados[data]['arin']['total_sa'])
            lacnic_total_sa.append(self.dados[data]['lacnic']['total_sa'])
            ripencc_total_sa.append(self.dados[data]['ripencc']['total_sa'])

        # Plotando linhas
        plt.plot(self.tempos, total_sa, label='Total ASes')
        plt.plot(self.tempos, afrinic_total_sa, label='Total ASes Afrinic')
        plt.plot(self.tempos, apnic_total_sa, label='Total ASes Apnic')
        plt.plot(self.tempos, arin_total_sa, label='Total ASes Arin')
        plt.plot(self.tempos, lacnic_total_sa, label='Total ASes Lacnic')
        plt.plot(self.tempos, ripencc_total_sa, label='Total ASes Ripencc')

        # Setando legendas
        plt.xlabel('Datas')
        plt.ylabel('Quantidade SA')
        plt.title('Quantidade de SA por Tempo')

        # Adicionando as legendas
        plt.legend()
        # Gerando grafico
        plt.show()

    def plot_grafico_quantidade_ipv4(self) -> None:
        quantidade_ipv4 = []
        afrinic_quantidade_ipv4 = []
        apnic_quantidade_ipv4 = []
        arin_quantidade_ipv4 = []
        lacnic_quantidade_ipv4 = []
        ripencc_quantidade_ipv4 = []

        for data in self.datas_em_ordem:
            quantidade_ipv4.append(self.dados[data]['quantidade_ipv4'])
            afrinic_quantidade_ipv4.append(self.dados[data]['afrinic']['quantidade_ipv4'])
            apnic_quantidade_ipv4.append(self.dados[data]['apnic']['quantidade_ipv4'])
            arin_quantidade_ipv4.append(self.dados[data]['arin']['quantidade_ipv4'])
            lacnic_quantidade_ipv4.append(self.dados[data]['lacnic']['quantidade_ipv4'])
            ripencc_quantidade_ipv4.append(self.dados[data]['ripencc']['quantidade_ipv4'])

        # Plotando linhas
        plt.plot(self.tempos, quantidade_ipv4, label='Total IPV4')
        plt.plot(self.tempos, afrinic_quantidade_ipv4, label='Total IPV4 Afrinic')
        plt.plot(self.tempos, apnic_quantidade_ipv4, label='Total IPV4 Apnic')
        plt.plot(self.tempos, arin_quantidade_ipv4, label='Total IPV4 Arin')
        plt.plot(self.tempos, lacnic_quantidade_ipv4, label='Total IPV4 Lacnic')
        plt.plot(self.tempos, ripencc_quantidade_ipv4, label='Total IPV4 Ripencc')

        # Setando legendas
        plt.xlabel('Datas')
        plt.ylabel('Quantidade IPV4')
        plt.title('Quantidade de IPV4 por Tempo')

        # Adicionando as legendas
        plt.legend()
        # Gerando grafico
        plt.show()

    def plot_grafico_quantidade_ipv6(self) -> None:
        quantidade_ipv6 = []
        afrinic_quantidade_ipv6 = []
        apnic_quantidade_ipv6 = []
        arin_quantidade_ipv6 = []
        lacnic_quantidade_ipv6 = []
        ripencc_quantidade_ipv6 = []

        for data in self.datas_em_ordem:
            quantidade_ipv6.append(self.dados[data]['quantidade_ipv6'])
            afrinic_quantidade_ipv6.append(self.dados[data]['afrinic']['quantidade_ipv6'])
            apnic_quantidade_ipv6.append(self.dados[data]['apnic']['quantidade_ipv6'])
            arin_quantidade_ipv6.append(self.dados[data]['arin']['quantidade_ipv6'])
            lacnic_quantidade_ipv6.append(self.dados[data]['lacnic']['quantidade_ipv6'])
            ripencc_quantidade_ipv6.append(self.dados[data]['ripencc']['quantidade_ipv6'])

        # Plotando linhas
        plt.plot(self.tempos, quantidade_ipv6, label='Total IPV6')
        plt.plot(self.tempos, afrinic_quantidade_ipv6, label='Total IPV6 Afrinic')
        plt.plot(self.tempos, apnic_quantidade_ipv6, label='Total IPV6 Apnic')
        plt.plot(self.tempos, arin_quantidade_ipv6, label='Total IPV6 Arin')
        plt.plot(self.tempos, lacnic_quantidade_ipv6, label='Total IPV6 Lacnic')
        plt.plot(self.tempos, ripencc_quantidade_ipv6, label='Total IPV6 Ripencc')

        # Setando legendas
        plt.xlabel('Datas')
        plt.ylabel('Quantidade IPV6')
        plt.title('Quantidade de IPV6 por Tempo')

        # Adicionando as legendas
        plt.legend()
        # Gerando grafico
        plt.show()

    def plot_grafico_sa_anunciando_ipv4(self) -> None:
        sa_anunciando_ipv4 = []
        afrinic_sa_anunciando_ipv4 = []
        apnic_sa_anunciando_ipv4 = []
        arin_sa_anunciando_ipv4 = []
        lacnic_sa_anunciando_ipv4 = []
        ripencc_sa_anunciando_ipv4 = []

        for data in self.datas_em_ordem:
            sa_anunciando_ipv4.append(self.dados[data]['anunciando_somente_ipv4'])
            afrinic_sa_anunciando_ipv4.append(self.dados[data]['afrinic']['anunciando_somente_ipv4'])
            apnic_sa_anunciando_ipv4.append(self.dados[data]['apnic']['anunciando_somente_ipv4'])
            arin_sa_anunciando_ipv4.append(self.dados[data]['arin']['anunciando_somente_ipv4'])
            lacnic_sa_anunciando_ipv4.append(self.dados[data]['lacnic']['anunciando_somente_ipv4'])
            ripencc_sa_anunciando_ipv4.append(self.dados[data]['ripencc']['anunciando_somente_ipv4'])

        # Plotando linhas
        plt.plot(self.tempos, sa_anunciando_ipv4, label='Total SA Anuncianado Somente IPV4')
        plt.plot(self.tempos, afrinic_sa_anunciando_ipv4, label='Total SA Anuncianado Somente IPV4 Afrinic')
        plt.plot(self.tempos, apnic_sa_anunciando_ipv4, label='Total SA Anuncianado Somente IPV4 Apnic')
        plt.plot(self.tempos, arin_sa_anunciando_ipv4, label='Total SA Anuncianado Somente IPV4 Arin')
        plt.plot(self.tempos, lacnic_sa_anunciando_ipv4, label='Total SA Anuncianado Somente IPV4 Lacnic')
        plt.plot(self.tempos, ripencc_sa_anunciando_ipv4, label='Total SA Anuncianado Somente IPV4 Ripencc')

        # Setando legendas
        plt.xlabel('Datas')
        plt.ylabel('Quantidade SA Anuncianado Somente IPV4')
        plt.title('Quantidade de SA Anunciando IPV4 por Tempo')

        # Adicionando as legendas
        plt.legend()
        # Gerando grafico
        plt.show()

    def plot_grafico_sa_anunciando_ipv6(self) -> None:
        sa_anunciando_ipv6 = []
        afrinic_sa_anunciando_ipv6 = []
        apnic_sa_anunciando_ipv6 = []
        arin_sa_anunciando_ipv6 = []
        lacnic_sa_anunciando_ipv6 = []
        ripencc_sa_anunciando_ipv6 = []

        for data in self.datas_em_ordem:
            sa_anunciando_ipv6.append(self.dados[data]['anunciando_somente_ipv6'])
            afrinic_sa_anunciando_ipv6.append(self.dados[data]['afrinic']['anunciando_somente_ipv6'])
            apnic_sa_anunciando_ipv6.append(self.dados[data]['apnic']['anunciando_somente_ipv6'])
            arin_sa_anunciando_ipv6.append(self.dados[data]['arin']['anunciando_somente_ipv6'])
            lacnic_sa_anunciando_ipv6.append(self.dados[data]['lacnic']['anunciando_somente_ipv6'])
            ripencc_sa_anunciando_ipv6.append(self.dados[data]['ripencc']['anunciando_somente_ipv6'])

        # Plotando linhas
        plt.plot(self.tempos, sa_anunciando_ipv6, label='Total SA Anuncianado Somente IPV6')
        plt.plot(self.tempos, afrinic_sa_anunciando_ipv6, label='Total SA Anuncianado Somente IPV6 Afrinic')
        plt.plot(self.tempos, apnic_sa_anunciando_ipv6, label='Total SA Anuncianado Somente IPV6 Apnic')
        plt.plot(self.tempos, arin_sa_anunciando_ipv6, label='Total SA Anuncianado Somente IPV6 Arin')
        plt.plot(self.tempos, lacnic_sa_anunciando_ipv6, label='Total SA Anuncianado Somente IPV6 Lacnic')
        plt.plot(self.tempos, ripencc_sa_anunciando_ipv6, label='Total SA Anuncianado Somente IPV6 Ripencc')

        # Setando legendas
        plt.xlabel('Datas')
        plt.ylabel('Quantidade SA Anuncianado Somente IPV6')
        plt.title('Quantidade de SA por Anunciando IPV6 por Tempo')

        # Adicionando as legendas
        plt.legend()
        # Gerando grafico
        plt.show()

    def plot_grafico_sa_anunciando_ambos(self) -> None:
        sa_anunciando_ambos = []
        afrinic_sa_anunciando_ambos = []
        apnic_sa_anunciando_ambos = []
        arin_sa_anunciando_ambos = []
        lacnic_sa_anunciando_ambos = []
        ripencc_sa_anunciando_ambos = []

        for data in self.datas_em_ordem:
            sa_anunciando_ambos.append(self.dados[data]['anunciando_ambos'])
            afrinic_sa_anunciando_ambos.append(self.dados[data]['afrinic']['anunciando_ambos'])
            apnic_sa_anunciando_ambos.append(self.dados[data]['apnic']['anunciando_ambos'])
            arin_sa_anunciando_ambos.append(self.dados[data]['arin']['anunciando_ambos'])
            lacnic_sa_anunciando_ambos.append(self.dados[data]['lacnic']['anunciando_ambos'])
            ripencc_sa_anunciando_ambos.append(self.dados[data]['ripencc']['anunciando_ambos'])

        # Plotando linhas
        plt.plot(self.tempos, sa_anunciando_ambos, label='Total SA Anuncianado IPV4 e IPV6')
        plt.plot(self.tempos, afrinic_sa_anunciando_ambos, label='Total SA Anuncianado IPV4 e IPV6 Afrinic')
        plt.plot(self.tempos, apnic_sa_anunciando_ambos, label='Total SA Anuncianado IPV4 e IPV6 Apnic')
        plt.plot(self.tempos, arin_sa_anunciando_ambos, label='Total SA Anuncianado IPV4 e IPV6 Arin')
        plt.plot(self.tempos, lacnic_sa_anunciando_ambos, label='Total SA Anuncianado IPV4 e IPV6 Lacnic')
        plt.plot(self.tempos, ripencc_sa_anunciando_ambos, label='Total SA Anuncianado IPV4 e IPV6 Ripencc')

        # Setando legendas
        plt.xlabel('Datas')
        plt.ylabel('Quantidade SA Anuncianado IPV4 e IPV6')
        plt.title('Quantidade de SA Anunciando IPV4 e IPV6 por Tempo')

        # Adicionando as legendas
        plt.legend()
        # Gerando grafico
        plt.show()

    @staticmethod
    def pegar_datas_em_ordem(dados) -> list:
        datas = []
        for data in dados:
            date_object = datetime.strptime(data, "%Y-%m-%d")
            datas.append(int(date_object.timestamp()))
        datas.sort()
        for i in range(0, len(datas)):
            dt_object = datetime.fromtimestamp(datas[i])
            # Format the datetime object as a string
            datas[i] = dt_object.strftime('%Y-%m-%d')

        return datas

    @staticmethod
    def numerar_datas(dados) -> list:
        tempos = []
        for i in range(0, len(dados)):
            tempos.append(i + 1)

        return tempos
