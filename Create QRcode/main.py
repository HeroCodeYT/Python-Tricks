import pyqrcode as qr#pip install pyqrcode
Message=input("Enter Your Message:")
MyCode=qr.create(Message)
MyCode.svg("HeroCode.svg",scale=25)