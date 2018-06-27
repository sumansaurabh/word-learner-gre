image_name="nguyenkims/satellizer-demo:$(git rev-parse HEAD)"
container_name="satellizer-demo"

echo "going to pull image $image_name and run container $container_name"

docker pull $image_name
# ignore if container doesn't exist
docker rm -f $container_name || true

docker run -p 5002:5002 -d --restart=always --name $container_name -e FACEBOOK_SECRET=$SATELLIZER_FACEBOOK_SECRET $image_name