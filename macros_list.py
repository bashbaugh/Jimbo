"""Jimbo macros
Each macro dict should have the following keys:
    type - 'command' or 'listener'
    name - command name or listener content
    delete - delete user's macro command after printing macro?
    help - help message. False to hide macro in help menu.
    content - macro content
"""

MACROS = [
        {
         'type': 'command',
         'name': 'bothelp',
         'delete': True,
         'help': "Display the bot help message",
         'content': "I am a bot. I was developed by <@563490372836130817>. Prefix commands with `--`. To access the help panel, type `--help`." 
        }, {
         'type': 'command',
         'name': 'botsource',
         'delete': True,
         'help': "Bot source code for James and Jimbo",
         'content': "Jimbo source is at https://github.com/scitronboy/Jimbo , James source is at https://github.com/jbis9051/JSProgrammingDiscordBot/ . Feel free to contribute to the bots."
        }, {
         'type': 'command',
         'delete': True,
         'name': 'listenershelp',
         'help': "What are Listeners?",
         'content': "I listen for special keywords to be mentioned in a conversation. When I hear one of the keywords I understand, I perform some action. I also listen for other things, such as when a new user joins, so I can welcome them. You can find a list of some of my listeners by using the `listListeners` command."
        }, {
         'type': 'command',
         'delete': False,
         'name': 'welcome',
         'help': "Server welcome message",
         'content': "All new recruits: Welcome to the server! Please introduce yourself after joining. This includes age and location (if you are comfortable with sharing that), favorite languages and frameworks, a few recent and past projects (if you have any you want to share), github profiles, personal websites, etc., and anything else that you want us to know about you."
        }, {
         'type': 'command',
         'delete': False,
         'name': 'serverdesc',
         'help': "Server description",
         'content': "This server is a general teen programming chat.  We work on projects together and help each other with programming questions and stuff. Most of the channel names are self-explanatory. Language and topic help channels are under the help category at the bottom, projects are under the projects category. General chat is in #general .Ping an Admin in #general if you want a new channel created." 
        }, {
         'type': 'command',
         'delete': True,
         'name': 'behave',
         'help': "Tell everyone to behave themselves.",
         'content': "Behave yourself please!"
        }
        ]

LISTENER_LIST = [
        "There are no listeners so far!!"
        ]
