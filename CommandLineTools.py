import click
#import PiWarsTurkiyeRobotKiti2019 as pitr

@click.group()
def main():
	print("main")

@main.command()
@click.option("--speed", "-s", default=480, help="The speed of the motors")
@click.argument("motors")
def run_motor(speed,motors):
	speeds = [0, 0]
	if(motors == "left"):
		speeds[0] = speed
	elif(motors == "right"):
		speeds[1] = speed
	elif(motors == "both"):
		speeds[0] = speed
		speeds[1] = speed
	else:
		click.echo("Not a valid argument")
		return
	click.echo(speeds)