class Example:

    @staticmethod
    def read_PPO_dat_file(dat_file):
        """ This function gets the curve parameters out from the given .dat file.

        Parameters
        ----------
        dat_file : str
            Path to the .dat file

        Returns
        -------
        tuple(list, list)
            The two list contains the curve data. First list x values, second list y values.
        """
        try:
            dat_file = open(dat_file, "r", encoding="utf-8")

            sim_x = []
            sim_y = []

            for data in dat_file:

                try:
                    sim_x.append(float(data.split(",")[0]))
                    sim_y.append(float(data.split(",")[1][:-2]))
                except ValueError:
                    continue

            dat_file.close()

            return sim_x, sim_y
        except FileNotFoundError:
            return "There is no PPO file on this path: " + dat_file

if __name__ == '__main__':
    dat_file = 'Examples_2022\\01_str_methods\\10HEAD0100HMANZ0.dat'

    output = Example.read_PPO_dat_file(dat_file)
    if isinstance(output, str):
        print(output)
    else:
        print(output[1])

    with open(dat_file, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            print(line)

