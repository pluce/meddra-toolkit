from pydantic import BaseModel


class MeddraConcept(BaseModel):
    code: str
    name: str


class MeddraSOC(MeddraConcept):
    abbrev: str


class MeddraHLGT(MeddraConcept):
    pass


class MeddraHLT(MeddraConcept):
    pass


class MeddraPT(MeddraConcept):
    soc_code: str


class MeddraLLT(MeddraConcept):
    active: bool
    pt_code: str
