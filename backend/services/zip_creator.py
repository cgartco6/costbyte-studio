import zipfile
import os
from io import BytesIO

def create_zip_from_files(file_paths: list, output_path: str = None):
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for path in file_paths:
            if os.path.exists(path):
                zip_file.write(path, os.path.basename(path))
    buffer.seek(0)
    if output_path:
        with open(output_path, "wb") as f:
            f.write(buffer.getvalue())
    return buffer
