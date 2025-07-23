# Brewery Pipeline - Data Engineering Challenge

Este projeto implementa um pipeline de dados baseado na **arquitetura Medallion** (Bronze, Silver, Gold), utilizando a API [Open Brewery DB](https://www.openbrewerydb.org/). O pipeline foi construído com **Apache Airflow**, é executado via **Docker**, e os dados são salvos localmente em camadas de um *data lake*.


- DAG do Airflow (pipeline)
- Scripts Python: extract, transform, load, validate
- Testes automatizados com pytest
- Data lake local
- Dados brutos (JSON)
- Dados tratados (Parquet)
- Dados agregados (Parquet)


### Como executar o projeto ?
Instalar Docker e Docker Compose instalados: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

1. Clonar o projeto:
git clone [https://github.com/seu-usuario/brewery_pipeline.git](https://github.com/seu-usuario/brewery_pipeline.git)

2. Navegue ate a pasta raiz do projeto (CMD ou Shell):
   
   ```cd C:/brewery_pipeline```

3. Subir os containers com o Airflow:
   
     ```docker-compose up --build```

4. Acesse a tela do Airflow em: 
[http://localhost:8080](http://localhost:8080)

5. Login no Airflow:
Usuário e senha padrão (gerado automaticamente):

    - **Usuário:** `admin`
    - **Senha:** `senha estará presente no arquivo (simple_auth_manager_passwords.json.generated)`

      (O arquivo se encontra na pasta raiz do projeto.)

6. Ativar DAG:
    a DAG está configurada para rodar todos os dias a 00h no entanto precisamos ativar.
    <img width="1362" height="382" alt="image" src="https://github.com/user-attachments/assets/7eb42f9f-a080-4695-8fec-cce6d1288721" />

    ao lado do botão de execução "Trigger DAG" clique para que fique azul conforme a imagem acima.

7. Execução DAG:
Clique em **"Trigger DAG"** (ícone de raio) para inciar e executar.


## Etapas do Pipeline (Arquitetura Medallion)
**Bronze** ->  Dados brutos da API são extraídos em JSON.
**Silver** ->   Dados transformados em formato Parquet, particionados por estado.
**Gold** ->     Agregação final: quantidade de cervejarias por tipo e estado.


## Validação dos Dados
Após rodar a DAG com sucesso, os dados ficam disponíveis em:

**Bronze:** `data/bronze/*.json`  
**Silver:** `data/silver/state=*/breweries.parquet`  
**Gold:** `data/gold/breweries_aggregated.parquet`

Você pode abrir os arquivos `.parquet` com:

```python
import pandas as pd

df_gold = pd.read_parquet("data/gold/breweries_aggregated.parquet")
print(df_gold.head())
```

Ou abrir diretamente no **DBeaver** usando uma conexão **DuckDB** com estes comandos:

```sql
SELECT * 
FROM read_parquet('C:/Alexandre/WORK/brewery_pipeline/data/gold/breweries_aggregated.parquet');


SELECT * 
FROM read_parquet('C:/Alexandre/WORK/brewery_pipeline/data/silver/breweries.parquet/state=*/*.parquet');


SELECT * 
FROM read_json_auto('C:/Alexandre/WORK/brewery_pipeline/data/bronze/breweries_*.json');

```

## Logs
Os logs das execuções ficam salvos em:

"logs/dag_id=brewery_pipeline/run_id=.../task_id=extract/attempt=1.log"

Você também pode visualizar todos os logs diretamente na interface do Airflow: clique em uma task > "View Log".


## Monitoramento

O monitoramento é feito via interface gráfica do Airflow (Graph View e Tree View).  
Além disso, a task `validate` implementa checagens básicas de integridade após o `load`.


## Testes
Para rodar os testes locais (se tiver Python instalado):

```bash
pip install -r requirements.txt
pytest tests/
```

## Melhorias Futuras

- Configurar alertas por e-mail em caso de falha
- Subir os dados para um data lake real (S3, GCS)
- Agregar em dashboards (Grafana, Superset)



Alexandre Vitor – Desafio técnico de Engenharia de Dados | BEES
