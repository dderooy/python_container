set -ex

USERNAME=dev
IMAGE=$(printf '%s\n' "${PWD##*/}")

docker build -t $USERNAME/$IMAGE:latest .
