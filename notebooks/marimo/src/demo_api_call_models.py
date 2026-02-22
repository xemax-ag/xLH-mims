from pydantic import BaseModel

class SearchQuery(BaseModel):
    query: str
    fts: str | None = None
    language: str = 'de'
    n_results: int = 20

    aa: int | None = 1
    am: int | None = 1
    au: int | None = 1
    et: int | None = 1
    kr: int | None = 1
    mp: int | None = 1
    pm: int | None = 1
    pr: int | None = 1
  
    be: int | None = 1
    bfs: int | None = 1
    uek: int | None = 1

    hkb: int | None = 1
    hkp: int | None = 1
    lkn: int | None = 1
    lfe: int | None = 1
    lfb: int | None = 1
    lze: int | None = 1

class Url(BaseModel):
    base_data: str | None = None

class MetaDatas(BaseModel):
    pk: str
    id: str
    tokens: int
    level: str
    language: str
    be: bool = False
    bfs: bool = False
    uek: bool = False
    hkb: bool = False
    hkp: bool = False
    lkn: bool = False
    lfe: bool = False
    lfb: bool = False
    lze: bool = False
    aa: bool = False
    am: bool = False
    au: bool = False
    et: bool = False
    kr: bool = False
    mp: bool = False
    pm: bool = False
    pr: bool = False

class SearchResponse(BaseModel):
    distance: float
    document: str
    metadatas: MetaDatas
    urls: list[Url] = []

class SearchResponseData(BaseModel):
    data: list[SearchResponse] = []