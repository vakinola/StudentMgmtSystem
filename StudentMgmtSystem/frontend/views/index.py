from StudentMgmtSystem.extensions import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    urlparse,
    urljoin,
    db,
)


from StudentMgmtSystem.backend.database.model import Student


index_page = Blueprint(
    "index_page",
    __name__,
    template_folder="../templates",
    static_folder="appname/static",
)


@index_page.route("/")
def index():
    students = Student.query.all()
    return render_template("index.html", students=students)


@index_page.route("student/<int:student_id>/")
def student_information(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template("student.html", student=student)


@index_page.route("/create/", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        age = int(request.form["age"])
        bio = request.form["bio"]

        student = Student(
            firstname=firstname, lastname=lastname, email=email, age=age, bio=bio
        )
        db.session.add(student)
        db.session.commit()

    return render_template("create.html")


@index_page.route("student/<int:student_id>/edit/", methods=("GET", "POST"))
def edit(student_id):
    student = Student.query.get_or_404(student_id)

    if request.method == "POST":
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        email = request.form["email"]
        age = int(request.form["age"])
        bio = request.form["bio"]

        student.firstname = firstname
        student.lastname = lastname
        student.email = email
        student.age = age
        student.bio = bio

        db.session.add(student)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("edit.html", student=student)


@index_page.route("student/<int:student_id>/delete/", methods=["POST"])
def delete(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("index_page.index"))


@index_page.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors-404-error.html"), 404


@index_page.app_errorhandler(500)
def internal_server_error(e):
    return render_template("errors-500-error.html"), 500
