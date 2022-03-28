import sys
import discord
import time

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
	usage = "Usage: python client.py <token>\noptional arguments:\n\t-b, --bot\tprovided token is for a bot"
	if len(sys.argv) == 3:
		if sys.argv[2] == "-b" or sys.argv[2] == "--bot":
			client.run(sys.argv[1], bot=True)
		else:
			print(usage)
	elif len(sys.argv) == 2:
		client.run(sys.argv[1], bot=False)
	else:
		print(usage)