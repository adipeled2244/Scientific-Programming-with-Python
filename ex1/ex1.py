import json
import csv

def convertJsonToDict(datafile):
    """get json and convert json dictionary- return dictionary"""
    try:
        with open(datafile, 'r') as jsonfile:
            reader = json.load(jsonfile)
        return reader
    except:
        return {}

def convertCSVToDict(metafile):
    """get csv and convert csv to dict - return dictionary"""
    try:
        dict = []
        with open(metafile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dict.append(row)
        return dict
    except:
        return []


class DataSummary:

    def __init__(self, datafile=[], metafile=[]):
        """constructor - this build the class:
        it's get two files -> if one of the file missing it throw exception.
        the files it convert to dictionary."""
        if datafile == [] or metafile == []:
            raise ValueError("Sorry, parameter missing")

        self.metafile = convertCSVToDict(metafile)
        self.datafile = convertJsonToDict(datafile)["data"]
        self.metafilekeys=self.metafile[0].keys()
        if self.datafile == [] or metafile == {}:
            raise ValueError("Sorry, convert failed")

        for dict in self.datafile:
            for metakey in self.metafilekeys:
                if not metakey in dict:
                    dict[metakey] = None

        for dict in self.datafile:
            for key in list(dict):
                if not key in self.metafilekeys:
                    del dict[key]


    def sum(self, feature):
        """sum(feature):get a feature and return the sum of all values in the feature."""
        if feature in self.metafilekeys and self.metafile[0][feature] != 'string' :
            return sum([float(dict[feature]) for dict in self.datafile if dict[feature] is not None])

        elif feature in self.metafilekeys and self.metafile[0][feature] == 'string':
            raise ValueError("Sorry, The feature is categorical")

        else :
            raise ValueError("Sorry, category does not exist")


    def mean(self, feature):
        """mean(feature):  get a feature return the average over all values in the feature that arent null """
        if feature in self.metafilekeys and self.metafile[0][feature] != 'string' :
            Elements= [float(dict[feature]) for dict in self.datafile if dict[feature] is not None]
            return sum(Elements)/len(Elements)
        elif feature in self.metafilekeys and self.metafile[0][feature] == 'string':
            raise ValueError("Sorry, The feature is categorical")
        else :
            raise ValueError("Sorry, feature dont found")

    def min(self, feature):
        """.min(feature): get a feature and return the minimal value in the feature."""
        if feature in self.metafilekeys and self.metafile[0][feature] != 'string' :
            return min([float(dict[feature]) for dict in self.datafile if dict[feature] is not None])
        elif feature in self.metafilekeys and self.metafile[0][feature] == 'string':
            raise ValueError("Sorry, The feature is categorical")

        else :
            raise ValueError("Sorry, feature dont found")

    def max(self, feature):
        """max(feature): get a feature and return the maximal value in the feature."""
        if feature in self.metafilekeys and self.metafile[0][feature] != 'string':
            return max([float(dict[feature]) for dict in self.datafile if dict[feature] is not None])
        elif feature in self.metafilekeys and self.metafile[0][feature] == 'string':
            raise ValueError("Sorry, The feature is categorical")
        else:
            raise ValueError("Sorry, feature dont found")

    def count(self, feature):
        """.count(feature): get a feature ans return the number of non-None values in the feature."""
        if feature in self.metafilekeys:
            return len([dict[feature] for dict in self.datafile if dict[feature] is not None])
        else:
            raise ValueError("Sorry, feature dont found")

    def empty(self, feature):
        """empty(feature): get a feature and return the number of None values in the feature"""
        if feature in self.metafilekeys:
            return len([dict[feature] for dict in self.datafile if dict[feature] is None])
        else:
            raise ValueError("Sorry, feature dont found")

    def unique(self, feature):
        """.unique(feature): get a feature and return a list of unique values in the feature, in ascending order (alphabetical for categorical features). (None is not included)"""
        if feature in self.metafilekeys:
            return sorted(set([dict[feature] for dict in self.datafile if dict[feature] is not None]))
        else:
            raise ValueError("Sorry, feature dont found")

    def mode(self, feature):
        """ mode-get feature and return the most in the feature"""
        dictCount ={}
        if feature in self.metafilekeys:
            for dict in self.datafile:
                if dict[feature] is not None:
                    if dict[feature] in dictCount:
                        dictCount[dict[feature]]+=1
                    else:
                        dictCount[dict[feature]]=1

            maxVal=0
            mode =[]
            for count in dictCount:
                if dictCount[count] > maxVal:
                    maxVal = dictCount[count]
                    mode =[]
                    mode.append(count)
                elif dictCount[count] == maxVal :
                    mode.append(count)

            return mode
        else:
            raise ValueError("Sorry, feature dont found")

    def to_csv(self, filename, delimiter=','):
        # check with
        if not delimiter in ['"','.',':','|',';','#','*','-',',',' ']:
            delimiter = ','
        with open(filename, "w", newline="") as csvfile:
            file_buffer = csv.writer(csvfile,delimiter=delimiter,quoting=csv.QUOTE_ALL)
            file_buffer.writerow(self.metafilekeys)
            for x in self.datafile:
                file_buffer.writerow(x.values())



def access(self, i):
    """access function return a copy of record by index or return a list of values by feature"""
    if type(i)==int:
        if i<len(self.datafile) and i>=(-1)*len(self.datafile):
            return self.datafile[i].copy()
        else:
            raise ValueError("Sorry, index out of bounds")
    elif type(i)==str :
        if i in self.metafilekeys:
            return [dict[i] for dict in self.datafile]
        else:
            raise ValueError("Sorry,KeyError- Category not found")
    else :
        raise ValueError("Sorry, between [] you need to send int or str")

DataSummary.__getitem__=access




