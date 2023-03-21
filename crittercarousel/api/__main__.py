import uvicorn

from crittercarousel.api.application import CritterApplication

uvicorn_config = uvicorn.Config(
    app = "crittercarousel.api.application:CritterApplication",
    host = "0.0.0.0",
    port = 8888,
    access_log = True,
    use_colors = False,
    factory = True,
    log_level = "debug")

uvicorn_server = uvicorn.Server(uvicorn_config)

uvicorn_server.run()
