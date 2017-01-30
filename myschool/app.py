from flask import Flask, render_template


app = Flask(__name__)

class MenuList(list):
    def __init__(self):
        self.extend(["Home", "About"])

@app.route("/")
@app.route("/index")
def index():
    """Entry point"""
    menus = MenuList()
    return render_template("index.html", menus=menus)

@app.route("/about")
def about():
    """About us page"""
    menus = MenuList()
    return render_template("about.html", menus=menus)
    

if __name__ == "__main__":
    app.run()
