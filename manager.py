from flask import current_app

from App import create_app

# redis_store.set("Dannis","manager")

app = create_app("develop")

if __name__ == "__main__":
    # current_app.logger.info('info log')
    # current_app.logger.debug('debug log')
    # current_app.logger.warning('warning log')
    # current_app.logger.error('error log')

    app.run()