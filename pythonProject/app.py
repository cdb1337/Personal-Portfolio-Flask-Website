from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Cinema Booking app",
        "thumb": "images/cinema.png",
        "hero": "images/cinema-hero.png",
        "categories": ["python"],
        "slug": "cinema-app",
        "prod": "https://github.com/cdb1337/CinemaApp"
    },
    {
        "name": "Selenium Automation",
        "thumb": "images/automation.png",
        "hero": "images/automation-hero.png",
        "categories": ["python", "selenium"],
        "slug": "selenium-automation",
        "prod": "https://github.com/cdb1337/Selenium_best_practice"
    },
    {
        "name": "Expense Tracker app",
        "thumb": "images/expense.png",
        "hero": "images/expense-hero.png",
        "categories": ["python"],
        "slug": "expense-tracker",
        "prod": "https://github.com/cdb1337/Spending-Tracker"
    }
]

slug_to_project = {project['slug']: project for project in projects}


@app.route('/')
def home():
    return render_template('home.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html",
                           project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__=="__main__":
    app.run(debug=True)
