from invoke import task

@task
def testisavelma(ctx):
    ctx.run("python3 src/testisavelma.py")


@task
def main(ctx):
    ctx.run("python3 src/main.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def kattavuus(ctx):
    ctx.run("coverage run --branch -m pytest")

@task(kattavuus)
def kattavuusraportti(ctx):
    ctx.run("coverage html")

@task
def lint(ctx):
    ctx.run("pylint src")

@task
def autopep(ctx):
    ctx.run("autopep8 --in-place --recursive src")
