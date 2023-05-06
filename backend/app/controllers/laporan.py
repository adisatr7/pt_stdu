# Import library yang dibutuhkan
from typing import Any, Literal
from flask import Blueprint, jsonify, request
from flask.wrappers import Response
from ..models import LaporanModel, session


# Inisiasi Blueprint
laporan_controller = Blueprint("laporan_controller", __name__)


# Buat endpoint untuk menambahkan data laporan
@laporan_controller.route("/laporan", methods=["POST"])
def add_laporan() -> Response | tuple[Response, Literal[500]]:

  try:
    # Ambil data dari request
    data: Any = request.json

    # Buat objek laporan baru
    laporan = LaporanModel(
      data["kd_laporan"],
      data["kd_customer"],
      data["kd_barang"],
      data["no_so"],
      data["no_do"],
      data["tgl_transaksi"],
      data["jml_masuk"],
      data["jml_keluar"],
      data["nama_driver"],
      data["no_polisi"]
    )

    # Tambahkan laporan baru ke database
    session.add(laporan)
    session.commit()

    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(laporan)
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while adding data: {e}")
    return jsonify({"error": "An error occurred while adding data"}), 500


# Buat endpoint untuk mengambil semua data laporan
@laporan_controller.route("/laporan", methods=["GET"])
def get_laporan() -> Response | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data laporan
    laporan = session.query(LaporanModel).all()
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(laporan)
  
  except Exception as e:
    # Handle the error appropriately, such as logging it and returning an error response
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": "An error occurred while retrieving data!"}), 500


# Buat endpoint untuk mengambil satu data laporan
@laporan_controller.route("/laporan/<string:kd_laporan>", methods=["GET"])
def get_one_laporan(kd_laporan) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data laporan
    laporan: Any = session.query(LaporanModel).filter(LaporanModel.kd_laporan == kd_laporan).first()
  
    # Jika laporan tidak ditemukan, tampilkan error 404
    if not laporan:
      return jsonify({"error": "Laporan not found!"}), 404
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(laporan)
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": "An error occurred while retrieving data"}), 500


# Buat endpoint untuk mengubah data laporan
@laporan_controller.route("/laporan/<string:kd_laporan>", methods=["PUT"])
def update_laporan(kd_laporan) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Ambil data dari request
    data: Any = request.json
  
    # Jalankan query untuk mengambil data laporan
    laporan: Any = session.query(LaporanModel).filter(LaporanModel.kd_laporan == kd_laporan).first()
  
    # Jika laporan tidak ditemukan, tampilkan error 404
    if not laporan:
      return jsonify({"error": "Laporan not found!"}), 404
  
    # Ubah data laporan yang sudah diambil
    laporan.nama_laporan = data["nama_laporan"]
    session.commit()
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(laporan)
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while updating data: {e}")
    return jsonify({"error": "An error occurred while updating data"}), 500


# Buat endpoint untuk menghapus data laporan
@laporan_controller.route("/laporan/<string:kd_laporan>", methods=["DELETE"])
def delete_laporan(kd_laporan) -> Response:
    
    # Jalankan query untuk mengambil data laporan
    laporan: Any = session.query(LaporanModel).filter(LaporanModel.kd_laporan == kd_laporan).first()
    
    # Hapus data laporan yang sudah diambil
    session.delete(laporan)
    session.commit()
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(laporan)