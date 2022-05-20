import os
import six
import requests
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO


def download_image(url):
    response = requests.get(url)
    file_name = 'profile_images/'  + url.split('/')[-1]  + '.png'
    file_path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    return file_name


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = AccountActivationTokenGenerator()

####### resize user image
# image_types = {
#     "jpg": "JPEG",
#     "jpeg": "JPEG",
#     "png": "PNG",
#     "gif": "GIF",
#     "tif": "TIFF",
#     "tiff": "TIFF",
# }

# def image_resize(image, width, height):
#     # Open the image using Pillow
#     if image:
#         img = Image.open(image)
#         # check if either the width or height is greater than the max
#         if img.width > width or img.height > height:
#             output_size = (width, height)
#             # Create a new resized “thumbnail” version of the image with Pillow
#             img.thumbnail(output_size)
#             # Find the file name of the image
#             img_filename = Path(image.file.name).name
#             # Spilt the filename on “.” to get the file extension only
#             img_suffix = Path(image.file.name).name.split(".")[-1]
#             # Use the file extension to determine the file type from the image_types dictionary
#             img_format = image_types[img_suffix]
#             # Save the resized image into the buffer, noting the correct file type
#             buffer = BytesIO()
#             img.save(buffer, format=img_format)
#             # Wrap the buffer in File object
#             file_object = File(buffer)
#             # Save the new resized file as usual, which will save to S3 using django-storages
#             image.save(img_filename, file_object)
#     else:
#         pass


#### end resize user image