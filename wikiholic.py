import yagmail, requests, shutil

def get_article():
    title = requests.get("https://en.wikipedia.org/api/rest_v1/page/random/title")
    req = requests.get("https://en.wikipedia.org/api/rest_v1/page/pdf/{title}".format(title=title))

    if req.status_code == 200:
        with open("./out.pdf", "wb") as file:
            req.raw.decode_content = True
            shutil.copyfileobj(req.raw, file)

if __name__ == '__main__':
    get_article()

    html_msg = """
        <table cellspacing="0" cellpadding="0">
        <tr>
        <td align="center" width="300" height="40" bgcolor="#000091" style="-webkit-border-radius: 5px; -moz-border-radius: 5px; border-radius: 5px; color: #ffffff; display: block;">
        <a href="{link}" style="font-size:16px; font-weight: bold; font-family: Helvetica, Arial, sans-serif; text-decoration: none; line-height:30px; width:100%; display:inline-block"><span style="color: #FFFFFF">Awesome Email Button</span></a>
        </td>
        </tr>
        </table>
        """.format(link = "")

    yag = yagmail.SMTP("wikiholictoday", "wikiwiki123")

    for email in ["anastasija.tortevska@gmail.com", "martin.ristovski@columbia.edu"]:
        yag.send(email, "the subject", html_msg)
