from datetime import timedelta

from feast import FeatureView, Field
from feast.types import Float32, String

from data_sources import driver_stats_source
from entities import driver

driver_stats_fv = FeatureView(
    name="driver_stats",
    entities=[driver],
    # ttl generoso (30 dias): `materialize_incremental` usa (now - ttl) como
    # início da janela na primeira execução (sem checkpoint prévio); o mock
    # gera eventos a partir de ~10 dias atrás, então o ttl precisa cobrir
    # isso com folga para os dados caírem dentro da janela materializada.
    ttl=timedelta(days=30),
    schema=[
        Field(name="latitude", dtype=Float32),
        Field(name="longitude", dtype=Float32),
        # status categórico como string: available | en_route | busy | offline
        # (Feast não tem tipo enum nativo; valores são fixados no notebook de mock)
        Field(name="status", dtype=String),
    ],
    online=True,
    source=driver_stats_source,
    tags={"team": "playground"},
)
