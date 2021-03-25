# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned
from expecter import expect

from meddra_toolkit.meddra import MeddraData


def describe_meddra_data():
    def describe_load_data():
        def when_load_everything():
            med = MeddraData("./tests/fixtures/data/")
            med.load()
            expect(len(med.concepts.values())) == 49
            expect(med.concepts["10007541"].name) == "Affections cardiaques"
            expect(
                med.concepts["10018865"].name
            ) == "Tumeurs hématopoïétiques (excl leucémies et lymphomes)"
