# bin/bash
coverage run setup.py test
coverage report -m -i --omit=/usr/*
