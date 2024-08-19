import logging

from typing import Any
from typing import TypeAlias

from flask import Flask
from flask import request


app = Flask(__name__)


gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(gunicorn_error_logger.level)


Json: TypeAlias = dict[str, Any]


@app.before_request
def log_request_headers() -> None:
    """
    Handler to log request headers.
    """
    headers = request.headers
    app.logger.info("Request Headers: %s", headers)



@app.route("/v1/hello")
def hello_plain() -> Json:
    """
    A simple endpoint to test the server can be accessed.
    """
    app.logger.info("We're just plain up!")
    return {"status": "Up!"}


@app.route("/kube/v1/hello")
def hello_kube() -> Json:
    """
    A simple endpoint to test the server can be accessed via kubernetes
    """
    app.logger.info("We're up on Kubernetes!")
    return {"status": "Up on Kube!"}


@app.route("/cr/v1/hello")
def hello_cr() -> Json:
    """
    A simple endpoint to test the server can be accessed via cloud run
    """
    app.logger.info("We're up on Cloud Run!")
    return {"status": "Up on Cloud Run!"}


if __name__ == '__main__':
    app.run()
