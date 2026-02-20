import pathlib
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request
from starlette.middleware import Middleware
from streamlit.starlette import App
from fastapi.staticfiles import StaticFiles
from app.core.toolbox.streamlit_middleware import StreamlitMiddleware
from starlette.responses import RedirectResponse

@asynccontextmanager
async def lifespan(app):
    # print('startup')
    pass
    yield
    # print('shutdown')
    pass

# https://github.com/streamlit/streamlit/issues/13600
streamlit_app = App(script_path=pathlib.Path(__file__).parents[1] / 'app_ui/main_ui.py',
                    middleware=[Middleware(StreamlitMiddleware)],
                    lifespan=lifespan)

app = FastAPI(
    lifespan=streamlit_app.lifespan(),
    title='xLH-mims',
    version='0.0.1',
    description='',
    swagger_ui_parameters={
        'syntaxHighlight': False,
    },
    # redirect_slashes=False,
    redirect_slashes=True,
)

# =====================================================================================================================
app.mount('/ui', streamlit_app)

# =====================================================================================================================

@app.get("/")
async def root():
    new_url = str('/ui/')
    return RedirectResponse(url=new_url, status_code=307)  # 307 preserves method/body

# Workaround: when Streamlit is mounted under /ui, some clients still call /_stcore/* at root.
# Redirect those to the mounted location.
@app.get("/_stcore/{path:path}")
async def stcore_redirect(path: str, request: Request):
    target = f"/ui/_stcore/{path}"
    if request.url.query:
        target = f"{target}?{request.url.query}"
    return RedirectResponse(url=target, status_code=307)

# =====================================================================================================================

@app.get("/api/contents")
def contents():
    return {"ok": True}

# =====================================================================================================================

app.mount(f'/static', StaticFiles(directory='app/static', html=True), name='static')

# =====================================================================================================================

# https://fastapi.tiangolo.com/es/tutorial/cors/#use-corsmiddleware
# https://medium.com/stackademic/securing-apis-with-fastapi-489c3d4d1ea0
origins = [
    # '*',
    'http://[::1]:8099',
    'http://localhost:8099',
    'https://addin.xlwings.org'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# =====================================================================================================================
