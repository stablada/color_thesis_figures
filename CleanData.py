import colorsys
import GenreProcessing as gp


def seek(query):
    return gp.seek(query=query)


def create_data(query):
    return Data(seek(query=query))


class Data:
    global Genre
    global d_h_value, d_s_value, d_l_value
    global m_h_value, m_s_value, m_l_value
    global l_h_value, l_s_value, l_l_value
    global d_color, m_color, l_color

    def __init__(self, genre):
        self.Genre = genre
        self.split()

    def hexify(self, h, s, l):
        r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
        hex_color = '#{:02x}{:02x}{:02x}'.format(int(r * 255), int(g * 255), int(b * 255))
        return hex_color

    def split(self):
        df = self.Genre.dataframe

        dislike = df[df["ln_%s" % self.Genre.name] < 4.0]
        moderate = df[df["ln_%s" % self.Genre.name] > 4.0]
        moderate = moderate[moderate["ln_%s" % self.Genre.name] < 7.0]
        like = df[df["ln_%s" % self.Genre.name] > 7.0]

        self.d_h_value = round(dislike["h_%s" % self.Genre.name].mean(),2)
        self.d_s_value = round(dislike["s_%s" % self.Genre.name].mean(),2)
        self.d_l_value = round(dislike["l_%s" % self.Genre.name].mean(),2)

        self.m_h_value = round(moderate["h_%s" % self.Genre.name].mean(),2)
        self.m_s_value = round(moderate["s_%s" % self.Genre.name].mean(),2)
        self.m_l_value = round(moderate["l_%s" % self.Genre.name].mean(),2)

        self.l_h_value = round(like["h_%s" % self.Genre.name].mean(),2)
        self.l_s_value = round(like["s_%s" % self.Genre.name].mean(),2)
        self.l_l_value = round(like["l_%s" % self.Genre.name].mean(),2)

        self.d_color = self.hexify(self.d_h_value, self.d_s_value, self.d_l_value)
        self.m_color = self.hexify(self.m_h_value, self.m_s_value, self.m_l_value)
        self.l_color = self.hexify(self.l_h_value, self.l_s_value, self.l_l_value)
