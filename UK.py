import matplotlib.pyplot as plt
deaths = [432420,494975,481250,471064,480932]
year = ['2019','2020','2021','2022','2023']
ax = plt.barh(year,deaths)
plt.bar_label(ax,labels=deaths,label_type='edge')
plt.xlabel('Total deaths in first 43 weeks (England & Wales)')
plt.ylabel('Year')
plt.title('UK Data: Why No "Save Lives" Hysteria in 2023')
plt.tight_layout()
manager = plt.get_current_fig_manager()
manager.window.state('zoomed')
plt.show()