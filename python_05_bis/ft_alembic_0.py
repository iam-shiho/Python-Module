import elements

def main() -> None:
    print(
        "=== Alembic 0 ===\n"
        "Using: 'import ...' structure to access elements.py\n"
        f"Testing create_fire: {elements.create_fire()}\n"
    )

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
