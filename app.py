import sql_interface
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    sql.add_comment("You are the best!")
    sql.add_comment("It has been good to know you!")
    sql.add_comment("Those are some fancy pants!")
    return render_template('index.html')


@app.route('/fetch_comments')
def fetch_comments():
    affirmations = sql.get_comments()
    return render_template('carousel.html', affirmations = affirmations)


# TODO: make sure user has permissions
@app.route('/manage')
def manage():
    affirmations = sql.get_comments()
    return render_template('manage.html', affirmations = affirmations)


# TODO: make sure user has permissions
def update_comment_status():
    pass


# TODO: make sure user has permissions
def delete_comment():
    pass


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/add_affirmatoin')
def add_affirmation():
    if sql.add_comment("You are the best!")
        return "success"
    else
        return "error"


@app.route('/approval')
def approval():
    affirmations = sql.get_comments()
    return render_template('approve.html', affirmations = affirmations)


if __name__ == '__main__':
    # create a database connection
    sql = sql_interface.SQL()
    sql.create_comments_table()
    app.run()
