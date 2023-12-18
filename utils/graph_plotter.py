import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime


class GraphPlotter:
    def __init__(self, charts_dir: str, dados: dict) -> None:
        self.charts_dir = charts_dir
        self.dados = dados

        self.dates = [datetime.strptime(date, '%Y-%m-%d') for date in dados]
        self.start_date = self.dates[0]
        self.end_date = self.dates[-1]

    def plot_grafico_total_sa(self) -> None:
        total_sa = []
        afrinic_total_sa = []
        apnic_total_sa = []
        arin_total_sa = []
        lacnic_total_sa = []
        ripencc_total_sa = []

        # Preenchendo as listas com dados para cada data
        for data in list(map(lambda date: date.strftime("%Y-%m-%d"), self.dates)):
            total_sa.append(self.dados[data]['total_sa'])
            afrinic_total_sa.append(self.dados[data]['afrinic']['total_sa'])
            apnic_total_sa.append(self.dados[data]['apnic']['total_sa'])
            arin_total_sa.append(self.dados[data]['arin']['total_sa'])
            lacnic_total_sa.append(self.dados[data]['lacnic']['total_sa'])
            ripencc_total_sa.append(self.dados[data]['ripencc']['total_sa'])

        # Configurações do gráfico
        plt.title('Quantidade de SAs por Tempo')
        plt.grid(True)
        plt.xlabel('Data')
        plt.ylabel('Quantidade')

        # Usar DateFormatter para formatar as datas no eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m %Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        plt.xlim(self.start_date, self.end_date)
        plt.tick_params(axis='x', rotation=45, labelsize=7)

        # Dividir o eixo y em partições menores
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=10000))
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(base=5000))

        # Plotando linhas
        plt.plot(self.dates, total_sa, label='Total')
        plt.plot(self.dates, afrinic_total_sa, label='Afrinic')
        plt.plot(self.dates, apnic_total_sa, label='Apnic')
        plt.plot(self.dates, arin_total_sa, label='Arin')
        plt.plot(self.dates, lacnic_total_sa, label='Lacnic')
        plt.plot(self.dates, ripencc_total_sa, label='Ripencc')

        # Adicionando a legenda após criar as linhas
        plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

        # Salvando o gráfico em um arquivo
        file_name = "chart_totalsa.png"
        plt.savefig(f"{self.charts_dir}{file_name}", bbox_inches='tight', dpi=900)
        plt.clf()
        print(f"{file_name} salvo em {self.charts_dir}")

    def plot_grafico_quantidade_ipv4(self) -> None:
        quantidade_ipv4 = []
        afrinic_quantidade_ipv4 = []
        apnic_quantidade_ipv4 = []
        arin_quantidade_ipv4 = []
        lacnic_quantidade_ipv4 = []
        ripencc_quantidade_ipv4 = []

        # Preenchendo as listas com dados para cada data
        for data in list(map(lambda date: date.strftime("%Y-%m-%d"), self.dates)):
            quantidade_ipv4.append(self.dados[data]['quantidade_ipv4'])
            afrinic_quantidade_ipv4.append(self.dados[data]['afrinic']['quantidade_ipv4'])
            apnic_quantidade_ipv4.append(self.dados[data]['apnic']['quantidade_ipv4'])
            arin_quantidade_ipv4.append(self.dados[data]['arin']['quantidade_ipv4'])
            lacnic_quantidade_ipv4.append(self.dados[data]['lacnic']['quantidade_ipv4'])
            ripencc_quantidade_ipv4.append(self.dados[data]['ripencc']['quantidade_ipv4'])

        # Configurações do gráfico
        plt.title('Quantidade de IPV4 por Tempo')
        plt.grid(True)
        plt.xlabel('Data')
        plt.ylabel('Quantidade')

        # Usar DateFormatter para formatar as datas no eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m %Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        plt.xlim(self.start_date, self.end_date)
        plt.tick_params(axis='x', rotation=45, labelsize=7)

        # Dividir o eixo y em partições menores
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=100000))
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(base=50000))

        # Plotando linhas
        plt.plot(self.dates, quantidade_ipv4, label='Total')
        plt.plot(self.dates, afrinic_quantidade_ipv4, label='Afrinic')
        plt.plot(self.dates, apnic_quantidade_ipv4, label='Apnic')
        plt.plot(self.dates, arin_quantidade_ipv4, label='Arin')
        plt.plot(self.dates, lacnic_quantidade_ipv4, label='Lacnic')
        plt.plot(self.dates, ripencc_quantidade_ipv4, label='Ripencc')

        # Adicionando a legenda após criar as linhas
        plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

        # Salvando o gráfico em um arquivo
        file_name = "chart_ipv4.png"
        plt.savefig(f"{self.charts_dir}{file_name}", bbox_inches='tight', dpi=900)
        plt.clf()
        print(f"{file_name} salvo em {self.charts_dir}")

    def plot_grafico_quantidade_ipv6(self) -> None:
        quantidade_ipv6 = []
        afrinic_quantidade_ipv6 = []
        apnic_quantidade_ipv6 = []
        arin_quantidade_ipv6 = []
        lacnic_quantidade_ipv6 = []
        ripencc_quantidade_ipv6 = []

        # Preenchendo as listas com dados para cada data
        for data in list(map(lambda date: date.strftime("%Y-%m-%d"), self.dates)):
            quantidade_ipv6.append(self.dados[data]['quantidade_ipv6'])
            afrinic_quantidade_ipv6.append(self.dados[data]['afrinic']['quantidade_ipv6'])
            apnic_quantidade_ipv6.append(self.dados[data]['apnic']['quantidade_ipv6'])
            arin_quantidade_ipv6.append(self.dados[data]['arin']['quantidade_ipv6'])
            lacnic_quantidade_ipv6.append(self.dados[data]['lacnic']['quantidade_ipv6'])
            ripencc_quantidade_ipv6.append(self.dados[data]['ripencc']['quantidade_ipv6'])

        # Configurações do gráfico
        plt.title('Quantidade de IPV6 por Tempo')
        plt.grid(True)
        plt.xlabel('Data')
        plt.ylabel('Quantidade')

        # Usar DateFormatter para formatar as datas no eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m %Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        plt.xlim(self.start_date, self.end_date)
        plt.tick_params(axis='x', rotation=45, labelsize=7)

        # Dividir o eixo y em partições menores
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=20000))
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(base=10000))

        # Plotando linhas
        plt.plot(self.dates, quantidade_ipv6, label='Total')
        plt.plot(self.dates, afrinic_quantidade_ipv6, label='Afrinic')
        plt.plot(self.dates, apnic_quantidade_ipv6, label='Apnic')
        plt.plot(self.dates, arin_quantidade_ipv6, label='Arin')
        plt.plot(self.dates, lacnic_quantidade_ipv6, label='Lacnic')
        plt.plot(self.dates, ripencc_quantidade_ipv6, label='Ripencc')

        # Adicionando a legenda após criar as linhas
        plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

        # Salvando o gráfico em um arquivo
        file_name = "chart_ipv6.png"
        plt.savefig(f"{self.charts_dir}{file_name}", bbox_inches='tight', dpi=900)
        plt.clf()
        print(f"{file_name} salvo em {self.charts_dir}")

    def plot_grafico_sa_anunciando_ipv4(self) -> None:
        sa_anunciando_ipv4 = []
        afrinic_sa_anunciando_ipv4 = []
        apnic_sa_anunciando_ipv4 = []
        arin_sa_anunciando_ipv4 = []
        lacnic_sa_anunciando_ipv4 = []
        ripencc_sa_anunciando_ipv4 = []

        # Preenchendo as listas com dados para cada data
        for data in list(map(lambda date: date.strftime("%Y-%m-%d"), self.dates)):
            sa_anunciando_ipv4.append(self.dados[data]['anunciando_somente_ipv4'])
            afrinic_sa_anunciando_ipv4.append(self.dados[data]['afrinic']['anunciando_somente_ipv4'])
            apnic_sa_anunciando_ipv4.append(self.dados[data]['apnic']['anunciando_somente_ipv4'])
            arin_sa_anunciando_ipv4.append(self.dados[data]['arin']['anunciando_somente_ipv4'])
            lacnic_sa_anunciando_ipv4.append(self.dados[data]['lacnic']['anunciando_somente_ipv4'])
            ripencc_sa_anunciando_ipv4.append(self.dados[data]['ripencc']['anunciando_somente_ipv4'])

        # Configurações do gráfico
        plt.title('Quantidade de SAs Anunciando Somente IPV4 por Tempo')
        plt.grid(True)
        plt.xlabel('Data')
        plt.ylabel('Quantidade')

        # Usar DateFormatter para formatar as datas no eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m %Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        plt.xlim(self.start_date, self.end_date)
        plt.tick_params(axis='x', rotation=45, labelsize=7)

        # Dividir o eixo y em partições menores
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=10000))
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(base=5000))

        # Plotando linhas
        plt.plot(self.dates, sa_anunciando_ipv4, label='Total')
        plt.plot(self.dates, afrinic_sa_anunciando_ipv4, label='Afrinic')
        plt.plot(self.dates, apnic_sa_anunciando_ipv4, label='Apnic')
        plt.plot(self.dates, arin_sa_anunciando_ipv4, label='Arin')
        plt.plot(self.dates, lacnic_sa_anunciando_ipv4, label='Lacnic')
        plt.plot(self.dates, ripencc_sa_anunciando_ipv4, label='Ripencc')

        # Adicionando a legenda após criar as linhas
        plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

        # Salvando o gráfico em um arquivo
        file_name = "chart_somenteipv4.png"
        plt.savefig(f"{self.charts_dir}{file_name}", bbox_inches='tight', dpi=900)
        plt.clf()
        print(f"{file_name} salvo em {self.charts_dir}")

    def plot_grafico_sa_anunciando_ipv6(self) -> None:
        sa_anunciando_ipv6 = []
        afrinic_sa_anunciando_ipv6 = []
        apnic_sa_anunciando_ipv6 = []
        arin_sa_anunciando_ipv6 = []
        lacnic_sa_anunciando_ipv6 = []
        ripencc_sa_anunciando_ipv6 = []

        # Preenchendo as listas com dados para cada data
        for data in list(map(lambda date: date.strftime("%Y-%m-%d"), self.dates)):
            sa_anunciando_ipv6.append(self.dados[data]['anunciando_somente_ipv6'])
            afrinic_sa_anunciando_ipv6.append(self.dados[data]['afrinic']['anunciando_somente_ipv6'])
            apnic_sa_anunciando_ipv6.append(self.dados[data]['apnic']['anunciando_somente_ipv6'])
            arin_sa_anunciando_ipv6.append(self.dados[data]['arin']['anunciando_somente_ipv6'])
            lacnic_sa_anunciando_ipv6.append(self.dados[data]['lacnic']['anunciando_somente_ipv6'])
            ripencc_sa_anunciando_ipv6.append(self.dados[data]['ripencc']['anunciando_somente_ipv6'])

        # Configurações do gráfico
        plt.title('Quantidade de SAs Anunciando Somente IPV6 por Tempo')
        plt.grid(True)
        plt.xlabel('Data')
        plt.ylabel('Quantidade')

        # Usar DateFormatter para formatar as datas no eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m %Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        plt.xlim(self.start_date, self.end_date)
        plt.tick_params(axis='x', rotation=45, labelsize=7)

        # Dividir o eixo y em partições menores
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=1000))
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(base=500))

        # Plotando linhas
        plt.plot(self.dates, sa_anunciando_ipv6, label='Total')
        plt.plot(self.dates, afrinic_sa_anunciando_ipv6, label='Afrinic')
        plt.plot(self.dates, apnic_sa_anunciando_ipv6, label='Apnic')
        plt.plot(self.dates, arin_sa_anunciando_ipv6, label='Arin')
        plt.plot(self.dates, lacnic_sa_anunciando_ipv6, label='Lacnic')
        plt.plot(self.dates, ripencc_sa_anunciando_ipv6, label='Ripencc')

        # Adicionando a legenda após criar as linhas
        plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

        # Salvando o gráfico em um arquivo
        file_name = "chart_somenteipv6.png"
        plt.savefig(f"{self.charts_dir}{file_name}", bbox_inches='tight', dpi=900)
        plt.clf()
        print(f"{file_name} salvo em {self.charts_dir}")

    def plot_grafico_sa_anunciando_ambos(self) -> None:
        sa_anunciando_ambos = []
        afrinic_sa_anunciando_ambos = []
        apnic_sa_anunciando_ambos = []
        arin_sa_anunciando_ambos = []
        lacnic_sa_anunciando_ambos = []
        ripencc_sa_anunciando_ambos = []

        # Preenchendo as listas com dados para cada data
        for data in list(map(lambda date: date.strftime("%Y-%m-%d"), self.dates)):
            sa_anunciando_ambos.append(self.dados[data]['anunciando_ambos'])
            afrinic_sa_anunciando_ambos.append(self.dados[data]['afrinic']['anunciando_ambos'])
            apnic_sa_anunciando_ambos.append(self.dados[data]['apnic']['anunciando_ambos'])
            arin_sa_anunciando_ambos.append(self.dados[data]['arin']['anunciando_ambos'])
            lacnic_sa_anunciando_ambos.append(self.dados[data]['lacnic']['anunciando_ambos'])
            ripencc_sa_anunciando_ambos.append(self.dados[data]['ripencc']['anunciando_ambos'])

        # Configurações do gráfico
        plt.title('Quantidade de SAs Anunciando IPV4 e IPV6 por Tempo')
        plt.grid(True)
        plt.xlabel('Data')
        plt.ylabel('Quantidade')

        # Usar DateFormatter para formatar as datas no eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m %Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        plt.xlim(self.start_date, self.end_date)
        plt.tick_params(axis='x', rotation=45, labelsize=7)

        # Dividir o eixo y em partições menores
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=2000))
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(base=1000))

        # Plotando linhas
        plt.plot(self.dates, sa_anunciando_ambos, label='Total')
        plt.plot(self.dates, afrinic_sa_anunciando_ambos, label='Afrinic')
        plt.plot(self.dates, apnic_sa_anunciando_ambos, label='Apnic')
        plt.plot(self.dates, arin_sa_anunciando_ambos, label='Arin')
        plt.plot(self.dates, lacnic_sa_anunciando_ambos, label='Lacnic')
        plt.plot(self.dates, ripencc_sa_anunciando_ambos, label='Ripencc')

        # Adicionando a legenda após criar as linhas
        plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

        # Salvando o gráfico em um arquivo
        file_name = "chart_ambos.png"
        plt.savefig(f"{self.charts_dir}{file_name}", bbox_inches='tight', dpi=900)
        plt.clf()
        print(f"{file_name} salvo em {self.charts_dir}")

    def plot_grafico_ipv4_ipv6(self) -> None:
        # Lists to store data for IPv4 and IPv6
        quantidade_ipv4 = []
        quantidade_ipv6 = []

        # Preenchendo as listas com dados para cada data
        for data in list(map(lambda date: date.strftime("%Y-%m-%d"), self.dates)):
            quantidade_ipv4.append(self.dados[data]['quantidade_ipv4'])
            quantidade_ipv6.append(self.dados[data]['quantidade_ipv6'])

        # Configurações do gráfico
        plt.title('Comparação de IPV4 e IPV6 por Tempo')
        plt.grid(True)
        plt.xlabel('Data')
        plt.ylabel('Quantidade')

        # Usar DateFormatter para formatar as datas no eixo X
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m %Y'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
        plt.xlim(self.start_date, self.end_date)
        plt.tick_params(axis='x', rotation=45, labelsize=7)

        # Dividir o eixo y em partições menores
        plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(base=80000))
        plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(base=40000))

        # Plotando linhas
        plt.plot(self.dates, quantidade_ipv4, label='IPv4', color='blue')
        plt.plot(self.dates, quantidade_ipv6, label='IPv6', color='green')

        # Adicionando a legenda após criar as linhas
        plt.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0))

        # Salvando o gráfico em um arquivo
        file_name = "chart_ipv4_ipv6.png"
        plt.savefig(f"{self.charts_dir}{file_name}", bbox_inches='tight', dpi=900)
        plt.clf()
        print(f"{file_name} salvo em {self.charts_dir}")


