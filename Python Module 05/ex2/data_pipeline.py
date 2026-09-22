#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any, Protocol


class DataProcessorError(Exception):
    def __init__(self, msg: str = "Data processing failed") -> None:
        super().__init__(msg)


class NumericProcessorError(DataProcessorError):
    def __init__(self, msg: str = "Numeric data rejected") -> None:
        super().__init__(msg)


class TextProcessorError(DataProcessorError):
    def __init__(self, msg: str = "Text data rejected") -> None:
        super().__init__(msg)


class LogProcessorError(DataProcessorError):
    def __init__(self, msg: str = "Log data rejected") -> None:
        super().__init__(msg)


class DataProcessor(ABC):
    """Blueprint for all data processor subclasses."""

    def __init__(self) -> None:
        super().__init__()
        self._storage: list[tuple[int, str]] = []
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def _save(self, data: str) -> None:
        self._storage.append((self.rank, data))
        self.rank += 1

    def output(self) -> tuple[int, str]:
        return self._storage.pop(0)

    def get_storage(self) -> list[tuple[int, str]]:
        return self._storage


class NumericProcessor(DataProcessor):
    """Processes int, float, and lists of both types."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)
        return isinstance(data, (int, float))

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise NumericProcessorError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._save(str(item))
        else:
            self._save(str(data))


class TextProcessor(DataProcessor):
    """Processes str and lists of strings."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TextProcessorError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._save(str(item))
        else:
            self._save(str(data))


class LogProcessor(DataProcessor):
    """Processes dict and lists of dicts."""

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()) for item in data)
        else:
            return isinstance(data, dict) and all(
                isinstance(key, str) and
                isinstance(value, str) for key, value in data.items())

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise LogProcessorError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self._save(f"{item['log_level']}: {item['log_message']}")
        else:
            self._save(f"{data['log_level']}: {data['log_message']}")


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self.count: list[int] = [0]

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            flag = False
            for proc in self._processors:
                if proc.validate(item):
                    proc.ingest(item)
                    flag = True
                    break
            if not flag:
                print("DataStream error - Can't process"
                      f"element in stream: {item}")

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==\n")
        if not self._processors:
            print("No processor found, no data")
        for proc in self._processors:
            print(f"{proc.__class__.__name__}: total {proc.rank} items "
                  f"processed, remaining {len(proc._storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            output_list: list[tuple[int, str]] = []

            for _ in range(nb):
                try:
                    output_list.append(proc.output())
                except IndexError:
                    break

            plugin.process_output(output_list)


class CsvExportPlugin:
    def process_output(self, data: list[tuple[int, str]]):
        values: list[str] = []

        for _, value in data:
            values.append(value)

        print(f"CSV Output:\n{','.join(values)}")


class JsonExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        json = list()
        for key, value in data:
            json.append(f'"item_{key}": "{value}"')

        print(f"JSON Output:\n{{{', '.join(json)}}}")


def title(text: str) -> None:
    """Display a title"""

    length: int = len(text)
    print("\n" + ("=" * length))
    print(text)
    print(("=" * length) + "\n")


def display_output(processor: DataProcessor,
                   label: str, count: int = 1) -> None:
    """Display the output method"""

    print(f"\nExtracting {count} value(s)...")
    print("-" * 50)
    for i in range(count):
        print(f"{label} {i}: {processor.output()[1]}\n")
    print("-" * 50)


def main() -> None:

    print("=== Code Nexus - Data Pipeline ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    processors_list = [numeric, text, log]

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processor\n")
    for proc in processors_list:
        stream.register_processor(proc)

    print("Send first batch of data on stream: ['Hello world', "
          "[3.14, -1, 2.71], "
          "[{'log_level': 'WARNING', 'log_message': "
          "'Telnet access! Use ssh instead'}, "
          "{'log_level': 'INFO', 'log_message': "
          "'User wil is connected'}], 42, ['Hi', 'five']]\n")

    full_list: list = ['Hello world',
                       [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                        'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                        'log_message': 'User wil is connected'}],
                       42, ['Hi', 'five']]

    stream.process_stream(full_list)
    stream.print_processors_stats()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CsvExportPlugin()
    stream.output_pipeline(3, csv_plugin)

    stream.print_processors_stats()

    print("Send another batch of data: [21, ['I love AI',"
          "'LLMs are wonderful', 'Stay healthy'],"
          "[{'log_level': 'ERROR', 'log_message': '500 server crash'},"
          "{'log_level': 'NOTICE',"
          "'log_message': 'Certificate expires in 10 days'}],"
          "[32, 42, 64, 84, 128, 168], 'World hello']")

    second_list: list[Any] = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    stream.process_stream(second_list)
    stream.print_processors_stats()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JsonExportPlugin()
    stream.output_pipeline(5, json_plugin)

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
