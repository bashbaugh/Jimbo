from discord.ext import commands
import paramiko

import config as cfg

class Sandbox_commands(commands.Cog, name="Eval"):
    def __init__(self, bot):
        self.bot = bot
        self.ssh_client = None

    @commands.command(name='$connect')
    async def openSSH(self, ctx):
        """- Open a connection the the Ubuntu shell sandbox"""
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.ssh_client.connect(cfg.SANDBOX_SSH_HOST, username=cfg.SANDBOX_SSH_USERNAME, key_filename=cfg.SANDBOX_SSHKEY_FILENAME)
        await ctx.send("Sucesfully connected to sandbox. **__PLEASE REMEMBER TO CLOSE THE CONNECTION WHEN YOU ARE FINISHED, USING__** `--$close`. Use shell by typing `--$ <command>`");

    @commands.command(name='$close')
    async def closeSSH(self, ctx):
        """- Close connection to shell sandbox"""
        self.ssh_client.close()

    @commands.command(name='$')
    async def SSH_command(self, ctx, *, cmd):
        """<command> - Run <command> in an ubuntu shell (run $connect first)"""
        stdin, stdout, stderror = self.ssh_client.exec_command(cmd)
        await ctx.send("`STDOUT:`")
        await ctx.send(stdout.read().decode('utf-8') + stderror.read().decode('utf-8'))

