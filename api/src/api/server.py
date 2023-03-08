# coding: utf-8

"""
    Pandemos

    API for visualization of Infection Models

    The version of the OpenAPI document: 1
    Generated by: https://openapi-generator.tech
"""
#from app import celery_app
from celery.result import AsyncResult
import logging


from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.apis.interventions_api import router as InterventionsApiRouter
from app.apis.groups_api import router as GroupsApiRouter
from app.apis.models_api import router as ModelsApiRouter
from app.apis.movements_api import router as MovementsApiRouter
from app.apis.nodes_api import router as NodesApiRouter
from app.apis.parameter_definitions_api import router as ParameterDefinitionsApiRouter
from app.apis.simulations_api import router as SimulationsApiRouter
from app.apis.aggregations_api import router as AggregationsApiRouter

app = FastAPI(
    title="Pandemos",
    description="API for visualization of Infection Models",
    version="1",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(GroupsApiRouter)
app.include_router(InterventionsApiRouter)
app.include_router(ModelsApiRouter)
app.include_router(MovementsApiRouter)
app.include_router(NodesApiRouter)
app.include_router(ParameterDefinitionsApiRouter)
app.include_router(SimulationsApiRouter)
app.include_router(AggregationsApiRouter)

"""
@app.post("/test_celery/{message}")
def send_message(message: str):
    task = celery_app.send_task(
        "test_worker",
        args=[],
        kwargs={"message": message},
    )
    logging.error(task.id)
    # res = AsyncResult(task.id, app=celery_app).get()
    return {"message": message}

"""