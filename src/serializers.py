from flask_restx import fields
from app import api

conf_serializer = api.model(
    'Configuration',
    {
        'min_area_threshold': fields.Integer,
        'contour_threshold': fields.Float,
    }
)

processing_serializer = api.model(
    'Processing',
    {
        'logo_path': fields.String(required=True),
        'video_path': fields.String(required=True),
    }
)