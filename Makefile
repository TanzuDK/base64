run:
	pipenv run uvicorn main:app --reload --static-dir="./api"