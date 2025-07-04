from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
import pandas as pd
import numpy as np
import pickle
import os

from model import *
from logger import logger
from schemas import PersonalityTraitResponseSchema, PersonalityInputSchema, ErrorResponseSchema
from flask_cors import CORS

# Instantiate the Flask application with OpenAPI
info = Info(title="Personality Trait API", version="1.0.0")
app = OpenAPI(__name__, info=info, static_folder="../front", static_url_path="/front")
CORS(app)

# Define tags for the API
home_tag = Tag(
    name="Documentation",
    description="Selection of the documentation: Swagger, Redoc or Rapidoc",
)
personality_trait_tag = Tag(
    name="Personality Trait", 
    description="Forecasting personality traits based on user input",
)

# Route for the home page
@app.get("/", tags=[home_tag])
def home():
    """
    Redirects to the home page of the application.
    """
    return redirect("/front/index.html")

# Route for API documentation
@app.get("/docs", tags=[home_tag])
def docs():
    """
    Redirects to the API documentation page.
    """
    return redirect("/openapi")


# Route for the personality trait prediction
@app.post("/predict", tags=[personality_trait_tag])
def predict_personality(body: PersonalityInputSchema):
    """
    Predicts the personality trait based on the input data.

    :param body: Input data for personality trait prediction.
    :return: Predicted personality trait.
    """
    try:
        # Log the received input data
        logger.info(f"Received input data: {body}")

        
        pipeline_path = './machinelearning/models/et_personality_trait_pipeline.pkl'
        logger.info(f"Loading model from: {pipeline_path}")

        pipeline_loader = Pipeline()
        pipeline = pipeline_loader.carrega_pipeline(pipeline_path)
        logger.info("Model loaded successfully.")

        # Prepare the input data for prediction
        preprocessador = PreProcessador()
        input_data = preprocessador.preparar_body(body)
        logger.info(f"Input data prepared: {input_data}")

        # Make the prediction
        prediction = pipeline.predict(input_data)
        
        # Log the prediction result
        logger.info(f"Prediction result: {prediction}")
        
        return PersonalityTraitResponseSchema(
            prediction=prediction
        ).dict()
        #return {"prediction": prediction}, 200
        
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return ErrorResponseSchema(message=f"Error during prediction: {str(e)}").dict(), 500
