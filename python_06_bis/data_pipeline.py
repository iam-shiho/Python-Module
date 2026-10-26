import typing
from data_processor\
    import DataProcessor, NumericProcessor, TextProcessor, LogProcessor


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(value for i, value in data))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        res = ", ".join(f'"item_{i}": "{value}"' for i, value in data)
        print("JSON Output:")
        print("{" f"{res}" "}")


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processers:
            data: list[tuple[int, str]] = []
            for i in range(nb):
                if not processor.log:
                    break
                data.append(processor.output())
            plugin.process_output(data)


def main() -> None:
    print(
        "=== Code Nexus - Data Pipeline ===\n"
        "\nInitialize Data Stream...\n"
        "== DataStream statistics =="
    )
    stream = DataStream()
    stream.print_processors_stats()

    print("Registering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

    print(
        "Send first batch of data on stream: "
        "['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is connected'}], "
        "42, ['Hi', 'five']]"
    )
    stream.process_stream([
        'Hello world', [3.14, -1, 2.71],
        [{'log_level': 'WARNING',
            'log_message': 'Telnet access! Use ssh instead'},
            {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42, ['Hi', 'five']
    ])
    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print(
        "\nSend 3 processed data from each processor to a CSV plugin:"
    )
    stream.output_pipeline(3, CSVPlugin())

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print(
        "Send another batch of data: "
        "[21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'], "
        "[{'log_level': 'ERROR', 'log_message': '500 server crash'}, "
        "{'log_level': 'NOTICE', "
        "'log_message': 'Certificate expires in 10 days'}], "
        "[32, 42, 64, 84, 128, 168], 'World hello']"
    )

    stream.process_stream([
        21, ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [{'log_level': 'ERROR', 'log_message': '500 server crash'},
         {'log_level': 'NOTICE',
         'log_message': 'Certificate expires in 10 days'}],
        [32, 42, 64, 84, 128, 168], 'World hello']
    )

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONPlugin())

    print("\n== DataStream statistics ==")
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
