# Import fungsi create_app
from app import create_app


# Buat instance Flask
app = create_app()

# Jalankan aplikasi/server Flask
if __name__ == "__main__":
  app.run(debug=True)