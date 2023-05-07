import os
import argparse
from jinja2 import Environment, FileSystemLoader
import xml.sax.saxutils

# Set up the Jinja2 environment to load templates from the LibraryTemplate directory
env = Environment(loader=FileSystemLoader('LibraryTemplate'))

# Set up the command-line argument parser
parser = argparse.ArgumentParser(description='Make a LibreOffice library from source')
parser.add_argument('--lib-name', dest='lib_name', required=True, help='name of the library')
parser.add_argument('--module-name', dest='module_name', required=True, help='name of the module')
parser.add_argument('--module-path', dest='module_path', required=True, help='path to the module .bas file')

args = parser.parse_args()

# Define the variables to use in the templates
lib_name = args.lib_name
module_name = args.module_name
# Read the module file
with open(args.module_path, 'r') as f:
    module_code = f.read()
    module_code = xml.sax.saxutils.escape(module_code)

# Create a new directory to hold the rendered templates
output_dir = lib_name
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

def render_and_output(in_filename, out_filename=None):
    if out_filename is None:
        out_filename = in_filename
    template = env.get_template(in_filename)
    rendered = template.render(lib_name=lib_name, module_name=module_name, module_code=module_code)
    with open(os.path.join(output_dir, out_filename), 'w') as f:
        f.write(rendered)

render_and_output('dialog.xlb')
render_and_output('Module1.xba', f'{module_name}.xba')
render_and_output('script.xlb')
