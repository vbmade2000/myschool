from flask import Flask, render_template


app = Flask(__name__)

class MenuList(list):
    def __init__(self):
        self.insert(0, ("Home", "/"))
        self.insert(1, ("About", "about"))

@app.route("/")
@app.route("/index")
def index():
    """Entry point"""
    menus = MenuList()
    print str(menus)
    return render_template("index.html", menus=menus)

@app.route("/about")
def about():
    """About us page"""
    menus = MenuList()
    print str(menus)
    return render_template("aboutus.html", menus=menus)
    

if __name__ == "__main__":
    app.run()
