# Projeto de Análise da Evolução do Uso de IPv4 e IPv6 em Sistemas Autônomos

Este projeto tem como objetivo realizar análises sobre a evolução do uso de IPv4 e IPv6 em Sistemas Autônomos (SAs), utilizando dados provenientes de arquivos RIB (Routing Information Base) e estatísticas de diferentes Registros de Internet (RIRs), como Afrinic, Apnic, Arin, Lacnic e Ripencc. Os scripts em Python desenvolvidos para este projeto permitem o processamento, análise e visualização detalhada desses dados.

## Contexto
A análise abrange diferentes regiões do mundo, cada uma representada por um RIR específico. O foco está na compreensão da adoção e distribuição de IPv4 e IPv6 ao longo do tempo, permitindo uma visão da transição entre essas versões do protocolo IP em Sistemas Autônomos.

## Estrutura do Projeto

- **apresentacao.pdf:** Apresentação em PDF do projeto.

- **main.py:** Script principal do projeto que realiza a execução das análises.

- **proposta.png:** Imagem contendo a proposta do projeto.

- **/charts:** Pasta onde são armazenados os gráficos gerados pelo script `graph_plotter.py`.

- **/data_files:** Pasta que contém os arquivos de dados utilizados pelo projeto.

  - **/data_files/ribs:** Contém os arquivos RIB, tanto na forma bruta quanto convertida.

    - **/data_files/ribs/converted:** Arquivos RIB convertidos.

    - **/data_files/ribs/raw:** Arquivos RIB brutos.

  - **/data_files/stats:** Contém estatísticas de SAs dos diferentes RIRs.

    - **/data_files/stats/afrinic:** Estatísticas específicas da Afrinic.

    - **/data_files/stats/apnic:** Estatísticas específicas da Apnic.

    - **/data_files/stats/arin:** Estatísticas específicas da Arin.

    - **/data_files/stats/lacnic:** Estatísticas específicas da Lacnic.

    - **/data_files/stats/ripencc:** Estatísticas específicas da Ripencc.

- **/utils:** Contém utilitários e scripts Python para processamento e visualização de dados.

    - **graph_plotter.py:** Script que utiliza a biblioteca Matplotlib para gerar gráficos a partir dos dados.

    - **parser.py:** Script para análise e processamento dos dados provenientes dos arquivos RIB.

## Requisitos

As dependências do projeto estão listadas no arquivo `requirements.txt`.

## Utilização
Para executar o projeto, você pode usar o script `main.py`. Certifique-se de instalar as dependências com:

```bash
pip install -r requirements.txt
```

Em seguida, execute o script principal:

```bash
python main.py
```
Os gráficos gerados serão salvos na pasta charts.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar pull requests.