"""Глава 19."""

# +
import matplotlib.pyplot as plt
import pandas as pd

# %matplotlib inline
# -

# # %matplotlib - это волшебная команда, которая указывает Jupyter Notebook отображать графики и изображения в самом документе.

# # Визуализация в Python.
#
#
# ### Основы визуализации

df = pd.read_csv("/Users/glebtrofimov/Downloads/air_quality_no2.csv")

df

df.plot()

df["station_london"].plot()

# ## Базовая диаграмма рассеяния

df.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

dir(df.plot)

s_ = [i_ for i_ in dir(df.plot) if not i_.startswith("_")]
s_

# ## Диаграмма размаха

df.plot.box()

# ## Несколько графиков
#
# На одной ячейке можно сразу построить несколько графиков

df.plot(figsize=(12, 4), subplots=True)

# ## Сохранение графика в файл

df.loc[df["station_antwerp"] < 0, "station_antwerp"] = 0

# +
fig, axs = plt.subplots(figsize=(12, 4))

df.plot.area(ax=axs)

axs.set_label("NO$_2$ concentration")
# -

fig.savefig("no2_concentrations.pdf")

# ## Библиотеки для визуализации данных
#
# **Matplotlib**
#
# Самая простая и основная библиотека Python для визуализации, есть все виды графиков
#
# **Seaborn**
#
# Основана на matplotlib, отлично подходит для статистических данных
#
# **ggplot**
#
# Основана на ggplot2 - системе построеня графиков языка R. Позволяет строить график по кусочкам, добавляя постепенно нужные элементы.
#
# **Bokeh**
#
# Также основана на ggplot2, но работает на Python, а не на R, удобна для создания интерактивных веб-графиков, которые можно легко выводить как объекты JSON.
#
# **Folium**
#
# Библиотека Folium упрощает визуализацию данных Python на интерактивной карте.
# Она позволяет привязать данные к карте и выполнять визуализацию хороплетных карт. Хороплетная карта (картограмма) — это тип тематической карты, на которой области затенены или раскрашены пропорционально статистической перемен-ной, которая представляет собой совокупную сводку географических характеристик в каждой области, например плотность населения или доход на душу населения.
#
# **Gleam**
#
# Библиотека Gleam позволяет создавать интерактивные веб-визуализации данных с помощью Python, при этом знание НТМL или JavaScript не требуется