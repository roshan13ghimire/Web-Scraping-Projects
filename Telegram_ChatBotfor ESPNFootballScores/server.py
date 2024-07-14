from bot import telegram_bot
import Scrap 

bot = telegram_bot("config.cfg")
def make_reply(msg,f_name):
    reply = None
    if msg == "":
        reply = (
            f"Welcome {f_name}, I provide the latest updates on Football Live Scores.\n\n"
            "Type 'yes' to get live scores.\n\n"
        )
    else:
        reply=Scrap.get_espn_soccer_scores()
    return reply

update_id = None
pName = {""}
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
                f_name=str(item["message"]["from"]["first_name"])
            except:
                message = None
                f_name=None
            from_ = item["message"]["from"]["id"]
            if(message == '/end' and f_name in pName):
                bot.send_message("See You Again! \n Ending Connection...",from_)
                pName.remove(f_name)
            else:
                if(pName == "" or f_name not in pName):
                    reply = make_reply("",f_name)
                    bot.send_message(reply,from_)
                    pName.add(f_name)
                else:
                    reply = make_reply(message,f_name)
                    bot.send_message(reply,from_)