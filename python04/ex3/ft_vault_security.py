#!/usr/bin/env python3

def secure_archive(
                   file_name: str,
                   perform: str,
                   contains: str = ""
                   ) -> tuple[bool, str]:
    if perform == "read":
        try:
            with open(file_name, 'r') as o_file:
                data = o_file.read()
            return (True, str(data))
        except Exception as e:
            return (False, str(e))

    elif perform == "write":
        try:
            with open(file_name, 'w') as o_file:
                print(contains, file=o_file)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))
    return (False, "No valid item provided. Usage: "
            "secure_archive(file_name, <read or write>)")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print()
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))
    print()
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt", "read"))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive(
        "new.txt", "write",
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n")
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
