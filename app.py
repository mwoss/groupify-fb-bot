import logging

from flask import Flask

import controllers


app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(controllers.auth_api)
    app.register_blueprint(controllers.hook_api)
    logging.debug(f'Registered routes {str(app.url_map)}')
    app.run(debug=True)
