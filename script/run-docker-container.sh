#!/bin/bash

docker run -p 80:80 --env-file ./.env giuseppett/app-budget

# Check: http://0.0.0.0:80/docs
# Check: http://127.0.0.1:80/docs
