import typing
from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self) -> None:
        self.log: list[typing.Any] = []


    @abstractmethod #提供されたデータがプロセッサーに取り込めるか判断
    def validate(self, data: typing.Any) -> bool:
        pass


    @abstractmethod #入力データを処理する
    def ingest(self, data: typing.Any) -> None:
        pass


    #一番古いデータを削除するオーバーライドしなくていい
    def output(self) -> typing.Any:
        old_data: typing.Any = self.log[0]
        self.log.pop(0)
        return old_data


#リストでもらった値をintまたは、flote型でいれていく
#int()にできるものを取り込むべきなの？

#int,float またはその混合のリストを取り込む
class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float, list)):
            if isinstance(data, (int, float)):
                return True
            else:
                for d in data:
                    if isinstance(d,(int, float)):
                        continue
                    return False
                return True
        return False

    #リストにして入れていく
    def ingest(self, data: int|float|list) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, (int, float)):
            self.log.append(data)
        else:
            for d in data:
                self.log.append(d)


#str及び文字列のリストを取り込む
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
            raise ValueError("Improper numeric data")
        if isinstance(data, str):
            self.log.append(data)
        else:
            for d in data:
                self.log.append(d)


#dictやそのリストを取り込む
class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (dict, list)):
            if isinstance(data, dict):
                return True
            else:
                for d in data:
                    if isinstance(d, dict):
                        continue
                    return False
                return True
        return False


    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, dict):
            self.log.append(data)
        else:
            for d in data:
                self.log.append(d)


def main() -> None:
    try:
        print("=== Code Nexus - Data Processor ===\n")
        print("Testing Numeric Processor...")
        num = NumericProcessor()
        print(f" Trying to validate input '42': {num.validate(42)}")
        print(f" Trying to validate input 'Hello': {num.validate('Hello')}")
        print(" Test invalid ingestion of string 'foo' without prior validation:")
        try:
            num.ingest('foo')
        except ValueError as e:
            print(f" Got exception: {e}")
        print(f" Processing data: [1, 2, 3, 4, 5]")
        num.ingest([1, 2, 3, 4, 5])
        print(" Extracting 3 values...")
        for i in range(3):
            value = num.output()
            print(f" Numeric value {i}: {value}")

        print("\nTesting Text Processor...")
        text = TextProcessor()
        print(f" Trying to validate input '42': {text.validate(42)}")
        print(f" Processing data: ['Hello', 'Nexus', 'World']")
        text.ingest(['Hello', 'Nexus', 'World'])
        print(" Extracting 1 values...")
        for i in range(1):
            value = text.output()
            print(f" Text value {i}: {value}")

        print("\nTesting Log Processor...")
        log = LogProcessor()
        print(f" Trying to validate input 'Hello': {log.validate('Hello')}")
        print(
            " Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, "
             "{'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]"
        )
        log.ingest(
             [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},\
              {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
        )
        print(" Extracting 2 values...")
        for i in range(2):
            logs = log.output()
            key1, key2 = logs
            print(f" Log entry {i}: {logs[key1]}: {logs[key2]}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
