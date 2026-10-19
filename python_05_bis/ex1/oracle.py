import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    load_dotenv(override=True)
    print(
        "ORACLE STATUS: Consulting the configuration...\n"
        "\nConfiguration loaded:\n"
        f"Mode: {os.getenv("MATRIX_MODE")}"
        f"Mode: {os.getenv("DATABASE_URL")}"
        f"Mode: {os.getenv("API_KEY")}"
        f"Mode: {os.getenv("LOG_LEVEL")}"
        f"Mode: {os.getenv("ZION_ENDPOINT")}"
    )
    file_flag = False
    with open("ex1/.gitignore", "r") as f:
        for line in f:
            if ".env" in line:
                print("[OK] .env file properly ignored by git")
        if file_flag == False:
            raise ValueError("[KO] .env file not properly ignored by git")
