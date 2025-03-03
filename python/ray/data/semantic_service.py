from typing import Iterator
import pyarrow as pa
import random

class SemanticService:
    def __init__(self, host, port, batch_size, batch_num):
        """初始化语义服务客户端
        Args:
            host (str, optional): 服务器主机地址. 默认为 "localhost"
            port (int, optional): 服务器端口号. 默认为 8000
        """
        self.service_host = host
        self.service_port = port
        self.service_address = f"grpc://{host}:{port}"
        self.batch_size = batch_size
        self.batch_num = batch_num

    def exec_command(self, command: str) -> str:
        """执行语义服务命令
        Args:
            command (str): 要执行的命令字符串
        Returns:
            str: 命令执行的结果
        """
        raise NotImplementedError("not implemented")

    def retrieve_data_all(self) -> Iterator[pa.Table]:
        """从语义数据服务获取所有数据
        Returns:
            Iterator[pa.Table]: 生成器，每次产生一个包含一批从语义服务获取记录数据的 pyarrow Table
        """
        try:
            metadata_client = pa.flight.connect(self.service_address)

            for flight_info in metadata_client.list_flights():
                try:
                    uri = flight_info.endpoints[0].locations[0].uri.decode('utf-8')
                    uri = uri.replace('0.0.0.0', self.service_host)
                    uri = uri.encode('utf-8')

                    steps = flight_info.total_records
                    ticket = flight_info.endpoints[0].ticket
                    data_client = pa.flight.connect(uri)

                    reader = data_client.do_get(ticket)
                    record_reader = reader.to_reader()

                    for _ in range(steps):
                        record = record_reader.read_next_batch()
                        table = pa.Table.from_batches([record])
                        yield table
                finally:
                    data_client.close()
        finally:
            metadata_client.close()

    def retrieve_data_all_mock(self) -> Iterator[pa.Table]:
        """模拟从语义数据服务获取所有数据接口
        Returns:
            Iterator[pa.Table]: 生成器，每次产生一个包含一批 mock 记录数据的 pyarrow Table
        """
        for _ in range(self.batch_num):
            data = [pa.array(
                [random.uniform(1, 100) for _ in range(self.batch_size)],
                type=pa.float64()
            )]
            schema = ["data"]
            yield pa.Table.from_arrays(data, schema)
