set -ex
USERNAME=dev
IMAGE=$(printf '%s\n' "${PWD##*/}")
VOLUME="$(pwd)/script"

docker run -it \
    --rm \
    --name $IMAGE \
    -v $VOLUME:/script \
    --memory=1500m \
    --cpus=1 \
    $USERNAME/$IMAGE /bin/bash