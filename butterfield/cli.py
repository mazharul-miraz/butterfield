import sys
import json
import asyncio
from . import Bot, ALL


def main():
    """
    CLI entrypoint for testing.
    """
    _, config, *args = sys.argv
    with open(config, 'r') as fd:
        config = json.load(fd)

    params = config.get('params') or {}

    bot = Bot(config.get("key"), config.get("name"), **params)
    for plugin in config.get("plugins", []):
        bot.listen(plugin)
    bot.start()


if __name__ == '__main__':
    main()
