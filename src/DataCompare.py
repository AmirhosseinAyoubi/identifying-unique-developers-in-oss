from Levenshtein import ratio as sim

class DataCompare:
    def __init__(self):
        pass
    threshold = 0.7

    sim1_result = 0
    sim2_result = 0
    sim3_result = []
    sim4_result = None
    sim5_result = None
    sim6_result = None
    sim7_result = None

    force_write_sim_result = False


    def comp_sim_c1(self, name1, name2):
        __sim_score1 = sim(name1, name2)

        if self.force_write_sim_result:
            self.sim1_result = __sim_score1

        if __sim_score1 >= self.threshold:
            self.sim1_result = __sim_score1
            return True
        else:
            return False
    def comp_sim_c2(self, prefix1, prefix2):
        __sim_score2 = sim(prefix1, prefix2)

        if self.force_write_sim_result:
            self.sim2_result = __sim_score2

        if __sim_score2 >= self.threshold:
            self.sim2_result = __sim_score2
            return True
        else:
            return False
    def comp_sim_c3(self, first_name1, first_name2, last_name1, last_name2):
        __sim_score3_1 = sim(first_name1, first_name2)
        __sim_score3_2 = sim(last_name1, last_name2)

        if self.force_write_sim_result:
            self.sim3_result[0] = __sim_score3_1
            self.sim3_result[1] = __sim_score3_2

        if __sim_score3_1 >= self.threshold:
            self.sim3_result[0] = __sim_score3_1
            return True
        if __sim_score3_2 >= self.threshold:
            self.sim3_result[1] = __sim_score3_2
            return True
        else:
            return False


com_obj = DataCompare()
com_obj.force_write_sim_result = True
com_obj.comp_sim_c2("Amirhossein", 'Ayoubi' )
print(com_obj.sim2_result)
