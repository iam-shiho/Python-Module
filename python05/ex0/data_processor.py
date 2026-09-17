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
    #辞書のみ別途で対応
    def output(self) -> typing.Any:
        return self.log.pop(0)


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
        print("=== Code Nexus - Data Processor ===")
        print()
        print("Testing Numeric Processor...")
        num = NumericProcessor()
        print(num.validate(42))
        print(num.validate("aa"))
        print(num.validate([42,2,1,5,6,7,4]))
        print(num.validate([42,2,1,5,"q",7,4]))
        num.ingest([42,2,1,5,6,7,4])
        print(num.log)
        print(num.output())
        print(num.log)

        print()
        num = TextProcessor()
        print(num.validate(42))
        print(num.validate("aa"))
        print(num.validate(["aaa","www","aaa",12]))
        print(num.validate(["q","a","as"]))
        num.ingest(["q","a","as"])
        print(num.log)
        print(num.output())
        print(num.log)


        print()
        num = LogProcessor()
        print(num.validate(42))
        print(num.validate({"a":"a"}))
        print(num.validate([{'log_level': 'NOTICE'}, {'log_message': 'Connection to server'}, {'log_level': 'ERROR'}, {'log_message': 'Unauthorized access!!'}]))
        print(num.validate([{'log_level': 'NOTICE', 'log_message': 'Connection to server'}]))
        num.ingest({'log_level': 'NOTICE', 'log_message': 'Connection to server'})
        print(num.log)
        print(num.output())
        print(num.log)
    except Exception as e:
        print(f"Error: {e}")

    # #validateでデータの検証
    # #validateでデータの検証
    # print("Test invalid ingestion of string 'foo' without prior validation:")
    # #エラー出力
    # print("Processing data: [1, 2, 3, 4, 5]")
    # #ingestで値を代入
    # print("Extracting 3 values...")
    # #output
    # #output
    # #output
    # print()

    # print("Testing Text Processor...")
    # #validateでデータの検証
    # print("Processing data: ['Hello', 'Nexus', 'World']")
    # #ingestで値を代入
    # print("Extracting 1 value...")
    # #output
    # print()

    # print("Testing Log Processor...")
    # #validateでデータの検証
    # print("Processing data: [{'log_level': 'NOTICE', 'log_message': 'Connection to server'}, {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]")
    # #ingestで値を代入
    # print("Extracting 2 values...")
    # #output
    # #output

main()
