from feast import Entity
from feast.value_type import ValueType

driver = Entity(
    name="driver",
    join_keys=["driver_id"],
    value_type=ValueType.INT64,
    description="Identificador único do motorista (dado mockado, sem PII real)",
)
