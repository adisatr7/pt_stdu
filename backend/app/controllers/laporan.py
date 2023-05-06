# Import library yang dibutuhkan
from typing import Any, Literal
from flask import Blueprint, jsonify, request
from flask.wrappers import Response
import datetime
from ..models import LaporanModel, session


# Inisiasi Blueprint
laporan_controller = Blueprint("laporan_controller", __name__)


# Buat endpoint untuk menambahkan data laporan (NOT TESTED)
@laporan_controller.route("/laporan", methods=["POST"])
def add_laporan() -> Response | tuple[Response, Literal[500]]:

  try:
    # Ambil data dari request
    data: Any = request.json

    # Buat objek laporan baru
    laporan = LaporanModel(
      int(data["nomor_laporan"]),
      data["kd_barang"],
      int(data["nomor_customer"]),
      data["no_so"],
      data["no_do"],
      data["tgl_laporan"],
      data["jml_masuk"],
      data["jml_keluar"],
      data["nama_driver"],
      data["no_polisi"]
    )

    # Tambahkan laporan baru ke database
    session.add(laporan)
    session.commit()

    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify({ "message": "Data added!", "data": laporan.get() })
  
  # Jika terjadi error, tampilkan pesan error
  except Exception as e:
    print(f"Error occurred while adding data: {e}")
    return jsonify({"error": f"An error occurred while adding data: {e}"}), 500


# Buat endpoint untuk mengambil semua data laporan
@laporan_controller.route("/laporan", methods=["GET"])
def get_laporan() -> Response | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data laporan
    results: list[LaporanModel] = session.query(LaporanModel).all()
    
    # Ubah hasil query (kumpulan laporan) menjadi bentuk Python list
    list_laporan: list = [b.get() for b in results]
  
    # Ubah Python list menjadi bentuk JSON
    return jsonify(list_laporan)
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": f"An error occurred while retrieving data: {e}"}), 500


# Buat endpoint untuk mengambil satu data laporan
@laporan_controller.route("/laporan/<int:nomor_laporan>", methods=["GET"])
def get_one_laporan(nomor_laporan) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Jalankan query untuk mengambil data laporan
    laporan: Any = session.query(LaporanModel).filter(LaporanModel.nomor_laporan == nomor_laporan).first()
  
    # Jika laporan tidak ditemukan, tampilkan error 404
    if not laporan:
      print(f"Error: Not found!")
      return jsonify({"error": "Laporan not found!"}), 404
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify(laporan.get())
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({"error": f"An error occurred while retrieving data: {e}"}), 500


# Buat endpoint untuk mengubah data laporan 
@laporan_controller.route("/laporan/<int:nomor_laporan>", methods=["PUT"])
def update_laporan(nomor_laporan) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]]:
  
  try:
    # Ambil data dari request
    data: Any = request.json
  
    # Jalankan query untuk mengambil data laporan
    laporan: LaporanModel | None = session.query(LaporanModel).filter(LaporanModel.nomor_laporan == nomor_laporan).first()
  
    # Jika laporan tidak ditemukan, tampilkan error 404
    if not laporan:
      return jsonify({ "error": "Laporan not found!" }), 404
  
    # Ubah data laporan yang sudah diambil
    laporan.nama_laporan = data["nama_laporan"]
    session.commit()
  
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify({ "message": "Data updated!", "data": laporan.get() })
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({ "error": f"An error occurred while updating data: {e}" }), 500


# Buat endpoint untuk menghapus data laporan
@laporan_controller.route("/laporan/<int:nomor_laporan>", methods=["DELETE"])
def delete_laporan(nomor_laporan) -> Response | tuple[Response, Literal[404]] | tuple[Response, Literal[500]] :
    
  try:
    # Jalankan query untuk mengambil data laporan
    laporan: Any = session.query(LaporanModel).filter(LaporanModel.nomor_laporan == nomor_laporan).first()
    
    # Jika laporan tidak ditemukan, tampilkan error 404
    if not laporan:
      return jsonify({"error": "Laporan not found!"}), 404

    # Hapus data laporan yang sudah diambil
    session.delete(laporan)
    session.commit()
    
    # Ubah data yang sudah diambil menjadi bentuk JSON
    return jsonify({ "message": "Data deleted!", "data": laporan.get() })
  
  # Jika terjadi error, tampilkan pesan error-nya
  except Exception as e:
    print(f"Error occurred while retrieving data: {e}")
    return jsonify({ "error": f"An error occurred while updating data: {e}" }), 500
