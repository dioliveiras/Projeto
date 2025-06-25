import pandas as pd
from logs import registrar_log
from forex_python.converter import CurrencyRates
import time

def extrair_df(caminho_arquivo):
    inicio = time.time()
    try:
        print("Executando tarefa: Extrair")
        df = pd.read_csv(caminho_arquivo, low_memory=False)
        print("Tarefa Extrair finalizada com sucesso.")
        duracao = time.time() - inicio
        registrar_log('Extrair', 'OK', duracao)
        return df
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho_arquivo}' não encontrado.")
        duracao = time.time() - inicio
        registrar_log('Extrair', 'ERRO', duracao)
    except Exception as e:
        print(f"Erro ao extrair arquivo: {e}")
        duracao = time.time() - inicio
        registrar_log('Extrair', 'ERRO', duracao)

def transformar_df(df):
    inicio = time.time()
    print("Executando tarefa: Transformar")
    try:
        c = CurrencyRates()
        # Filtragem básica
        df_cleaned = df[df['id'] != '']
        df_cleaned = df_cleaned[df_cleaned['instant_bookable'] == True] 
        df_cleaned = df_cleaned[df_cleaned['host_identity_verified'] == 'verified']
        df_cleaned = df_cleaned[df_cleaned['cancellation_policy'] == 'flexible']
        df_cleaned = df_cleaned[df_cleaned['room type'] == 'Entire home/apt']

        # Convertendo last review para datetime e removendo NaT
        df_cleaned['last review'] = pd.to_datetime(df_cleaned['last review'], format='%d/%m/%Y', errors='coerce')
        df_cleaned = df_cleaned.dropna(subset=['last review'])

        # Filtrar apenas o último ano disponível
        ultimo_ano = df_cleaned['last review'].dt.year.max()
        df_cleaned = df_cleaned[df_cleaned['last review'].dt.year == ultimo_ano]

        # Limpar e converter 'price' e 'service fee' para float
        df_cleaned['price'] = df_cleaned['price'].str.replace(r'[\$,]', '', regex=True)
        df_cleaned['price'] = pd.to_numeric(df_cleaned['price'], errors='coerce')

        df_cleaned['service fee'] = df_cleaned['service fee'].str.replace(r'[\$,]', '', regex=True)
        df_cleaned['service fee'] = pd.to_numeric(df_cleaned['service fee'], errors='coerce')

        # Converter valores para reais
        cotacao_usd_brl = c.get_rate('USD', 'BRL')
        df_cleaned['price_RS'] = c.convert('USD', 'BRL', df_cleaned['price'])  
        df_cleaned['service fee_RS'] = c.convert('USD', 'BRL', df_cleaned['service fee'])   
        
        print("Tarefa Transformar finalizada com sucesso.")
        duracao = time.time() - inicio
        registrar_log('Transformar', 'OK', duracao)        
        return df_cleaned
    
    except Exception as e:
        print(f"Erro durante a tarefa Transformar: {e}")
        duracao = time.time() - inicio
        registrar_log('Transformar', 'ERRO', duracao) 
        return None

def carregar_df(df, caminho_arquivo_saida):
    inicio = time.time()
    try:
        print("Executando tarefa: Carregar")
        df.to_csv(caminho_arquivo_saida, index=False)
        print("Tarefa Carregar finalizada com sucesso.")
        duracao = time.time() - inicio
        registrar_log('Carregar', 'OK', duracao) 
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        duracao = time.time() - inicio
        registrar_log('Carregar', 'ERRO', duracao) 
