import PyPluMA
class TSVFilterPlugin:
    def input(self, filename):
        self.inputfile = open(filename, 'r')

    def run(self):
      self.parameters = dict()
      for line in self.inputfile:
          contents = line.strip().split('\t')
          self.parameters[contents[0]] = contents[1]
      self.filestuff = open(PyPluMA.prefix()+"/"+self.parameters["tsvfile"], 'r')
      self.threshold = float(self.parameters["threshold"])
      self.firstline = self.filestuff.readline().strip()

    def output(self, filename):
        outputfile = open(filename, 'w')
        outputfile.write(self.firstline+"\n")
        for line in self.filestuff:
            line = line.strip()
            contents = line.split('\t')
            m = float(len(contents))-1
            nonzerocount = 0.0
            for j in range(1, len(contents)):
                if (float(contents[j]) != 0):
                    nonzerocount += 1
            if (nonzerocount/m >= 0.5):
                outputfile.write(line+"\n")
            else:
                print("REMOVING "+contents[0])

