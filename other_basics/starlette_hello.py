from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def greet(request):
    return JSONResponse("Hello World!!")

app = Starlette(debug=True, routes=[
    Route("/hello", greet)
])