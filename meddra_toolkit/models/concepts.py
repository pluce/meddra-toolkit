from pydantic import BaseModel


class MeddraConcept(BaseModel):
    code: str
    name: str


class MeddraSOC(MeddraConcept):
    abbrev: str


class MeddraHLGT(MeddraConcept):
    pass
