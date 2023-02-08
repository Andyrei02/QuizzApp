import file_w_r as f_manage


dict_scenario = {
	"0": ("question 1", ["answer 1", "answer 2", "answer 3"], "1"),
	"1": ("question 2", ["answer 1", "answer 2", "answer 3", "answer 4"], "3"),
	"2": ("question 3", ["answer 1", "answer 2", "answer 3"], "1"),
	"3": ("question 4", ["answer 1", "answer 2", "answer 3", "answer 4", "answer 5"], "3"),

}

def main():
	file_wr = f_manage.FileWR()
	file_wr.write_json("dict_scenario.json", dict_scenario)
	print(file_wr.read_json("dict_scenario.json"))


if __name__ == "__main__":
	main()
