def HTMLify(title,text,effects=[],background="",header="",linkAddress="",linkText=""):
    if "marquee" in effects:
        text="<marquee>%s</marquee>"%text
    if "bounceMarquee" in effects:
        text="<marquee behavior=alternate>%s</marquee>"%text
    if "bold" in effects:
        text="<b>%s</b>"%text
    if "underline" in effects:
        text="<u>%s</u>"%text
    if "italicize" in effects:
        text="<i>%s</i>"%text
    if "link" in effects:
        text+="<a href=%s>%s</a>"%(linkAddress,linkText)
    if "backgroundColor" in effects:
        background=" bgcolor=%s"%str(background)
    elif "backgroundImage" in effects:
        background=" background=%s"%background
    if "header1" in effects:
        header="<h1>%s</h1>"%header
    elif "header2" in effects:
        header="<h2>%s</h2>"%header
    elif "header3" in effects:
        header="<h3>%s</h3>"%header
    elif "header4" in effects:
        header="<h4>%s</h4>"%header
    elif "header5" in effects:
        header="<h5>%s</h5>"%header
    elif "header6" in effects:
        header="<h6>%s</h6>"%header
    while "\n" in text:
        text1=text[0:text.find("\n")]
        text2=text[text.find("\n")+1:]
        text=text1+"<br>"+text2
    html="<!DOCTYPE html><html><head><title>%s</title>%s</head><body%s>%s</body></html>"%(title,header,background,text)
    return html
