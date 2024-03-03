import pandas as pd


md_inc = pd.read_csv('Documents/DS_projects/Datasets/CAINC1/CAINC1_MD_1969_2022.csv', 
                     skipfooter=4,
                     engine = 'python'
                    ).drop(columns = ['Region', 'TableName', 'IndustryClassification', 'Unit', 'LineCode'])
md_inc['Description'] = md_inc.Description.apply(lambda x: x.split(' (')[0])
md_inc['GeoName'] = md_inc.GeoName.apply(lambda x: x.split(',')[0])

md_pinc = md_inc.loc[md_inc.Description == 'Personal income', :].reset_index()
md_pop = md_inc.loc[md_inc.Description == 'Population',:].reset_index()

md_pinc_pct = md_pinc.loc[1:,'1969':'2022'].div(md_pinc.loc[0,'1969':'2022']).set_index(md_pinc.GeoName[1:])
md_pop_pct = md_pop.loc[1:,'1969':'2022'].div(md_pop.loc[0,'1969':'2022']).set_index(md_pop.GeoName[1:])


md_diff = md_pinc_pct - md_pop_pct

