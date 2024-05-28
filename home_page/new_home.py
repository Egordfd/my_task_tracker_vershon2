def homePage(app, render_template):
    @app.route('/', methods=["GET"])
    def hello_world():
        return render_template('home.html')
