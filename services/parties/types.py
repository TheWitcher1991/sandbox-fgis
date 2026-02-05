from typing import NewType, TypedDict

ImportPartyId = NewType("ImportPartyId", int)
ImportPartySeedId = NewType("ImportPartySeedId", int)
ExportPartyId = NewType("ExportPartyId", int)


class CreateImportPartyDTO(TypedDict):
    pass


class UpdateImportPartyDTO(TypedDict):
    pass


class CreateExportPartyDTO(TypedDict):
    pass


class UpdateExportPartyDTO(TypedDict):
    pass
