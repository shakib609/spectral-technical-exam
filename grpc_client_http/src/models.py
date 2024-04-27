from pydantic import BaseModel


class MeterUsageDataModel(BaseModel):
    time: str
    meterusage: float


class MeterUsageResponseModel(BaseModel):
    data: list[MeterUsageDataModel]
    pageNumber: int
    pageSize: int
    totalPages: int
