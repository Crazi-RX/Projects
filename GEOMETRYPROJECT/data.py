import pygal

# Our data is a list of series.
# Each series is a list with a label and a list of data points
data = [["Spotify", [300, 350, 400, 230, 120, 150, 80]],
        ["Pandora",  [200, 27, 180, 200, 190, 100, 190]],
        ["Apple Music", [240, 400, 70, 130, 180, 100, 100]],
        ["IHeartRadio", []],
        ["Others",  []]]


# Make a Pygal chart
stackedline_chart = pygal.StackedLine(fill=True)
stackedline_chart.title = "Age Preference Of Streaming Apps (in )"
stackedline_chart.x_labels = map(str, range(16, 65))

# For each series in our data, add label and data points
for label, data_points in data:
    stackedline_chart.add(label, data_points)

# Render the chart
stackedline_chart.render()

# Example modified from the pygal.org documentation
