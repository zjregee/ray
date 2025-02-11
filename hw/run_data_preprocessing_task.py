import ray
from ray.data import read_semantic_service_data

ray.init()

ds = read_semantic_service_data("0.0.0.0", 8000)
print(ds.count())
print(ds.schema())
print(ds.take(5))

ray.shutdown()
