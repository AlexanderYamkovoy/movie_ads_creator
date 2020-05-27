from flask_restx import fields
from app import api

conf_serializer = api.model(
    'Configuration',
    {
        'contour_threshold': fields.Float,
    }
)
processing_serializer = api.model(
    'Processing',
    {
        'logo': fields.String(required=True),
        'video': fields.String(required=True),
    }
)
