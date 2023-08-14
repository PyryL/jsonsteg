from invoke import task

@task
def test(ctx):
    ctx.run("pytest tests cli_tests", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest tests cli_tests", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)
