import pandas as pd

proposal_path = "proposal_data.csv"
df = pd.read_csv(proposal_path)

edm = df[["h_edm", "s_edm", "l_edm", "ln_edm"]]
metal = df[["h_metal", "s_metal", "l_metal", "ln_metal"]]
country = df[["h_country", "s_country", "l_country", "ln_country"]]
classical = df[["h_classical", "s_classical", "l_classical", "ln_classical"]]
rap = df[["h_rap", "s_rap", "l_rap", "ln_rap"]]
rock = df[["h_rock", "s_rock", "l_rock", "ln_rock"]]
jazz = df[["h_jazz", "s_jazz", "l_jazz", "ln_jazz"]]
pop = df[["h_pop", "s_pop", "l_pop", "ln_pop"]]
indie = df[["h_indie", "s_indie", "l_indie", "ln_indie"]]
reggae = df[["h_reggae", "s_reggae", "l_reggae", "ln_reggae"]]
folk = df[["h_folk", "s_folk", "l_folk", "ln_folk"]]