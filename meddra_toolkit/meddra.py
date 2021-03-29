import os
from typing import Dict, List, Optional, Type

from meddra_toolkit.asc import read_asc_file
from meddra_toolkit.models.concepts import (
    MeddraConcept,
    MeddraHLGT,
    MeddraHLT,
    MeddraLLT,
    MeddraPT,
    MeddraSOC,
)


class MeddraData:
    def __init__(self, path: str):
        self.path: str = path
        self.concepts: Dict[str, MeddraConcept] = {}

    def load(self):
        self._load_concept(
            "soc.asc",
            concept=MeddraSOC,
            columns=["code", "name", "abbrev", "_", "_", "_", "_", "_", "_", "_", "_"],
        )
        self._load_concept(
            "hlgt.asc",
            concept=MeddraHLGT,
            columns=["code", "name", "_", "_", "_", "_", "_", "_", "_", "_"],
        )
        self._load_concept(
            "hlt.asc",
            concept=MeddraHLT,
            columns=["code", "name", "_", "_", "_", "_", "_", "_", "_", "_"],
        )
        self._load_concept(
            "pt.asc",
            concept=MeddraPT,
            columns=[
                "code",
                "name",
                "_",
                "soc_code",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
            ],
        )
        self._load_concept(
            "llt.asc",
            concept=MeddraLLT,
            columns=[
                "code",
                "name",
                "pt_code",
                "_",
                "_",
                "_",
                "_",
                "_",
                "_",
                "active",
                "_",
                "_",
            ],
        )

    def _load_concept(
        self,
        file_name: str,
        columns: Optional[List[str]] = None,
        concept: Type[MeddraConcept] = MeddraConcept,
    ):
        for concept_line in read_asc_file(
            os.path.join(self.path, file_name), columns=columns
        ):
            concept_object = concept(**concept_line)
            if concept_object.code not in self.concepts:
                self.concepts[concept_object.code] = concept_object


class Meddra:
    def __init__(self, version: str, language: str, data: MeddraData):
        self.version = version
        self.language = language
        self.data = data
