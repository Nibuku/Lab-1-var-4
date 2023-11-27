import pandas as pd


def open_new_csv(csv_path: str) -> pd.DataFrame:
    '''Function for opening the original annotation as a dataframe,
    naming columns of the dataframe and removing unnecessary'''
    dframe = pd.read_csv(
        csv_path, delimiter=",", names=["Absolute path", "Relative path", "Class"]
    )
    dframe = dframe.drop("Relative path", axis=1)
    return dframe

def open_csv(csv_path: str) -> pd.DataFrame:
    '''Function for opening the csv-annotation as a dataframe'''
    dframe = pd.read_csv(csv_path)
    return dframe

def save_csv(dframe: pd.DataFrame, file_path: str) -> None:
    '''Function of saving a dataframe to a csv file'''
    dframe.to_csv(file_path, index=False)
