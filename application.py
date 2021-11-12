from flask import Flask, render_template, request
from flask_mail import Mail, Message
from flask import escape

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'noreplytothis377@gmail.com'
app.config['MAIL_PASSWORD'] = 'ggdtnufxeesuxwwj'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        name = escape(request.form.get("name"))
        email = escape(request.form.get("email"))
        message = escape(request.form.get("message"))

        html_body = create_html_body(name, email, message)
        msg = Message('Запитване', sender='noreplytothis377@gmail.com', recipients=['mshaklev@gmail.com'])
        msg.html = html_body
        mail.send(msg)

        return render_template("index.html")


# helper function create html body
def create_html_body(name, email, message):
    html = """\
    <html>
      <body>"""
    html += f"""<ul>
         <li><strong>Name:</strong> {name}</li>
         <li><strong>Email:</strong><a href="mailto:{email}"> {email}</a></li>
         <li><strong>Message:</strong> {message}</li>
         </ul>
         """

    html += """</body>
               </html>"""

    return html
