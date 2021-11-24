GREEN="\033[32m"
RED="\033[31m"
NC="\033[0m"

if [ -z "$@" ]
then
  echo "checking for everything"
  black ./tests/ &&
  black ./intranet_back/ &&
  flake8 ./tests/ &&
  flake8 ./intranet_back/ &&
  isort ./tests/ &&
  isort ./intranet_back/ &&
  mypy ./tests/ &&
  mypy ./intranet_back/
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
  black ./intranet_back/$app &&
  flake8 ./tests/test_$app &&
  flake8 ./intranet_back/$app &&
  isort ./tests/$app  &&
  isort ./intranet_back/$app  &&
  mypy ./tests/$app  &&
  mypy ./intranet_back/$app  &&
  if [ $? -eq 0 ]; then
    echo "${GREEN}all good ! ready to commit !${NC}"
    pytest ./tests/test_$app
  else
    echo "${RED}FAILED, Still work to do${NC}"
  fi
  done
fi
