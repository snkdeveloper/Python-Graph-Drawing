import matplotlib.pyplot as plt

slices=[8,9,48,21,33,242]
labels =['Not taken the vaccine[2.3%]','Pressured,for some other reason[2.5%]','Pressured to take, for education or work[13.3]','Pressured to take,for travel[5.8%]',"Willingly,  for others' health[9.1%]",'Willingly,for own health[67%]']

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format
    

plt.pie(slices,labels=labels,autopct=autopct_format(slices))
plt.title('Quantification of COVID-19 Vaccine Coercion in India: A Survey Study')
plt.tight_layout()
manager = plt.get_current_fig_manager()
manager.window.state('zoomed')
plt.show()