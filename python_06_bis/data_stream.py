import typing
from data_processor\
    import DataProcessor, NumericProcessor, TextProcessor, LogProcessor


class DataStream():
    def __init__(self) -> None:
        self.processers: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processers.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for v in stream:
            try:
                not_proc = False
                for processor in self.processers:
                    if processor.validate(v):
                        processor.ingest(v)
                        not_proc = True
                        break
                if not_proc is False:
                    raise ValueError(
                        "DataStream error - "
                        f"Can't process element in stream: {v}"
                    )
            except ValueError as e:
                print(e)

    def print_processors_stats(self) -> None:
        if self.processers == []:
            print("No processor found, no data")
        for processor in self.processers:
            print(
                f"{processor.__class__.__name__}: total {processor._logcount} "
                f"items processed, remaining {len(processor.log)} on processor"
            )


def main() -> None:
    print(
        "=== Code Nexus - Data Stream ===\n"
        "\nInitialize Data Stream...\n"
        "== DataStream statistics =="
    )
    stream = DataStream()
    stream.print_processors_stats()

    print(
        "\nRegistering Numeric Processor\n"
        "\nSend first batch of data on stream: "
        "['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is connected'}], "
        "42, ['Hi', 'five']]"
    )
    stream.register_processor(NumericProcessor())
    stream.process_stream([
            'Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
                {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42, ['Hi', 'five']
        ])
    print("== DataStream statistics ==")
    stream.print_processors_stats()

    print(
        "\nRegistering other data processors\n"
        "Send the same batch again\n"
        "== DataStream statistics =="
    )
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    stream.process_stream(
        [
            'Hello world', [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
                {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42, ['Hi', 'five']
        ]
    )
    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1\n"
        "== DataStream statistics =="
    )
    for i in range(3):
        stream.processers[0].output()
    for i in range(2):
        stream.processers[1].output()
    for i in range(1):
        stream.processers[2].output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
