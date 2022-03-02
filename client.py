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
	if len(sys.argv) < 2:
		print("Usage: python client.py <token>")
		sys.exit(1)
	client.run(sys.argv[1], bot=False)