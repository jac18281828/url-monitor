FROM jac18281828/pythondev:latest

WORKDIR /workspaces/urlmonitor

COPY --chown=jac:jac . .

USER jac