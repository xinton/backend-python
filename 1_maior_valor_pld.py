
import pandas as pd

def extrair_maximos_submercado_anual(arquivo_excel):
    try:
        # Lê o Excel completo
        df = pd.read_excel(arquivo_excel)

        # Captura as datas (linha 0) e os submercados (coluna 2) e valores (a partir da 4ª coluna)
        datas = df.iloc[0, 2:].values
        submercados = df.iloc[1:6, 1].values
        valores = df.iloc[1:6, 3:].values

        # Formata os dados como lista de dicionários
        dados_formatados = []
        for i, sub in enumerate(submercados):
            for j, data in enumerate(datas):
                try:
                    valor = float(valores[i][j])
                    dados_formatados.append({
                        'Data': pd.to_datetime(data),
                        'Submercado': sub,
                        'Valor': valor
                    })
                except:
                    continue

        # Cria DataFrame tabular
        df_formatado = pd.DataFrame(dados_formatados)
        df_formatado['Ano'] = df_formatado['Data'].dt.year

        # Agrupa por submercado e ano e extrai o maior valor
        resultado = df_formatado.groupby(['Submercado', 'Ano'])['Valor'].max().reset_index()

        # Exibe os resultados
        for submercado in resultado['Submercado'].unique():
            print(f"\nSubmercado: {submercado}")
            dados_sub = resultado[resultado['Submercado'] == submercado]
            for _, row in dados_sub.iterrows():
                print(f"Ano: {row['Ano']} - Maior PLD: {row['Valor']:.2f}")

    except Exception as e:
        print("Erro ao processar o arquivo:", e)

if __name__ == "__main__":
    extrair_maximos_submercado_anual("PLD.xlsx")