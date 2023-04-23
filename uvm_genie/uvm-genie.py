from uvm_genie.config import UvmGenieConfig
from uvm_genie.generator import UvmGenerator
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("command", help="Command to perform, there are two commands 'config' and 'generate'",
                    choices=['config', 'generate'])
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("-cf", "--config-file", help="Initial config is dumped with this file name")
args = parser.parse_args()

configuration = UvmGenieConfig()
if args.command == 'generate':
    print(args)
elif args.command == 'config':
    if args.config_file:
        configuration.print_configuration_file(args.config_file)
    else:
        configuration.print_configuration_file('default.genie')

generator = UvmGenerator()
generator.generate(configuration)
