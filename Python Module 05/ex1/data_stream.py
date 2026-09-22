#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any


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


class DataStream():
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
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
        for proc in self._processors:
            print(f"{proc.__class__.__name__}: total {proc.rank} items "
                  f"processed, remaining {len(proc._storage)} on processor")


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
        print(f"{label} {i}: {processor.output()[1]}")
    print("-" * 50)


def main() -> None:

    print("=== Code Nexus - Data Stream ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    stream.register_processor(numeric)

    print("Send first batch of data on stream: ['Hello world', "
          "[3.14, -1, 2.71], "
          "[{'log_level': 'WARNING', 'log_message': "
          "'Telnet access! Use ssh instead'}, "
          "{'log_level': 'INFO', 'log_message': "
          "'User wil isconnected'}], 42, ['Hi', 'five']] ")

    full_list: list = ['Hello world',
                       [3.14, -1, 2.71],
                       [{'log_level': 'WARNING',
                        'log_message': 'Telnet access! Use ssh instead'},
                        {'log_level': 'INFO',
                        'log_message': 'User wil is connected'}],
                       42, ['Hi', 'five']]

    stream.process_stream(full_list)
    stream.print_processors_stats()

    print("Registering other data processors")
    print("Send the same batch again")

    stream.register_processor(text)
    stream.register_processor(log)

    print("== DataStream statistics== ")
    stream.process_stream(full_list)
    stream.print_processors_stats()

    print("Consume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")

    display_output(numeric, "Numeric Processor", 3)
    display_output(text, "Text Processor", 2)
    display_output(log, "Log Processor")

    stream.print_processors_stats()


if __name__ == "__main__":
    main()
