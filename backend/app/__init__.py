# Import Flask
from flask import Flask
from app.controllers import barang_controller, customer_controller, laporan_controller


def create_app() -> Flask:
  """Method ini akan dipanggil oleh file run.py untuk membuat instance Flask."""
  
  app = Flask(__name__)
  app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://admin:121995@localhost:3306/pt_stdu"
  
  # Memasang blueprint ke instance Flask agar dapat diakses
  app.register_blueprint(barang_controller)
  app.register_blueprint(customer_controller)
  app.register_blueprint(laporan_controller)
  
  return app