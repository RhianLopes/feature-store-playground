from feast import FeatureService

from features import driver_stats_fv

driver_activity_v1 = FeatureService(
    name="driver_activity_v1",
    features=[driver_stats_fv],
)
