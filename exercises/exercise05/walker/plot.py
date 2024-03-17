import pandas as pd
import matplotlib.pyplot as plt

def filter_columns(dataframe, *selected_columns):
    return dataframe.loc[:, selected_columns]

def plot_projects_by_status(affordable_housing_data, ward_population_data):
    affordable_columns_to_keep = ('MAR_WARD', 'STATUS_PUBLIC')
    ward_columns_to_keep = ('WARD', 'LABEL')

    filtered_affordable_data = filter_columns(affordable_housing_data, *affordable_columns_to_keep)
    filtered_ward_data = filter_columns(ward_population_data, *ward_columns_to_keep)

    plt.figure(figsize=(12, 6))

    status_to_plot = 'Under Construction'

    if status_to_plot in filtered_affordable_data['STATUS_PUBLIC'].unique():
        status_data = filtered_affordable_data[filtered_affordable_data['STATUS_PUBLIC'] == status_to_plot]
        wards = sorted(status_data['MAR_WARD'].unique(), key=lambda x: int(x.split()[-1]))
        heights = status_data.groupby('MAR_WARD').size()
        plt.bar(wards, heights, label=status_to_plot, alpha=0.7)

        plt.xlabel('Ward Name')
        plt.ylabel('Count')
        plt.title('Units Currently Under Construction in each Ward of Washington DC')
        plt.show()
    else:
        print(f"No projects found with status '{status_to_plot}'.")