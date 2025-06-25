from etl import extrair_df, transformar_df, carregar_df


caminho_arquivo_entrada = 'src/AirbnbOpenData.csv'
caminho_arquivo_saida = 'src/AirbnbOpenDataOutput.csv'


df = extrair_df(caminho_arquivo_entrada)
df = transformar_df(df)
df = carregar_df(df, caminho_arquivo_saida)

