import yaml
from yaml.loader import SafeLoader




class UvmGenieConfig:

    def __init__(self):
        self.config = {
            'templates_path': 'templates',
            'output_path': 'output',
            'components': {
                'package': {
                    'filename': 'uart_pkg',
                    'author': 'anup reddy',
                    'description': 'This package contains uart uvc',
                    'package_name': 'uart',
                    'includes': [
                        'uart_config',
                        'uart_driver',
                        'uart_monitor',
                        'uart_sequencer',
                        'uart_agent',
                        'uart_env'
                    ],
                    'template_name': 'package.sv.jinja'
                },
                'interface': {
                    'filename': 'uart_intf',
                    'author': 'anup reddy',
                    'description': 'This package contains uart interface',
                    'interface_name': 'uart',
                    'ports': [
                        'input uart_clk',
                        'input uart_reset'
                    ],
                    'signals': [
                        'uart_tx',
                        'uart_rx',
                        'uart_s1',
                        'uart_s2'
                    ],
                    'template_name': 'interface.sv.jinja'
                },
                'driver': {
                    'filename': 'uart_driver',
                    'author': 'anup reddy',
                    'description': 'This package contains uart driver',
                    'class_name': 'uart_driver',
                    'vintf_type': 'uart_intf',
                    'vintf_name': 'vintf',
                    'template_name': 'driver.sv.jinja'
                },
                'monitor': {
                    'filename': 'uart_monitor',
                    'author': 'anup reddy',
                    'description': 'This package contains uart monitor',
                    'class_name': 'uart_monitor',
                    'vintf_type': 'uart_intf',
                    'vintf_name': 'm_vintf',
                    'template_name': 'monitor.sv.jinja'
                },
                'agent': {
                    'filename': 'uart_agent',
                    'author': 'anup reddy',
                    'description': 'This package contains uart agent',
                    'class_name': 'uart_agent',
                    'template_name': 'agent.sv.jinja'
                },
                'env': {
                    'filename': 'uart_env',
                    'author': 'anup reddy',
                    'description': 'This package contains uart env',
                    'class_name': 'uart_env',
                    'template_name': 'env.sv.jinja'
                },
                'sequence_item': {
                    'filename': 'uart_sequence_item',
                    'author': 'anup reddy',
                    'description': 'This package contains uart sequence item',
                    'class_name': 'uart_sequence_item',
                    'template_name': 'sequence_item.sv.jinja'
                },
                'sequence': {
                    'filename': 'uart_sequence',
                    'author': 'anup reddy',
                    'description': 'This package contains uart sequence',
                    'class_name': 'uart_sequence',
                    'template_name': 'sequence.sv.jinja'
                },
                'test': {
                    'filename': 'uart_test',
                    'author': 'anup reddy',
                    'description': 'This package contains uart test',
                    'class_name': 'uart_test',
                    'template_name': 'test.sv.jinja'
                }
            }
        }

        self.component_iter = iter(self.config['components'])

    def load_config(self, configuration_file):
        # Open the file and load the file
        with open(configuration_file) as file_handle:
            data = yaml.load(file_handle, Loader=SafeLoader)
            self.config = data


    def get_next_component(self):
        component = next(self.component_iter)
        return self.config['components'][component]

    def get_num_components(self):
        return len(self.config['components'].keys())

    def print_configuration(self):
        yaml_string = yaml.dump(self.config)
        return yaml_string

    def print_configuration_file(self, config_file):
        file_handle = open(config_file, 'w')
        file_handle.write(self.print_configuration())

    def get_output_path(self):
        return self.config['output_path']