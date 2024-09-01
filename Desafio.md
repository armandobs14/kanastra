# Take Home Test

Todos os datasets mencionados, serão encontrados na sessão *Datasets,* em um .ZIP, ao final do documento.

## 1 -  Análises com SQL

Para esse desafio será usado o DBeaver, para obter os dados e escrever consultas SQL:

1. Acesse o link https://dbeaver.io/download/, baixe e instale a versão compatível com seu sistema operacional.
2. Inicie o programa e aceite a sugestão de iniciar o 'Sample Database’, se preciso mais informações acesse https://dbeaver.com/docs/wiki/Sample-Database/. 
3. Clique duas vezes na pasta 'Tables' e depois em 'ER Diagram' para acessar o schema do banco. Acesse https://dbeaver.com/docs/wiki/Database-Structure-Diagrams/ para entender como utilizar e ler o ERD (Entity Relation Diagram) no DBeaver. 

Caso tenha problemas técnicos para realizar esses passos, envie seu problema para o recrutamento.

Os dados do Sample Database do DBeaver contém informações de músicas vendidas em uma loja. Com base nesses dados, um analista estruturou em Excel a seguinte análise:

| artist | genre | sales | sales_percentage_by_genre | cumulative_sum_by_genre |
| --- | --- | --- | --- | --- |
| Audioslave | Alternative | 4.95 | 35.7% | 35.7% |
| Chris Cornell | Alternative | 3.96 | 28.6% | 64.3% |
| Temple of the Dog | Alternative | 3.96 | 28.6% | 92.9% |
| Calexico | Alternative | 0.99 | 7.1% | 100.0% |
| Titãs | Alternative & Punk | 33.66 | 13.9% | 13.9% |
| Faith No More | Alternative & Punk | 32.67 | 13.5% | 27.5% |
| Green Day | Alternative & Punk | 32.67 | 13.5% | 41.0% |
| R.E.M. | Alternative & Punk | 24.75 | 10.2% | 51.2% |
| Smashing Pumpkins | Alternative & Punk | 23.76 | 9.8% | 61.1% |
| The Tea Party | Alternative & Punk | 16.83 | 7.0% | 68.0% |
| … | … | … | … | … |

Descrição das colunas da análise, a origem dos dados é mostrada na notação **(Coluna | Tabela de origem)** :

- **artist:** contém o nome dos artistas autores das músicas vendidas / faturadas (Name | Artist)
- **genre:** contém o gênero das músicas (Name | Genre)
- **sales:** valor do faturamento referente as músicas vendidas daquele artista, naquele gênero (*UnitPrice|InvoiceLine* * *Quantity|InvoiceLine*)
- **sales_by_percentage_by_genre:** Essa coluna divide o valor de vendas de um determinado artista e gênero pelo total de vendas no gênero. Ex: No gênero 'Alternative' o artista 'audioslave' teve 4.95 de vendas, representando 35.7% do total de vendas desse gênero
- **cumulative_sum_by_genre:** contém a soma acumulada dos valores na coluna *sales_by_percentage_by_genre*. A soma cumulativa resulta em 100% para a última música listada de cada gênero. Note que os valor da soma é igual ao valor da linha atual somado com as músicas listadas anteriormente para um determinado gênero

A ordenação dos dados também é importante, a tabela desenvolvida pelo analista está ordenada de forma ascendente pelo nome do gênero e de forma descendente pela coluna *sales_percentage_by_genre.*

O mesmo artista pode ter músicas com gêneros diferentes

**Entrega:**

Pedimos que crie uma consulta em SQL que replique o resultado da tabela acima, ou seja, o resultado das 10 primeira linhas da consulta devem resultar na mesma tabela vista no exemplo.

Considere que a consulta deve seguir boas práticas, pois será salva no repositório do time e pode ser editada no futuro. 

Caso não consiga replicar a tabela como mostrada no exemplo, envie o resultado mais próximo que conseguiu obter.

**O que esperamos:**

- Fundamentos e casos de uso avançados de SQL
- Boas práticas de programação
- Código limpo e simples de entender

---

### 2 - ETL em PySpark

Também utilizando os dados de viagens de táxi realizadas em New York, agora vamos construir um processo ETL, este será responsável por escrever um output com as seguintes informações e características:

- Qual vendor mais viajou de táxi em cada ano
**Critério de desempate:** quem percorreu o maior percurso, ordem alfabética dos nomes
- Qual a semana de cada ano que mais teve viagens de táxi.
- Quantas viagens o vendor com mais viagens naquele ano fez na semana com mais viagens de táxi no ano.

**O que esperamos:**

- Fundamentos de linguagem de programação e estruturas de dados
- Boas práticas de programação: setup de ambiente, documentação, Orientação a Objeto, Design Patterns e S.O.L.I.D
- Código limpo e simples de entender

**Entrega:**

O entregável desse exercício será um pacote .zip com o código e o output de execução do ETL em formato CSV. Atente-se a deixar descrito um passo a passo de como executar a sua solução. O framework / tecnologia utilizada pra desenvolver a *pipeline* será considerada na avaliação (preferencialmente PySpark) e esperamos boas práticas de engenharia de software na construção da solução (referente a estruturação e construção do código, setup do ambiente, testes, etc).

**Bônus:** Deixe comentários no código explicando o que você estava pensando no momento em que escreveu aquele bloco de código.

---

### 3 - Arquitetura da Plataforma de Dados para eventos

Sabendo que hoje temos serviços de aplicativos que conectam motoristas e pessoas que precisam de carona, possibilitando a criação de uma alternativa ao táxi. Imagine que temos as seguintes fontes de dados:

- **Usuários:** Contempla clientes e motoristas identificados por uma coluna tipo.
- **Corridas:** Referência cliente e motorista, também contém informações sobre a viagem realizada.

Crie um desenho de solução que utiliza CDC para coletar informações de ambas as fontes e une os dados e armazena em um Data Lake.

Atente-se que não podemos ter corridas sem usuários cadastrados, então não pode haver assincronia entre os dados.

⚠️ **Pontos de atenção:**

- **Descreva o racional** das decisões de cada um dos componentes que adicionar em sua arquitetura (em bullet points, texto, slide ou da forma que preferir);
- Não esqueça de componentes importantes da plataforma como **qualidade e governança de dados;**
- Favoreça tecnologias *open-source*! Não gostamos de ficar presos a soluções específicas de *cloud providers;*
- Se achar relevante, também mencione componentes ou módulos a mais que não colocou no desenho.

**Bônus:** Deixe explícito quais tecnologias você utilizaria para implementar o desenho de solução.

### Datasets para download

[kanastra-data-eng-test-datasets.zip](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51b83ae3-2edb-4516-9464-34842954651a/kanastra-data-eng-test-datasets.zip)