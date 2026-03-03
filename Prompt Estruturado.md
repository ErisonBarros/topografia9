

```
## Papel (Role) ###
Você é um Engenheiro de Dados e Desenvolvedor Python Sênior.

### Tarefa (Task) ###
Sua tarefa DEVE ser escrever um script em Python para ler um diretório local, extrair metadados dos arquivos e gerar um relatório estruturado em Excel.

### Instruções Passo a Passo ###
Pense passo a passo e implemente o código seguindo rigorosamente estas etapas:
1. Importe as bibliotecas necessárias para manipulação de sistema de arquivos e dados (ex: `os`, `pandas`, `datetime`).
2. Defina o caminho alvo do diretório exatamente como: `G:\Meu Drive\UFPE\DECART\DISCIPLINAS\GRADUAÇÃO\Topografia 9`.
3. Itere sobre todos os arquivos contidos na pasta para extrair as seguintes informações de cada arquivo:
   - Data de criação do arquivo
   - Nome do arquivo
   - Tamanho do arquivo (em bytes ou KB)
   - Tipo do arquivo (extensão)
   - Caminho do arquivo
4. Armazene esses dados em um DataFrame do Pandas e organize as colunas começando obrigatoriamente pela coluna "Data".
5. Ordene todos os registros pela data de criação em ordem crescente.
6. Adicione uma linha final na planilha contendo o somatório total exclusivo da coluna "Tamanho do arquivo", garantindo que todas as notas/arquivos da pasta tenham sido processados.
7. Exporte o resultado final para um arquivo no formato Excel (`.xlsx`) salvo no mesmo diretório.

### Formato (Format) ###
- Forneça a documentação e as bibliotecas a serem instaladas delimitadas por <code>...</code>.
- O código em Python deve ser entregue limpo, otimizado e dentro de um bloco de código ` ```python ... ``` `.
- Não inclua arquivos ausentes ou diretórios na soma, limite a execução aos arquivos válidos.
```
