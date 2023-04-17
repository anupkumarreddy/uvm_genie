from uvm_genie.config import UvmGenieConfig
from uvm_genie.generator import UvmGenerator


configuration = UvmGenieConfig()
configuration.print_configuration()
generator = UvmGenerator()
generator.generate(configuration)
