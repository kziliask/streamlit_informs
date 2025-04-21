import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

st.title("Welcome to the Front Page of Monte Carlo")
generator = np.random.default_rng()
days = st.slider("Days", 1, 30, 10)


demand = []
iteration = []
for i in range(1000):
    for day in range(days):
        num_of_people = generator.poisson(5)
        demand.append(num_of_people)
        iteration.append(sum(demand))

fig, ax = plt.subplots()
sns.histplot(demand, bins=30, kde=True, ax=ax)
st.write(fig)
