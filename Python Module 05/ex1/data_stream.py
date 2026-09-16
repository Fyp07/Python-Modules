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
    def __init__(self, data: Any) -> None:
        self._processors: list[DataProcessor] = []

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
            if flag is False:
                raise DataProcessorError("Error")


def title(text: str) -> None:
    """Display a title"""

    length: int = len(text)
    print("\n" + ("=" * length))
    print(text)
    print(("=" * length) + "\n")


def display_output(processor: DataProcessor,
                   label: str, count: int = 1) -> None:
    """Display the output method"""

    print(f"\nExtracting {count} value...")
    print("-" * 50)
    for i in range(count):
        print(f"{label} {i}: {processor.output()[1]}")
    print("-" * 50)


def main() -> None:
    pass


if __name__ == "__main__":
    main()
