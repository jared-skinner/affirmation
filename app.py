import sql_interface
from flask import Flask, render_template, request
app = Flask(__name__)

TRUE = "1"
FALSE = "0"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fetch_comments')
def fetch_comments():
    affirmations = sql.get_comments(approved = TRUE)
    return render_template('carousel.html', affirmations = affirmations)


# TODO: make sure user has permissions
@app.route('/manage')
def manage():
    affirmations = sql.get_comments()
    return render_template('manage.html', affirmations = affirmations)


@app.route('/update_comment_status', methods=['POST'])
def update_comment_status():
    # TODO: make sure user has permissions

    comment_id = request.form['id']
    new_status = request.form['new_status']

    if sql.update_status(comment_id, new_status):
        return "success"
    else:
        return "error"


def delete_comment():
    # TODO: make sure user has permissions
    pass


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/add_affirmation', methods=['POST'])
def add_affirmation():
    affirmation = request.form['affirmation']

    if sql.add_comment(affirmation):
        return "success"
    else:
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
