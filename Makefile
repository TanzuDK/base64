run:
	pipenv run uvicorn main:app --reload --static-dir="$(pwd)/app"