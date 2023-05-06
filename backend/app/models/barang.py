from sqlalchemy import Column, VARCHAR
from .base import Base


class BarangModel(Base):
  
  # Nama Tabel
  __tablename__: str = "barang"
  
  # Primary Key
  kd_barang: Column = Column(VARCHAR(16), primary_key=True)
  
  # Kolom Lainnya
  nama_barang: Column = Column(VARCHAR(64))
  
  # Konstruktor
  def __init__(self, kd_barang, nama_barang) -> None:
    self.kd_barang = kd_barang
    self.nama_barang = nama_barang
  
  # Method untuk mengonversi obyek barang menjadi dictionary
  def get(self) -> dict:
    return {
      "kd_barang": self.kd_barang,
      "nama_barang": self.nama_barang
    }