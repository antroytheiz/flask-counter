from datetime import datetime
from app import db

class PageCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ipaddress  = db.Column(db.Text(20), nullable=True)
    tanggal  = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)   

    def __repr__(self):
        return f"('{self.id},{self.ipaddress},{self.tanggal}')"
     

# <td>{{date.strftime("%A, %d-%B-%Y")}}</td>
# <td>{{date.strftime("%X")}}</td>