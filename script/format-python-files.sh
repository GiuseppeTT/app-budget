#!/bin/bash

poetry run isort app
poetry run black app
