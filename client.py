import sys
import discord
import time
import argparse

client = discord.Client()
printPrompts = False

@client.event
async def on_ready():
	print(f'{client.user} has connected to Discord!')
	
	channel = None
	channelPrompt =  ""
	messagePrompt = ""
	if printPrompts:
		channelPrompt =  "Enter channel ID: "
		messagePrompt = "Enter message: "
	
	while True:
		if channel is None: # input channel
			line = input(channelPrompt)
			if line == "":
				break
			
			if not line.isnumeric():
				print(f"Expected Channel ID. Got: \"{line}\"", file=sys.stderr)
				continue
			
			channelid = int(line)
			channel = client.get_channel(channelid)
			if channel is None:
				print(f"Invalid Channel ID: \"{line}\"", file=sys.stderr)
		else: # input message
			line = input(messagePrompt)
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
	parser.add_argument("-p", "--print", action="store_true", help="print prompts")
	args = parser.parse_args()
	
	printPrompts = args.print
	client.run(args.token, bot=args.bot)