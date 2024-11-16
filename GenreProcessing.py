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
        global dataframe

        # funcs
        def __init__(self, name, h_val, s_val, l_val, likeness):
                self.name = name
                self.h_val = h_val
                self.s_val = s_val
                self.l_val = l_val
                self.likeness = likeness
                self.dataframe = pd.concat([h_val, s_val, l_val, likeness], axis=1)

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
genre_list.append(Genre(name="metal",
                        h_val=df["h_metal"],
                        s_val=df["s_metal"],
                        l_val=df["l_metal"],
                        likeness=df["ln_metal"]))
# Country
genre_list.append(Genre(name="country",
                        h_val=df["h_country"],
                        s_val=df["s_country"],
                        l_val=df["l_country"],
                        likeness=df["ln_country"]))
# Classical
genre_list.append(Genre(name="classical",
                        h_val=df["h_classical"],
                        s_val=df["s_classical"],
                        l_val=df["l_classical"],
                        likeness=df["ln_classical"]))
# Rap
genre_list.append(Genre(name="rap",
                        h_val=df["h_rap"],
                        s_val=df["s_rap"],
                        l_val=df["l_rap"],
                        likeness=df["ln_rap"]))
# Rock
genre_list.append(Genre(name="rock",
                        h_val=df["h_rock"],
                        s_val=df["s_rock"],
                        l_val=df["l_rock"],
                        likeness=df["ln_rock"]))
# Jazz
genre_list.append(Genre(name="jazz",
                        h_val=df["h_jazz"],
                        s_val=df["s_jazz"],
                        l_val=df["l_jazz"],
                        likeness=df["ln_jazz"]))
# Pop
genre_list.append(Genre(name="pop",
                        h_val=df["h_pop"],
                        s_val=df["s_pop"],
                        l_val=df["l_pop"],
                        likeness=df["ln_pop"]))
# Indie
genre_list.append(Genre(name="indie",
                        h_val=df["h_indie"],
                        s_val=df["s_indie"],
                        l_val=df["l_indie"],
                        likeness=df["ln_indie"]))
# Reggae
genre_list.append(Genre(name="reggae",
                        h_val=df["h_reggae"],
                        s_val=df["s_reggae"],
                        l_val=df["l_reggae"],
                        likeness=df["ln_reggae"]))
# Folk
genre_list.append(Genre(name="folk",
                        h_val=df["h_folk"],
                        s_val=df["s_folk"],
                        l_val=df["l_folk"],
                        likeness=df["ln_folk"]))