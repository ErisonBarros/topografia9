import os
from datetime import datetime
from pathlib import Path
import pandas as pd

def gerar_relatorio_arquivos():
    """
    Função principal que varre o diretório alvo, extrai metadados dos arquivos
    e gera um relatório em formato Excel (.xlsx) contendo a listagem e o 
    somatório total do tamanho dos arquivos.
    """
    # 2. Caminho alvo do diretório
    diretorio_alvo = Path(r"G:\Meu Drive\UFPE\DECART\DISCIPLINAS\GRADUAÇÃO\Topografia 9")
    
    dados_arquivos = []

    # 3. Iterar sobre todos os arquivos (incluindo subdiretórios)
    for caminho_arquivo in diretorio_alvo.rglob('*'):
        # Avaliar estritamente apenas arquivos válidos e existentes
        if not caminho_arquivo.is_file() or not caminho_arquivo.exists():
            continue
            
        try:
            # Extração de metadados
            estatisticas = caminho_arquivo.stat()
            
            # Data de criação (st_ctime no Windows representa criação)
            data_criacao = datetime.fromtimestamp(estatisticas.st_ctime)
            
            nome_arquivo = caminho_arquivo.name
            tamanho_bytes = estatisticas.st_size
            extensao = caminho_arquivo.suffix if caminho_arquivo.suffix else "Sem extensão"
            caminho_absoluto = str(caminho_arquivo.absolute())
            
            dados_arquivos.append({
                'Data': data_criacao,
                'Nome': nome_arquivo,
                'Tamanho (Bytes)': tamanho_bytes,
                'Extensão': extensao,
                'Caminho': caminho_absoluto
            })
            
        except Exception as e:
            print(f"Aviso: Não foi possível processar o arquivo {caminho_arquivo}. Erro: {e}")

    # 4. Criação do DataFrame e organização das colunas (começando por Data)
    df = pd.DataFrame(dados_arquivos)
    
    if not df.empty:
        df = df[['Data', 'Nome', 'Tamanho (Bytes)', 'Extensão', 'Caminho']]
        
        # 5. Ordenação decrescente não! A regra dita "crescente"
        df = df.sort_values(by='Data', ascending=True)
        
        # 6. Adição da linha com o somatório total exclusivo da coluna tamanho
        tamanho_total = df['Tamanho (Bytes)'].sum()
        
        linha_total = pd.DataFrame([{
            'Data': pd.NaT, 
            'Nome': 'TOTAL', 
            'Tamanho (Bytes)': tamanho_total, 
            'Extensão': '', 
            'Caminho': ''
        }])
        
        df_final = pd.concat([df, linha_total], ignore_index=True)
        
        # 7. Exportar para Excel no mesmo diretório
        arquivo_saida = diretorio_alvo / "Relatorio_Metadados_Topografia.xlsx"
        df_final.to_excel(arquivo_saida, index=False)
        print(f"Relatório gerado com sucesso em: {arquivo_saida}")
    else:
        print("Nenhum arquivo encontrado no diretório especificado.")

if __name__ == "__main__":
    gerar_relatorio_arquivos()
