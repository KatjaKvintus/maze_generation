'''Routing details for the web app'''
from invoke import task


@task
def coverage(ctx):
    '''Test coverage'''
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    '''For generating test coverage report'''
    ctx.run("coverage html", pty=True)


@task
def test(ctx):
    '''For running automatic tests for all .py files'''
    ctx.run("pytest", pty=True)
