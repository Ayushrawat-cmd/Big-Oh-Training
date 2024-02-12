import os
from pathlib import Path
import environment
from configparser import ConfigParser

this_dir = Path(__file__).resolve().parent

conf_dir = this_dir/'properties.ini'

#create config parser instance
parser = ConfigParser()

#read the properties of config file
parser.read(conf_dir, encoding='utf-8')

class Config:
    @staticmethod 
    def read(section, property, default =None):
        return parser.get(section, property, fallback=default)

# Get the value of the 'env' key from the 'app' section
env_value = parser.get('app', 'env')

#perform environment variable interpolation
env_value = os.path.expandvars(env_value)
print(env_value)

selected_env_file = environment.dev # Here we are setting the desired environment

with open(selected_env_file) as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):  # Skip empty lines and comments
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()
            print(key, value)
            os.environ[key] = value

#set the environment variable
os.environ['ENV'] = env_value
print(os.environ['sample_controller'])
