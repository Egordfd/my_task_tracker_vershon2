
from flask import Flask, render_template
from home_page.new_home import homePage


app = Flask(__name__)

homePage(app, render_template)




if __name__ == "__main__":
    app.run(debug=True)