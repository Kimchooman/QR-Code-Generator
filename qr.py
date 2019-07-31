import qrcode
from os import walk
from PIL import Image
import os
import random
import sys
import png

def save_png(id):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 1,
        border = 1,
    )

    url = "/%s" %(id)

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image()

    img = img.resize((176,176))
    file_name = "%s.png" % (id)
    img.save(file_name)

    old_path = file_name
    new_path = "qrcodes/%s" % (file_name)
    os.rename(old_path, new_path)

def gen_qr_batch(batch_size):
        batch_size = batch_size
        existing_files = walk("qrcodes").next()

        for _ in range(batch_size):
            while True:
                current_int = random.randint(100000000,999999999)
                for files in existing_files:
                    if "%s.png" % (str(current_int)) is not files:
                        pass

                    else:
                        current_int = random.randint(100000000,999999999)
                        break

                else:
                    break
            save_png(str(current_int))

gen_qr_batch(int(sys.argv[1]))
