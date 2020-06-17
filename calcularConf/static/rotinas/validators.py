from django.core.exceptions import ValidationError

# def validate_file_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]
#     valid_extensions = ['.json']
#     if not ext.lower() in valid_extensions:
#         raise ValidationError('Unsupported file extension.')

def file_size(value):
    limit = 2 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 kB.')