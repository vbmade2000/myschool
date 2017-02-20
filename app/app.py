from flask import Flask, render_template
from pub_site.views import pub_site

myschool_app = Flask(__name__)
myschool_app.register_blueprint(pub_site)

if __name__ == "__main__":
    myschool_app.run()
