from data_summary import DataSummary

print("-----------------------------------The results of constructor: -------------------------")

if __name__ == "__main__":
    try:
        DS_err = DataSummary()
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected DataSummary constructor")

    DS = DataSummary(datafile="happiness.json",metafile="happiness_meta.csv")
    # print(DS.getDataFile())
    # print("\n")
    # print(DS.getMetaFile())

    print("-----------------------------------The results of read with []: -------------------------")

    print("The result of read index [3] : ")
    print(DS[3])
    try:
        print(DS[1000])
    except Exception as err:
         print("Exception: ", err)
    else:
        print("unexpected error")

    print("The result of read  ['country'] : ")
    print(DS["Country"])

    print("The result of read  ['GDP'] : ")
    try:
        DS['GDP']
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature GDP")

    print("The result of read  ['data'] :")
    try:
        DS['data']
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")


    print("-----------------------------------The results of sum: -------------------------")
    print("The results of sum family: ")
    print(DS.sum("Family"))

    print("The results of sum notReallyCat: ")
    try:
        print(DS.sum("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("The results of sum Country: ")
    try:
        print(DS.sum("Country"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")


    print("-----------------------------------The results of mean: -------------------------")
    print("Hapiness score mean: ")
    print(DS.mean("Happiness Score"))

    print("notReallyCat mean: ")

    try:
        print(DS.mean("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")
    print("notReallyCat Country: ")
    try:
        print(DS.mean("Country"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("-----------------------------------The results of min: -------------------------")

    print("Hapiness score min: ")
    print(DS.min("Happiness Score"))

    print("notReallyCat min: ")
    try:
        print(DS.min("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("Country min: ")
    try:
        print(DS.min("Country"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("-----------------------------------The results of max: -------------------------")

    print("Hapiness score max: ")
    print(DS.max("Happiness Score"))

    print("notReallyCat max: ")
    try:
        print(DS.max("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("Country max: ")
    try:
        print(DS.max("Country"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected function min for categorical feature")


    print("-----------------------------------The results of count: -------------------------")
    print("Hapiness score count: ")
    print(DS.count("Happiness Score"))
    print("notReallyCat count: ")

    try:
        print(DS.count("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("-----------------------------------The results of empty: -------------------------")
    print("Hapiness score empty: ")
    print(DS.empty("Happiness Score"))

    print("notReallyCat count: ")
    try:
        print(DS.empty("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("-----------------------------------The results of unique: -------------------------")
    print("Country unique: ")
    print(DS.unique("Country"))
    print("Happiness Score unique: ")
    print(DS.unique("Happiness Score"))
    print("Class unique: ")
    print(DS.unique("Class"))

    print("notReallyCat unique: ")
    try:
        print(DS.unique("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("-----------------------------------The results of mode: -------------------------")
    print("Class mode: ")
    print(DS.mode("Country"))

    print("notReallyCat mode: ")
    try:
        print(DS.mode("notReallyCat"))
    except Exception as err:
        print("Exception: ", err)
    else:
        print("unexpected feature data")

    print("-----------------------------------to_csv: open happiness.csv with delimiter , to see result-------------------------")
    DS.to_csv("happiness.csv", ",")
    print("-----------------------------------to_csv: open happiness#.csv with  delimiter #  to see result-------------------------")
    DS.to_csv("happiness#.csv", "#")

