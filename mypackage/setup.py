# setup.py
from setuptools import setup, find_packages
from os import path

from mypackage import module1
working_directory = path.abspath(path.dirname(module1))

with open(path.join(working_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='mypackage',  # Nama package Anda
    version='0.01',  # Versi package
    packages=find_packages(),  # Mencari semua subfolder
    description='Package sederhana untuk menyapa user pemain game',
    author='Anugrah Fitri Novanda' 'Rifqi Alan Maulana' 'Sita Rasmi Raihana' 'Hanifah Atthahira Basir' 'Agung Allo Karaeng' 'A. Alya Musaenab asmin', 
    author_email='irafitrinovanda@gmail.com',
    url='https://github.com/anugrahfitri-code/mypackage',  # URL repositori (GitHub atau lainnya)
    license='MIT',  # Lisensi
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
