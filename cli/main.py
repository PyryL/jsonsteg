from cli.read_subcommand import read_subcommand
from cli.write_subcommand import write_subcommand
import argparse

def start():
    parser = argparse.ArgumentParser(
        description="Write payload into JSON without modifying it",
    )
    command_subparser = parser.add_subparsers(title="operation", dest="command")

    # CLI to read data
    read_parser = command_subparser.add_parser("read", help="read written data from JSON")
    read_parser.add_argument("--output", "-o", metavar="FILE", help="A file where read data will be written (default: stdout)")
    read_parser.add_argument("JSON", help="The JSON file from which to read the data")

    write_parser = command_subparser.add_parser("write", help="write data to JSON")
    write_input_group = write_parser.add_mutually_exclusive_group(required=True)
    write_input_group.add_argument("--input", "-i", metavar="TEXT", help="Text to write to JSON")
    write_input_group.add_argument("--input-file", "-I", metavar="FILE", help="A file whose content to write to JSON")
    write_parser.add_argument("--output", "-o", metavar="FILE", help="A file in which to write the output instead of modifying JSON")
    write_parser.add_argument("JSON", help="The JSON to use to store the data")

    arguments = parser.parse_args()
    if arguments.command == "read":
        read_subcommand(arguments)
    elif arguments.command == "write":
        write_subcommand(arguments)
