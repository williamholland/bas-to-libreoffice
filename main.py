import os
from jinja2 import Environment, FileSystemLoader

# Set up the Jinja2 environment to load templates from the LibraryTemplate directory
env = Environment(loader=FileSystemLoader('LibraryTemplate'))

# Define the variables to use in the templates
lib_name = 'Library2'
module_name = 'Module2'
module_code = '''
Sub Main
    MsgBox "Hello world"
End Sub
'''

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
