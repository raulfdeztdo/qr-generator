from setuptools import setup, find_packages

setup(
    name='qr-generator-gui',
    version='0.1.0',
    author='Tu Nombre',
    author_email='tu.email@example.com',
    description='Una aplicación gráfica para generar códigos QR.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'qrcode',
        'Pillow',
        'tkinter',  # o 'PyQt5' si decides usar PyQt
    ],
    entry_points={
        'console_scripts': [
            'qr-generator=main:main',  # Asegúrate de tener una función main en main.py
        ],
    },
)