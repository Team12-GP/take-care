import os
import importlib
from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)

# Path to the directory containing route files
router_path = os.path.join(os.path.dirname(__file__), 'routers')

# Loop through all Python files in the router directory
for filename in os.listdir(router_path):
    if filename.endswith('.py') and filename != '__init__.py':
        # Import the module dynamically
        module_name = f"routers.{filename[:-3]}"
        module = importlib.import_module(module_name)
        
        # Find and register the Blueprint in the module
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, Blueprint):
                app.register_blueprint(attribute)

if __name__ == '__main__':
    import os
    
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
