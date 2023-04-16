# UVM Genie
UVM Genie is a Python-based template engine for generating Universal Verification Methodology (UVM) components for SystemVerilog.

## Features
UVM Genie supports the following features:

- Generates UVC (Universal Verification Component) for SystemVerilog
- Generates testbench components (sequencer, driver, monitor, scoreboard) for UVM
- Configurable via YAML configuration files
- Based on Jinja2 template engine

## Getting Started
### Installation
Coming up...

### usage
To generate UVM components using UVM Genie, create a YAML configuration file specifying the desired components to 
generate, then run the uvm-genie command with the path to the configuration file as an argument
```
uvm-genie config.yml
```
This will generate the UVM components specified in the configuration file.

## Configuration
The YAML configuration file specifies the desired UVM components to generate, as well as any necessary parameters. 
See the example config.yml file (coming up...)

## Contributing
Contributions to UVM Genie are welcome! To contribute, please fork the repository, create a branch for your changes, 
make your changes, and submit a pull request

## License
UVM Genie is released under the GNU GENERAL PUBLIC LICENSE Version 3.0 License. See LICENSE for more information.