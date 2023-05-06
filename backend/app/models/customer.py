from sqlalchemy import Column, VARCHAR, Integer
from .base import Base


class CustomerModel(Base):
  
  # Nama Tabel
  __tablename__: str = "customer"
  
  # Primary Key
  nomor_customer: Column = Column(Integer, primary_key=True)
  
  # Kolom Lainnya
  nama_customer: Column = Column(VARCHAR(64))

  # Konsktruktor
  def __init__(self, nomor_customer, nama_customer) -> None:
    self.nomor_customer = nomor_customer
    self.nama_customer = nama_customer
  
  # Method untuk mengonversi obyek barang menjadi dictionary
  def get(self) -> dict:
    return {
      "nomor_customer": self.nomor_customer,
      "nama_customer": self.nama_customer
    }