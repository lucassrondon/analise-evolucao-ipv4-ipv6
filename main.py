# Denner Ayres (dennerayres@gmail.com)
# Guilherme Azambuja (guilhermevazambuja@gmail.com)
# Lucas Rondon (lucasrondonn@gmail.com)
# https://github.com/lucassrondon/trabalho-ipv4-ipv6.git

from utils.parser import Parser
from utils.graph_plotter import GraphPlotter

RIB_DATA = "data_files/ribs/converted/"
STATS_DATA = "data_files/stats"

if __name__ == '__main__':
    print('Running...')
    # Extraindo dados
    parser = Parser(RIB_DATA, STATS_DATA)
    dados = parser.run()

    # Plotando gráficos
    graph_plotter = GraphPlotter(dados=dados)

    graph_plotter.plot_grafico_total_sa()
    graph_plotter.plot_grafico_quantidade_ipv4()
    graph_plotter.plot_grafico_quantidade_ipv6()
    graph_plotter.plot_grafico_sa_anunciando_ipv4()
    graph_plotter.plot_grafico_sa_anunciando_ipv6()
    graph_plotter.plot_grafico_sa_anunciando_ambos()
