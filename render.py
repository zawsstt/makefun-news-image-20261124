from PIL import Image, ImageDraw, ImageFont
import os
W=H=1024
BG=(247,243,232); INK=(20,20,20); RED=(178,34,34); NAVY=(23,48,84); TEAL=(0,110,110); GOLD=(184,134,11)
def font(name, size):
    p=f"/usr/share/fonts/truetype/dejavu/{name}"
    return ImageFont.truetype(p, size)
F_TITLE=font("DejaVuSerif-Bold.ttf", 64)
F_DATE=font("DejaVuSans-Bold.ttf", 34)
F_KICK=font("DejaVuSans-Bold.ttf", 22)
F_H1=font("DejaVuSans-Bold.ttf", 44)
F_H2=font("DejaVuSans-Bold.ttf", 30)
F_H3=font("DejaVuSans-Bold.ttf", 26)
F_BODY=font("DejaVuSans.ttf", 24)
F_SMALL=font("DejaVuSans.ttf", 21)
F_FOOT=font("DejaVuSans-Bold.ttf", 22)
img=Image.new("RGB",(W,H),BG)
d=ImageDraw.Draw(img)
# border
d.rectangle([8,8,W-9,H-9], outline=INK, width=4)
d.rectangle([20,20,W-21,H-21], outline=INK, width=1)
# masthead
d.text((W//2, 52), "THE WORLD IN ONE PAGE", font=F_KICK, fill=NAVY, anchor="ma")
d.text((W//2, 108), "24 NOVEMBER 2026", font=F_TITLE, fill=INK, anchor="ma")
d.text((W//2, 188), "TUESDAY  •  WORLD NEWS IN ONE IMAGE", font=F_DATE, fill=RED, anchor="ma")
d.line([(40,232),(W-40,232)], fill=INK, width=3)
d.line([(40,239),(W-40,239)], fill=INK, width=1)

# Lead: Nvidia - full width block y 235-480
d.rectangle([40,250,W-40,492], outline=INK, width=2, fill=(255,255,255))
# chip icon
cx,cy=110,370
d.rectangle([cx-52,cy-52,cx+52,cy+52], fill=(0,110,90), outline=INK, width=2)
for i in range(3):
    d.line([(cx-52,cy-30+i*30),(cx-70,cy-30+i*30)], fill=INK, width=4)
    d.line([(cx+52,cy-30+i*30),(cx+70,cy-30+i*30)], fill=INK, width=4)
d.text((cx,cy), "AI", font=font("DejaVuSans-Bold.ttf",36), fill=(255,255,255), anchor="mm")
d.text((200,270), "NVIDIA BRINGS BACK HUANG", font=F_H1, fill=INK)
d.text((200,322), "Nvidia reinstates Jensen Huang", font=font("DejaVuSans-Bold.ttf",30), fill=INK)
d.text((200,358), "as CEO after Trump push.", font=font("DejaVuSans-Bold.ttf",30), fill=INK)
d.text((200,408), "His fortune rises $34bn in a day,", font=F_BODY, fill=INK)
d.text((200,438), "to $143.8bn, Forbes reports.", font=F_BODY, fill=INK)
d.text((40,504), "LEAD STORY  •  BUSINESS & TECH", font=F_KICK, fill=NAVY)

# Row 2: two columns y 530-730
def card(x0,x1,y0,y1,tag,headline,body,accent):
    d.rectangle([x0,y0,x1,y1], outline=INK, width=2, fill=(255,255,255))
    d.rectangle([x0,y0,x1,y0+34], fill=accent)
    d.text((x0+12,y0+17), tag, font=F_KICK, fill=(255,255,255), anchor="lm")
    # headline wrapped manually via lines passed
    yy=y0+48
    for line in headline:
        d.text((x0+12,yy), line, font=F_H2, fill=INK)
        yy+=36
    yy+=6
    for line in body:
        d.text((x0+12,yy), line, font=F_SMALL, fill=(60,60,60))
        yy+=27

card(40,502,540,738,"UKRAINE  •  WAR AT SEA",["UKRAINE STRIKE SINKS","RUSSIAN WARSHIP"],["Off Libya, Kyiv's reach","widens beyond Europe."], NAVY)
card(522,984,540,738,"UKRAINE  •  STRIKES",["KYIV REGION STRIKES","KILL AT LEAST 14"],["Homes hit, AFP reports.","Russian toll nears 500,000."], RED)

# Row 3: three columns y 745-935
def card3(x0,x1,tag,headline,body,accent):
    y0,y1=745,935
    d.rectangle([x0,y0,x1,y1], outline=INK, width=2, fill=(255,255,255))
    d.rectangle([x0,y0,x1,y0+32], fill=accent)
    d.text((x0+10,y0+16), tag, font=font("DejaVuSans-Bold.ttf",18), fill=(255,255,255), anchor="lm")
    yy=y0+44
    for line in headline:
        d.text((x0+10,yy), line, font=F_H3, fill=INK)
        yy+=32
    yy+=4
    for line in body:
        d.text((x0+10,yy), line, font=font("DejaVuSans.ttf",19), fill=(60,60,60))
        yy+=24

card3(40,342,"INDONESIA",["FACTORY FIRE","KILLS 24"],["24 killed in an","Indonesia factory fire."], (150,60,0))
card3(362,662,"DENMARK",["SCHOOL PHONES","TO BE BANNED"],["Denmark to ban phones","to 10th grade after","poor PISA results."], TEAL)
card3(682,984,"USA  •  TECH",["STATES SUE MUSK","OVER GROK"],["States sue Musk firms","over sexualised images","made with Grok chatbot."], (90,40,110))

# Footer
d.line([(40,950),(W-40,950)], fill=INK, width=2)
d.text((W//2,972), "ALSO: UN warns wars put food aid for 7.3m more at risk  •  24 NOV 2026", font=font("DejaVuSans.ttf",19), fill=INK, anchor="ma")
img.save("/home/hatch/workspace/makefun/news-image-20261124-entry/entry.png", optimize=True)
print("saved", os.path.getsize("/home/hatch/workspace/makefun/news-image-20261124-entry/entry.png"))
print(img.size, img.mode)
