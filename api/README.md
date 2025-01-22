# How to run DB locally?

> Run the following commands at the root of the project. (Outside of api or frontend)

1. Create a .env file, you can copy the .env.example

```shell
    cp .env.example .env
```

2. Fill in all the fields with the values you want to use locally. Completely up to you.

3. Spin up the container.

```shell
    docker compose up -d
```