from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
import pandas as pd
import numpy as np
import pickle

from model import *
from logger import logger
from schemas import *
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

# Route for forecast of personality traits
@app.get(
    "/personality_trait", 
    tags=[personality_trait_tag],
    responses={
        "200": PersonalityTraitResponseSchema,
        "400": ErrorResponseSchema,
        "500": ErrorResponseSchema,
    },
)
def get_personality_trait(form: PersonalityTraitSchema):
    """
    Forecasts personality traits based on user input.

    :param form: User input data for personality trait prediction.
    :return: Predicted personality trait.
    """
    try:
        # Log the received form data
        logger.info(f"Received form data: {form}")

        name = form.name
        timeSpentAlone = form.timeSpentAlone
        stageFear = form.stageFear
        socialEventAttendance = form.socialEventAttendance
        goingOutside = form.goingOutside
        drainedAfterSocializing = form.drainedAfterSocializing
        friendsCircleSize = form.friendsCircleSize
        postFrequency = form.postFrequency
        
        X_input = np.array([
            timeSpentAlone, 
            stageFear, 
            socialEventAttendance, 
            goingOutside, 
            drainedAfterSocializing, 
            friendsCircleSize, 
            postFrequency
        ]).reshape(1, -1)
        # Log the input data for prediction
        logger.info(f"Input data for prediction: {X_input}")
        
        # Load the pre-trained model pipeline
        # Log the pipeline loading
        logger.info("Loading the personality trait prediction pipeline.")
        
        model_path = ".machinelearning/models/et_personality_trait_pipeline.pkl"
        with open(model_path, 'rb') as file:
            pipeline = pickle.load(file)
            
        # predict the personality trait
        prediction = int(pipeline.predict(X_input)[0])
               
        # Log the prediction result
        logger.info(f"Prediction result: {prediction]}")
        
        return PersonalityTraitResponseSchema(
    