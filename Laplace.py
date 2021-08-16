from PIL import Image


class ProcesadorImagenes:
    def __init__(self, url):
        self.url = url
        self.img = Image.open(url)
        self.pix = self.img.load()

    def Laplace(self):
        img_size = [self.img.size[0], self.img.size[1]]
        new_img = Image.new('RGB', (img_size[0], img_size[1]), 'black')
        new_pix = new_img.load()
        for i in range(1, img_size[0] - 1):
            for j in range(1, img_size[1] - 1):
                c2 = self.pix[i - 1, j]
                c4 = self.pix[i,     j - 1]
                c5 = self.pix[i,     j]
                c6 = self.pix[i,     j + 1]
                c8 = self.pix[i + 1, j]
                nR = (c2[0] * (-1)) + (c4[0] * (-1)) + \
                    (c5[0] * (4)) + (c6[0] * (-1)) + (c8[0] * (-1))
                nG = (c2[1] * (-1)) + (c4[1] * (-1)) + \
                    (c5[1] * (4)) + (c6[1] * (-1)) + (c8[1] * (-1))
                nB = (c2[2] * (-1)) + (c4[2] * (-1)) + \
                    (c5[2] * (4)) + (c6[2] * (-1)) + (c8[2] * (-1))
                if nR > 255:
                    nR = 255
                elif nR < 0:
                    nR = 0
                if nG > 255:
                    nG = 255
                elif nG < 0:
                    nG = 0
                if nB > 255:
                    nB = 255
                elif nB < 0:
                    nB = 0
                avg = (nR+nG+nB) // 3
                new_pix[i, j] = (avg, avg, avg)
        return new_img
