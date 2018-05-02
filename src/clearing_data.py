import pandas as pd

df = pd.read_csv('../prepared_dataset.csv')

metric_0 = 'R&D Expenditures'
metric_1 = 'GDP per Capita'


def recycler(data, metric):
    data_ = data[['country', 'date', metric]]
    n = 0
    recycled = pd.DataFrame(columns=['country', 'date', metric])
    std_ = data_[metric].std()
    mean_ = data_[metric].mean()
    max_ = data_[metric].max()
    min_ = data_[metric].min()
    while (max_ > (mean_ + 3*std_)) or (min_ < (mean_ - 3 * std_)):
        recycled = recycled.append(
            data_[data_[metric] > (mean_ + 3 * std_)]
        )
        recycled = recycled.append(
            data_[data_[metric] < mean_ - 3 * std_]
        )
        data_ = data_[
            data_[metric] < mean_ + 3 * std_
        ]
        data_ = data_[
            data_[metric] > mean_ - 3 * std_
        ]
        n += 1
        std_ = data_[metric].std()
        mean_ = data_[metric].mean()
        max_ = data_[metric].max()
        min_ = data_[metric].min()

        print('\nIteration:', n)

        print('max:', max_)
        print('min:', min_)
        print('mean:', mean_)
        print('std:', std_)

    return recycled['country'].unique()

print(recycler(df, metric_0))
print(recycler(df, metric_1))

