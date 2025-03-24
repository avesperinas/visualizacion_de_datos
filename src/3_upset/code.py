import pandas as pd
from matplotlib import pyplot as plt
from upsetplot import UpSet, from_indicators


df = pd.read_csv("pokemon.csv")

df["Type 2"].fillna("No other", inplace=True)
types = df[["Type 1", "Type 2"]]

unique_types = set(types["Type 1"]).union(set(types["Type 2"]))
type_matrix = pd.DataFrame({t: (types["Type 1"] == t) | (types["Type 2"] == t) for t in unique_types})

upset_data = from_indicators(type_matrix.columns, type_matrix)
upset = UpSet(upset_data, subset_size="count", show_percentages=True)

plt.figure(figsize=(10, 6))
upset.plot()
plt.suptitle("Combinaciones de Tipos de Pokémon")
plt.savefig("upset_pokemon.png", dpi=300, bbox_inches="tight")
plt.close()
