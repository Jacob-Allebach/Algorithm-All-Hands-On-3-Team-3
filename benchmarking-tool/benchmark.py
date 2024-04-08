def execute_function(file, function_name, list):
    with open(file) as f:
        command = f"{f.read()}\n{function_name}({str(list)})"
        return exec(command)

new_list = [24,6,547,2,5,83,3546,7,35,26,2626,215]
execute_function("../sorting-algorithms/insertion-sort.py","insertion",new_list)