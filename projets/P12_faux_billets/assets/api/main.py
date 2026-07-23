from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from api.router import router
from api.services.prediction import get_model


app = FastAPI(
    title="ONCFM - API de detection de faux billets",
    description=(
        "API de prediction pour classer un billet comme vrai ou faux "
        "a partir de 6 mesures physiques."
    ),
    version="1.0.0",
)


@app.on_event("startup")
def preload_model() -> None:
	get_model()


app.include_router(router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    for path_item in openapi_schema["paths"].values():
        for operation in path_item.values():
            operation.get("responses", {}).pop("422", None)
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi