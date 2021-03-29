# pylint: disable=redefined-outer-name,unused-variable,expression-not-assigned
from expecter import expect

from meddra_toolkit.meddra import MeddraData


def describe_meddra_data():
    def describe_load_data():
        def when_load_everything():
            med = MeddraData("./tests/fixtures/data/")
            med.load()
            expect(len(med.concepts.values())) == 949
            expect(med.concepts["10007541"].name) == "Affections cardiaques"
            expect(
                med.concepts["10018865"].name
            ) == "Tumeurs hématopoïétiques (excl leucémies et lymphomes)"
            expect(med.concepts["10053567"].name) == "Coagulopathies"
            expect(med.concepts["10002915"].name) == "Insuffisance aortique"
            expect(med.concepts["10053871"].soc_code) == "10010331"
            expect(med.concepts["10020972"].pt_code) == "10020969"
            expect(med.concepts["10020972"].name) == "Anémie microcytaire hypochrome"
            expect(med.concepts["10020972"].active) == True
            expect(med.concepts["10010375"].active) == False
