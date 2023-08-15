from invoke import task
import os

@task
def test(ctx):
    ctx.run("pytest tests cli_tests", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest tests cli_tests", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

# By removing the build directory before publish commands
# interactive question made by Poetry can be avoided
def remove_build_directory(ctx):
    ctx.run("rm -rf dist/", pty=True)

@task
def publish(ctx):
    remove_build_directory(ctx)
    ctx.run("poetry publish --build", pty=True)

@task
def publish_test(ctx):
    remove_build_directory(ctx)
    ctx.run("poetry config repositories.test-pypi https://test.pypi.org/legacy/", pty=True)
    ctx.run("poetry publish --build --repository test-pypi", pty=True)
