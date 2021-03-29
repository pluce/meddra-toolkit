from pydantic import BaseModel
from typing import List, ForwardRef

MeddraConcept = ForwardRef('MeddraConcept')

class MeddraConcept(BaseModel):
    code: str
    name: str
    parents: List[MeddraConcept] = []
    children: List[MeddraConcept] = []

    def concept_type(self):
        return self.__class__.__name__[6:]

    def __str__(self):
        return f"{self.concept_type().rjust(5)} | {self.code} > {self.name}"

MeddraConcept.update_forward_refs()

class MeddraSOC(MeddraConcept):
    abbrev: str


class MeddraHLGT(MeddraConcept):
    pass


class MeddraHLT(MeddraConcept):
    pass


class MeddraPT(MeddraConcept):
    soc_code: str
    soc: MeddraSOC


class MeddraLLT(MeddraConcept):
    active: bool
    pt_code: str
    pt: MeddraPT
