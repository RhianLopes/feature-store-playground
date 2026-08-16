# feature-store-playground

Playground local, ponta a ponta, de feature store com [Feast](https://feast.dev)
0.65.0, gerenciado com [uv](https://docs.astral.sh/uv/):

- **Offline store**: Delta Lake local (arquivos, sem Spark), lido via
  offline store `duckdb`/ibis do Feast.
- **Registry**: local (`data/registry.db`).
- **Online store**: Redis, rodando via Docker Compose (+ RedisInsight para
  inspeção visual das chaves).
- **Feature server HTTP**: `feast serve`, expõe `POST /get-online-features`
  (rodando via Docker Compose).
- **Feast UI**: `feast ui`, visualiza entidades/feature views/lineage
  (rodando via Docker Compose).
- **Notebooks** (`notebooks/*.ipynb`, via JupyterLab): um para gerar os dados
  mockados de localização/status de motoristas, outro de playground
  explorando plan/apply, historical features, materialize e online features
  (via SDK e via HTTP).

Dados 100% sintéticos — sem qualquer relação com clientes reais.

## Serviços locais

Com tudo no ar (passos abaixo), os links ficam disponíveis em:

| Serviço | URL |
|---|---|
| Feature server (HTTP) | http://localhost:6566 |
| Feast UI | http://localhost:8888 |
| RedisInsight | http://localhost:5540 |
| Feast Docs | https://feast.dev/ |

## Quickstart

```powershell
# 1. Ambiente
uv python install 3.11
uv python pin 3.11
uv sync

# 2. Redis + RedisInsight + Feature server (HTTP) + Feast UI
docker compose up -d --build

# 3. JupyterLab — rodar os notebooks (gera os dados mock, aplica o feature
#    repo, materializa no Redis, testa online features via SDK e HTTP)
uv run jupyter lab
# abrir notebooks/01_generate_mock_data.ipynb e depois notebooks/02_playground.ipynb,
# rodando todas as células em ordem
```

O feature server e o Feast UI leem `feature_repo/` e `data/` via bind mount, então
mudanças feitas pelos notebooks (registry, dados materializados) aparecem sem
rebuild — só é preciso `docker compose restart feature-server feast-ui` depois
de um `feast apply`/`feast materialize` para o Feast recarregar o registry.
