import numpy as np
from typing import Dict

import ray
from ray.data import read_semantic_service_data

ray.init()

def data_calaculate_task(batch: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
    batch["transform_data"] = batch["data"] * 2
    return batch

def data_filter_task(row):
    return row["transform_data"] > 100

batch_size = 10
batch_num = 10

dataset = (
    read_semantic_service_data("0.0.0.0", 8000, batch_size, batch_num)
    .map_batches(data_calaculate_task)
    .filter(data_filter_task)
    .materialize()
)

pytorch_dataset = dataset.iter_torch_batches(batch_size=batch_size)

for batch in pytorch_dataset:
    print(batch)
