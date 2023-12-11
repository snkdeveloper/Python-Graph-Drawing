import matplotlib.pyplot as plt

year = ['Jan-Mar 2018','Apr-Jun 2018','Jul-Sep 2018','Oct-Dec 2018','Jan-Mar 2019','Apr-Jun 2019','Jul-Sep 2019','Oct-Dec 2019','Jan-Mar 2020','Apr-Jun 2020','Jul-Sep 2020','Oct-Dec 2020','Jan-Mar 2021','Apr-Jun 2021','Jul-Sep 2021','Oct-Dec 2021','Jan-Mar 2022','Apr-Jun 2022','Jul-Sep 2022']
births = [187530,197839,215220,186934,182138,194292,214279,187381,184643,192053,210211,186237,191980,194334,216171,193007,170049,186685,201375]

ax = plt.bar(year,births)

plt.xlabel('Time')
plt.ylabel('Number of births in Germany')
plt.xticks(rotation=90)
plt.bar_label(ax,labels=births,label_type='edge')
plt.title('Germany Birth-Rate Decline')
ax[16].set_color('red')
ax[17].set_color('darkred')
ax[18].set_color('saddlebrown')
plt.tight_layout()
manager = plt.get_current_fig_manager()
manager.window.state('zoomed')
plt.show()
