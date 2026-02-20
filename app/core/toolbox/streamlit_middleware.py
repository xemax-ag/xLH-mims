from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse
from app.core.toolbox.cookies import set_cookie

TTL_SESSION_KEY = 2 * 24 * 60 * 60


class StreamlitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        # start_time = time.perf_counter()

        session_key = request.cookies.get('session_key')
        refresh_session_key = False
        if session_key is None:
            new_url = str('/login/')
            return RedirectResponse(url=new_url, status_code=307)  # 307 preserves method/body
        else:
            if request.url.path == '/ui/':
                refresh_session_key = True

        response = await call_next(request)

        if refresh_session_key:
            try:
                # Verlängerung Session key falls User Objekt existiert
                set_cookie(key='session_key', value=session_key, expires=TTL_SESSION_KEY,
                           request=request, response=response, forced=True)
            except Exception as e:
                pass
        # process_time = time.perf_counter() - start_time
        # response.headers['x-process-time'] = f'{process_time * 1000.0:0.03f} ms'
        return response