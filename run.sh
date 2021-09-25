set -ex
USERNAME=dev
IMAGE=$(printf '%s\n' "${PWD##*/}")
VOLUME="$(pwd)/script"

docker run -it --rm --name $IMAGE -v $VOLUME:/script $USERNAME/$IMAGE /bin/bash
