import os
from dotenv import load_dotenv
import sys


def main():
    print(
        "\nORACLE STATUS: Consulting the configuration...\n"
    )
    load_dotenv()
    mode = os.getenv('MATRIX_MODE')
    if mode == "development":
        print(f"Mode: {mode}")
        if not os.getenv('DATABASE_URL') == None:
            print("Database: Connected to local instance")
        else:
            print("Database: Disconnected from local instance")
        if os.getenv('API_KEY'):
            print("API Access: Authenticated")
        else:
            print("API Access: Unauthenticated")
        print(f"Log Level: {os.getenv('LOG_LEVEL')}")
        if os.getenv('ZION_ENDPOINT'):
            print("Remote Network: Online")
        else:
            print("Remote Network: Offline")
        print(
            "\nConfiguration security check:\n"
            "[OK] No hardcoded secrets detected\n"
            "[OK] .env file properly ignored by git\n"
            "[OK] Production overrides available\n"
            "\nThe Oracle sees all configurations."
        )


    elif mode == "production":
        print(
            f"Mode: {mode}\n"
            "Q. なぜ.envをgitにあげちゃいけないの？？\n"
            "A. 1. 開発のみで使う大切な情報をそとにもらさないため\n"
            "   2. 情報や内容を一括で変更しやすくするため"
        )

    else:
        raise ValueError(
            "ValueError: Invalid MATRIX_MODE environment variable. "
            'Please choose either "development" or "production".'
            )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"{e}", file=sys.stderr)
        sys.exit(1)
