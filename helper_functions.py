# create html body
def create_html_body(name, email, message):
    html = """\
    <html>
      <body>"""
        html += f"""<ul>
         <li><strong>Name:</strong> {{name}}<li>
         <li><strong>Email:</strong><a href="mailto:{{email}}"> {{email}}</a><li>
         <li><strong>Message:</strong> {{message}}<li>
         </ul>
         """

    html += """</body>
               </html>"""

    return html
