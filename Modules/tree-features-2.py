import utils as ut
import accuracy as ac

data_set_train, data_sets_test = ut.get_data()

columns = [30, 34, 53]
data_set_train_selected, data_sets_test_selected = ut.select_data(data_set_train, data_sets_test, columns)

ac.get_accuracy(data_set_train_selected, data_sets_test_selected)
