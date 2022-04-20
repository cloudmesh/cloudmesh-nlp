from typing import Optional
from fastapi.param_functions import Query
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

description = """
Cloudmesh NLP API allows you to access NLP services from multiple cloud providers

## Supported Providers 

* Google
* AWS
* Azure

## Services

* Translation
* Language detection

## Contact
"""

import os
app = FastAPI(
title="Cloudmesh NLP Services",
    description=description,
    version="0.0.1",
    terms_of_service="http://cloudmesh.org/terms/TBD",
    contact={
        "name": "Gregor von Laszewski",
        "url": "http://laszewski.github.io",
        "email": "laszewski@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get("/")
def home():
    return {"Cloudmesh": "Multi-Cloud NLP Service"}

@app.get("/detect/{content}", summary="detect", name="detect", tags=["Detect"])
def detect(
        content: str = Query(default=None, description="The ID of the article to find related articles for.")
):
    return False

@app.get("/translate/{content}", summary="Translate", name="translate", tags=["Translate"])
def translate(
        content: str = Query(default=None, description="This is the content"),
        provider: Optional[str] = Query(default='google', description="The cloud provider that conducts the translation"),
        fromlang: Optional[str] = Query(default='en', description="The language the content is in"),
        tolang: Optional[str] = Query(default='de', description="The language to which we want to translate"),):
    """
    Translate the content with a cloud NLP translation service. The default service used is google.

    * **content**: Content to be translated by user
    * **provider**: The cloud/service provider
    * **fromlang**: The language code representing in which the content is written
    * **tolang**: The language code that is being written to.

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




