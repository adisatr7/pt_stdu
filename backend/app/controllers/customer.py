# Import library yang dibutuhkan
from typing import Any, Literal
from flask import Blueprint, jsonify, request
from flask.wrappers import Response
from ..models import CustomerModel, session


# Inisiasi Blueprint
customer_controller = Blueprint("customer_controller", __name__)


# Buat endpoint untuk menambahkan data customer
@customer_controller.route("/customer", methods=["POST"])
def add_customer() -> Response | tuple[Response, Literal[500]]:

  try:
    # Ambil data dari request
    data: Any = request.json

    # Buat objek customer baru
    customer = CustomerModel(data["kd_customer"],data["nama_customer"])

    # Tambahkan customer baru ke database
    session.add(customer)
    session.commit()

    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(customer)
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while adding data: {e}")
    return jsonify({"error": "An error occurred while adding data"}), 500


# Buat endpoint untuk mengambil semua data customer
@customer_controller.route("/customer", methods=["GET"])
def get_customer() -> Response | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data customer
    customer = session.query(CustomerModel).all()
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(customer)
  
  except Exception as e:
    # Handle the error appropriately, such as logging it and returning an error response
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": "An error occurred while retrieving data!"}), 500


# Buat endpoint untuk mengambil satu data customer
@customer_controller.route("/customer/<string:kd_customer>", methods=["GET"])
def get_one_customer(kd_customer) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data customer
    customer: Any = session.query(CustomerModel).filter(CustomerModel.kd_customer == kd_customer).first()
  
    # Jika customer tidak ditemukan, tampilkan error 404
    if not customer:
      return jsonify({"error": "Customer not found!"}), 404
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(customer)
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": "An error occurred while retrieving data"}), 500


# Buat endpoint untuk mengubah data customer
@customer_controller.route("/customer/<string:kd_customer>", methods=["PUT"])
def update_customer(kd_customer) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Ambil data dari request
    data: Any = request.json
  
    # Jalankan query untuk mengambil data customer
    customer: Any = session.query(CustomerModel).filter(CustomerModel.kd_customer == kd_customer).first()
  
    # Jika customer tidak ditemukan, tampilkan error 404
    if not customer:
      return jsonify({"error": "Customer not found!"}), 404
  
    # Ubah data customer yang sudah diambil
    customer.nama_customer = data["nama_customer"]
    session.commit()
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(customer)
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while updating data: {e}")
    return jsonify({"error": "An error occurred while updating data"}), 500


# Buat endpoint untuk menghapus data customer
@customer_controller.route("/customer/<string:kd_customer>", methods=["DELETE"])
def delete_customer(kd_customer) -> Response:
    
    # Jalankan query untuk mengambil data customer
    customer: Any = session.query(CustomerModel).filter(CustomerModel.kd_customer == kd_customer).first()
    
    # Hapus data customer yang sudah diambil
    session.delete(customer)
    session.commit()
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(customer)