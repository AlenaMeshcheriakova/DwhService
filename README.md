# DWH Service

## Overview

This is a DWH Service, which part of telegram project - "DeutschLernen" designed for interacting with DWH database. 
The application get data from different services via rabitMQ and saved it to DWH DB.

## Dependensy

This service provide data from another service: DataServive via rabitMQ. 

## Features

Saved information about next objects:
 - Group
 - Level
 - Word
 - Word Type
 - User

## Prerequisites

- Python 3.8 or higher
- Use Poetry for a dependency installation from pyproject.toml:
(Install poetry and execute comand "poetry install")

## Environment

For enviroment installetion, you need to create you own .env and .test.env file
In cfg/config.py please write link to your cfg files
For a template use file: .env.template

## Installation

### Clone the Repository

https://github.com/AlenaMeshcheriakova/DwhService.git
cd DwhService

### Starting project

For start up project, use: /src/main.py
