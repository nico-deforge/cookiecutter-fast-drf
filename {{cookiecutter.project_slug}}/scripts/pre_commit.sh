GREEN="\033[32m"
RED="\033[31m"
NC="\033[0m"

if [ -z "$@" ]
then
  echo "checking for everything"
  black ./tests/ &&
  black ./{{cookiecutter.project_slug}}/ &&
  flake8 ./tests/ &&
  flake8 ./{{cookiecutter.project_slug}}/ &&
  isort ./tests/ &&
  isort ./{{cookiecutter.project_slug}}/ &&
  mypy ./tests/ &&
  mypy ./{{cookiecutter.project_slug}}/
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
  black ./{{cookiecutter.project_slug}}/$app &&
  flake8 ./tests/test_$app &&
  flake8 ./{{cookiecutter.project_slug}}/$app &&
  isort ./tests/$app  &&
  isort ./{{cookiecutter.project_slug}}/$app  &&
  mypy ./tests/$app  &&
  mypy ./{{cookiecutter.project_slug}}/$app  &&
  if [ $? -eq 0 ]; then
    echo "${GREEN}all good ! ready to commit !${NC}"
    pytest ./tests/test_$app
  else
    echo "${RED}FAILED, Still work to do${NC}"
  fi
  done
fi
