import click

@click.group()
def main():
	print("main")
@main.command()
def run_motor():
	print("Running motors")