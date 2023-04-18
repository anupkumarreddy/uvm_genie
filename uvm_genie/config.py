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
                'driver': {
                    'filename': 'my_driver',
                    'author': 'anup reddy',
                    'class_name': 'FirstDriver',
                    'description': "this is a simple test description for testing jinja template system",
                    'template_name': 'driver.sv.jinja'
                },
                'monitor': {
                    'name': 'my_driver',
                    'vif_name': 'my_vif'
                }

            }
        }

        self.component_iter = iter(self.config['components'])

    def load_config(self, configuration):
        self.__dict__.update(configuration)

    def get_next_component(self):
        component = next(self.component_iter)
        return self.config['components'][component]

    def print_configuration(self):
        yaml_string = yaml.dump(self.config)
        print(yaml_string)
