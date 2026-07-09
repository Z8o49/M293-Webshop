from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
import math, random
root=Path('/mnt/data/sitework')
imgdir=root/'images'; imgdir.mkdir(exist_ok=True)
perfumes=[
('noir-ambre','Noir Ambre','Amber · Oud · Vanilla','Icon','CHF 280',('#2a160c','#c78b42','#f0d090')), 
('fleur-dor','Fleur d’Or','Jasmine · Musk · Iris','Radiant','CHF 245',('#efe5c7','#e7c55f','#fff7e8')),
('midnight-oud','Midnight Oud','Saffron · Rose · Oud','Evening','CHF 310',('#080b25','#7b2842','#d79c54')),
('velvet-iris','Velvet Iris','Iris · Violet · Sandalwood','Powdery','CHF 230',('#2a2144','#8d78b8','#e5d7ff')),
('cedar-smoke','Cedar Smoke','Cedar · Incense · Leather','Smoky','CHF 260',('#17120e','#6d4b32','#b9966f')),
('rose-elixir','Rose Élixir','Rose · Pink Pepper · Musk','Romantic','CHF 250',('#37121d','#b9435b','#ffd5dd')),
]

def make_img(slug,name,notes,colors):
    W,H=900,650
    base=Image.new('RGB',(W,H),colors[0])
    px=base.load()
    c1=tuple(int(colors[1].lstrip('#')[i:i+2],16) for i in (0,2,4))
    c2=tuple(int(colors[2].lstrip('#')[i:i+2],16) for i in (0,2,4))
    bg=tuple(int(colors[0].lstrip('#')[i:i+2],16) for i in (0,2,4))
    for y in range(H):
        for x in range(W):
            dx=(x-W*.55)/(W*.55); dy=(y-H*.36)/(H*.48)
            r=max(0,1-(dx*dx+dy*dy))
            t=y/H
            col=tuple(int(bg[i]*(1-r*.75)+c1[i]*(r*.55)+c2[i]*(max(0,1-t)*r*.25)) for i in range(3))
            px[x,y]=col
    im=base.filter(ImageFilter.GaussianBlur(0.5)).convert('RGBA')
    d=ImageDraw.Draw(im,'RGBA')
    random.seed(slug)
    for i in range(45):
        x=random.randint(-100,W); y=random.randint(-80,H); rr=random.randint(20,120)
        col=c2 if i%2 else c1
        d.ellipse((x,y,x+rr,y+rr), fill=(*col, random.randint(10,34)))
    # note-specific motifs
    if 'Rose' in notes:
        for i in range(7):
            cx=random.randint(90,800); cy=random.randint(80,540)
            for p in range(8):
                ang=math.pi*2*p/8
                d.ellipse((cx+math.cos(ang)*18-18,cy+math.sin(ang)*12-28,cx+math.cos(ang)*18+18,cy+math.sin(ang)*12+10), fill=(*c2,45))
    if 'Cedar' in notes or 'Oud' in notes:
        for i in range(18):
            x=random.randint(0,W)
            d.line((x,H,x+random.randint(-160,160),random.randint(0,H)), fill=(*c1,45), width=random.randint(2,5))
    if 'Jasmine' in notes or 'Iris' in notes:
        for i in range(14):
            cx=random.randint(80,820); cy=random.randint(70,570)
            for p in range(5):
                ang=math.pi*2*p/5
                d.ellipse((cx+math.cos(ang)*16-11,cy+math.sin(ang)*16-22,cx+math.cos(ang)*16+11,cy+math.sin(ang)*16+22), fill=(*c2,38))
    # bottle silhouette
    cx=W//2; top=95; bw=190; bh=380
    d.rounded_rectangle((cx-bw//2,top+58,cx+bw//2,top+bh), radius=60, fill=(8,7,7,165), outline=(*c2,135), width=2)
    d.rounded_rectangle((cx-45,top+10,cx+45,top+70), radius=10, fill=(*c1,185), outline=(*c2,140), width=1)
    d.rectangle((cx-82,top+225,cx+82,top+310), fill=(255,248,222,32), outline=(*c2,95), width=1)
    d.text((cx,top+244), name, fill=(*c2,230), anchor='mm')
    d.text((cx,top+282), notes, fill=(255,250,230,180), anchor='mm')
    im=im.convert('RGB')
    im.save(imgdir/f'{slug}.jpg', quality=92)
for slug,name,notes,tag,price,colors in perfumes:
    make_img(slug,name,notes,colors)
