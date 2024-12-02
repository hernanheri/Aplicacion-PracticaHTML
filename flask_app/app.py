from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesaria para usar mensajes flash
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_completo = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    fecha_nacimiento = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Ruta principal: Formulario de registro
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Obtener datos del formulario
        nombre_completo = request.form["nombre_completo"].strip()
        email = request.form["email"].strip()
        fecha_nacimiento = request.form["fecha_nacimiento"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Validaciones
        if not nombre_completo or not email or not fecha_nacimiento or not password or not confirm_password:
            flash("Todos los campos son obligatorios.")
            return redirect(url_for("index"))

        if password != confirm_password:
            flash("Las contraseñas no coinciden.")
            return redirect(url_for("index"))

        # Guardar en la base de datos
        nuevo_usuario = Usuario(
            nombre_completo=nombre_completo,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            password=password  # Nota: No es seguro almacenar contraseñas sin cifrar
        )
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash("Registro exitoso.")
            return redirect(url_for("profile", user_id=nuevo_usuario.id))
        except Exception as e:
            db.session.rollback()
            flash("Error al registrar el usuario. Quizás el correo ya está registrado.")
            return redirect(url_for("index"))

    return render_template("index.html")

# Ruta de perfil del usuario
@app.route("/profile/<int:user_id>")
def profile(user_id):
    usuario = Usuario.query.get_or_404(user_id)
    return render_template("profile.html", usuario=usuario)

# Crear tablas de la base de datos al ejecutar el script
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
