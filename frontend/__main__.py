import logging

from frontend.config import config
from frontend.app import create_app

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info('application started')

    app = create_app()
    app.run(host=config.server.host, port=config.server.port, debug=False)


if __name__ == "__main__":
    main()
