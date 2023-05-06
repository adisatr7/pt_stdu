from typing import Any
from sqlalchemy import ForeignKey, Column, Integer, VARCHAR, Date
from .base import Base


class LaporanModel(Base):
  
  # Nama Tabel
  __tablename__: str = "laporan"
  
  # Primary Key
  kd_laporan: Column = Column(VARCHAR(16), primary_key=True)
  
  # Foreign Keys
  kd_customer: Column = Column(VARCHAR(16), ForeignKey("customer.kd_customer"))
  kd_barang: Column = Column(VARCHAR(16), ForeignKey("barang.kd_barang"))
  
  # Kolom Lainnya
  no_so: Column = Column(VARCHAR(16))
  no_do: Column = Column(VARCHAR(16))
  tgl_transaksi: Column = Column(Date)
  jml_masuk: Column = Column(Integer)
  jml_keluar:  Column = Column(Integer)
  nama_driver: Column = Column(VARCHAR(64))
  no_polisi: Column = Column(VARCHAR(12))
  
  # Konstruktor
  def __init__(self, kd_transaksi, kd_customer, kd_barang, no_so, no_do, tgl_transaksi, jml_masuk, jml_keluar, nama_driver, no_polisi) -> None:
    self.kd_transaksi = kd_transaksi
    self.kd_customer = kd_customer
    self.kd_barang = kd_barang
    self.no_so = no_so
    self.no_do = no_do
    self.tgl_transaksi = tgl_transaksi
    self.jml_masuk = jml_masuk
    self.jml_keluar = jml_keluar
    self.nama_driver = nama_driver
    self.no_polisi = no_polisi