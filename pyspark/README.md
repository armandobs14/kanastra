# 2 - ETL em PySpark
Esse projeto foi desenvolvido utilizando linux, dessa forma é recomendável utilizar alguma distribuição da sua escolha para a realização dos testes.

Todos os scripts principais, bem como funções auxiliares podem ser encontradas na pasta [scripts](scripts/)

## Requisitos
  - [make](https://pt.linux-console.net/?p=14595): Para a execução do makefile
  - [docker](https://docs.docker.com/engine/install/ubuntu/): para a execução dos containeres


## Processo de execução

### 1. baixar dados
Salve o arquivo `kanastra-data-eng-test-datasets.zip` na sua pasta de Downloads `/home/{usuario}/Downlods`.

### 2. Configurar minio
Para trazer o conteúdo do zip para dentro do data-lake rode o comando

```bash
# Cria datalake com arquivos baixados
make setup_minio
```
Ele irá descompactar o conteúdo e salvar dentro do data-lake local no seguinte diretório [/kanastra/raw/taxi](localhost:9001/browser/kanastra/raw/taxi/). Para acessar o lake utilize as senhas [1]

### 3. Iniciar cluster spark
Para o processo exeutar de forma adequada o cluster spark precisa estar em execução. Para isso execute o comando a seguir:
```bash
# inicia clister spark
make cluster_create
```
### 3. Executar ETL
Com o cluster em execução rode o seguinte comando
```bash
# executa pipeline
make pipeline
```

Nessa etapa o script de [pipeline](scripts/pipeline.py) executa três ETLs:

**Staging**:
- [Trip](scripts/trip_staging.py):
  - Lê arquivos json
  - Cria colunas `year` e `year_week`
  - Salva dados em [staging](http://localhost:9001/browser/kanastra/staging/taxi-trips/) particionados pelas colunas `year` e `year_week`
- [Vendor](scripts/vendor_staging.py):
  - Lê arquivo csv
  - Salva dados em [staging](http://localhost:9001/browser/kanastra/staging/vendor-lookup/)

**Curated**:
- [Trip](scripts/trip_curated.py):
  - Lê arquivos de [staging](http://localhost:9001/browser/kanastra/staging/)
  - Calcula as viagens
  - Salva dado CSV em [curated](http://localhost:9001/browser/kanastra/curated/taxi-trips.csv/)


### 4. Conteúdo final
Ao termino da execução p teudo do [CSV](arquivo.csv) será o como o abaixo:
| year | year_week | name                              | trips |
|------|-----------|-----------------------------------|-------|
| 2012 | 4         | Creative Mobile Technologies, LLC | 11400 |
| 2011 | 8         | Creative Mobile Technologies, LLC | 10691 |
| 2009 | 11        | Creative Mobile Technologies, LLC | 10097 |
| 2010 | 6         | Creative Mobile Technologies, LLC | 10004 |

# Referências
[1] Senhas de acesso ao minio
  - usuário: minio_key
  - senha: minio_secret