# Todo App with React and FastAPI

This is a simple Todo application built with:

* React (frontend)
* FastAPI (backend)

The documentation for each part is in the respective folder.

## Development

This uses a `.devcontainer` to provide a containerized development environment from within Cursor.

When Cursor starts up, it will start a container from the `.devcontainer/Dockerfile` and mount the current directory as a volume inside the container.

When you use terminal inside Cursor, you're actually using a shell inside the container.

## TODO

- [ ] Get deployment working on Vercel
- [ ] Setup Postgres on Supabase
- [ ] Actual migrations instead of just using SQLAlchemy models