import click 
# _____________________________________________________________________________________


@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass


@click.command()
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    pass


click.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    pass


click.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a cliente"""
    pass


click.command()
@click.pass_context
def delete(ctx, client_uid):
    """delete a cliente"""
    pass

all = clients

