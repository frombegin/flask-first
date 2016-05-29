#!/usr/bin/env bash

gunicorn -w 3 app:app