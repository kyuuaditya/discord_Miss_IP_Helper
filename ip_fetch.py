# Author: kyuuaditya

import socket
import psutil
import discord
import credentials

def get_ipv4_address():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and "Wi-Fi" in interface:  # Adjust for your system
                return addr.address
    return "No Wi-Fi IPv4 found"

local_ip = get_ipv4_address()

async def send_discord_message():
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')
        channel = client.get_channel(credentials.Ishu_testing_Channel_ID)
        if channel:
            await channel.send(f"@everyone IPv4-Address: {local_ip} Password: horse-plinko1234 ")
        await client.close()

    await client.start(credentials.DISCORD_TOKEN)

import asyncio
asyncio.run(send_discord_message())
