from flask import Blueprint, render_template

pub_site = Blueprint("pub_site", __name__, template_folder='templates')

@pub_site.route("/")
@pub_site.route("/index")
def index():
    """Entry point"""
    topmenus = [("Home", "/"), ("About", "about")] 
    return render_template("index.html", menus=topmenus)

@pub_site.route("/about")
def about():
    """About school"""
    topmenus = [("Home", "/"), ("About", "about")] 
    return render_template("aboutus.html", menus=topmenus)
