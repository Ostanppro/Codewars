class List:
    def remove_(self, integer_list, values_list):
        list_Out = []
        for i in integer_list:
            if i not in values_list:
                list_Out.append(i)
        return list_Out