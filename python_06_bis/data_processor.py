import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.log: list[list[typing.Any]] = []
        self._logcount: int = 0

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.log) == 0:
            raise IndexError("IndexError: No logs found")
        old_data: list[typing.Any] = self.log.pop(0)
        return (old_data[0], old_data[1])


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float, list)):
            if isinstance(data, (int, float)):
                return True
            else:
                for d in data:
                    if isinstance(d, (int, float)):
                        continue
                    return False
                return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("ValueError: Improper numeric data")
        if isinstance(data, (int, float)):
            c = self._logcount
            self.log.append([c, str(data)])
            self._logcount += 1
        else:
            for d in data:
                c = self._logcount
                self.log.append([c, str(d)])
                self._logcount += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (str, list)):
            if isinstance(data, str):
                return True
            else:
                for d in data:
                    if isinstance(d, str):
                        continue
                    return False
                return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("ValueError: Improper numeric data")
        if isinstance(data, str):
            c = self._logcount
            self.log.append([c, data])
            self._logcount += 1
        else:
            for d in data:
                c = self._logcount
                self.log.append([c, d])
                self._logcount += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (dict, list)):
            if isinstance(data, dict):
                if all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items()
                ):
                    return True
            else:
                for d in data:
                    if isinstance(d, dict):
                        if not all(
                            isinstance(k, str) and isinstance(v, str)
                            for k, v in d.items()
                        ):
                            return False
                return True
        return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("ValueError: Improper numeric data")
        if isinstance(data, dict):
            c = self._logcount
            self.log.append([c, ': '.join(data.values())])
            self._logcount += 1
        else:
            for d in data:
                c = self._logcount
                self.log.append([c, ': '.join(d.values())])
                self._logcount += 1


def main() -> None:
    try:
        print(
            "=== Code Nexus - Data Processor ===\n"
            "\nTesting Numeric Processor..."
        )
        num = NumericProcessor()
        print(
            f" Trying to validate input '42': {num.validate(42)}\n"
            f" Trying to validate input 'Hello': {num.validate('Hello')}\n"
            " Test invalid ingestion of string 'foo' without prior validation:"
        )
        try:
            num.ingest('foo')
        except ValueError as e:
            print(f" Got exception: {e}")
        print(" Processing data: [1, 2, 3, 4, 5]")
        num.ingest([1, 2, 3, 4, 5])
        print(" Extracting 3 values...")
        for i in range(3):
            c, value = num.output()
            print(f" Numeric value {c}: {value}")

        print("\nTesting Text Processor...")
        text = TextProcessor()
        print(f" Trying to validate input '42': {text.validate(42)}")
        print(" Processing data: ['Hello', 'Nexus', 'World']")
        text.ingest(['Hello', 'Nexus', 'World'])
        print(" Extracting 1 values...")
        for i in range(1):
            c, value = text.output()
            print(f" Text value {c}: {value}")

        print("\nTesting Log Processor...")
        log = LogProcessor()
        print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
        print(
            " Processing data:"
            "[{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, "
            "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]"
        )
        log.ingest(
            [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
             {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
        )
        print(" Extracting 2 values...")
        for i in range(2):
            c, logs = log.output()
            print(f" Log entry {c}: {logs}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
