from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("--name", type=str, help="optional name")
    args = parser.parse_args();

    if args.name is not None:
        print(f"Hello, {args.name}.")
    else:
       print("Hello World.")
