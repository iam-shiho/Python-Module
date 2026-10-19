import sys
import os

def main() -> None:
    if sys.prefix != sys.base_prefix:
        print(
            "\nLABORATORY STATUS: The laboratory is sealed\n"
            f"\nCurrent Python: {sys.executable}"
            f"\nVirtual Environment: {os.path.basename(sys.prefix)}"
            f"\nEnvironment Path: {sys.prefix}\n"
            "\nSUCCESS: You are working in an isolated environment!"
            "\nSafe to install reagents without affecting"
            "\nthe global system.\n"
            "\nReagent installation path:"
        )
        for p in sys.path:
            if "site-packages" in p:
                print(p)
    else:
        print(
            "\nLABORATORY STATUS: You are working in the open\n"
            f"\nCurrent Python: {sys.executable}"
            "\nVirtual Environment: None detected\n"
            "\nWARNING: You are in the global environment!"
            "\nEvery reagent you install here leaks into the whole system.\n"
            "\nTo seal the laboratory, run:"
            "\npython3 -m venv lab_env"
            "\nsource lab_env/bin/activate # On Unix"
            "\nlab_env\Scripts\\activate # On Windows\n"
            "\nThen run this program again."
        )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
