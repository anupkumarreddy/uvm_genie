import yaml


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
                }
            }
        }

        self.component_iter = iter(self.config['components'])

    def load_config(self, configuration):
        self.__dict__.update(configuration)

    def get_next_component(self):
        component = next(self.component_iter)
        return self.config['components'][component]

    def get_num_components(self):
        return len(self.config['components'].keys())

    def print_configuration(self):
        yaml_string = yaml.dump(self.config)
        print(yaml_string)

    def get_output_path(self):
        return self.config['output_path']