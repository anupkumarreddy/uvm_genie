from jinja2 import Environment, FileSystemLoader


class UvmGenerator:

    def __init__(self):
        self.environment = Environment(loader=FileSystemLoader('templates/'))

    def generate(self, config):
        num_of_components = config.get_num_components();
        print(num_of_components)
        for component in range(num_of_components):
            component = config.get_next_component()
            template = self.environment.get_template(component['template_name'])
            output_file_path = config.get_output_path() + "/" + component['filename'] + ".sv"
            output_file = open(output_file_path, 'w')
            output_file.write(template.render(component))