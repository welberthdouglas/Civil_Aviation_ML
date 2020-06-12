import pandas as pd
import requests
import os

from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def yearmonthlist(dates:tuple):
    """ Creates a list of year-month to all months in between the specified dates"""

    start, end = [datetime.strptime(i, "%Y-%m") for i in dates]
    total_months = lambda dt: dt.month + 12 * dt.year
    ymlist = []
    for tot_m in range(total_months(start)-1, total_months(end)):
        y, m = divmod(tot_m, 12)
        ymlist.append(datetime(y, m+1, 1).strftime("%Y-%m"))
    return ymlist

def download_data( period:tuple = ('2016-01','2020-06')):
    """ Download the data from the ANAC website """

    r = requests.get('https://www.anac.gov.br/assuntos/setor-regulado/empresas/envio-de-informacoes/microdados')
    soup = BeautifulSoup(r.text, 'lxml')

    monthlist = yearmonthlist(period)

    links = {i.get('href') for i in soup.find_all('a') if 'basica' in str(i.get('href'))}
    links_set = {x for x in links if any(y in x for y in monthlist)}

    directory = 'ANAC_DATA'

    try:
        os.mkdir(directory)

    except:
        pass

    for link in links_set:
        down = requests.get(link)
        with open(directory+'/'+link[-17:],'wb') as f:
            f.write(down.content)
            print(link[-17:],'downloaded')

    print("data successfully downloaded")

def dataprep(keep_cols:str = ['id_basica', 
                              'sg_empresa_icao', 
                              #'nm_empresa', 
                              #'nm_pais', 
                              #'ds_tipo_empresa',
                              #'ds_di',
                              #'ds_grupo_di',
                              #'ds_tipo_linha',
                              #'ds_servico_tipo_linha',
                              #
                              #'nr_etapa',
                              'nr_ano_partida_real', 
                              #'nm_semestre_partida_real',
                              #'nm_trimestre_partida_real',
                              #
                              'hr_partida_real', 
                              'dt_partida_real', 
                              'nm_mes_partida_real', 
                              'nr_mes_partida_real', 
                              'nm_dia_semana_partida_real', 
                              'nr_dia_partida_real', 
                              'sg_iata_origem', 
                              #'nm_pais_origem',
                              #'nm_regiao_origem',
                              'sg_uf_origem',
                              'nm_municipio_origem',
                              #
                              #'nr_escala_destino',
                              #'hr_chegada_real',
                              #'dt_chegada_real',
                              #'nm_mes_chegada_real',
                              #'nr_mes_chegada_real',
                              #'nm_dia_semana_chegada_real',
                              #'nr_dia_chegada_real',
                              'sg_iata_destino', 
                              #'nm_pais_destino',
                              #'nm_regiao_destino',
                              #'sg_uf_destino',
                              #'nm_municipio_destino',
                              #
                              'nr_assentos_ofertados', 
                              'nr_passag_pagos', 
                              #'nr_passag_gratis',
                              #
                              #'sg_equipamento_icao',
                              #'lt_combustivel',
                              'km_distancia', 
                              'nr_horas_voadas'#, 
                              #'kg_payload',
                              #'kg_bagagem_livre',
                              #'kg_bagagem_excesso',
                              #'kg_carga_paga',
                              #'kg_peso',
                              #'nr_velocidade_media',
             
                              #'nr_carga_paga_km',
                              #'nr_ask',
                              #'nr_rpk'
                             ]):
    """ writes the data.csv file with the columns of interest sumarized for all the months"""

    keep_cols = str(keep_cols).strip('[]').replace("'","").replace(" ","")

    with open('ANAC_DATA/keep_columns.txt','w') as file:
        file.write(keep_cols)

    print('joining and filtering data ...')

    os.system('bash script.sh')

    print('data.csv file created successfully')

def getdata(period:tuple = ('2016-01','2020-06')):
    download_data(period)
    dataprep()

if __name__=='__main__':
    getdata()
