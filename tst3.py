from pyrogram import Client, Filters,Emoji
from pyrogram.errors import FloodWait
import time
from emoji import UNICODE_EMOJI
app = Client(session_name="llx",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token ="765108996:AAGYA2lsT6yw1q5SEx1PXesPWYdwb8RBivc")
d = -1001315425757
s = -1001203491308
g = ["0","1","2","3","4","6","NEED","RUN","CATCH","DROP","BALL","HAWA","WD","WIDE","NB","PLAYING","OVER","WON","WIN","START","STOP","]

@app.on_message(Filters.chat(s) & Filters.text & ~Filters.edited)
def forward(client,Message):
 v = z = f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
   f = True
 if not f:
  for i in Message.text:
   if i in UNICODE_EMOJI:
    z = True
   for p in g:
    if i.casefold() in p.casefold():
     v = True
  if v or z:
   mes = client.send_message(d, Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
   with open("sure.txt", "r") as f:
    x = f.readlines()
   y = [j for j in x[0].split(" ")]
   del y[:2]
   y = " ".join(str(x) for x in y)
   o = open("sure.txt","w")
   o.write(y + " " +str(Message.message_id) + " " + str(mes.message_id))
   o.close()

@app.on_message(Filters.chat(s) & Filters.text & Filters.edited)
def forward(client,Message):
 file = open("sure.txt" , "r")
 lines = file.readlines()
 file.close()
 for line in lines:
  x = line.split()
  id = str(Message.message_id)
  if id in x:
   try:
    client.edit_message_text(d,int(x[x.index(id)+1]),Message.text.markdown.replace("🖲","🙇🏼‍♂").replace("📟","🎳").replace("🇩🇪","🇮🇶").replace("🇦🇲","🇮🇶")) 
   except FloodWait as e:
    time.sleep(e.x)
@app.on_message(Filters.command("c"))
def main(client, message):
 with open("sure.txt" , "w") as files:
  files.write("000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000")
  files.close()
  message.reply("Done") 
app.run()
