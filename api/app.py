from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

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
@app.get("/")