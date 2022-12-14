# About

Example project for developing a single package using Python and Poetry.

## Features

- Python 3.10
- basic CLI running `cowsay` with `typer`. Try it with `mypackage-cli greet aiguasol` after installing the project.
- basic configuration file using `pydantic`.
- Aiguasol repository added to `pyproject.toml` for publishing the package.

## Getting started with Docker

1. Install [Docker](https://docs.docker.com/get-docker/) and `docker-compose` if you haven't already.
1. Clone this repository
   1. Optional: adapt `pyproject.toml` to your needs: package name, CLI commands, etc.
1. Copy `.env.sample` to `.env` and edit the variables as needed.
   1. `POETRY_HTTP_BASIC_AIGUASOL_PASSWORD` should not be committed to version control.
1. Build containers with `docker compose build`
1. Launch containers with `docker compose up -d`
1. Inspect container health with `docker compose ps`
1. Test the boilerplate CLI with `docker compose exec -it demo mypackage-cli greet aiguasol`
   
   ```
   docker compose exec -it demo mypackage-cli greet aiguasol
     ________
   | aiguasol |
     ========
           \
            \
              ^__^
              (oo)\_______
              (__)\       )\/\
                  ||----w |
                  ||     ||
   ```

1. Open the project inside a container using `vscode` remote container utilities. Read more about this in the [vscode documentation](https://code.visualstudio.com/docs/remote/containers).
   1. with the `Remote - Containers` extension, open the command palette and select `Remote-Containers: Open Folder in Container`.
   1. Alternatively use `docker compose exec -it demo bash` to access the container through `bash.
   1. From inside the container: 
      1. Update the code in `src/` and add dependencies as needed with `poetry add <package>`.
      1. Build the project and publish it to Aiguasol's repository using `poetry build` and `poetry publish --repository aiguasol`.

## Getting started without Docker

1. Install [Poetry](https://python-poetry.org/docs/#installation) if you haven't already.
2. Add environment variables

   1. `export POETRY_HTTP_BASIC_AIGUASOL_USERNAME=aiguasol`
   2. `export POETRY_HTTP_BASIC_AIGUASOL_PASSWORD=<password>`

3. Install dependencies with `poetry install`.
4. Update code as needed.
5. Build the project and publish it to Aiguasol's repository using `poetry build` and `poetry publish --repository aiguasol`.

## Roadmap

- [ ] Add tests boilerplate
- [ ] add CI boilerplate code
- [ ] add Helm chart
- [x] convert the repository to template
- [ ] convert the repository to a cookiecutter template
