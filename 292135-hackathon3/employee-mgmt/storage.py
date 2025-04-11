import pickle

class Storage:
    
    # save to pickle file
    @staticmethod
    def save_to_file(data, filename=r"D:\py_training\python-training\292135-hackathon3\employee-mgmt\employees.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(data, file)
        print(f"Saved the data to {filename} successfully.")

    # load file from pickle file
    @staticmethod
    def load_from_file(filename=r"D:\py_training\python-training\292135-hackathon3\employee-mgmt\employees.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Can't find the file {filename}.")
            return []
