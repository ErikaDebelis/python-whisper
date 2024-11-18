from whisper import run_whisper


def init_app(app):

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.get("/test")
    async def test():
        result = await run_whisper()
        return {"result": result}

    @app.get("/hello/{name}")
    async def say_hello(name: str):
        return {"message": f"Hello {name}"}