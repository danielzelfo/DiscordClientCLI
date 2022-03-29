import sys
import discord
import time
import argparse

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	
	channel = None
	
	while True:
		line = input()
		if channel is None: #  input channel
			if line == "":
				break
			
			if not line.isnumeric():
				print(f"Expected Channel ID. Got: \"{line}\"", file=sys.stderr)
				continue
			
			channelid = int(line)
			channel = client.get_channel(channelid)
			if channel is None:
				print(f"Invalid Channel ID: \"{line}\"", file=sys.stderr)
		else:
			if line == "":
				channel = None
				continue
			
			await channel.send(line)
	
	print("EXITING CLIENT...")
	await client.close()
	time.sleep(1)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("token", help="account token (user token by default)")
	parser.add_argument("-b", "--bot", action="store_true", help="provided token is for a bot")
	args = parser.parse_args()
	
	client.run(args.token, bot=args.bot)