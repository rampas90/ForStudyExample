
import pandas as pd

df = pd.read_csv('../dataset/pima-indians-diabetes.csv',
                 names=["pregant","plasma","pressure","thickness",
                       "insulin","BMI","pedigree","age","class"])

print(df.head(5))
print(df.info())


print(df[['pregant','class']].groupby([
    'pregant'],as_index=False).mean().sort_values(by='pregant',ascending=True))