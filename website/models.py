from . import db
import time

def curr_time():
    return int(time.time())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    uvid = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    txnId = db.Column(db.Integer, nullable=False)
    otp = db.Column(db.String(6), nullable=False)
    time = db.Column(db.Integer, default=curr_time)

    
class Update(db.Model):
    # Upate request number
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # Name of requester
    name = db.Column(db.String(100), nullable=False)
    # UID or VID of requester
    uvid = db.Column(db.String(256), nullable=False)
    # landlord uid / vid
    luvid = db.Column(db.Integer, nullable=False)
    # landlord mobile nummber
    lmo = db.Column(db.Integer, nullable=False)
    # New address of requester
    new_address = db.Column(db.String(100), nullable=False)
    # landlord address
    laddress = db.Column(db.String(100))
    # Does the request accepted by the landlord
    lapproved = db.Column(db.Boolean , default=False)
    # Is the request still open to be verified
    open = db.Column(db.Boolean , default=True)
    # Reason in case of rejection
    status = db.Column(db.String(500))

    def __repr__(self) -> str:
        return f"Update('{self.id}', '{self.name}', '{self.uvid}', '{self.umo}', '{self.luvid}', '{self.lmo}', '{self.new_address}', '{self.laddress}', '{self.lapproved}', '{self.open}', '{self.status}')"
    
