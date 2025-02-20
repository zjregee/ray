import time
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

batch_size = 10000
batch_nums = [100, 200, 300, 400, 500]

for batch_num in batch_nums:
    start_time = time.perf_counter()

    dataset = (
        read_semantic_service_data("0.0.0.0", 8000, batch_size, batch_num)
        .map_batches(data_calaculate_task)
        .filter(data_filter_task)
        .materialize()
    )

    end_time = time.perf_counter()

    elapsed_time = (end_time - start_time) * 1000
    print(f"num: {batch_size * batch_num}, duration: {elapsed_time:.2f}ms, batch_size: {batch_size}, batch_num: {batch_num}")
