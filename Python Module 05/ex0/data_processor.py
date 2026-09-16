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
    """Processes str and lists of str's."""

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
    """Processes dict and lists of dict's."""

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


def title(title: str) -> None:
    length: int = len(title)
    print("\n" + ("=" * length))
    print(title)
    print(("=" * length) + "\n")


def display_output(processor: DataProcessor,
                   label: str, count: int = 1) -> None:
    print(f"\nExtracting {count} value...")
    print("-" * 50)
    for i in range(count):
        print(f"{label} {i}: {processor.output()[1]}")
    print("-" * 50)


def main() -> None:

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("=== Code Nexus - Data Processor ===")

    title("Testing Numeric Processor...")

    # Testing validate with both valid and invalid parameters
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    # Testing invalid ingestion parameter
    print("Testing invalid ingestion of"
          "string 'foo' without prior validation:")
    try:
        print(numeric.ingest('foo'))
    except NumericProcessorError as e:
        print(f"Got exception: {e}")

    # Using valid ingest and output methods
    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])
    display_output(numeric, "Numeric value", 3)

    title("Testing Text Processor...")

    # Testing validate with a invalid parameter
    print(f"Trying to validate input '42': "
          f"{text.validate(42)}")

    # Using valid ingest and output methods
    print("Processing data: ['Hello', 'Nexus', 'World']")
    text.ingest(['Hello', 'Nexus', 'Word'])
    display_output(text, "Text value")

    title("Testing Log Processor...")

    # Testing validate with a invalid parameter
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    # Using valid ingest and output methods
    print("Processing data:  [{'log_level': 'NOTICE', 'log_message':"
          "'Connection to server'}, {'log_level': 'ERROR', 'log_message':"
          "'Unauthorized access!!'}]")
    log.ingest([{'log_level': 'NOTICE',
                 'log_message': 'Connection to server'},
                {'log_level': 'ERROR',
                 'log_message': 'Unauthorized access!!'}])
    display_output(log, "Log entry", 2)


if __name__ == "__main__":
    main()
