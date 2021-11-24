GREEN="\033[32m"
RED="\033[31m"
NC="\033[0m"

if [ -z "$@" ]
then
  echo "checking for everything"
  black ./tests/ &&
  black ./{{cookiecutter_slug}}/ &&
  flake8 ./tests/ &&
  flake8 ./{{cookiecutter_slug}}/ &&
  isort ./tests/ &&
  isort ./{{cookiecutter_slug}}/ &&
  mypy ./tests/ &&
  mypy ./{{cookiecutter_slug}}/
  if [ $? -eq 0 ]; then
    echo "${GREEN}all good ! ready to commit !${NC}"
    pytest ./tests/
  else
    echo "${RED}FAILED, Still work to do${NC}"
  fi
else
  echo "checking for $@"
  for app in "$@"
  do
  black ./tests/test_$app &&
  black ./{{cookiecutter_slug}}/$app &&
  flake8 ./tests/test_$app &&
  flake8 ./{{cookiecutter_slug}}/$app &&
  isort ./tests/$app  &&
  isort ./{{cookiecutter_slug}}/$app  &&
  mypy ./tests/$app  &&
  mypy ./{{cookiecutter_slug}}/$app  &&
  if [ $? -eq 0 ]; then
    echo "${GREEN}all good ! ready to commit !${NC}"
    pytest ./tests/test_$app
  else
    echo "${RED}FAILED, Still work to do${NC}"
  fi
  done
fi
