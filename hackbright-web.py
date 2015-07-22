from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html", first = first, last = last, github = github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)

@app.route("/add-student-form")
def add_student_form():
    """Show form for adding students."""

    return render_template("add-student.html")

@app.route("/add-student-confirm", methods=['POST'])
def add_student_confirmation():
    """Show a confirmation that a student has been added to the DB"""

    fname = request.form.get('given-name')
    lname = request.form.get('surname')
    github = request.form.get('github')
    hackbright.make_new_student(fname, lname, github)
    return render_template("add-student-confirm.html", github = github)

if __name__ == "__main__":
    app.run(debug=True)