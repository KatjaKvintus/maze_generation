from invoke import task
'''Module for @task tasks.'''


@task
def coverage(ctx):
    '''Running pytest evaluation'''
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    '''To run test coverage report'''
    ctx.run("coverage html", pty=True)


@task
def test(ctx):
    '''To run unittests'''
    ctx.run("pytest", pty=True)
