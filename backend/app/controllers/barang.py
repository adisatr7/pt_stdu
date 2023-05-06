# Import library yang dibutuhkan
from typing import Any, Literal
from flask import Blueprint, jsonify, request
from flask.wrappers import Response
from ..models import BarangModel, session


# Inisiasi Blueprint
barang_controller = Blueprint("barang_controller", __name__)


# Buat endpoint untuk menambahkan data barang (NOT TESTED)
@barang_controller.route("/barang", methods=["POST"])
def add_barang() -> Response | tuple[Response, Literal[500]]:

  try:
    # Ambil data dari request
    data: Any = request.json

    # Buat objek barang baru
    barang = BarangModel(data["kd_barang"],data["nama_barang"])

    # Tambahkan barang baru ke database
    session.add(barang)
    session.commit()

    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(barang)
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while adding data: {e}")
    return jsonify({"error": f"An error occurred while adding data: {e}"}), 500


# Buat endpoint untuk mengambil semua data barang
@barang_controller.route("/barang", methods=["GET"])
def get_barang() -> Response | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data barang
    results: list[BarangModel] = session.query(BarangModel).all()
    
    # Ubah hasil query (kumpulan barang) menjadi bentuk Python list
    list_barang: list = [b.get() for b in results]
  
    # Ubah Python list menjadi bentuk JSON
    return jsonify(list_barang)
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": f"An error occurred while retrieving data: {e}"}), 500


# Buat endpoint untuk mengambil satu data barang
@barang_controller.route("/barang/<string:kd_barang>", methods=["GET"])
def get_one_barang(kd_barang) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data barang
    barang: Any = session.query(BarangModel).filter(BarangModel.kd_barang == kd_barang).first()
  
    # Jika barang tidak ditemukan, tampilkan error 404
    if not barang:
      print(f"Error: Not found!")
      return jsonify({"error": "Barang not found!"}), 404
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(barang.get())
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": f"An error occurred while retrieving data: {e}"}), 500


# Buat endpoint untuk mengubah data barang
@barang_controller.route("/barang/<string:kd_barang>", methods=["PUT"])
def update_barang(kd_barang) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Ambil data dari request
    data: Any = request.json
  
    # Jalankan query untuk mengambil data barang
    barang: BarangModel | None = session.query(BarangModel).filter(BarangModel.kd_barang == kd_barang).first()
  
    # Jika barang tidak ditemukan, tampilkan error 404
    if not barang:
      return jsonify({"error": "Barang not found!"}), 404
  
    # Ubah data barang yang sudah diambil
    barang.nama_barang = data["nama_barang"]
    session.commit()
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(barang.get())
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": f"An error occurred while updating data: {e}"}), 500


# Buat endpoint untuk menghapus data barang (NOT TESTED)
@barang_controller.route("/barang/<string:kd_barang>", methods=["DELETE"])
def delete_barang(kd_barang) -> Response:
    
    # Jalankan query untuk mengambil data barang
    barang: Any = session.query(BarangModel).filter(BarangModel.kd_barang == kd_barang).first()
    
    # Hapus data barang yang sudah diambil
    session.delete(barang)
    session.commit()
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(barang)