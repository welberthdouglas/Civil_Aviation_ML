import pandas as pd

def keep_columns(keep_cols:str = ['id_basica',
             'sg_empresa_icao',
             'nm_empresa',
             'nm_pais',
             'ds_tipo_empresa',
             'ds_di',
             'ds_grupo_di',
             'ds_tipo_linha',
             'ds_servico_tipo_linha',
             
             'nr_etapa',
             'nr_ano_partida_real',
             'nm_semestre_partida_real',
             'nm_trimestre_partida_real',
             
             'hr_partida_real',
             'dt_partida_real',
             'nm_mes_partida_real',
             'nm_dia_semana_partida_real',
             'nr_dia_partida_real',
             'sg_iata_origem',
             'nm_pais_origem',
             'nm_regiao_origem',
             'sg_uf_origem',
             'nm_municipio_origem',
            
             'hr_chegada_real',
             'dt_chegada_real',
             'nm_mes_chegada_real',
             'nm_dia_semana_chegada_real',
             'nr_dia_chegada_real',
             'sg_iata_destino',
             'nm_pais_destino',
             'nm_regiao_destino',
             'sg_uf_destino',
             'nm_municipio_destino',
            
             'nr_assentos_ofertados',
             'nr_passag_pagos',
             'nr_passag_gratis',
             
             'sg_equipamento_icao',
             'lt_combustivel',
             'km_distancia',
             'nr_horas_voadas',
             'kg_payload',
             'kg_bagagem_livre',
             'kg_bagagem_excesso',
             'kg_carga_paga',
             'kg_peso',
             'nr_velocidade_media',
             
             'nr_carga_paga_km',
             'nr_ask',
             'nr_rpk']):
	""" writes a .txt file with the columns of interest"""

	keep_cols = str(keep_cols).strip('[]').replace("'","").replace(" ","")
	f = open('keep_columns.txt','w')
	f.write(keep_cols)
	f.close()

if __name__=='__main__':
	keep_columns()
