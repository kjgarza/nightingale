import argparse
from nightingale import nightingale


def main():
    parser = argparse.ArgumentParser(description="Prioritize GitHub issues")

    parser.add_argument("input", help="CSV file with GitHub issues names and links or URL to GitHub repo issue list")
    parser.add_argument("-o", "--output", help="Output file for prioritized issues")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose output")




    args = parser.parse_args()
    nightingale.nightingale(args.input)

    print(args)

if __name__ == "__main__":
    main()