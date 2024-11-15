import pandas as pd

# Seek command for LikenessCards data pulling
def seek(query):
        for genre in genre_list:
                if genre.name is query:
                        return genre

# Genre Object Class which holds items for later analysis
class Genre:
        # global vars
        global name
        global h_val, s_val, l_val
        global likeness

        # funcs
        def __init__(self, name, h_val, s_val, l_val, likeness):
                self.name = name
                self.h_val = h_val
                self.s_val = s_val
                self.l_val = l_val
                self.likeness = likeness

genre_list = []

proposal_path = "proposal_data.csv"
df = pd.read_csv(proposal_path)

## List Generation (albeit the inefficient way) ##
# EDM
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Metal
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Country
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Classical
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Rap
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Rock
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Jazz
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Pop
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Indie
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Reggae
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))
# Folk
genre_list.append(Genre(name="edm",
                        h_val=df["h_edm"],
                        s_val=df["s_edm"],
                        l_val=df["l_edm"],
                        likeness=df["ln_edm"]))