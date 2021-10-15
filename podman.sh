rm -r screenshots-container
podman rm bk-tests
podman create --env-file docker-secrets.list --name bk-tests -t bk-tests
podman cp features/. bk-tests:features/
podman start -a bk-tests
podman cp bk-tests:screenshots/. screenshots-container
