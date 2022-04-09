from typing import Optional

from fastapi import FastAPI

from fastapi.param_functions import Query
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

#Then, write a function that sets app.openapi_schema:

import os
app = FastAPI()








@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/translate/{content}", summary="summary", name="translate", tags=["Tsranslate"])
def translate(
        content: str = Query(description="The ID of the article to find related articles for.", title="Article ID", default = "world"),
        provider: Optional[str] = 'google',
        fromlang: Optional[str] = 'en',
        tolang: Optional[str] = 'de'):
    """
    Translate blah

    * **content**: Content to be translated by user
    * provider: The cloud/service provider
    * fromlang: The language code representing in which the content is written
    * tolang: The language code that is being written to.

    :return:
    """

    from_language = fromlang
    to_language = tolang


    if provider == "google":
        from cloudmesh.nlp.provider.google.translate import Translate

    elif provider == "aws":
        from cloudmesh.nlp.provider.aws.translate import Translate

    elif provider == "azure":
        from cloudmesh.nlp.provider.azure.translate import Translate

    else:
        return {"error": f"provider {provider} not supported"}



    s = Translate()
    r = s.get(content, SourceLanguageCode=from_language, TargetLanguageCode=to_language)
    return r



def my_schema():
   openapi_schema = get_openapi(
       title="Cloudmesh Translation API Service",
       version="1.0",
       description="Multi-cloud provider service",
       routes=app.routes,
   )
   app.openapi_schema = openapi_schema
   return app.openapi_schema

app.openapi = my_schema


