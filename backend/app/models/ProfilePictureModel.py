from config.db import db, ma
from marshmallow import fields

class ProfilePicture(db.Model):
    __tablename__ = 'profile_pictures'

    id = db.Column(db.BigInteger, primary_key=True)
    usuario_id = db.Column(db.BigInteger, db.ForeignKey('users.id'), unique=True, nullable=False)
    downloadUrl = db.Column(db.String(255))
    file_name = db.Column(db.String(255))
    file_type = db.Column(db.String(255))

    def __init__(self, usuario_id, downloadUrl, file_name, file_type):
        self.usuario_id = usuario_id
        self.downloadUrl = downloadUrl
        self.file_name = file_name
        self.file_type = file_type

class ProfilePictureSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    usuario_id = fields.Integer(required=True)
    downloadUrl = fields.String()
    file_name = fields.String()
    file_type = fields.String()

    class Meta:
        fields = ('id', 'usuario_id', 'downloadUrl', 'file_name', 'file_type')
        model = ProfilePicture

profile_picture_schema = ProfilePictureSchema()
profile_pictures_schema = ProfilePictureSchema(many=True)