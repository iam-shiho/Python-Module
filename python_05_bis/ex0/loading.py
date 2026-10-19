import sys
from importlib.metadata import version, PackageNotFoundError

def main():
    try:
        _version = version("pandas")
        print(f"[OK] pandas ({_version}) - Data manipulation ready\n")
    except PackageNotFoundError:
        print (f"[KO] pandas")
        print(
            "pip install pandas\n"
            "poetry add pandas^2.1.0\n"
        )
    try:
        _version = version("numpy")
        print(f"[OK] numpy ({_version}) - Numerical computation ready\n")
    except PackageNotFoundError:
        print (f"[KO] numpy")
        print(
            "pip install numpy\n"
            "poetry add numpy^1.25.0"
        )

if __name__ == "__main__":
    try:
        main()
        print(
            "\npip vs Poetry:\n"
            " requirements.txt declares what to install; pip resolves it at install time.\n"
            " pyproject.toml declares the same constraints, and Poetry pins the resolved\n"
            " versions in poetry.lock so every install is identical.\n"
            "\nAll reagents present and accounted for."
        )
    except Exception as e:
        print(f"Error: {e}")
