import yaml

class UvmGenieConfig:

    def __init__(self):
        self.config = {
            'templates_path': 'templates',
            'output_path': 'output',
            'components': [
                {
                    'driver': {
                        'name': 'my_driver',
                        'vif_name': 'my_vif'
                    },
                },
                {
                    'driver': {
                        'name': 'my_driver',
                        'vif_name': 'my_vif'
                    }
                }
            ]
        }

    def load_config(self, configuration):
        self.__dict__.update(configuration)

    def print_configuration(self):
        yaml_string = yaml.dump(self.config)
        print(yaml_string)
