# url = "https://sheenarbw.github.io/pres-playwright-2024-pycascades/"

# import segno

# qrcode = segno.make_qr(url)
# qrcode.save(
#     "images/qr2.png",
#     scale=5,
#     border=0,
#     light="#222",
#     dark="#fda061"
#     )



# #    --r-link-color: #ff812c;
# #    --r-link-color-dark: #ef582c;
# #    --r-link-color-hover: #fda061;
# #    --r-selection-background-color: #fda061;
# #    --r-selection-color: #222;



from segno import helpers

# Some params accept multiple values, like email, phone, url
qrcode = helpers.make_mecard(name="O'Connell,Sheena",
                             email=('sheena.oconnell@umuzi.org'),
                             url=['https://sheenaoc.com', "https://umuzi.org"])
qrcode.save('my-mecard.png', scale=4)