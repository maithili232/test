# File: docs/conf.py

extensions = [
   "multiproject",
   # Your other extensions.
   "sphinx.ext.intersphinx",
]

# Define the projects that will share this configuration file.
multiproject_projects = {
    "dev": {
        "use_config_file": False,
    },
    "user": {
        "use_config_file": False,
    },
}

current_project  = multiproject_projects

# Set all values directly
# -----------------------

if current_project == 'dev':
   # File: docs/dev/conf.py
   from dev.conf import *
elif current_project == 'user':
   # File: docs/user/conf.py
   from user.conf import *

# Set value by value
# ------------------

if current_project == 'dev':
   # File: docs/dev/conf.py
   import dev.conf as config
elif current_project == 'user':
   # File: docs/user/conf.py
   import user.conf as config

# Replace the original values.
project = config.project
version = config.version
language = config.language

# Extending the original value.
extensions += config.extensions

# Common options.
html_theme = "sphinx_rtd_theme"