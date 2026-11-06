"""Entry point for toolkit."""

from utils import optimize


def main():
    result = optimize(20)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
