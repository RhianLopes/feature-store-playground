from pathlib import Path

from feast import FileSource
from feast.data_format import DeltaFormat

# Usamos `feast.data_format.DeltaFormat` (não `feast.table_format.DeltaFormat`)
# porque este último só é suportado em conjunto com SparkSource. Aqui a tabela
# Delta é lida sem Spark, via offline_store `duckdb` (backend ibis/duckdb).
#
# Path absoluto (e não relativo tipo "../data/...") de propósito: o backend
# duckdb/ibis resolve `FileSource.path` relativo ao cwd do processo que
# invoca o `feast`, e não ao diretório do feature_repo/ (diferente do
# `registry`, que é sempre resolvido relativo ao feature_store.yaml). Um path
# relativo aqui quebraria dependendo de onde `feast apply`/`materialize`
# fossem chamados; calculamos o path a partir da localização deste arquivo
# para funcionar sempre, independente do cwd.
REPO_ROOT = Path(__file__).resolve().parent.parent
DELTA_TABLE_PATH = REPO_ROOT / "data" / "offline_store" / "driver_stats"

driver_stats_source = FileSource(
    name="driver_stats_source",
    path=str(DELTA_TABLE_PATH),
    file_format=DeltaFormat(),
    timestamp_field="event_timestamp",
    created_timestamp_column="created_timestamp",
    description="Mock de localização/status de motoristas, offline store em Delta Lake local",
)
