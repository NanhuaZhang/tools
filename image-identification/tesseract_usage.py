try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract


def binarization_process(p, threshold=140):
    if p < threshold:
        return 0
    else:
        return 1


def get_bin_table():
    return list(map(binarization_process, [x for x in range(256)]))


# def run():
#     name = "./pictures/"
#     image = Image.open(name)
#     # image.show()
#
#     text = pytesseract.image_to_string(image, lang="eng")
#
#     print(text)

def run():
    path = "./pictures/"
    name = '4.png'
    image = Image.open(path+name)
    imgry = image.convert('L')

    imgry.save(path+'g'+name)
    table = get_bin_table()
    # print(table)
    out = imgry.point(table, '1')
    out.save(path+'b'+name)

    text = pytesseract.image_to_string(out,config='digits',lang="eng")
    print(text)
    # text = text.strip()
    # text = text.upper()
    # print(text)


if __name__ == '__main__':
    run()
