"""A sample CLI."""

import click
import log

from meddra_toolkit.meddra import MeddraData


@click.command()
#@click.argument('term')
def main(term=None):
    log.init()

    med = MeddraData("./tests/fixtures/data/")
    med.load()
    

if __name__ == '__main__':  # pragma: no cover
    main()
