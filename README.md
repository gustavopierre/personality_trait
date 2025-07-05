<p align="left"  style="display: flex;">
    <a href="https://www.linkedin.com/in/gustavo_pierre">
        <img src="https://img.shields.io/badge/LinkedIn-gustavo--pierre-blue" alt="Gustavo Pierre's LinkedIn link">
    </a>
    <a href="https://github.com/gustavopierre/portfolio">
        <img src="https://img.shields.io/badge/portfolio-github-orange" alt="Gustavo Pierre's GitHub portfolio link">
    </a>
    <a href="https://github.com/gustavopierre/personality_trait/issues">
        <img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat" alt="Contributions to the project">
    </a>
</p>

# Personality Trait
## Introduction
This project is the MVP for the subject **Software Quality, Security and Intelligent Systems** in the posgraduation in **Software Engineering** at the Pontifical Catholic University of Rio de Janeiro. The goal is predict whether a person is introverted or extroverted based on their social behavior.<br>

## Components
The repository contains:
- Notebook - ([personality_trait.ipynb](https://github.com/gustavopierre/personality_trait/blob/main/api/machinelearning/notebook/personality_trait.ipynb)) This notebook include data analysis exploration, models training and evaluation, pipelines creation, and export of the pipelines as files to be used in the API.
- Frontend - A use interface with a form to input data about a person's social behavior and access the API to return their persanlity trait.
- Backend - An API that receives data from the interface or from [Swagger](https://swagger.io/) and returns the personality trait based on the best-performing model. The API is documented by [Swagger](https://swagger.io/). 

## Execution
To run the projec, you need to install all libraries listed in `.api/requirements.txt`. 
After cloning the repository, navigate to the **api** folder in the terminal and run the commands described below:
> **It is strongly recommended to use a virtual environment such as [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).**

### Installing Dependencies
To install the dependencies listed in `.api/requirements.txt`, run the following command inside the **api** folder: 
```
(env)$ pip install -r requirements.txt
```
---
### Running the API
To start the API, run the following command in the **api** folder:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```
For the development mode, it is recommended to add the **--reload** parameter, which restarts the server automactally after each code change:

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```
---
### Accessing the application

- To access the Swagger documentation, open:<br>
[http://localhost:5000/docs](http://localhost:5000/docs) and select **Swagger**.

- To access the web interface, open:<br>
[http://localhost:5000/](http://localhost:5000/)
