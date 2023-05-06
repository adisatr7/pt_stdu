from typing import Any
from sqlalchemy import Column, Date, ForeignKey, Integer, VARCHAR
from .base import Base


class LaporanModel(Base):
  
  # Nama Tabel
  __tablename__: str = "laporan"
  
  # Primary Key
  nomor_laporan: Column = Column(Integer, primary_key=True)
  
  # Foreign Keys
  nomor_customer: Column = Column(Integer, ForeignKey("customer.nomor_customer"))
  kd_barang: Column = Column(VARCHAR(24), ForeignKey("barang.kd_barang"))
  
  # Kolom Lainnya
  no_so: Column = Column(VARCHAR(24))
  no_do: Column = Column(VARCHAR(24))
  tgl_laporan: Column = Column(Date)
  jml_masuk: Column = Column(Integer)
  jml_keluar:  Column = Column(Integer)
  nama_driver: Column = Column(VARCHAR(64))
  no_polisi: Column = Column(VARCHAR(16))
  
  # Konstruktor
  def __init__(self, nomor_laporan, kd_barang, nomor_customer, no_so, no_do, tgl_laporan, jml_masuk, jml_keluar, nama_driver, no_polisi) -> None:
    self.nomor_laporan = nomor_laporan
    self.kd_barang = kd_barang
    self.nomor_customer = nomor_customer
    self.no_so = no_so
    self.no_do = no_do
    self.tgl_laporan = tgl_laporan
    self.jml_masuk = jml_masuk
    self.jml_keluar = jml_keluar
    self.nama_driver = nama_driver
    self.no_polisi = no_polisi
  
  # Method untuk mengambil data laporan
  def get(self) -> dict[str, Any]:
    return {
      "nomor_laporan": self.nomor_laporan,
      "nomor_customer": self.nomor_customer,
      "kd_barang": self.kd_barang,
      "no_so": self.no_so,
      "no_do": self.no_do,
      "tgl_laporan": self.tgl_laporan,
      "jml_masuk": self.jml_masuk,
      "jml_keluar": self.jml_keluar,
      "nama_driver": self.nama_driver,
      "no_polisi": self.no_polisi
    }