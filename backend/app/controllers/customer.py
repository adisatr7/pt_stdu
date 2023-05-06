# Import library yang dibutuhkan
from typing import Any, Literal
from flask import Blueprint, jsonify, request
from flask.wrappers import Response
from ..models import CustomerModel, session


# Inisiasi Blueprint
customer_controller = Blueprint("customer_controller", __name__)


# Buat endpoint untuk menambahkan data customer (NOT TESTED)
@customer_controller.route("/customer", methods=["POST"])
def add_customer() -> Response | tuple[Response, Literal[500]]:

  try:
    # Ambil data dari request
    data: Any = request.json

    # Buat objek customer baru
    customer = CustomerModel(data["nomor_customer"],data["nama_customer"])

    # Tambahkan customer baru ke database
    session.add(customer)
    session.commit()

    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify({ "message": "Data added!", "data": customer.get() })
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while adding data: {e}")
    return jsonify({"error": f"An error occurred while adding data: {e}"}), 500


# Buat endpoint untuk mengambil semua data customer
@customer_controller.route("/customer", methods=["GET"])
def get_customer() -> Response | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data customer
    results: list[CustomerModel] = session.query(CustomerModel).all()
    
    # Ubah hasil query (kumpulan customer) menjadi bentuk Python list
    list_customer: list = [b.get() for b in results]
  
    # Ubah Python list menjadi bentuk JSON
    return jsonify(list_customer)
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": f"An error occurred while retrieving data: {e}"}), 500


# Buat endpoint untuk mengambil satu data customer
@customer_controller.route("/customer/<string:nomor_customer>", methods=["GET"])
def get_one_customer(nomor_customer) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data customer
    customer: Any = session.query(CustomerModel).filter(CustomerModel.nomor_customer == nomor_customer).first()
  
    # Jika customer tidak ditemukan, tampilkan error 404
    if not customer:
      print(f"Error: Not found!")
      return jsonify({"error": "Customer not found!"}), 404
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(customer.get())
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": f"An error occurred while retrieving data: {e}"}), 500


# Buat endpoint untuk mengubah data customer 
@customer_controller.route("/customer/<string:nomor_customer>", methods=["PUT"])
def update_customer(nomor_customer) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Ambil data dari request
    data: Any = request.json
  
    # Jalankan query untuk mengambil data customer
    customer: CustomerModel | None = session.query(CustomerModel).filter(CustomerModel.nomor_customer == nomor_customer).first()
  
    # Jika customer tidak ditemukan, tampilkan error 404
    if not customer:
      return jsonify({ "error": "Customer not found!" }), 404
  
    # Ubah data customer yang sudah diambil
    customer.nama_customer = data["nama_customer"]
    session.commit()
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify({ "message": "Data updated!", "data": customer.get() })
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({ "error": f"An error occurred while updating data: {e}" }), 500


# Buat endpoint untuk menghapus data customer
@customer_controller.route("/customer/<string:nomor_customer>", methods=["DELETE"])
def delete_customer(nomor_customer) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]] :
    
  try:
    # Jalankan query untuk mengambil data customer
    customer: Any = session.query(CustomerModel).filter(CustomerModel.nomor_customer == nomor_customer).first()
    
    # Jika customer tidak ditemukan, tampilkan error 404
    if not customer:
      return jsonify({"error": "Customer not found!"}), 404

    # Hapus data customer yang sudah diambil
    session.delete(customer)
    session.commit()
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify({ "message": "Data deleted!", "data": customer.get() })
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({ "error": f"An error occurred while updating data: {e}" }), 500